import random
import numpy as np
import copy

def SelectNextGeneration(population = [],children=[],generation_size=10, elite_frac = 0.5, children_frac = 0.5):
  
    nb_population = int(generation_size*elite_frac)
    nb_children = int(generation_size*children_frac)

    population_sorted = sorted(population, key=lambda x: x[1], reverse=True)  

    next_generation = []
    next_generation +=  [copy.deepcopy(indiv[0]) for indiv in population_sorted[0:nb_population]]
    """print("selected individus:")
    for indi in next_generation:
        print(indi)"""
    next_generation += copy.deepcopy(list(random.sample(children,nb_children)))

    if (nb_population+nb_children) < generation_size :
        nb_random_indivs = int((1 - (elite_frac+children_frac)) * generation_size)

        for i in range(nb_random_indivs):
            random_number = random.sample(list(population.keys()),nb_random_indivs)

    return next_generation

def SelectBestSolution(population = []):
    sorted_population = sorted(population, key=lambda x: x[1])
    return sorted_population[-1]


def BestRankedSelection(nb_parents, population:list):

    population_sorted = sorted(population, key=lambda x: x[1],reverse=True)
    parents  = [parent[:] for parent in [indiv[0][:] for indiv in population_sorted]][0:nb_parents]
    
    return parents

def rank_selection(population, num_parents):
    fitness = [individual.fitness for individual in population]
    rank = np.argsort(np.argsort(fitness))[::-1]
    selected_parents = []
    for i in range(num_parents):
        rand = np.random.randint(0, sum(range(len(rank)))+1)
        for j in range(len(rank)):
            rand -= j
            if rand < 0:
                selected_parents.append(population[rank[j]])
                break
    return selected_parents

def random_selection(population, nb_parents):
    selected = []
    parents = []
    for i in range(nb_parents):
        r = random.randint(0,len(population))
        while r in selected:
            r = random.randint(0,len(population))
    
        selected.append(r)
        parents.append(list(population.keys())[r])
  
    return parents


def SelectionAphaBeta(population,children, alpha, beta):
    
    pass