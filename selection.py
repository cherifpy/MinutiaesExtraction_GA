import random
import numpy as np
import copy

def SelectNextGeneration(population = [],children=[], elite_frac = 0.5, children_frac = 0.5):
    """
        Fonction de remplacement de la generation

        parametres:
            - population: population actuelle
            - children: solution generées apres Croisement et mutation
            - elite_frac: le pourcentage d'elites selectionnés
            - children_frac: le pourcentage d'enfants a selectionnés
    """

    generation_size = len(population)

    nb_population = int(generation_size*elite_frac)
    nb_children = int(generation_size*children_frac)

    population_sorted = sorted(population, key=lambda x: x[1], reverse=True)  

    next_generation = []
    next_generation +=  [copy.deepcopy(indiv[0]) for indiv in population_sorted[0:nb_population]]

    next_generation += copy.deepcopy(list(random.sample(children,nb_children)))

    if (nb_population+nb_children) < generation_size :
        nb_random_indivs = int((1 - (elite_frac+children_frac)) * generation_size)

        for i in range(nb_random_indivs):
            random_number = random.sample(list(population.keys()),nb_random_indivs)

    return next_generation


def BestRankedSelection(proba_parents, population:list):

    """
        Fonction de selection des meilleurs individus de la population selon la fonction fitness

        parametres:
            - proba_parents: pourcentage des individus a selectionnés
            - population: list de la population actuelle
    """

    nb_parents = int(len(population)*proba_parents)
    population_sorted = sorted(population, key=lambda x: x[1],reverse=True)
    parents  = [parent[:] for parent in [indiv[0][:] for indiv in population_sorted]][0:nb_parents]
    
    return parents

def RouletteWheelSelection(proba_parents, population:list):
    """
        Fonction de selection d'individus en utilisant la selectino en roulette

        parametres:
            - proba_parents: pourcentage des individus a selectionnés
            - population: list de la population actuelle
    """
    nb_parents = int(len(population)*proba_parents)
    fitness_values = [fit[1] for fit in population]
    total_fitness = sum(fitness_values)
    probabilities = [fitness / total_fitness for fitness in fitness_values]
    selected = random.choices(population, weights=probabilities, k=nb_parents)
    return selected


def RandomSelection(population, proba_parent):
    """
        Fonction de selection aleatoire individus de la population

        parametres:
            - proba_parents: pourcentage des individus a selectionnés
            - population: list de la population actuelle
    """
    nb_parents = int(len(population)*proba_parent)
    parents = [copy.deepcopy(indiv[0]) for indiv in population]
    selected = random.choices(parents,k=nb_parents)
    return parents

def SelectBestSolution(population = []):
    """
        Fonction de selection de la meilleure solution de la generation courante 
        parametres:
            - population: list de la population actuelle
    """
    sorted_population = sorted(population, key=lambda x: x[1])
    return sorted_population[-1]
