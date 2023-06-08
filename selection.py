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


def BestRankedSelection(proba_parents, population:list):
    nb_parents = int(len(population)*proba_parents)
    population_sorted = sorted(population, key=lambda x: x[1],reverse=True)
    parents  = [parent[:] for parent in [indiv[0][:] for indiv in population_sorted]][0:nb_parents]
    
    return parents

def RouletteWheelSelection(population,  proba_parents):
    nb_parents = int(len(population)*proba_parents)
    fitness_values = [fit[1] for fit in population]
    total_fitness = sum(fitness_values)
    probabilities = [fitness / total_fitness for fitness in fitness_values]
    selected = random.choices(population, weights=probabilities, k=nb_parents)
    return selected


def RandomSelection(population, proba_parent):
    nb_parents = int(len(population)*proba_parent)
    parents = [copy.deepcopy(indiv[0]) for indiv in population]
    selected = random.choices(parents,k=nb_parents)
    return parents


def BestRankedSelectionV2(population, proba_selection):
    nb_parents = int(len(population)*proba_selection)

    population_sorted = sorted(population, key=lambda x: x[1],reverse=True)

    parents  = [parent[:] for parent in [indiv[0][:] for indiv in population_sorted]]
    ranks = list(range(1,len(parents)+1))
    #Pi = Min+(Max-Min)(rang(i)-1)/(N-1).
    probability = [rank/sum(ranks) for rank in ranks ]
    
    selected = random.choices(parents,weights=probability, k=nb_parents)
    
    return selected

def SelectionAphaBeta(population,children, alpha, beta):
    
    pass


def SelectBestSolution(population = []):

    sorted_population = sorted(population, key=lambda x: x[1])
    return sorted_population[-1]
