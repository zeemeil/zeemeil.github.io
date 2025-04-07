import numpy as np    
    
def prepare_data(data, normalize_data=True):    
    # 标准化特征矩阵（可选）    
    if normalize_data:    
        features_mean = np.mean(data, axis=0)    #特征的平均值
        features_dev = np.std(data, axis=0)      #特征的标准偏差
        features = (data - features_mean) / features_dev    #标准化数据
    else:    
        features_mean = None    
        features_dev = None    
        
    # 为特征添加偏置项     
    data_processed = np.hstack((np.ones((features.shape[0], 1)), features)).T
    # 返回处理后的数据
    return data_processed, features_mean, features_dev

def get_predict_score(predict_table):
    score_table = []
    pass_count = 0
    for pair in predict_table:
        if (abs(pair[0] - pair[1]) / pair[1] < 0.1):
            score_table.append("good")
            pass_count += 1
        elif (abs(pair[0] - pair[1]) / pair[1] < 0.4):
            score_table.append("around")
            pass_count += 0.8
        else:
            score_table.append("bad")
    accuracy = pass_count / len(predict_table)
    return score_table, accuracy
        
class LinearRegression:
    '''
    1. 对数据进行预处理操作
    2. 先得到所有的特征个数
    3. 初始化参数矩阵
    '''
    def __init__(self, data,labels, normalize_data = True) -> None:
        (data_proccessed,
         features_mean,
         features_dev) = prepare_data(data, normalize_data)
        self.data = data_proccessed
        self.labels = labels
        self.features_mean = features_mean
        self.features_dev = features_dev
        self.normalize_data = normalize_data
        
        num_features = self.data.shape[0] #特征个数
        self.theta = np.zeros((num_features,1)) #初始化权重向量
        
    def train(self, lr, num_iter = 500):
        #训练模块
        cost_history = self.gradient_desent(lr, num_iter) #梯度下降过程
        return self.theta,cost_history
        
    def gradient_step(self,lr):
        '''
        梯度下降参数更新，使用矩阵运算
        '''
        num_examples = self.data.shape[1] # 多少行
        prediction = LinearRegression.predict(self.data, self.theta) #每次计算所有样本的预测值，使用矩阵乘法
        delta = prediction - self.labels # 偏差向量
        theta = self.theta
        theta -= lr*(1/num_examples)*(np.dot(delta.T, self.data.T)).T #更新权重
        self.theta = theta #记录当前权重参数
    
    def gradient_desent(self, lr, num_iter):
        cost_history = []
        for _ in range(num_iter): # 在规定的迭代次数里执行训练
            self.gradient_step(lr)
            cost_history.append(self.cost_function(self.data, self.labels)) # 记录损失值，以便可视化展示
        return cost_history
    
    def cost_function(self,data,labels):
        num_examples = data.shape[0]
        delta = LinearRegression.predict(self.data, self.theta) - labels #偏差
        cost = (1/2)*np.dot(delta.T, delta) #最小二乘法计算损失
        #print(cost.shape)
        return cost[0][0]
    
    #针对测试集
    def get_cost(self, data, labels):
        data_proccessed = prepare_data(data, self.normalize_data)[0]
        return self.cost_function(data_proccessed, labels)
    
    def predict_test(self, data):
        data_proccessed = prepare_data(data, self.normalize_data)[0]
        prediction = LinearRegression.predict(data_proccessed, self.theta)
        return prediction
    @staticmethod
    def predict(data, theta):
        prediction = np.dot(data.T, theta) #特征值和权重参数做点积，计算预测值
        return prediction
        
import pandas as pd
import matplotlib.pyplot as plt
def main():        
    data_file = "./data_collections/housing.csv"
    data = pd.read_csv(data_file, sep="\s+").sample(frac=1).reset_index(drop=True)
    train_data = data.sample(frac=0.8)
    test_data = data.drop(train_data.index)
    input_param_index = 'NOX'
    output_param_index = 'MEDV'
    x_train = train_data[input_param_index].values
    y_train = train_data[output_param_index].values
    x_test = test_data[input_param_index].values
    y_test = test_data[output_param_index].values
    
    x_train = train_data.iloc[:, :13].values
    y_train = train_data[output_param_index].values.reshape(len(x_train),1)
    x_test = test_data.iloc[:, :13].values
    y_test = test_data[output_param_index].values.reshape(len(test_data),1)
    print(x_train.shape)
    print(y_train.shape)
    
    linearReg = LinearRegression(x_train, y_train)
    train_theta, loss_history = linearReg.train(0.0001, 50000)
    fomula = 'Y = '
    index = 0
    for w in np.round(train_theta, 2)[1:]:
        fomula += "{}{}X{}".format(" + " if w >=0 else " - " if index != 0 else "", float(abs(w[0])), index)
        index += 1
    fomula += "{}{}".format(" + " if train_theta[0] >= 0 else "-", round(float(abs(train_theta[0][0])), 2))
    print(fomula)
    print(train_theta.shape)
    plt.plot(loss_history)
    plt.show()
    
    predic_result = np.round(linearReg.predict_test(x_test), 2)
    predict_table = np.column_stack((predic_result, y_test))
    score, accuracy = get_predict_score(predict_table)
    print("Accuracy is {}".format(accuracy))
    color_table = {"good": "green", "around":"yellow", "bad": "red"}
    # print(predic_result)
    fig, ax = plt.subplots()
    table = ax.table(cellText = predict_table, loc = 'center')
    for i, cell in enumerate(table._cells.values()):
        color_index = int(i / 2)
        cell.set_facecolor(color_table[score[color_index]])
    ax.axis("off")
    plt.show()
    
    
 
if (__name__ == "__main__"):
    main()
