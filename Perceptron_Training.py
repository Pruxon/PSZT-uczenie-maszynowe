import Multilayer_Perceptron as MP



NO_HIDDEN_NEURONS = 3

class Perceptron_training:

    def __init__(self,training_data_set):
        self.data_set = training_data_set
        self.perceptron = MP.Multilayer_perceptron(NO_HIDDEN_NEURONS)



    """  
train on_one_example : to funkcja która wykonuje się tylko raz,w jednej epoce powinna być
wywyołana tyle razy ile mamy próbek(517). dostaje na wejście input wektor wejścia 12 elementów i
desired output data[12] -13 element = wielkość pożaru
"""

    def train_on_one_example(self,input,desired_output):
        observed_output = self.perceptron.estimate(input)
        error = desired_output - observed_output
        #self.perceptron.check_state()
        self.perceptron.adjust_weights(error,0.5)



