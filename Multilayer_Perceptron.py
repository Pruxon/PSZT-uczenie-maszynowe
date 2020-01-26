import numpy as np
import random
from math import e
from math import sqrt

NO_OF_INPUTS = 3
BIAS = 1
class Multilayer_perceptron:



    def __init__(self,no_hidden_layer_neurons:int ) ->None :
        self.no_of_inputs = NO_OF_INPUTS
        self.no_hidden_layer_neurons =no_hidden_layer_neurons

        self.hidden_layer_weights = [] # list of lists  -- num of neurons x num of inputs
        self.output_layer_weights = []

        self.initialize_weights()

        self.hidden_layer_output=[]#this variables are to be used then back propagating
        self.output_layer_output=0

    def initialize_weights(self):
        x = (1 / sqrt(self.no_of_inputs))

        for i in range(self.no_hidden_layer_neurons):    #inicjalizacja wag warstwy ukrytej
            weights = []
            for j in range(self.no_of_inputs + 1):  # +1 bo jeszcze bias
                weight = random.uniform(-x, x)
                weights.append(weight)
            self.hidden_layer_weights.append(weights)

            self.output_layer_weights.append(random.uniform(-1,1))
        self.output_layer_weights.append(random.uniform(-1, 1)) #dla biasu

    def estimate(self,input):# or predict, function that calculates output
                            #input zawiera 12 danych wejściowych dodajemy 1 jako bias

        input+=[BIAS]

        output_of_hidden_layer = []
        for i in range(self.no_hidden_layer_neurons):
            weighted_sum = []
            weighted_sum = np.dot(input,self.hidden_layer_weights[i])
            print("weighted_sum:",i,weighted_sum)

            output_of_hidden_layer.append(self.sigmmoid_function(weighted_sum))#activation function

        print("output of hidden layer",output_of_hidden_layer)

        self.hidden_layer_output = output_of_hidden_layer

        output_of_hidden_layer+=[BIAS]
        perceptron_output = np.dot(output_of_hidden_layer,self.output_layer_weights)#activation function in output layer is linear y = x
        self.output_layer_output = perceptron_output
        return perceptron_output # returns aproxmated function



    def sigmmoid_function(self,x)->float:

        return 1/(1+ e**(-x))

    def read__input(self,input):
        raise NotImplementedError






d = Multilayer_perceptron(3)
print("wynik",d.estimate([10,1,1]))


print(d.output_layer_weights)
print(d.hidden_layer_weights)


