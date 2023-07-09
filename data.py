from keras.preprocessing.image import ImageDataGenerator
import pandas as pd
import cv2 as cv
import numpy as np
from sklearn.model_selection import train_test_split
#from sklearn.model_selection import train_test_split
#import cv2 as cv

def LoadDataBaseM1(TrainingPath:str, TestPath:str,batchsize=150,input_size=45):
    """
        Fonction de chargement des données pour le modele de classification des blcos

        Parametres:
          TrainingPath: Emplacement des donnees d'entrainement
          TestPath: Emplacement des données de test
          batchsize:
          input_size: Taile d'un bloc
    """
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        horizontal_flip=True,
        validation_split=0.2)

    training_set= train_datagen.flow_from_directory(
        TrainingPath,
        target_size=(input_size, input_size),
        color_mode="grayscale",
        batch_size=batchsize,
        class_mode='categorical'
        )
    
    
    test_datagen = ImageDataGenerator(
            rescale=1./255)

    test_set= test_datagen.flow_from_directory(
            TestPath,
            target_size=(input_size, input_size),
            color_mode="grayscale",
            batch_size=batchsize,
            class_mode='categorical'
            )
    
    return training_set,test_set


def LoadDataBaseM2(DataSet_Path:str,Images_Path:str, TestSplit=0.2):
    
    """
        Charger les données pour le modele de detection de la minuties

        Parametres:
          Dataset_Path: L'emplacement du fichier CSV
          Images_Path: L'emplacement des blocs
          TestSplit: Le pourcentage du testset
    """

    TrainSet_X, TestSet_X= [],[]

    df = pd.read_csv(DataSet_Path)
    df.columns = ["Images","classe", "TYPE", "Orientation"]
    Train, Test = train_test_split(df, test_size=TestSplit,shuffle=True)


    one_hot_encoded_classes_train = pd.get_dummies(Train['classe'])
    df_train_encoded = pd.concat([Train, one_hot_encoded_classes_train], axis=1)

    one_hot_encoded_classes_test = pd.get_dummies(Test['classe'])
    df_test_encoded = pd.concat([Test, one_hot_encoded_classes_test], axis=1)

    
    for path in Train["Images"]:
      img = cv.imread(Images_Path+"/"+path)
      img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
      img = img/255

      TrainSet_X.append(img)

    for path in Test["Images"]:
      img = cv.imread(Images_Path+"/"+path)
      img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
      img = img/255

      TestSet_X.append(img)

    TrainSet_Y = one_hot_encoded_classes_train
    TestSet_Y = one_hot_encoded_classes_test

    TrainSet_X = np.array(TrainSet_X)
    TestSet_X = np.array(TestSet_X)
    print(f"Taille de Train {len(TrainSet_X)} {len(TrainSet_Y)}")
    print(f"Taille de Test {len(TestSet_X)} {len(TestSet_Y)}")

    return TrainSet_X,TestSet_X,TrainSet_Y, TestSet_Y