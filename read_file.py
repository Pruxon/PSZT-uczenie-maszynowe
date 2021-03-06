import csv
import types
class Data:
    def __init__(self, x, y, month, day, ffmc, dmc, dc, isi, temp, rh, wind, rain, area):
        self.x = x
        self.y = y
        self.month = month
        self.day = day
        self.ffmc = ffmc
        self.dmc = dmc
        self.dc = dc
        self.isi = isi
        self.temp = temp
        self.rh = rh
        self.wind = wind
        self.rain = rain
        self.area = area

    def printing(self):
        print(self.data, self.area)


class Data_set:
    def __init__(self):
        self.data_list = []
        self.row_number = 0

    def read_file(self, file_name):
        with open(file_name) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')

            for row in readCSV:
                tmp = row
                tmp[2] = self.month_to_float(row[2])
                tmp[3] = self.day_to_float(row[3])
                for i  in range(len(tmp)):
                    if isinstance(tmp[i], str):
                        tmp[i] =float (tmp[i])
                self.data_list.append(tmp)
                self.row_number = self.row_number+1

            return self.data_list

    def month_to_float(self, month):
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

    def day_to_float(self, day):
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

