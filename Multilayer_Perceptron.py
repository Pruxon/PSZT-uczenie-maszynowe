import Neuron



#
#layer 0 :input linear
# layer 1 : hidden neurons ->sigmoid function
#  layer 2 : output linear
#
class Multilayer_perceptron:

    number_of_hidden_layer_neurons = 10
    hidden_neurons = []

    def read_training_input(self,training_input):
        raise NotImplementedError

    def initialize_weights(self):
        raise NotImplementedError

    def initialize_neurons(self):
        for i in self.number_of_hidden_layer_neurons:
            self.hidden_neurons.append(Neuron())


    def __init__(self,number_of_hidden_layer_neurons:int ) ->None :
        self.number_of_hidden_layer_neurons = number_of_hidden_layer_neurons





