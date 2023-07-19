
"""
    Espace de recherche
"""

nb_bloc_conv_valeus = [5,6,7,8]
nb_filters_valeus = [32,64,128,256] 
filter_size_valeus = [3,5,7,9]
nb_dense_layer_valeus = [1,2,3,4]
nb_dense_units_valeus = [128,256,512]
polling_size_valeus = [0,3,4,5] #Dans le cas ou c'est 0 on ajoute pas de pooling

search_space_conv = [nb_filters_valeus,filter_size_valeus,polling_size_valeus,[0,1]]
search_space_dense = [nb_dense_units_valeus,[0,1]]


"""
    Parametres de l'algorithme genetique et l'entrainement du model
"""

MODEL_MUN = 1
NB_OF_GENERATION = 25
POPULATION_SIZE = 20
PROBA_PARENTS = 1/2

ELITE_FRAC = 0.5
CHILDREN_FRAC = 0.5

PROBA_MUTATION = 0.1
PROBA_CROSSOVER = 0.7
VERSION_ENCODAGE = "dynamic"

TEST_SIZE = 0.4
BATCH_SIZE = 200
NB_EPOCHS = 20
INPUT_SHAPE =(45,45,1)
LEARNING_RATE = 0.02
REGULARIZATION = 0.01

NB_CLASSES = 2


