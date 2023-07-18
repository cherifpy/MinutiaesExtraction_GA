from mutation import Mutation
from generation import *
from selection import *
from itertools import combinations
from crossover import *
import copy


def GeneticAlgorithme(version_encodage,population_size, nb_generation,proba_parents,elite_frac,
                      children_frac,optimizer,input_shape,DataBase, 
                      nb_epochs,batch_size,proba_crossover,proba_mutation,paths,model):
    
    """
        Algorithme genetique

        parametres:
            version_encodage: Version de l'encodage "static" ou "dynamic"
            population_size: Taille de la population
            nb_generation: nombre de generation "condition d'arret"
            proba_parents: probabilité des parents selectoinnés pour le croisement
            elite_frac: proabilté des meilleurs individus selectionnés pour la future generation
            children_frac: probabilité des enfants selectionés pour la future generation
            optimizer: Algorithme d'entrainement
            input_shape: Dimension des blocs
            DataBase: Données d'evaluation de chaque solution [TrainSet, TestSet]
            nb_epochs: Nombre d'epoch d'entrainemet
            batch_size: Taille de chaque batchs
            proba_crossover: probabilité de croisement
            proba_mutation: probabilité de mutation 
            paths: enplasement des fichier des resultats 
            model: numero du modéle a optimiser
    """


    best_in_generation = []
    #initalise la population aleatoirement
    population = InitPopulation(population_size,version_encodage)
    
    for i in range(nb_generation):
    
        with open(paths["TextFile"], "a") as f:
            f.write(f"Generation:{i} \n")
        f.close()

        print("Debut generation: ",i)
        population_evaluated = EvaluatePopulation(version_encodage,population=population,optimizer=optimizer,input_shape=input_shape,DataBase=DataBase, 
                                        nb_epochs=nb_epochs,batch_size=batch_size, paths=paths,nb_generation=i,model=model)
        best_in_generation.append(SelectBestSolution(population_evaluated))
        
        parents = BestRankedSelection(proba_parents,population_evaluated)
        
        #Appliquer le crossover pour cree de nouveau enfants
        new_children = []
        for parent_1, parent_2 in combinations(parents,2):
            
            #appliquer le crossover sur chaque 2 de parents
            child_1,child_2 = OnePointCrossover2Parties(parent_1,parent_2,proba_crossover)
            new_children.append(child_1)
            new_children.append(child_2)

        #Appliquer la mutation sur les enfants
        children_after_mutation = []
        for child in new_children:
            mutated_child = Mutation(copy.deepcopy(child),proba_mutation,version=version_encodage)
            children_after_mutation.append(copy.deepcopy(mutated_child))
        
        #selection la population de la future generation
        population = SelectNextGeneration(population_evaluated, children_after_mutation,population_size,elite_frac,children_frac)
        
        """        
        #Evaluer la population
        population_evaluated = EvaluatePopulation(version_encodage,population=population,optimizer=optimizer,input_shape=input_shape, DataBase=DataBase, 
                                        nb_epochs=nb_epochs,batch_size=batch_size, paths=paths)
        best_in_generation.append(SelectBestSolution(population_evaluated))
        """
    #Selectionner la meilleur solution attiente
    #best_in_generation = SelectBestSolution(population_evaluated, best_in_generation)

    return best_in_generation
