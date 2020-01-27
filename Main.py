import Multilayer_Perceptron
import Perceptron_Training as PT
import read_file
import Divide_data as dd
from math import log

"""
data_set = dd.Divided_data()
data_set.divide_data(5)
print(data_set.divided_data[0][0])



array = [1,2.2,3,4,5,6,7,8,9,10,11,12]
training = PT.Perceptron_training([])
for i in range(10):
    training.train_on_one_example(array,56,0.3)


"""




test = PT.Perceptron_training([])
test.train_whole_set(5, 0.3,3)



