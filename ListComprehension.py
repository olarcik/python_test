my_list = [1, 2, 3, 4, 5, 6, 7, 8, 10]

new_list = []
for x in my_list:
    new_list.append(x * 2)

print(new_list)

#Lambda example
lambda_new_list = map(lambda x: x * 2, my_list)

print(list(lambda_new_list))


#List comprehension
list_comprehension = [x * 2 for x in my_list]

print(list_comprehension)

#Filters with comprehension example
my_list2 = [1, 2, 3, 7, 9, 4]

#simple
new_list2 = []
for x in my_list2:
    if x % 2 == 0:
        new_list2.append(x)

#lambda
new_list_labmda2 = filter(lambda x: x % 2 == 0, my_list2)

#comprehensio list
new_list_comprehension_filter = [x for x in my_list2 if x % 2 ==0]
new_list_comprehension2 = [x if x % 2 == 0 else x + 1 for x in my_list2]
new_list_comprehension_ternar = [x if x % 2 == 0 else print(f'{x} is not even' or x in my_list2)]
new_generator = (x for x in my_list2 if x % 2 == 0)

print(new_list2)
print(list(new_list_labmda2))
print(new_list_comprehension_filter)

#Dictionary
data = [('one', 'two'), ('four', 'three')]
new_dict = dict(data)
print(new_dict)

countries = ['USA', 'Hawaii', 'Cuba']
temps = [2, 33, 45]
country_temps_dict = dict(zip(countries, temps))
print(country_temps_dict)