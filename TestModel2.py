from models import Model45Net
from parametres import *
from data import *
from keras.optimizers import SGD


ImagesSet = "../DatabaseM2/Images"
LablesSet = "../DatabaseM2/Lables.csv"

TrainSet_X,TestSet_X,TrainSet_Y, TestSet_Y = LoadDataBase3(ImagesSet,LablesSet,TestSplit=0.3)


optimizer = SGD(LEARNING_RATE)
model = Model45Net()

history = model.fit(x = TrainSet_X,y=TrainSet_Y, batch_size=200, epochs=20,verbose=0)

# validation_split=validation_split,
train_acc = history.history['accuracy'][-1]
test_loss, test_acc = model.evaluate(x = TestSet_X,y=TestSet_Y)

print(test_loss, test_acc)