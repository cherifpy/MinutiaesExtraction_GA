import random
from models import *
from searchspace import *
import time
import csv
import copy
import json

def InitPopulation(population_size,version="dynamic"):

    population = []
    individual = []
    conv_layers =  []
    layer = []
    dense_layers = []

    for i in range(0,population_size):
    
        conv_layers =  []
        nb_conv_layers = random.choice(nb_bloc_conv_valeus)
        for j in range(nb_conv_layers):
            layer.append(random.choice(nb_filters_valeus))
            layer.append(random.choice(filter_size_valeus))
            layer.append(random.choice(polling_size_valeus))
            layer.append(random.choice([0,1])) #Choixe d'ajouter ou pas une couche d'activation
            conv_layers.append(layer)
            layer = []
        
        if version == "static":
            for i in range(nb_conv_layers, max(nb_bloc_conv_valeus)):
                conv_layers.append([])
        
        individual.append(conv_layers)
        
        dense_layers = []
        nb_dense_layers = random.choice(nb_dense_layer_valeus)
        for j in range(nb_dense_layers):
            layer.append(random.choice(nb_dense_units_valeus))
            layer.append(random.choice([0,1])) #Choix d'ajouter ou pas une couche d'activation
            dense_layers.append(layer)
            layer=[]
        
        if version =="static":
            for i in range(nb_dense_layers, max(nb_dense_layer_valeus)):
                dense_layers.append([])

        individual.append(dense_layers)

        population.append(individual)
        print(copy.deepcopy(individual))
        individual = []

    return population

def Fitness(version_encodage,individual,optimizer=None,input_shape=(),
                     nb_classe=2,train_set = [],
                     test_set=[],nb_epochs = 4, 
                     batch_size = 100,validation_split = 0.2):
    try:
        
        model = CreateModel1(optimizer=optimizer,input_shape=input_shape,
                             nb_classe=nb_classe,individual=individual,version=version_encodage)
        history = model.fit(x = train_set[0], batch_size=batch_size, epochs=nb_epochs,verbose=0)
        # validation_split=validation_split,
        train_acc = history.history['accuracy'][-1]
        test_loss, test_acc = model.evaluate(test_set[0], steps=len(test_set[0]))
        #print(f"test loss:{test_loss}, test accuracy:{test_acc}")
    except:
        return 0,0,0
    
    
    return train_acc,test_loss,test_acc

def EvaluatePopulation(version_endcodage,population = [], optimizer = None,input_shape=(),
                        train_set = [], test_set=[], nb_epochs = 15,
                        batch_size = 50,file_path1=None,file_path2=None,memorie_path=None):

    evaluation = []
    if len(train_set) != 0: 
        
        for i,individual in enumerate(population):
            print("Evaluation individu: ",i)
            
            train_acc, fitness, time_, exist = CheckInMemorie(memorie_path,individual)
            
            if not exist:

                debut = time.time()
                train_acc, test_loss, fitness = Fitness(version_endcodage,optimizer=optimizer, individual = individual,input_shape=input_shape,
                                        train_set=train_set,test_set=test_set,nb_epochs=nb_epochs,batch_size=batch_size)
                #evaluated_population[tuple(individual)] = fitness
                fin = time.time()
                time_ = fin-debut
                AddToMemorie(memorie_path, individual,train_acc,fitness, time_)

            data = {"train accuracy":round(train_acc,4),"test accuracy":round(fitness,4),"time":round(time_,2)}
            WriteOnCSV(file_path2,data)

            evaluation.append((copy.deepcopy(individual),fitness))

            with open(file_path1,"a") as f:
                f.write(f"{individual}\n")
            f.close()
            print(f"Train accuracy:{round(train_acc,4)} Test accuracy:{round(fitness,4)} temp: {round(time_,2)}")
    return evaluation




def WriteOnCSV(file_path, data):
    file = open(file_path, "a",newline='')
    writer = csv.DictWriter(file, fieldnames=list(data.keys()))
    writer.writerow(data)
    file.close()

def AddToMemorie(file_path, individual, train_acc,fitness,time):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        newkey =  f"individual{len(data)+1}"

        data[newkey] = {
            "individual": individual,
            "train_acc":train_acc,
            "fitness":fitness,
            "time":time
        }

        with open(file_path,"w") as file:
            json.dump(data,file)
    except(json.decoder.JSONDecodeError):
        
        data = {"individual1": {
            "individual": individual,
            "train_acc":train_acc,
            "fitness":fitness,
            "time":time
        }}

        with open(file_path,"w") as file:
            json.dump(data,file)

def CheckInMemorie(file_path:str, individu):
    
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        for list in data:
            if data[list]["individual"] == individu:
                print("Trouvé", individu)
                return data[list]["train_acc"], data[list]["fitness"],data[list]["time"], True
    
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return 0,0,0,False 
     
    return 0,0,0, False
