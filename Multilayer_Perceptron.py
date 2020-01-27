import numpy as np
import random
from math import e
from math import sqrt

NO_OF_INPUTS = 12
BIAS = 1
class Multilayer_perceptron:



    def __init__(self,no_hidden_layer_neurons:int ) ->None :
        self.no_of_inputs = NO_OF_INPUTS
        self.no_hidden_layer_neurons =no_hidden_layer_neurons

        self.hidden_layer_weights = [] # list of lists  -- num of neurons x num of inputs
        self.output_layer_weights = []

        self.initialize_weights()

        self.hidden_layer_output=[]#this variables are to be used for back propagating
        self.output_layer_output=0
        self.input_layer_input = []

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

        input=input + [BIAS]

        self.input_layer_input= input
        output_of_hidden_layer = []
        for i in range(self.no_hidden_layer_neurons):
            weighted_sum = []
            weighted_sum = np.dot(input,self.hidden_layer_weights[i])


            output_of_hidden_layer.append(self.sigmmoid_function(weighted_sum))#activation function


        output_of_hidden_layer+=[BIAS]
        self.hidden_layer_output = output_of_hidden_layer

        perceptron_output = np.dot(output_of_hidden_layer,self.output_layer_weights)#activation function in output layer is linear y = x
        self.output_layer_output = perceptron_output
        return perceptron_output # returns aproxmated function


    def adjust_weights(self,error,lr):
        propagated_hidden_error = np.dot(self.output_layer_weights,error)
        print("error",error)
        print("wagi_przed:",self.output_layer_weights)
        print("error w hidden layer:",propagated_hidden_error)
        print(self.hidden_layer_output)

        self.output_layer_weights = np.add(self.output_layer_weights,lr * np.array(self.hidden_layer_output)*error)
        print("wagi po",self.output_layer_weights)
        """pozbywamu się biasu n k-tej pozycji potencjalnie niebezpieczne     POP"""
        self.hidden_layer_output.pop()
        list(propagated_hidden_error).pop()
        print("hidden error bez biasu",propagated_hidden_error)

        """liczymy delty"""
        #y = self.hidden_layer_output.copy()
        #one_minus_y = (np.array(y)*-1)+1
        #delta =np.multiply(np.multiply(y,one_minus_y),propagated_hidden_error)








    def sigmmoid_function(self,x)->float:

        return 1/(1 + e**(-x))

    def read__input(self, input):
        raise NotImplementedError

    def calculate_errors(self, output, expected_output):
        return expected_output - output

   # def calculate_hidden_errors(self, layer_number):


    def check_state(self):
        print("input: ",self.input_layer_input)
        print("hidden_layer_output",self.hidden_layer_output)
        print("output: ",self.output_layer_output )





