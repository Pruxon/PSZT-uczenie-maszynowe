import Multilayer_Perceptron
import Perceptron_Training
import read_file
import Divide_data as dd

"""
data_set = read_file.Data_set().read_file("forestfires.csv")


print(data_set)
"""
data_set = dd.Divided_data()
data_set.divide_data(5)
print(data_set.divided_data[4])
print("###################################")
print(data_set.divided_data[2])
