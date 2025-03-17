# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

my_list = [1, 3]
my_tuple = (2, 6, 9)
print(my_list)
print(my_tuple)
a, b = my_list
template = 'a si b sunt {0} si {1}'
my_text1 = template.format(a,b)
print(my_text1)
my_text = f'a = {a}, b = {b}'
print(my_text)

lll = [1,3,5,2,5,7,1,3]
print(lll)
print(lll[::-1])

text =  'my lone long string'
text2 =  'my2/lone2/long/2string'
print(text[3])
print(len(text))
print(text.index('long'))
print('long' in text)
print(text.count('long'))
print(text.find('long '))
list_from_test = text2.split('/')
print(list_from_test)