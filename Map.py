

my_list = [1, 2, 3, 4, 6, 7, 0]

def mult_by_2(x):
    return x * 2

new_list = map(mult_by_2, my_list)
print(list(new_list))

#лямбда функция используется когда у нас простая функция котороя выполняет одно дейтсвие
new_list_ly = map(lambda  x: x * 2, my_list)
print(list(new_list_ly))

#тернарный оператор
b = 1 if len(my_list) > 5 else 5
print(b)