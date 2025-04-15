from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn import metrics

#----数据加载------
data = load_breast_cancer()
X    = data.data
y    = data.target
feature_names = data.feature_names
#----数据归一化------
xmin=X.min(axis=0)
xmax=X.max(axis=0)
X_norm=(X-xmin)/(xmax-xmin)

#-----初始化模型--------------------
# 备注：penalty一开始训练时先用'none'，训练出的系数不满意，再切换回l2
clf =LogisticRegression(penalty='l2',dual=False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, 
                   class_weight=None, random_state=None, solver='lbfgs', max_iter=100, multi_class='ovr',
                   verbose=0, warm_start=False, n_jobs=None, l1_ratio=None)

#-----逐步回归挑选变量--------------------
select_var = []                            # 已挑选的变量  
var_pool   = np.arange(X_norm.shape[1])    # 待挑选变量池
auc_rec    = []
print("\n===========逐回步归过程===============")
while(len(var_pool)>0):
    max_auc  = 0
    best_var = None
    #---选出剩余变量中能带来最好效果的变量--------
    for i in var_pool:
        # -------将新变量和已选变量一起训练模型------
        cur_x = X_norm[:,select_var+[i]]               # 新变量和已选变量作为建模数据                
        clf.fit(cur_x,y)                               # 训练模型
        pred_prob_y = clf.predict_proba(cur_x)[:,1]    # 预测概率
        cur_auc = metrics.roc_auc_score(y,pred_prob_y) # 计算AUC
        # ------更新最佳变量---------------------------
        if(cur_auc>max_auc):
            max_auc =  cur_auc
            best_var = i
    #-------检验新变量能否带来显著效果---------------------------
    last_auc = auc_rec[-1] if len(auc_rec)>0 else 0.0001
    valid = True  if ((max_auc-last_auc)/last_auc>0.005) else False
    # 如果有显著效果，则将该变量添加到已选变量
    if(valid):
        print("本轮最佳AUC:",max_auc,",本轮最佳变量：",feature_names[best_var])
        auc_rec.append(max_auc)  
        select_var.append(best_var)  
        var_pool = var_pool[var_pool!=best_var]
    # 如果没有显著效果，则停止添加变量
    else:
        print("本轮最佳AUC:",max_auc,",本轮最佳变量：",feature_names[best_var],',效果不明显,不再添加变量')
        break
print("最终选用变量",len(select_var),"个：",feature_names[select_var])

#------模型训练--------------------------------
clf.fit(X_norm[:,select_var],y)

#------模型预测-------------------------------
pred_y      = clf.predict(X_norm[:,select_var])
pred_prob_y = clf.predict_proba(X_norm[:,select_var])[:,1]
auc = metrics.roc_auc_score(y,pred_prob_y)   #
print("\n============建模结果=================")
print("选用变量",len(select_var),"个：",feature_names[select_var])
print("AUC:",auc)

#------------提取系数w与阈值b-----------------------
w_norm = clf.coef_[0]                            # 模型系数(对应归一化数据)
b_norm = clf.intercept_                          # 模型阈值(对应归一化数据)
w = w_norm/(xmax[select_var]-xmin[select_var])                           # 模型系数(对应原始数据)
b = b_norm -  (w_norm/(xmax[select_var] - xmin[select_var])).dot(xmin[select_var])   # 模型阈值(对应原始数据)
self_prob_y = 1/(1+np.exp(-(X[:,select_var].dot(w)+ b) ))      # 用公式预测

#------------打印信息--------------------------
print("\n=========对应归一化数据的模型参数========")     
print( "模型系数(对应归一化数据):",clf.coef_[0])
print( "模型阈值(对应归一化数据):",clf.intercept_)
print("\n=========对应原始数据的模型参数==========")   
print("模型系数(对应原始数据):",w)
print("模型阈值(对应原始数据):",b)
print("提取公式计算的概率与模型概率的最大误差", abs(pred_prob_y-self_prob_y).max())

