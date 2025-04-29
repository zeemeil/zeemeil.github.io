import numpy as np
np.random.seed(35)

#定义激活函数及其导数
def nonlinear(x, deriv=False):
    if (deriv == True):
        return x * (1 - x) #如果deriv为true，求导数
    return 1 / (1 + np.exp(-x))

X = np.array([[0.35],[0.9]]) #输入值
y = np.array([[0.5]]) #输出值

W0 = np.array([[0.1,0.8],[0.4,0.6]]) # 权重
W1 = np.array([[0.3,0.9]])
#print ('original ',W0,'\n',W1)
for j in range(20):
    l0 = X #第0层输入
    l1 = nonlinear(np.dot(W0,l0))  #第一层输出y1
    l2 = nonlinear(np.dot(W1,l1))  #第一层输出y2
    l2_error = y - l2
    Error = 1/2.0*(y-l2)**2
    print ('循环轮次:第%d轮'%j,"误差:",Error)
    l2_delta = l2_error * nonlinear(l2, deriv=True) 
    #print 'l2_delta=',l2_delta
    l1_error = l2_delta*W1; 
    l1_delta = l1_error * nonlinear(l1, deriv=True)

    W1 += l2_delta*l1.T; 
    W0 += l0.T.dot(l1_delta)
    print('第%d轮循环参数W0的值:'%j,W0)
    print('第%d轮循环参数W1的值:'%j,W1)