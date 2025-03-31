import numpy as np
def fitness_func(X):
    a = 10
    pi = np.pi
    x = X[:, 0]
    y = X[:, 1]
    return 2 * a + x ** 2 - a * np.cos(2 * pi * x) + y ** 2 - a * np.cos(2 * 3.14 * y)

def decode(x, a, b):
    xt = 0
    for i in range(len(x)):
        xt = xt + x[i] * np.power(2, i)
    return a + xt * (b - a) / (np.power(2, len(x)) - 1)

def decode_X(X: np.array):
    X2 = np.zeros((X.shape[0], 2))
    for i in range(X.shape[0]):
        xi = decode(X[i, :20], -5, 5)
        yi = decode(X[i, 20:], -5, 5)
        X2[i, :] = np.array([xi, yi])
    return X2

def select(X, fitness):
    fitness = 1 / fitness
    fitness = fitness / fitness.sum()
    idx = np.array(list(range(X.shape[0])))
    X2_idx = np.random.choice(idx, size=X.shape[0], p=fitness)
    X2 = X[X2_idx, :]
    return X2

def crossover(X, c):
    for i in range(0, X.shape[0], 2):
        xa = X[i, :]
        xb = X[i + 1, :]
        for j in range(X.shape[1]):
            if np.random.rand() <= c:
                xa[j], xb[j] = xb[j], xa[j]
        X[i, :] = xa
        X[i + 1, :] = xb
    return X

def mutation(X, m):
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            if np.random.rand() <= m:
                X[i, j] = (X[i, j] + 1) % 2
    return X

def Ras_main():
    c = 0.3
    m = 0.05
    min_data = []
    min_local = []
    iter_num = 100
    X0 = np.random.randint(0, 2, (50, 40))
    for i in range(iter_num):
        X1 = decode_X(X0)
        fitness = fitness_func(X1)
        X2 = select(X0, fitness)
        X3 = crossover(X2, c)
        X4 = mutation(X3, m)
        X5 = decode_X(X4)
        fitness = fitness_func(X5)
        min_data.append(fitness.min())
        x, y = X5[fitness.argmin()]
        min_local.append((x, y))
        X0 = X4
    print("Rastrigin函数的最小值是：%.5f" % min_data[-1])
    print("函数取得最小值时，x1与x2的值分别为：x1=%.5f, x2=%.5f" % min_local[-1])


if __name__ == "__main__":
    Ras_main()
