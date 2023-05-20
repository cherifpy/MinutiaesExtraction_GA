from geneticalgorithme import *
from selection import SelectBestSolution
from data import LaodDataBase
import datetime
from keras.optimizers import SGD, Adam
import os
import sys

if __name__ == "__main__":

    NB_OF_GENERATION = 15
    POPULATION_SIZE = 20
    NB_PARENTS = 15
    INPUT_SHAPE =(32,32,1)
    BATCH_SIZE = 150
    NB_EPOCHS = 15
    ELITE_FRAC = 0.5
    CHILDREN_FRAC = 0.5
    TEST_SIZE = 0.4
    PROBA_MUTATION = 0.7
    PROBA_CROSSOVER = 0.7
    VERSION_ENCODAGE = "dynamic"
    LEARNING_RATE = 0.02
    
    TrainSetPath = sys.argv[1]
    TestSetPath = sys.argv[2]
    

    date = datetime.datetime.now()
    date = date.strftime("%m_%d_%H_%M_%S")

    FILE_NAME1 = f"Tests/file_{date}.txt"
    FILE_NAME2 = f"Tests/file_{date}.csv"
    MEMORIE_PATH = "Tests/memorie.json"

    f = open(FILE_NAME1,"w")
    f.write(f"NB_OF_GENERATION = {NB_OF_GENERATION}\nPOPULATION_SIZE = {POPULATION_SIZE}\nINPUT_SHAPE "+
            f"= {INPUT_SHAPE}\nBATCH_SIZE = {BATCH_SIZE}\nNB_EPOCHS = {NB_EPOCHS}\nELITE_FRAC = {ELITE_FRAC}\nCHILDREN_FRAC = "+
           f"{CHILDREN_FRAC}\nTEST_SIZE = {TEST_SIZE}\nPROBA_MUTATION = {PROBA_MUTATION}\n"+
           f"PROBA_CROSSOVER = {PROBA_CROSSOVER}\nVERSIONEN_CODAGE = {VERSION_ENCODAGE}\n")

    f.close()

    if not os.path.isfile(FILE_NAME2):
        columns = ["train accuracy", "test accuracy", "time"]
        csv_file = open(FILE_NAME2, 'w',newline='')
        writer = csv.DictWriter(csv_file,fieldnames=columns)
        writer.writeheader()
        csv_file.close()


    TrainSet, TestSet = LaodDataBase(TrainSetPath,TestSetPath)

    optimizer = SGD(LEARNING_RATE)
    best_solution = GeneticAlgorithme(VERSION_ENCODAGE,POPULATION_SIZE,NB_OF_GENERATION,NB_PARENTS,
                                      ELITE_FRAC,CHILDREN_FRAC,optimizer,INPUT_SHAPE,[TrainSet],
                                      [TestSet],NB_EPOCHS,BATCH_SIZE, FILE_NAME1,FILE_NAME2,
                                      MEMORIE_PATH,PROBA_CROSSOVER,PROBA_MUTATION)
    print("Best Solution: ",best_solution)