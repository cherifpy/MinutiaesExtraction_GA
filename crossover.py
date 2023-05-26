import random
import copy
def CrossoverConv(parent1, parent2, proba_crossover = 0.7):
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

def CrossoverDense(parent1, parent2, proba_crossover=0.7):
    """
        Crossover applique sur la partie des couches fully connected
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

def Crossover2Parties(parent1, parent2, proba_crossover):
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


def UniformCrossover(parent1,parent2,proba_crossover):
    """
        Crossover uniforme applique sur les deux parties du chromosome 
            -  proba_crossover: la probabilité de faire un crossover
    """
    parent_1 = parent1[:]
    parent_2 = parent2[:]
    child_1, child_2 = [[],[]],[[],[]]

    for i in range(len(parent_1[0])):
        if random.random() < proba_crossover: 
            child_1[0][i] = parent_1[0][i]
            child_2[0][i] = parent_2[0][i]
        else : 
            child_1[0][i] = parent_2[0][i]
            child_2[0][i] = parent_1[0][i]

    for i in range(len(parent_1[1])):
        if random.random() < proba_crossover: 
            child_1[1][i] = parent_1[1][i]
            child_2[1][i] = parent_2[1][i]
        else : 
            child_1[1][i] = parent_2[1][i]
            child_2[1][i] = parent_1[1][i]

    return child_1,child_2
