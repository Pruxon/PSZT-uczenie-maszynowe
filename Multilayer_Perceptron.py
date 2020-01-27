import numpy as np
import random
from math import e
from math import sqrt
from math import pow
from math import log

NO_OF_INPUTS = 12
BIAS = 1
class Multilayer_perceptron:



    def __init__(self,no_hidden_layer_neurons:int ):
        self.no_of_inputs = NO_OF_INPUTS
        self.no_hidden_layer_neurons = no_hidden_layer_neurons

        self.hidden_layer_weights = []
        self.output_layer_weights = []

        self.initialize_weights()

        self.hidden_layer_output = []
        self.output_layer_output = 0
        self.input_layer_input = []

    def initialize_weights(self):
        x = (1 / sqrt(self.no_of_inputs))

        for i in range(self.no_hidden_layer_neurons):
            weights = []
            for j in range(self.no_of_inputs + 1):  # +1 bo jeszcze bias
                weight = random.uniform(-x, x)
                weights.append(weight)
            self.hidden_layer_weights.append(weights)

            self.output_layer_weights.append(random.uniform(-1,1))
        self.output_layer_weights.append(random.uniform(-1, 1)) #dla biasu

    def estimate(self,input):

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
        return perceptron_output


    def adjust_weights(self,error,lr):

        propagated_hidden_error = np.dot(self.output_layer_weights,error)# old weights

        self.output_layer_weights = np.add(self.output_layer_weights,lr * np.array(self.hidden_layer_output)*error)

        self.hidden_layer_output.pop()# był output plus bias
        propagated_hidden_error = propagated_hidden_error[:-1]#deleting bias

        y = self.hidden_layer_output.copy()
        one_minus_y = (np.array(y)*-1)+1

        delta =np.multiply(np.multiply(y,one_minus_y),propagated_hidden_error)

        for i in range(len(self.hidden_layer_weights)):
            self.hidden_layer_weights = np.add(self.hidden_layer_weights,lr*(delta[i]) * np.array(self.input_layer_input))




    def sigmmoid_function(self,x):
        if x>100:
            return 1;
        elif x<-100:
            return -1;
        return (1/1+ pow(e,-x))
        #return 1/(1 + e**(-x))

    def read__input(self, input):
        raise NotImplementedError

    def calculate_errors(self, output, expected_output):
        return expected_output - output

    def check_state(self):
        print("input: ",self.input_layer_input)
        print("hidden_layer_output",self.hidden_layer_output)
        print("output: ",self.output_layer_output )





