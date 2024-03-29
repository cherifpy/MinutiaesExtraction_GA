import random
from parametres import *
import copy
def AddConvBloc(child,i=0,version="dynamic"):

    """
        Fonction d'ajout d'un bloc de convolutio
        
        paramtres:
            - child: solution a muter
            - i: l'emplacement ou le bloc sera ajouté
    """

    individual = copy.deepcopy(child)
    layer = []

    if version == "dynamic":
        if len(individual[0])<max(nb_bloc_conv_valeus):
        
            layer.append(random.choice(nb_filters_valeus))
            layer.append(random.choice(filter_size_valeus))
            layer.append(random.choice(polling_size_valeus))
            layer.append(random.choice([0,1]))

            #rand_pos = random.randint(0,len(individual[0]))

            individual[0].append(layer)
            #individual[0].insert(rand_pos,layer) 
            
    else:

        layer.append(random.choice(nb_filters_valeus))
        layer.append(random.choice(filter_size_valeus))
        layer.append(random.choice(polling_size_valeus))
        layer.append(random.choice([0,1]))

        individual[0][i] =copy.deepcopy(layer)
        
    return copy.deepcopy(individual)
  

def DelConvBloc(child,i=0,version="dynamic"):

    """
        Fonction de suppression d'un bloc de convolution

        paramtres:
            - child: solution a muter
            - i: l'emplacement ou le bloc sera ajouté

    """

    individual = copy.deepcopy(child)
    if version == "dynamic":
        if len(individual[0]) > min(nb_bloc_conv_valeus):
            rand_layer = random.randrange(0,len(individual[0]))
            del individual[0][rand_layer]

    else:
        individual[0][i] = []
        
    return copy.deepcopy(individual)

def AlterConvBloc(child,i=0,version="dynamic"):


    """
        Fonction de modification d'un bloc de convolution

        paramtres:
            - child: solution a muter
            - i: l'emplacement ou le bloc sera ajouté
    """
    individual = copy.deepcopy(child)
    if version=="dynamic":
        rand_layer = random.randrange(0,len(individual[0]))
        rand_param = random.randrange(0,len(search_space_conv))
        val_selected = random.choice(search_space_conv[rand_param])

        while val_selected == individual[0][rand_layer][rand_param]:
            val_selected = random.choice(search_space_conv[rand_param])

        individual[0][rand_layer][rand_param] = val_selected
        
    else:
        rand_param = random.randrange(0,len(individual[0][i]))
        val_selected = random.choice(search_space_conv[rand_param])
        while val_selected == individual[0][i][rand_param]:
            val_selected = random.choice(search_space_conv[rand_param])
        individual[0][i][rand_param] = val_selected
    
    return copy.deepcopy(individual)

def AddDenseLayer(child,i=0,version="dynamic"):

    """
        Fonction d'ajout une couche entierement connectée

        paramtres:
            - child: solution a muter
            - i: l'emplacement ou le bloc sera ajouté
    """
    individual = copy.deepcopy(child)
    layer = []
    if version == "dynamic":
        if len(individual[1])<max(nb_dense_layer_valeus):
            layer.append(random.choice(nb_dense_units_valeus))
            layer.append(random.choice([0,1]))

            rand_pos = random.randint(0,len(individual[1]))

            individual[1].insert(rand_pos,layer)
    else:
        layer.append(random.choice(nb_dense_units_valeus))
        layer.append(random.choice([0,1]))

        individual[1][i] = layer
    
    return copy.deepcopy(individual)
  

def DelDenseLayer(child,i=0,version="dynamic"):

    """
        Fonction de suppression d'une couche entierement connectée

        paramtres:
            - child: solution a muter
            - i: l'emplacement ou le bloc sera ajouté
    """

    individual = copy.deepcopy(child)
    if version == "dynamic":
        if len(individual[1]) > min(nb_dense_layer_valeus):
            rand_layer = random.randrange(0,len(individual[1]))
            del individual[1][rand_layer]
    else:
        individual[1][i] = []
    
    return copy.deepcopy(individual)
  

def AlterDenseLayer(child,i=0,version="dynamic"):

    """
        Fonction de modification d'une couche entierement connectée

        paramtres:
            - child: solution a muter
            - i: l'emplacement ou le bloc sera ajouté
    """
    individual = copy.deepcopy(child)
    if version=="dynamic":

        rand_layer = random.randrange(0,len(individual[1]))
        rand_param = random.randrange(0,len(individual[1][0]))
        val_selected = random.choice(search_space_dense[rand_param])

        while val_selected == individual[1][rand_layer][rand_param]:
            val_selected = random.choice(search_space_dense[rand_param])

        individual[1][rand_layer][rand_param] = val_selected

    else:
        rand_param = random.randrange(0,len(individual[1][i]))
        val_selected = random.choice(search_space_dense[rand_param])
        while val_selected == individual[1][i][rand_param]:
            val_selected = random.choice(search_space_dense[rand_param])
        individual[1][i][rand_param] = val_selected

    return copy.deepcopy(individual)

def Mutation(child, proba_mutation=1, version="dynamic"):

    """
        Fonction d'application de la mutation

        parametres:
            - child: solution a muter
            - proba_mutation: la probabilité de mutation
    """
    
    if random.random() > proba_mutation:
        return copy.deepcopy(child)

    individual = copy.deepcopy(child)
    
    if version == "dynamic":
        
        rand_operation = random.choice([1,2,3])

        while (rand_operation==2 and len(individual[1]) == min(nb_dense_layer_valeus)) or (rand_operation==1 and len(individual[1]) == max(nb_dense_layer_valeus)):
            rand_operation = random.choice([1,2,3])

        if rand_operation == 1:individual = copy.deepcopy(AddDenseLayer(individual,version=version))
        elif rand_operation == 2:individual = copy.deepcopy(DelDenseLayer(individual,version=version))
        else:individual = copy.deepcopy(AlterDenseLayer(individual,version=version))

        rand_operation = random.choice([1,2,3])
        while (rand_operation==2 and len(individual[0]) == min(nb_bloc_conv_valeus)) or (rand_operation==1 and len(individual[0]) == max(nb_bloc_conv_valeus)):
            rand_operation = random.choice([1,2,3])

        if rand_operation == 1: individual = copy.deepcopy(AddConvBloc(individual,version=version))
        elif rand_operation == 2:individual = copy.deepcopy(DelConvBloc(individual,version=version))
        else: individual = copy.deepcopy(AlterConvBloc(individual,version=version))
    
    elif version == "static":

        count1, count2 = 0,0
        del_layer_conv, del_layer_dense = True,True

        for layer in individual[0]: 
            if layer == []: count1 += 1
        if count1<= min(nb_bloc_conv_valeus): del_layer_conv = False

        for layer in individual[1]:
                if layer == []:count2 += 1
        if count2<= min(nb_dense_layer_valeus): del_layer_dense = False
            

        rand_layer = random.randrange(0,max(nb_bloc_conv_valeus))

        if individual[0][rand_layer]!=[] and del_layer_conv == True:
            
            rand_operation = random.choice([1,2])
            if rand_operation == 0: individual = AlterConvBloc(individual, rand_layer,version=version)[:]
            else: individual = DelConvBloc(individual,rand_layer,version=version)[:]

        elif individual[0][rand_layer] != [] and del_layer_conv == False:
            individual = AlterConvBloc(individual, rand_layer,version=version)[:]

        else :
            individual = AddConvBloc(individual, rand_layer,version=version)[:]

        rand_layer = random.randrange(0,max(nb_dense_layer_valeus))

        if individual[1][rand_layer]!=[] and del_layer_dense== True:
            
            rand_operation = random.choice([1,2])
            if rand_operation == 0: individual = AlterDenseLayer(individual, rand_layer,version=version)[:]
            else: individual = DelDenseLayer(individual,rand_layer,version=version)[:]

        elif individual[1][rand_layer] != [] and del_layer_dense == False:
            individual = AlterDenseLayer(individual, rand_layer,version=version)[:]
        else :  individual = AddDenseLayer(individual, rand_layer,version=version)[:]     
        
    else:
        print("Erreur de version")
    return copy.deepcopy(individual)
