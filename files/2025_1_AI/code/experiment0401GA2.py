import numpy as np 
import matplotlib.pyplot as plt
from typing import List


class GA:
    """ 遗传算法 """

    def __init__(self, pop_size=200, dna_size=20, top_rate=0.2, crossover_rate=0.8, mutation_rate=0.01, n_iters=100):
        """
        Parameters
        ----------
        pop_size: int
            种群大小

        dna_size: int
            染色体大小

        top_rate: float
            保留的优秀染色体个数

        crossover_rate: float
            交叉概率

        mutation_rate: float
            变异概率

        n_iters: int
            迭代次数
        """
        self.pop_size = pop_size
        self.dna_size = dna_size
        self.top_rate = top_rate
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.n_iters = n_iters

    def get_solution(self, obj_func, bound: List[tuple], is_min=True):
        """ 获取最优解

        Paramters
        ---------
        obj_func: callable
            n 元目标函数

        bound: List[tuple]
            维度为 `(n, 2)` 的取值范围矩阵

        is_min: bool
            寻找的是否为最小值

        Returns
        -------
        index: int
            最优解的下标

        Xm: list
            历次迭代的最优解

        Ym: list
            历次迭代的最优值
        """
        Xm, Ym = [0], [0]

        # 初始化种群
        pop = np.random.randint(
            2, size=(self.pop_size, self.dna_size*len(bound)))
        Xm[0], Ym[0] = self._get_best(pop, obj_func, bound, is_min)

        # 迭代求最优解
        for _ in range(self.n_iters):
            X = self._decode(pop, bound)
            fitness = self._fitness(obj_func, X, is_min)
            keep, selected = self._select(pop, fitness)
            new = self._crossover_mutation(selected)
            pop = np.vstack((keep, new))

            xm, ym = self._get_best(pop, obj_func, bound, is_min)
            Xm.append(xm)
            Ym.append(ym)

        idx = np.argmin(Ym) if is_min else np.argmax(Ym)
        return idx, Xm, Ym

    def _decode(self, pop: np.ndarray, bound: List[tuple]):
        """ 将二进制数解码为十进制数 """
        result = []
        N = 2**self.dna_size-1
        pows = 2**np.arange(self.dna_size, dtype=float)[::-1]
        for i, (low, high) in enumerate(bound):
            X = pop[:, i*self.dna_size:(i+1)*self.dna_size]
            X = low + (high-low)*X.dot(pows)/N
            result.append(X)

        return result

    def _fitness(self, obj_func, X: tuple, is_min=True):
        """ 适应度函数 """
        y = obj_func(*X)
        e = 1e-3
        return -y+np.max(y)+e if is_min else y-np.min(y)+e

    def _select(self, pop: np.ndarray, fitness: np.ndarray):
        """ 根据使用度选择染色体 """
        # 保留一定比例的优秀染色体
        n_keep = int(self.pop_size*self.top_rate)
        idx_keep = (-fitness).argsort()[:n_keep]

        # 按照适应度值随机挑选出剩下的染色体
        n_select = self.pop_size-n_keep
        p = fitness/fitness.sum()
        idx = np.random.choice(np.arange(self.pop_size), n_select, True, p)

        return pop[idx_keep], pop[idx]

    def _crossover_mutation(self, pop: np.ndarray):
        """ 交叉变异 """
        result = []
        for child in pop:
            # 交叉
            if np.random.rand() < self.crossover_rate:
                mother = pop[np.random.randint(len(pop))]
                point = np.random.randint(pop.shape[1])
                child[point:] = mother[point:]

            # 变异
            if np.random.rand() < self.mutation_rate:
                pos = np.random.randint(pop.shape[1])
                child[pos] = 1 - child[pos]

            result.append(child)

        return np.array(result)

    def _get_best(self, pop: np.ndarray, obj_func, bound: List[tuple], is_min):
        """ 获取最优解及其目标函数值 """
        X = self._decode(pop, bound)
        Y = obj_func(*X)
        idx = np.argmin(Y) if is_min else np.argmax(Y)
        xm = [x[idx] for x in X]
        return xm, Y[idx]
    
def f(x, y):
    """ 目标函数 """
    return 20+x*x+y*y-10*(np.cos(2*np.pi*x)+np.cos(2*np.pi*y))


if __name__ == '__main__':
    ga = GA(dna_size=50)

    idx, Xm, Ym = ga.get_solution(f, [(-5, 5), (-5, 5)])
    print("最优解：", Xm[idx], "目标函数值：", Ym[idx])

    plt.plot(np.arange(ga.n_iters+1), Ym)
    plt.show()
