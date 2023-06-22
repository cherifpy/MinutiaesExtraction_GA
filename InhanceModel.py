from data import *
import datetime
from keras.optimizers import SGD, Adam
import sys
from models import *
import pandas as pd

if __name__ == "__main__":

    csv_file = sys.argv[1]
    image_path = sys.argv[2]

    TrainSet_X,TestSet_X,TrainSet_Y, TestSet_Y = LoadDataBaseWithNormal(csv_file,image_path)

    individu = [[[512, 9, 0, 1], [128, 11, 2, 1], [128, 11, 2, 1], [512, 5, 3, 1], [128, 7, 0, 1], [256, 5, 5, 1]], [[512, 1], [512, 0], [512, 0]]]

    optimizer = SGD(0.02)

    model = ModelAvecregul(optimizer,(45,45,1),nb_classe=9,individual=individu,version="dynamic")

    history = model.fit(x = TrainSet_X,y = TrainSet_Y, batch_size=200, epochs=500,verbose=0)

    history_df = pd.DataFrame(history.history)

    history_df.to_csv('history.csv', index=False)
