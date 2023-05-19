from keras.preprocessing.image import ImageDataGenerator
import cv2 as cv
import pandas as pd
from sklearn.model_selection import train_test_split

def LaodDataBase(TrainingPath:str, TestPath:str,batchsize=150):

    train_datagen = ImageDataGenerator(
        rescale=1./255,
        horizontal_flip=True,
        validation_split=0.2)

    training_set= train_datagen.flow_from_directory(
        TrainingPath,
        target_size=(32, 32),
        color_mode="grayscale",
        batch_size=batchsize,
        class_mode='categorical'
        )
    
    
    test_datagen = ImageDataGenerator(
            rescale=1./255)

    test_set= test_datagen.flow_from_directory(
            TestPath,
            target_size=(32, 32),
            color_mode="grayscale",
            batch_size=batchsize,
            class_mode='categorical'
            )
    
    return training_set,test_set

def LoadDataBase2(DataSet_Path:str,Images_Path:str, TestSplit=0.3):
  
  TrainSet_X, TestSet_X= [],[],[],[],
  df = pd.read_csv(DataSet_Path)
  Train, Test = train_test_split(df, test_size=TestSplit,shuffle=True)


  for path in Train["Images"]:
    img = cv.imread(Images_Path+"/"+path, cv.IMREAD_GRAYSCALE)
    img = cv.reshape(img,(32,32,1))

    TrainSet_X.append(img)

  for path in Test["Images"]:
    img = cv.imread(Images_Path+"/"+path, cv.IMREAD_GRAYSCALE)
    img = cv.reshape(img,(32,32,1))

    TestSet_X.append(img)

  TrainSet_Y = Train[["X","Y"]]
  TestSet_Y = Test[["X","Y"]]
  

  return TrainSet_X,TestSet_X,TrainSet_Y, TestSet_Y