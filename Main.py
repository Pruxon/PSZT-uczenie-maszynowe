import Multilayer_Perceptron
import read_file



data_set = read_file.Data_set().read_file("forestfires.csv")

print(data_set[0])
