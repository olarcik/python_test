import json

file_data = open('../utils/data1.txt', 'r')
data = file_data.read()
data = json.loads(data)
print(data)
file_data.close()

print(data['Country'])
print(data['avg_temp'])

print('create a class to use one time for file reading(singleton)')
class CountryData:

    def __init__(self, file_name):
        self.__file_name = file_name
        self._data = self.__read_file()
        self.__country = self._data['Country']
        self.__avg_temp = self._data['avg_temp']
        self.__comfort = self.__is_comfortable()

    def __read_file(self):
        file_data = open(self.__file_name, 'r')
        data = json.load(file_data)
        file_data.close()
        return data

    def __is_comfortable(self):
        return self.__avg_temp > 25

    def __str__(self):
        return f'str File {self.__file_name} with data {self._data}'

    def __repr__(self):
        return f'repr File {self.__file_name} with data {self._data}'

    def __lt__(self, obj):
        return self.avg_temp <= obj.avg_temp

    def __add__(self, obj):
        return [self.data, obj.data]

    @property
    def data(self):
        return self._data

    @property
    def country(self):
        return self.__country

    @property
    def avg_temp(self):
        return self.__avg_temp

    @property
    def comfort(self):
        return self.__comfort

    @comfort.setter
    def comfort(self, value):
        self.__comfort = value

    @avg_temp.setter
    def avg_temp(self, value):
        self.__avg_temp = value


class CountryDataWithMinTemp(CountryData):

    def __init__(self, file_name):
        super().__init__(file_name)
        self.__min_temp = self._data['min_temp']

    @property
    def min_temp(self):
        return self.__min_temp

    @min_temp.setter
    def min_temp(self, value):
        self.__min_temp = value

print('data1 Object description')
data1 = CountryData('../utils/data1.txt')
print(data1.avg_temp)
data1.avg_temp = 20
print(data1.avg_temp)
print(data1.country)
print(data1.comfort)
print(data1)

print('data2 Object description')
data2 = CountryData('../utils/data2.txt')
print(data1.avg_temp)
data1.avg_temp = 25
print(data1.avg_temp)
print(data1.country)
print(data1.comfort)
print(data2)

print('data3 Object description')
data3 = CountryDataWithMinTemp('../utils/data3.txt')
print(data3.avg_temp)
print(data3.min_temp)
data3.min_temp = '-20'
print(data3.min_temp)
print(data3)

print(data1.avg_temp, data2.avg_temp)
print(data1 < data2)

print(data1)
print(data1 + data2)








