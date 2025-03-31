import numpy as np
import matplotlib.pyplot as plt

class GA(object):

    def __init__(self, DNA_size, DNA_bound, POP_size, target_func,
                 cross_rate=0.8, mutation_rate=1e-3, n_generations=100,
                 feature_bound=[0,1]):

        DNA_bound[1] += 1
        self.POP_size = POP_size
        self.DNA_size = DNA_size
        self.DNA_bound = DNA_bound
        self.cross_rate = cross_rate
        self.target_func = target_func
        self.mutation_rate = mutation_rate
        self.feature_bound = feature_bound
        self.n_generations = n_generations

        self.pop = np.random.randint(*DNA_bound, size=(POP_size, DNA_size))
    
    def translateDNA(self):
        '''
            Transform binary DNA squence into decimal number
        '''
        return self.pop.dot(2 ** np.arange(self.DNA_size)[::-1])\
               / float(2**self.DNA_size - 1) * self.feature_bound[1]
    
    def get_fitness(self, dec_pop):
        '''
            Get the fitness value according to the target func 
        '''
        pred = self.target_func(dec_pop)
        return pred, pred + 1e-3 - np.min(pred)

    def select(self, fitness):
        '''
            Select the DNA to the next generation accoding to the fitness value
        '''
        idx = np.random.choice(np.arange(self.POP_size), size=self.POP_size,
                               replace=True, p=fitness/fitness.sum())
        self.pop = self.pop[idx]
    
    def crossover(self, parent, pop):
        '''
            Operate crossover on the DNAs
        '''
        if np.random.rand() < self.cross_rate:
            idx = np.random.randint(0, self.POP_size, size=1)
            cross_points = np.random.randint(*self.DNA_bound,
                                             size=self.DNA_size).astype(np.bool)
            parent[cross_points] = pop[idx, cross_points]
        return parent
    
    def mutate(self, child):
        '''
            Operate the mutation on the DNAs
        '''
        for i in range(self.DNA_size):
            if np.random.rand() < self.mutation_rate:
                child[i] = 1 if child[i] == 0 else 0
        return child

    def evolve(self, verbose=False):
        '''
            Operate the evolutions
        '''
        for i in range(self.n_generations):
            dec_DNA = self.translateDNA()
            pred, fitness = self.get_fitness(dec_DNA)
            print("No.{} Generation Most fitted DNA: {}  Max value: {}"\
                  .format(i, self.pop[np.argmax(fitness), :], np.max(pred)))
            self.select(fitness)
            pop_copy = self.pop.copy()

            for parent in self.pop:
                child = self.crossover(parent, pop_copy)
                child = self.mutate(child)
                parent[:] = child
            
            if verbose:
                x = np.linspace(*self.feature_bound, 200)
                plt.title("No.{} Generation Max value: {}".format(i, np.max(pred)))
                plt.plot(x, self.target_func(x))
                plt.scatter(dec_DNA, pred, s=200, lw=0, c='red', alpha=0.5)
                plt.pause(0.05)
                if (i+1) < self.n_generations:
                    plt.cla()

class TSPGA(GA):
    
    def __init__(self, DNA_size, POP_size, tsp,
                 cross_rate=0.8, mutation_rate=1e-3, n_generations=100):
        self.tsp = tsp
        self.DNA_size = DNA_size
        self.POP_size = POP_size
        self.cross_rate = cross_rate
        self.mutation_rate = mutation_rate
        self.n_generations = n_generations
        
        self.pop = np.vstack([np.random.permutation(DNA_size) for _ in range(POP_size)])
    
    def translateDNA(self):
        '''
            Transform DNA squences into the lines between the cities
        '''
        line_x = np.empty_like(self.pop, dtype=np.float64)
        line_y = np.empty_like(self.pop, dtype=np.float64)
        cities = self.tsp.cities
        
        for i, d in enumerate(self.pop):
            line_x[i, :] = cities[d, 0]
            line_y[i, :] = cities[d, 1]
        
        return line_x, line_y
    
    def get_fitness(self, line_x, line_y):
        '''
            Get the fitness values according to minimizing the distances between cities
        '''
        total_distances = np.zeros((line_x.shape[0], ), dtype=np.float64)
        
        for i, (xs, ys) in enumerate(zip(line_x, line_y)):
            total_distances[i] = np.sum(np.sqrt(np.diff(xs)**2 + np.diff(ys)**2))
        
        fitness = np.exp(2. * self.DNA_size / total_distances)
        
        return fitness, total_distances
    
    def crossover(self, parent, pop):
        '''
        
        '''
        if np.random.rand() < self.cross_rate:
            index = np.random.randint(0, self.POP_size, size=1)
            cross_points = np.random.randint(0, 2, self.DNA_size).astype(np.bool)
            keep_cities = parent[~cross_points]
            swap_cities = pop[index, np.isin(pop[index].ravel(), keep_cities, invert=True)]
            parent[:] = np.concatenate((keep_cities, swap_cities))
        
        return parent
    
    def mutate(self, child):
        '''
        
        '''
        for point in range(self.DNA_size):
            if np.random.rand() < self.mutation_rate:
                swap_point = np.random.randint(0, self.DNA_size)
                child[point], child[swap_point] = child[swap_point], child[point]
        
        return child
    
    def evolve(self):
        '''
            Operate the evolutions
        '''
        for i in range(self.n_generations):
            line_x, line_y = self.translateDNA()
            fitness, total_distances = self.get_fitness(line_x, line_y)
            self.select(fitness)
            pop_copy = self.pop.copy()

            for parent in self.pop:
                child = self.crossover(parent, pop_copy)
                child = self.mutate(child)
                parent[:] = child
            
            best_index = np.argmax(fitness)
            
            plt.title("No.{} Generation Total distances {}"\
                      .format(i, '%.3f'%total_distances[best_index]))
            self.tsp.plot_result(line_x[best_index], line_y[best_index])
            plt.savefig("{}.png".format(i))
            
            plt.pause(0.05)
            
            if i < self.n_generations - 1:
                plt.cla()