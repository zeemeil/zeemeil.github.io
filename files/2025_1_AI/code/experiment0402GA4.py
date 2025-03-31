import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------- #
# 使用遗传算法（GA）求解旅行商（TSP）问题
# -------------------------------------- #

# -------------------------------------- #
# 初始参数设置
# -------------------------------------- #
# 编码长度，即城市个数
n = 30
# 种群规模，即每轮共存在样本个数
pop = 100
# 迭代次数
M = 300
# 交叉的概率
crossover_prob = 0.6
# 变异的概率
mutation_prob = 0.2
# 记录每一代中的最优个体
best_distance = []
best_route = []

# -------------------------------------- #
# 生成随机城市数据
# -------------------------------------- #
city_ids = np.arange(1, n + 1).reshape(-1, 1)
random_cities_location = np.random.uniform(0, 20, size=(n, 2))
cities = np.hstack((city_ids, random_cities_location))
# 保存数据点图像
plt.scatter(cities[:, 1], cities[:, 2], color='blue')
plt.title('random city locations')
plt.xlabel('x')
plt.ylabel('y')
for city in cities:
    plt.annotate(int(city[0]), (city[1], city[2]), textcoords="offset points", xytext=(0,10), ha='center')
plt.savefig(r'./city_locations.png')


# -------------------------------------- #
# 生成初始种群
# -------------------------------------- #
initial_pop = np.zeros((pop, n), dtype=int)
for i in range(pop):
    initial_pop[i, :] = np.random.permutation(n) + 1  # 加1以匹配城市编号

# -------------------------------------- #
# 遗传迭代
# -------------------------------------- #
plt.ion()
fig, ax = plt.subplots()
for g in range(M):
    # -------------------------------------- #
    # 1-种群计算适应度
    # route存储每次迭代的种群路径,每条路径经过n+1个城市，+1表示最后回到原点
    # distance存储每次迭代中种群的路径代价
    # fitness是种族适应度，这里设置fitness为distance的倒数
    # -------------------------------------- #
    route = np.zeros((pop, n + 1), dtype=int)
    distance = np.zeros((pop, 1), dtype=float)
    fitness = np.zeros((pop, 1), dtype=float)
    for i in range(pop):
        route[i, :] = np.hstack((initial_pop[i, :], initial_pop[i, 0]))
        for j in range(n):
            # 编号为k的城市存储在索引k-1
            city_idx = route[i, j] - 1
            next_city_idx = route[i, j + 1] - 1
            distance[i] += np.sqrt((cities[city_idx, 1] - cities[next_city_idx, 1]) ** 2 + \
                                   (cities[city_idx, 2] - cities[next_city_idx, 2]) ** 2)
        fitness[i] = 1 / distance[i]
    # 记录适应度最优的个体索引
    best_idx = np.argmax(fitness)

    # -------------------------------------- #
    # 2-选择
    # -------------------------------------- #
    choosen_pop = np.zeros((pop, n), dtype=int)
    # 轮盘赌策略
    fit1 = (fitness - np.min(fitness)) / (np.max(fitness) - np.min(fitness))
    fit2 = fit1 / np.sum(fit1)
    fit3 = np.cumsum(fit2)
    compare = np.sort(np.random.rand(pop, 1), axis=0)
    i = 0
    j = 0
    while i < pop:
        if compare[i] < fit3[j]:
            choosen_pop[i, :] = initial_pop[j, :]
            i += 1
        else:
            j += 1

    # -------------------------------------- #
    # 3-交叉
    # -------------------------------------- #
    crossover_pop = choosen_pop
    crossover_begin = np.random.randint(0, n // 2)
    crossover_end = crossover_begin + n // 2
    for i in range(0, pop - 1, 2):
        if np.random.rand() < crossover_prob:
            temp = crossover_pop[i, crossover_begin:crossover_end]
            f = np.zeros(len(temp), dtype=int)

            for k in range(len(temp)):
                f[k] = np.where(crossover_pop[i + 1, :] == temp[k])[0][0]

            f = np.sort(f)

            for p in range(len(temp)):
                crossover_pop[i, p + crossover_begin] = crossover_pop[i + 1, f[p]]
                crossover_pop[i + 1, f[p]] = temp[p]

    # -------------------------------------- #
    # 4-变异
    # -------------------------------------- #
    mutation_pop = crossover_pop

    for i in range(pop):
        if np.random.rand() < mutation_prob:
            r = np.random.permutation(n) + 1
            row = mutation_pop[i, :]
            for j in range(0, n // 10, 2):
                r1 = r[j]
                r2 = r[j + 1]
                m1 = np.where(row == r1)[0][0]
                m2 = np.where(row == r2)[0][0]
                mutation_pop[i, m1] = r2
                mutation_pop[i, m2] = r1

    mutation_pop[-1, :] = initial_pop[best_idx, :]
    best_distance.append(distance[best_idx])
    best_route = route[best_idx, :]
    initial_pop = mutation_pop

    # -------------------------------------- #
    # 5-画图
    # -------------------------------------- #
    ax.clear()
    # 绘制城市分布
    ax.scatter(cities[:, 1], cities[:, 2], label='Cities', color='blue')
    ax.set_title(f'generation={g + 1}, distance={best_distance[g][0]}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    # 绘制路线
    best_route_indices = best_route[0:n + 1]
    best_route_cities_x = cities[best_route_indices - 1, 1]
    best_route_cities_y = cities[best_route_indices - 1, 2]
    ax.plot(best_route_cities_x, best_route_cities_y, 'b', label='Best Route')
    ax.legend()
    plt.pause(0.1)
    if g == M-1:
        plt.savefig(r'./best_route.png')
plt.ioff()
plt.show()

# 结果输出
print("最短路径长度：", best_distance[M - 1])
print("最短路径：", best_route)

# 绘制距离下降曲线
generations = range(1, M + 1)
plt.plot(generations, best_distance)
plt.title('distance vs generation')
plt.xlabel('generation')
plt.ylabel('distance')
plt.grid(True)
plt.savefig(r'./drop_curve.png')
plt.show()