
nb_bloc_conv_valeus = [3,4,5,6]
nb_filters_valeus = [32,64,128,256] #[10,20,30,40]
filter_size_valeus = [3,5,7,9]
nb_dense_layer_valeus = [1,2,3]
nb_dense_units_valeus = [64,128,256,512]
polling_size_valeus = [0,3,5] #Dans le cas ou c'est 0 on ajoute pas de pooling

learning_rate = [0.1,0.01,0.02,0.001,0.002,0.0001] 

search_space_conv = [nb_filters_valeus,filter_size_valeus,polling_size_valeus,[0,1]]
search_space_dense = [nb_dense_units_valeus,[0,1]]


NB_OF_GENERATION = 15
POPULATION_SIZE = 26
NB_PARENTS = 15
INPUT_SHAPE =(32,32,1)
BATCH_SIZE = 200
NB_EPOCHS = 15
ELITE_FRAC = 0.5
CHILDREN_FRAC = 0.5
TEST_SIZE = 0.4
PROBA_MUTATION = 0.7
PROBA_CROSSOVER = 0.7
VERSION_ENCODAGE = "dynamic"
LEARNING_RATE = 0.02