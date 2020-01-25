import csv
import sys
import re

#from numpy.distutils.fcompiler import none


class Data:
    data = []
    area = 0

    def __init__(self, x, y, month, day, ffmc, dmc, dc, isi, temp, rh, wind, rain, area):
        self.data.append(x)
        self.data.append(y)
        self.data.append(month)
        self.data.append(day)
        self.data.append(ffmc)
        self.data.append(dmc)
        self.data.append(dc)
        self.data.append(isi)
        self.data.append(temp)
        self.data.append(rh)
        self.data.append(wind)
        self.data.append(rain)
        self.area = area

    def printing(self):
        print(self.data, self.area)

class Data_set:
    data_list = []

    def __init__(self):
        data_list = []


    def read_file(self, file_name):
        with open(file_name) as csv_file:
            reader = csv.reader(csv_file)
            i = 0
            for row in reader:
                if i == 0:
                    i = i+1
                else:
                    x = float(row[0])
                    y = float(row[1])
                    month = self.__month_to_float( row[2])
                    day = self.__day_to_float( row[3])
                    ffmc = float(row[4])
                    dmc = float(row[5])
                    dc = float(row[6])
                    isi = float(row[7])
                    temp = float(row[8])
                    rh = float(row[9])
                    wind = float(row[10])
                    rain = float(row[11])
                    area = float(row[12])
                    temp1= Data(x, y, month, day, ffmc, dmc, dc, isi, temp, rh, wind, rain, area)
                    self.data_list.append(temp1)
                    print(temp1.data)


    def __month_to_float(self, month):
        if month == 'jan':
            return 1.0
        elif month == 'feb':
            return 2.0
        elif month == 'mar':
            return 3.0
        elif month == 'apr':
            return 4.0
        elif month == 'may':
            return 5.0
        elif month == 'jun':
            return 6.0
        elif month == 'jul':
            return 7.0
        elif month == 'aug':
            return 8.0
        elif month == 'sep':
            return 9.0
        elif month == 'oct':
            return 10.0
        elif month == 'nov':
            return 11.0
        elif month == 'dec':
            return 12.0

    def __day_to_float(self, day):
        if day == 'mon':
            return 1.0
        elif day == 'tue':
            return 2.0
        elif day == 'wed':
            return 2.0
        elif day == 'thu':
            return 4.0
        elif day == 'fri':
            return 5.0
        elif day == 'sat':
            return 6.0
        elif day == 'sun':
            return 7.0


d = Data_set()
d.read_file("forestfires.csv")

print(d.data_list)