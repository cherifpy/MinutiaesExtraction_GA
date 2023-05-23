from keras.models import Model, Sequential
from keras.layers import Conv2D, Dense, Input, MaxPool2D, Dropout, Activation, Flatten
from keras.activations import relu, softmax

def CreateModel1(optimizer=None,input_shape=(),nb_classe=2, individual=[],
                    version="static",loss='categorical_crossentropy',
                    mertics="accuracy"):
    """
        Fonction de ceation du pemiere modele utilisé pour la classification des blocs
            -  Input Shape : dimension d'entré
            -  nb_classe: nombre de classe de classification dans notre cas c'est 2
            -  individual: le chromosome de l'individu
            -  version: version de l'encodage soit "dynamique" ou "statique"
            -  loss: la fonction erreur
            -  metrics: metrique d'evaluation
    """
    my_model = Sequential(name="Model")
    my_model.add(Input(shape=input_shape))
    #my_model.add(Reshape((28,28,1)))

    conv_layers = individual[0]
    dense_layers = individual[1]

    if version=="dynamic":
        for i,layer in enumerate(conv_layers):
            my_model.add(Conv2D(layer[0], layer[1], name=f'conv{i}',padding="same")) #Add conv parameters
            if layer[3] == 1: my_model.add(Activation(relu))
            if layer[2] != 0: my_model.add(MaxPool2D((layer[2],layer[2]),padding="same"))

        my_model.add(Flatten())

        for i,layer in enumerate(dense_layers):
            my_model.add(Dense(layer[0]))
            if layer[1] == 1:  my_model.add(Activation(relu))

    elif version=="static":
        for i,layer in enumerate(conv_layers):
            if layer != []:
                my_model.add(Conv2D(layer[0], layer[1], name=f'conv{i}',padding="same")) #Add conv parameters
                if layer[3] == 1:  my_model.add(Activation(relu))
                if layer[2] != 0: my_model.add(MaxPool2D((layer[2],layer[2]),padding="same"))
    
        my_model.add(Flatten())

        for i,layer in enumerate(dense_layers):
            if layer != []:
                my_model.add(Dense(layer[0]))
                if layer[1] == 1:  my_model.add(Activation(relu))
    else:
        print("Erreur de version dans le parametre version")
    
    my_model.add(Dense(nb_classe,activation=softmax))

    my_model.compile(loss=loss, optimizer=optimizer, metrics=[mertics])

    return my_model



def CreateModel2(optimizer=None,input_shape=(),nb_features=2, individual=[],
                version="dynamique",loss='categorical_crossentropy',
                mertics="accuracy"):
    """
        Fonction de ceation du 2eme modele utilisé detecter la minuties dnas les blocs
            -  Input Shape : dimension d'entré
            -  nb_feature: nombre de parametre predire
            -  individual: le chromosome de l'individu
            -  version: version de l'encodage soit "dynamique" ou "statique"
            -  loss: la fonction erreur
            -  metrics: metrique d'evaluation
    """
    my_model = Sequential(name="Model")
    my_model.add(Input(shape=input_shape))
    #my_model.add(Reshape((28,28,1)))

    conv_layers = individual[0]
    dense_layers = individual[1]

    if version=="dynamic":
        for i,layer in enumerate(conv_layers):
            my_model.add(Conv2D(layer[0], layer[1], name=f'conv{i}',padding="same")) #Add conv parameters
            if layer[3] == 1: my_model.add(Activation(relu))
            if layer[2] != 0: my_model.add(MaxPool2D((layer[2],layer[2]),padding="same"))

        my_model.add(Flatten())

        for i,layer in enumerate(dense_layers):
            my_model.add(Dense(layer[0]))
            if layer[1] == 1:  my_model.add(Activation(relu))

    elif version=="static":
        for i,layer in enumerate(conv_layers):
            if layer != []:
                my_model.add(Conv2D(layer[0], layer[1], name=f'conv{i}',padding="same")) #Add conv parameters
                if layer[3] == 1:  my_model.add(Activation(relu))
                if layer[2] != 0: my_model.add(MaxPool2D((layer[2],layer[2]),padding="same"))
    
        my_model.add(Flatten())

        for i,layer in enumerate(dense_layers):
            if layer != []:
                my_model.add(Dense(layer[0]))
                if layer[1] == 1:  my_model.add(Activation(relu))
    else:
        print("Erreur de version dans le parametre version")
    
    my_model.add(Dense(nb_features))
    my_model.compile(loss=loss, optimizer=optimizer, metrics=[mertics])

    return my_model
