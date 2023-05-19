import random
from ..searchspace import *

def add_conv_layer(individual,i):
  
  layer = []
  layer.append(random.choice(nb_filters_valeus))
  layer.append(random.choice(filter_size_valeus))
  layer.append(random.choice(polling_size_valeus))
  layer.append(random.choice([0,1]))

  individual[0][i] = layer
  
  return individual
  

def del_conv_layer(individual,i):

  individual[0][i] = []
  return individual
 

def alter_conv_layer(individual,i):

  rand_param = random.randrange(0,len(individual[0][i]))
  val_selected = random.choice(search_space_conv[rand_param])
  while val_selected == individual[0][i][rand_param]:
    val_selected = random.choice(search_space_conv[rand_param])
  individual[0][i][rand_param] = val_selected
  return individual

def add_dense_layer(individual,i):

  layer = []
  
  layer.append(random.choice(nb_dense_units_valeus))
  layer.append(random.choice([0,1]))

  individual[1][i] = layer
  
  return individual
  

def del_dense_layer(individual,i):
  individual[1][i] = []
  return individual
  

def alter_dense_layer(individual,i):

  rand_param = random.randrange(0,len(individual[1][i]))
  val_selected = random.choice(search_space_dense[rand_param])
  while val_selected == individual[1][i][rand_param]:
    val_selected = random.choice(search_space_dense[rand_param])
  individual[1][i][rand_param] = val_selected

  return individual

def Mutation(individual, proba_mutation=1):

  for i, layer in enumerate(individual[0]):
    if random.random() < proba_mutation:

      if layer != []: 
        r = random.choice([1,2])
        if r == 1 : individual = alter_conv_layer(individual, i)
        else : individual = del_conv_layer(individual,i)

      elif random.random() < 0.5: individual = add_dense_layer(individual,i)
    
  for i, layer in enumerate(individual[1]):
    if random.random() < proba_mutation:

      if layer != []: 
        r = random.choice([1,2])
        if r == 1 : individual = alter_dense_layer(individual, i)
        else : individual = del_dense_layer(individual,i)

      elif random.random() < 0.5: individual = add_dense_layer(individual,i)
  
  return individual
