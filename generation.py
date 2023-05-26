import random
from models import *
from parametres import *
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
        
    except:
        return 0,0,0
    
    
    return train_acc,test_loss,test_acc

def EvaluatePopulation(version_endcodage,population = [], optimizer = None,input_shape=(),
                        DataBase=[], nb_epochs = 15,
                        batch_size = 50,paths:dict = None):

    evaluation = []
    if len(DataBase[0]) != 0: 
        
        for i,individual in enumerate(population):
            print("Evaluation individu: ",i)
            
            train_acc, fitness, time_, exist = CheckInMemorie(paths["MemorieFile"],individual)
            
            if not exist:

                debut = time.time()
                train_acc, test_loss, fitness = Fitness(version_endcodage,optimizer=optimizer, individual = individual,input_shape=input_shape,
                                        train_set=DataBase[0],test_set=DataBase[1],nb_epochs=nb_epochs,batch_size=batch_size)
                #evaluated_population[tuple(individual)] = fitness
                fin = time.time()
                time_ = fin-debut
                AddToMemorie(paths["MemorieFile"], individual,train_acc,fitness, time_)

            data = {"train accuracy":round(train_acc,4),"test accuracy":round(fitness,4),"time":round(time_,2)}
            WriteOnCSV(paths["CSVFile"],data)
            
            AddToResults(paths["ResultsFile"],i,individual,round(fitness,4),round(train_acc,4),round(time_,4),round(time_/nb_epochs,4))

            evaluation.append((copy.deepcopy(individual),fitness))

            with open(paths["TextFile"],"a") as f:
                f.write(f"{individual}\n")
            f.close()
    
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
                return data[list]["train_acc"], data[list]["fitness"],data[list]["time"], True
    
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        with open(file_path,'w') as file:
            file.close()
     
    return 0,0,0, False


def AddToResults(file_path:str,nb_gener, individual, fitness,train_acc, time, time_per_epoch):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        newkey =  f"individual{len(data)+1}"

        data[newkey] = {
            "individual": individual,
            "generation":nb_gener,
            "train_acc":train_acc,
            "fitness":fitness,
            "time":time,
            "time_per_epoch": time_per_epoch 
        }

        with open(file_path,"w") as file:
            json.dump(data,file)
    except(json.decoder.JSONDecodeError):
        
        data = {"individual1": {
            "individual": individual,
            "generation":nb_gener,
            "train_acc":train_acc,
            "fitness":fitness,
            "time":time,
            "time_per_epoch": time_per_epoch 
        }}

    with open(file_path,"w") as file:
        json.dump(data,file)