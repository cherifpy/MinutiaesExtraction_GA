import random
from ..searchspace import *

def add_conv_layer(individual):
    if len(individual[1])<max(nb_bloc_conv_valeus):
        layer = []
        layer.append(random.choice(nb_filters_valeus))
        layer.append(random.choice(filter_size_valeus))
        layer.append(random.choice(polling_size_valeus))
        layer.append(random.choice([0,1]))

        rand_pos = random.randint(0,len(individual[0]))

        individual[0].insert(rand_pos,layer)
    
    return individual
  

def del_conv_layer(individual):
    if len(individual[0]) > min(nb_bloc_conv_valeus):
        rand_layer = random.randrange(0,len(individual[0]))
        del individual[0][rand_layer]

    return individual
 

def alter_conv_layer(individual):

    rand_layer = random.randrange(0,len(individual[0]))
    rand_param = random.randrange(0,len(individual[0][0]))
    val_selected = random.choice(search_space_conv[rand_param])

    while val_selected == individual[0][rand_layer][rand_param]:
        val_selected = random.choice(search_space_conv[rand_param])

    individual[0][rand_layer][rand_param] = val_selected

    return individual

def add_dense_layer(individual):

    if len(individual[1])<max(nb_dense_layer_valeus):
        layer = []
        
        layer.append(random.choice(nb_dense_units_valeus))
        layer.append(random.choice([0,1]))

        rand_pos = random.randint(0,len(individual[1]))

        individual[1].insert(rand_pos,layer)
    
    return individual
  

def del_dense_layer(individual):
    if len(individual[1]) > min(nb_dense_layer_valeus):
        rand_layer = random.randrange(0,len(individual[1]))
        del individual[1][rand_layer]

    return individual
  

def alter_dense_layer(individual):

    rand_layer = random.randrange(0,len(individual[1]))
    rand_param = random.randrange(0,len(individual[1][0]))
    val_selected = random.choice(search_space_dense[rand_param])

    while val_selected == individual[1][rand_layer][rand_param]:
        val_selected = random.choice(search_space_dense[rand_param])

    individual[1][rand_layer][rand_param] = val_selected

    return individual
  

def uniform_mutation(individual):
  
    rand_operation = random.choice([1,2,3])

    while rand_operation==2 and len(individual[1]) ==1:
        rand_operation = random.choice([1,2,3])

    if rand_operation == 1:individual = add_dense_layer(individual)
    elif rand_operation == 2:individual = del_dense_layer(individual)
    else:individual = alter_dense_layer(individual)

    rand_operation = random.choice([1,2,3])

    rand_operation = random.choice([1,2,3])
    while rand_operation==2 and len(individual[1]) ==1:
        rand_operation = random.choice([1,2,3])

    if rand_operation == 1: individual = add_conv_layer(individual)
    elif rand_operation == 2:individual = del_conv_layer(individual)
    else: individual = alter_conv_layer(individual)
    
    return individual
