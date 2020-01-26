from math import e
from math import sqrt
import random
import numpy

#niedokończony   zakładam że perceptron zajmuje się tablicą

class Neuron:

    input_signal = []
    weights = []
    output = 0.0



    def __init__(self,number_of_input_neurons):


        self.initialize_weights(number_of_input_neurons)


    def initialize_weights(self,number_of_input_neurons):
        x = (1/sqrt(number_of_input_neurons))
        self.weights = []
        for i in range(number_of_input_neurons+1): # +1 bo jeszcze bias
            weight =random.uniform(-x,x)
            self.weights.append(weight)



    def get_output(self) ->float:
        return self.output

    def get_input(self,input:[]):# klasa lub lista co tam będzie   ## do korekty
        self.input_signal = input

    def weigthted_summing(self) ->float:
        weighted_sum = 0
        for i in range(len(self.input_signal)):
            weighted_sum += self.weights[i]* self.input_signal[i]

        weighted_sum+= Constants.BIAS * self.weights[len(self.input_signal)] #
        return  weighted_sum


    def sigmmoid_function(self,x)->float:

        return 1/(1+ e**(-x))

    def activation_function(self,weighted_sum):
        self.output = self.sigmmoid_function(weighted_sum)

    def activation_function(self):
        self.output = self.sigmmoid_function(self.weigthted_summing())


class Output_neuron(Neuron):

    def initialize_weights(self,number_of_input_neurons):
        x = 1
        self.weights = []
        for i in range(number_of_input_neurons+1): # +1 bo jeszcze bias
            weight =random.uniform(-x,x)
            self.weights.append(weight)

        def activation_function(self, weighted_sum):
            self.output = weighted_sum

        def activation_function(self):
            self.output = self.weigthted_summing()









