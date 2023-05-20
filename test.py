from generation import InitPopulation
import pickle


#population = InitPopulation(20,version="dynamic")


with open("memorie.pkl", 'rb') as file:
    list = pickle.load(file)

x = [[[256, 4, 0, 0], [256, 3, 5, 0]], [[256, 1], [64, 1]]]

for elem in list:
    print(elem)

if x in list:print("Goooooooooooood")