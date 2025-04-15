# -*- coding: utf-8 -*-
"""
sklearn逻辑回归多分类例子(带模型公式提取)
"""
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.datasets import load_iris
#----数据加载------

iris = load_iris()    
X    = iris.data
y    = iris.target
#----数据归一化------
xmin   = X.min(axis=0)
xmax   = X.max(axis=0)
X_norm = (X-xmin)/(xmax-xmin)

#-----训练模型--------------------
clf = LogisticRegression(random_state=0,multi_class='multinomial')            
clf.fit(X_norm,y)

#------模型预测-------------------------------
pred_y      = clf.predict(X_norm)
pred_prob_y    = clf.predict_proba(X_norm) 

#------------提取系数w与阈值b-----------------------
w_norm = clf.coef_                             # 模型系数(对应归一化数据)
b_norm = clf.intercept_                           # 模型阈值(对应归一化数据)
w    = w_norm/(xmax-xmin)                       # 模型系数(对应原始数据)
b    = b_norm -  (w_norm/(xmax - xmin)).dot(xmin)      # 模型阈值(对应原始数据)
# ------------用公式预测------------------------------
wxb = X.dot(w.T)+ b
wxb = wxb - wxb.sum(axis=1).reshape((-1, 1)) # 由于担心数值过大会溢出，对wxb作调整
self_prob_y = np.exp(wxb)/np.exp(wxb).sum(axis=1).reshape((-1, 1))
self_pred_y = self_prob_y.argmax(axis=1)


#------------打印信息--------------------------
print("\n------模型参数-------")     
print( "模型系数:",w)
print( "模型阈值:",b)
print("\n-----验证准确性-------")  
print("提取公式计算的概率与sklearn自带预测概率的最大误差", abs(pred_prob_y-self_prob_y).max())