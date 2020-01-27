import Multilayer_Perceptron as MP
import Divide_data as DD

from math import log
NO_HIDDEN_NEURONS = 3

class Perceptron_training:

    def __init__(self,training_data_set):
        self.data_set = training_data_set
        self.perceptron = MP.Multilayer_perceptron(NO_HIDDEN_NEURONS)
        self.divided_data = DD.Divided_data()




    """  
train on_one_example : to funkcja która wykonuje się tylko raz,w jednej epoce powinna być
wywyołana tyle razy ile mamy próbek(517). dostaje na wejście input wektor wejścia 12 elementów i
desired output data[12] -13 element = wielkość pożaru
"""

    def train_on_one_example(self,input,desired_output,lr):
        observed_output = self.perceptron.estimate(input)
        error = desired_output - observed_output
        print(error)
        self.perceptron.adjust_weights(error,lr)

        """
        napisac trenowanie dla wszystkich, w kazdym trainig secie, potem wyciagnac blad sredniokwadratowy
        """

    def train_whole_set(self, k_fold, lr,no_epoch):
        self.divided_data.divide_data(k_fold)
        error_sum = 0
        error = 0
        MSE=0
        for k in range(k_fold):
           for i in range(no_epoch):#wybieramy zbiór walidacyjny
                for j in range(k_fold):
                    if j!=k:
                        data = self.divided_data.divided_data[j]
                        self.train_whole_set_one_epoch(data, lr)
                data = self.divided_data.divided_data[k]
                MSE += self.validate(data)
        strata_modelu = MSE/k
        print(strata_modelu)




    def train_whole_set_one_epoch(self, data, lr):

            for i in range(len(data)):
                checked_data = [data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5],
                                data[i][6], data[i][7], data[i][8], data[i][9], data[i][10], data[i][11]]

                desired_output = data[i][12]
                observed_output = self.perceptron.estimate(checked_data)
                error = desired_output - observed_output
                self.perceptron.adjust_weights(error, lr)
            MSE = 0
            for i in range(len(data)):
                checked_data = [data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5],
                                data[i][6], data[i][7], data[i][8], data[i][9], data[i][10], data[i][11]]

                desired_output = data[i][12]
                observed_output = self.perceptron.estimate(checked_data)
                error = desired_output - observed_output
                MSE += error**2
            return MSE/len(data)

    def validate(self,data):
        MSE = 0
        for i in range(len(data)):
            checked_data = [data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5],
                            data[i][6], data[i][7], data[i][8], data[i][9], data[i][10], data[i][11]]

            desired_output = data[i][12]
            observed_output = self.perceptron.estimate(checked_data)
            error = desired_output - observed_output
            MSE += error ** 2
            print(MSE)
        return MSE / len(data)