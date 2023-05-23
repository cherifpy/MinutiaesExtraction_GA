from geneticalgorithme import *
from selection import SelectBestSolution
from parametres import *
from data import LoadDataBase
import datetime
from keras.optimizers import SGD, Adam
import os
import sys


if __name__ == "__main__":


    
    TrainSetPath =  sys.argv[1]
    TestSetPath = sys.argv[2]
    

    date = datetime.datetime.now()
    date = date.strftime("%m_%d_%H_%M_%S")


    PATHS = {
        "TextFile":f"Tests/file_{date}.txt",
        "CSVFile":f"Tests/file_{date}.csv",
        "MemorieFile":"Tests/memorie.json",
        "ResultsFile":"Tests/results.json"
    }

    f = open(PATHS["TextFile"],"w")
    f.write(f"NB_OF_GENERATION = {NB_OF_GENERATION}\nPOPULATION_SIZE = {POPULATION_SIZE}\nINPUT_SHAPE "+
            f"= {INPUT_SHAPE}\nBATCH_SIZE = {BATCH_SIZE}\nNB_EPOCHS = {NB_EPOCHS}\nELITE_FRAC = {ELITE_FRAC}\nCHILDREN_FRAC = "+
           f"{CHILDREN_FRAC}\nTEST_SIZE = {TEST_SIZE}\nPROBA_MUTATION = {PROBA_MUTATION}\n"+
           f"PROBA_CROSSOVER = {PROBA_CROSSOVER}\nVERSIONEN_CODAGE = {VERSION_ENCODAGE}\n")

    f.close()

    if not os.path.isfile(PATHS["CSVFile"]):
        columns = ["train accuracy", "test accuracy", "time"]
        csv_file = open(PATHS["CSVFile"], 'w',newline='')
        writer = csv.DictWriter(csv_file,fieldnames=columns)
        writer.writeheader()
        csv_file.close()


    TrainSet, TestSet = LoadDataBase(TrainSetPath,TestSetPath)

    Database = [[TrainSet],[TestSet]]
    optimizer = SGD(LEARNING_RATE)
    best_solution = GeneticAlgorithme(VERSION_ENCODAGE,POPULATION_SIZE,NB_OF_GENERATION,NB_PARENTS,
                                      ELITE_FRAC,CHILDREN_FRAC,optimizer,INPUT_SHAPE,Database,NB_EPOCHS,BATCH_SIZE,PROBA_CROSSOVER,PROBA_MUTATION,PATHS)
    
    
    with open(PATHS["TextFile"],'a') as file:
        file.write("Best solutions in each generation:")
        for x in best_solution:
            file.write(x)
    
    file.close()
