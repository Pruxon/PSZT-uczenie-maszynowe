import Multilayer_Perceptron
import Perceptron_Training as PT
import read_file
import Divide_data as dd

"""
data_set = read_file.Data_set().read_file("forestfires.csv")


print(data_set)
"""
data_set = dd.Divided_data()
data_set.divide_data(5)


array = [1,2,3,4,5,6,7,8,9,10,11,12]
training = PT.Perceptron_training([])
training.train_on_one_example(array,8)
training.train_on_one_example(array,8)





"""


print(data_set.divided_training_data[4])
print("###################################")
print(data_set.test_data)
"""
