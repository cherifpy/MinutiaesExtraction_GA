import random
import copy
def OnePointCrossoverConv(parent1, parent2, proba_crossover = 0.7):
    """
        Crossover applique sur la partie des couches convolution
            -  proba_crossover: la probabilité de faire un crossover
    """
    parent_1 = copy.deepcopy(parent1)
    parent_2 =copy.deepcopy(parent2)
    if random.random() < proba_crossover:
        child_1,child_2 = [],[]
        min_length = min(len(parent_1[0]),len(parent_2[0]))
        random_point = random.randint(0,min_length)
        child_1.append(parent_1[0][0:random_point]+parent_2[0][random_point:len(parent_2[0])])
        child_2.append(parent_2[0][0:random_point]+parent_1[0][random_point:len(parent_1[0])])
        min_length = min(len(parent_1[1]),len(parent_2[1]))
        random_point = random.randint(0,min_length)
        child_1.append(parent_1[1])
        child_2.append(parent_2[1])

        return copy.deepcopy(child_1),copy.deepcopy(child_2)
    else:
        return parent_1, parent_2

def OnePointCrossoverDense(parent1, parent2, proba_crossover=0.7):
    """
        Crossover applique sur la partie des couches entierement connectées
            -  proba_crossover: la probabilité de faire un crossover
    """
    parent_1 = copy.deepcopy(parent1)
    parent_2 =copy.deepcopy(parent2)
    if random.random() < proba_crossover:
        child_1,child_2 = [],[]
        min_length = min(len(parent_1[1]),len(parent_2[1]))
        random_point = random.randint(0,min_length)
        child_1.append(parent_1[0])
        child_2.append(parent_2[0])
        min_length = min(len(parent_1[0]),len(parent_2[0]))
        random_point = random.randint(0,min_length)
        child_1.append(parent_1[1][0:random_point]+parent_2[1][random_point:len(parent_2[0])])
        child_2.append(parent_2[1][0:random_point]+parent_1[1][random_point:len(parent_1[0])])
        

        return child_1,child_2
    else:
        return parent_1, parent_2

def OnePointCrossover2Parties(parent1, parent2, proba_crossover):
    """
        Crossover applique sur les deux parties du chromosome
            -  proba_crossover: la probabilité de faire un crossover
    """
    parent_1 = copy.deepcopy(parent1)
    parent_2 = copy.deepcopy(parent2)
    if random.random() < proba_crossover:
        child_1,child_2 = [],[]
        min_length = min(len(parent_1[0]),len(parent_2[0]))
        random_point = random.randint(0,min_length)
        child_1.append(parent_1[0][0:random_point]+parent_2[0][random_point:len(parent_2[0])])
        child_2.append(parent_2[0][0:random_point]+parent_1[0][random_point:len(parent_1[0])])
        min_length = min(len(parent_1[1]),len(parent_2[1]))
        random_point = random.randint(0,min_length)
        child_1.append(parent_1[1][0:random_point]+parent_2[1][random_point:len(parent_2[1])])
        child_2.append(parent_2[1][0:random_point]+parent_1[1][random_point:len(parent_1[1])])

        return copy.deepcopy(child_1),copy.deepcopy(child_2)
    else:
        return parent_1, parent_2



def TwoPointsCrossover2Parts(parent1,parent2,proba_crossover):
    """
        Random 2 point crossover applique sur les deux parties du chromosome 
            -  proba_crossover: la probabilité de faire un crossover
    """
    parent_1 = parent1[:]
    parent_2 = parent2[:]
    child_1, child_2 = [],[]


    if random.random()<proba_crossover:

        min_size = min(len(parent_1[0]),len(parent_2[0]))  
        if min_size == 2:
            crossover_points = [0,1]  
        
        else :
            crossover_points = random.sample(range(1,min_size), 2)
            crossover_points.sort()

        child_1.append(parent_1[0][:crossover_points[0]] + parent_2[0][crossover_points[0]:crossover_points[1]] + parent_1[0][crossover_points[1]:])
        child_2.append(parent_2[0][:crossover_points[0]] + parent_1[0][crossover_points[0]:crossover_points[1]] + parent_2[0][crossover_points[1]:])

        min_size = min(len(parent_1[1]),len(parent_2[1]))    

        if min_size == 1:
            child_1.append(parent_1[1])
            child_2.append(parent_2[1])
        
        else:
            if min_size == 2:
                crossover_points = [0,1]
            else:
                crossover_points = random.sample(range(1,min_size), 2)
                crossover_points.sort()

            child_1.append(parent_1[1][:crossover_points[0]] + parent_2[1][crossover_points[0]:crossover_points[1]] + parent_1[1][crossover_points[1]:])
            child_2.append(parent_2[1][:crossover_points[0]] + parent_1[1][crossover_points[0]:crossover_points[1]] + parent_2[1][crossover_points[1]:])

        
    else:
        child_1 = copy.deepcopy(parent_1)
        child_2 = copy.deepcopy(parent_2)
    

    return copy.deepcopy(child_1),copy.deepcopy(child_2)


def TwoPointsCrossoverConv(parent1,parent2,proba_crossover):

    """
        Random 2 point crossover applique sur la partie des blocs de convolution
            -  proba_crossover: la probabilité de faire un crossover
    """
    parent_1 = parent1[:]
    parent_2 = parent2[:]
    child_1, child_2 = [],[]


    if random.random()<proba_crossover:

        min_size = min([len(parent_1[0]),len(parent_2[0])])    
        crossover_points = random.sample(range(1,min_size), 2)
        crossover_points.sort()

        child_1.append(parent_1[0][:crossover_points[0]] + parent_2[0][crossover_points[0]:crossover_points[1]] + parent_1[0][crossover_points[1]:])
        child_2.append(parent_2[0][:crossover_points[0]] + parent_1[0][crossover_points[0]:crossover_points[1]] + parent_2[0][crossover_points[1]:])

        child_1.append(parent_1[1])
        child_2.append(parent_2[1])



    else:
        child_1 = copy.deepcopy(parent_1)
        child_2 = copy.deepcopy(parent_2)
    

    return copy.deepcopy(child_1),copy.deepcopy(child_2)

def TwoPointsCrossoverDense(parent1,parent2,proba_crossover):
    """
        Random 2 point crossover applique sur la partie des couche entierement connectées du chromosome 
            -  proba_crossover: la probabilité de faire un crossover
    """
    parent_1 = parent1[:]
    parent_2 = parent2[:]
    child_1, child_2 = [[],[]],[[],[]]


    if random.random()<proba_crossover:
        
        child_1.append(parent_1[0])
        child_2.append(parent_2[0])

        min_size = min([len(parent_1[1]),len(parent_2[1])])    
        crossover_points = random.sample(range(1,min_size), 2)
        crossover_points.sort()

        child_1.append(parent_1[1][:crossover_points[0]] + parent_2[1][crossover_points[0]:crossover_points[1]] + parent_1[1][crossover_points[1]:])
        child_2.append(parent_2[1][:crossover_points[0]] + parent_1[1][crossover_points[0]:crossover_points[1]] + parent_2[1][crossover_points[1]:])

        

    else:
        child_1 = copy.deepcopy(parent_1)
        child_2 = copy.deepcopy(parent_2)
    

    return copy.deepcopy(child_1),copy.deepcopy(child_2)

def UniformCrossover(parent1,parent2,proba_crossover):
    """
        Crossover uniforme applique sur les deux parties du chromosome 
            -  proba_crossover: la probabilité de faire un crossover
    """
    parent_1 = parent1[:]
    parent_2 = parent2[:]
    child_1, child_2 = [[],[]],[[],[]]
    min_size = min(len(parent_1[0]),len(parent_2[0]))
    for i in range(min_size):
        if random.random() < proba_crossover: 
            child_1[0].append(parent_1[0][i])
            child_2[0].append(parent_2[0][i])
        else : 
            child_1[0].append(parent_2[0][i])
            child_2[0].append(parent_1[0][i])

    min_size = min(len(parent_1[1]),len(parent_2[1]))

    for i in range(min_size):
        if random.random() < proba_crossover: 
            child_1[1].append(parent_1[1][i])
            child_2[1].append(parent_2[1][i])
        else : 
            child_1[1].append(parent_2[1][i])
            child_2[1].append(parent_1[1][i])

    return copy.deepcopy(child_1),copy.deepcopy(child_2)
