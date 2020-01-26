import read_file as rf



class Divided_data:
    def __init__(self):
        self.divided_training_data = []
        self.test_data = []

    def divide_data(self, division_number):
        full_data_set = rf.Data_set()
        full_data_set.read_file("forestfires.csv")
        row_number = full_data_set.row_number
        row_modulo = row_number % (division_number + 1)
        row_number_without_rest = row_number-row_modulo
        iteration_amount = row_number_without_rest / (division_number + 1)
        iteration_amount = int(iteration_amount)
        for i in range(division_number):
            training_list = []
            self.divided_training_data.append(training_list)
        iterator = 0
        print(full_data_set.data_list)
        for i in range(iteration_amount):
            for j in range(division_number):
                self.divided_training_data[j].append(full_data_set.data_list.pop(0))
                iterator = iterator+1
            self.test_data.append(full_data_set.data_list.pop(0))
        if row_modulo != 0:
            for i in range(row_modulo):
                self.divided_training_data[i].append(full_data_set.data_list.pop())
