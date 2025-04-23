# 定义欧式距离
import numpy as np
def get_distance(x1, x2):
    return np.sqrt(np.sum(np.square(x1-x2)))

import random
# 定义中心初始化函数，中心点选择的是样本特征
def center_init(k, X):
    n_samples, n_features = X.shape
    centers = np.zeros((k, n_features))
    selected_centers_index = []
    for i in range(k):
        # 每一次循环随机选择一个类别中心,判断不让centers重复
        sel_index = random.choice(list(set(range(n_samples))-set(selected_centers_index)))
        centers[i] = X[sel_index]
        selected_centers_index.append(sel_index)
    return centers


# 判断一个样本点离哪个中心点近， 返回的是该中心点的索引
## 比如有三个中心点，返回的是0，1，2
def closest_center(sample, centers):
    closest_i = 0
    closest_dist = float('inf')
    for i, c in enumerate(centers):
        # 根据欧式距离判断，选择最小距离的中心点所属类别
        distance = get_distance(sample, c)
        if distance < closest_dist:
            closest_i = i
            closest_dist = distance
    return closest_i


# 定义构建聚类的过程
# 每一个聚类存的内容是样本的索引，即对样本索引进行聚类，方便操作
def create_clusters(centers, k, X):
    clusters = [[] for _ in range(k)]
    for sample_i, sample in enumerate(X):
        # 将样本划分到最近的类别区域
        center_i = closest_center(sample, centers)
        # 存放样本的索引
        clusters[center_i].append(sample_i)
    return clusters


# 根据上一步聚类结果计算新的中心点
def calculate_new_centers(clusters, k, X):
    n_samples, n_features = X.shape
    centers = np.zeros((k, n_features))
    # 以当前每个类样本的均值为新的中心点
    for i, cluster in enumerate(clusters):  # cluster为分类后每一类的索引
        new_center = np.mean(X[cluster], axis=0) # 按列求平均值
        centers[i] = new_center
    return centers
# 获取每个样本所属的聚类类别
def get_cluster_labels(clusters, X):
    y_pred = np.zeros(np.shape(X)[0])
    for cluster_i, cluster in enumerate(clusters):
        for sample_i in cluster:
            y_pred[sample_i] = cluster_i
            #print('把样本{}归到{}类'.format(sample_i,cluster_i))
    return y_pred


# 根据上述各流程定义kmeans算法流程
def Mykmeans(X, k, max_iterations,init):
    # 1.初始化中心点
    if init == 'kmeans':
        centers = center_init(k, X)
    else: centers = get_kmeansplus_centers(k, X)
    # 遍历迭代求解
    for _ in range(max_iterations):
        # 2.根据当前中心点进行聚类
        clusters = create_clusters(centers, k, X)
        # 保存当前中心点
        pre_centers = centers
        # 3.根据聚类结果计算新的中心点
        new_centers = calculate_new_centers(clusters, k, X)
        # 4.设定收敛条件为中心点是否发生变化
        diff = new_centers - pre_centers
        # 说明中心点没有变化，停止更新
        if diff.sum() == 0:
            break
    # 返回最终的聚类标签
    return get_cluster_labels(clusters, X)

# 测试执行
X = np.array([[0,2],[0,0],[1,0],[5,0],[5,2]])
# 设定聚类类别为2个，最大迭代次数为10次
labels = Mykmeans(X, k = 2, max_iterations = 10,init = 'kmeans')
# 打印每个样本所属的类别标签
print("最后分类结果",labels)
## 输出为  [1. 1. 1. 0. 0.]

# 使用sklearn验证
from sklearn.cluster import KMeans
X = np.array([[0,2],[0,0],[1,0],[5,0],[5,2]])
kmeans = KMeans(n_clusters=2,init = 'random').fit(X)
# 由于center的随机性，结果可能不一样
print(kmeans.labels_)
