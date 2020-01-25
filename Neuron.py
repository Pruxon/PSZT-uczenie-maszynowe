from math import e


#niedokończony   zakładam że perceptron zajmuje się tablicą

class Neuron:

    input_signal = []
    weights = []
    output = 0.0

    bias = 1

    def get_output(self) ->float:
        return self.output

    def get_input(self,input:[]):# klasa lub lista co tam będzie   ## do korekty
        self.input_signal = input

    def weigthted_summing(self) ->float:
        weighted_sum = 0
        for i in range(len(self.input_signal)):
            weighted_sum += self.weights[i]* self.input_signal[i]

        weighted_sum+= self.bias * self.weights[len(self.input_signal)] #
        return  weighted_sum


    def sigmmoid_function(self,x)->float:

        return 1/(1+ e**(-x))

    def activation_function(self,weighted_sum):
        self.output = self.sigmmoid_function(weighted_sum)

    def activation_function(self):
        self.output = self.sigmmoid_function(self.weigthted_summing())








b = Neuron()
#b.activation_function()
print(b.output)





