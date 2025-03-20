names = ['John', 'Tom', 'Vlad', 'Daria', 'Alexandr', 'Alan']

for name in names:
    if name == 'Vlad':
        print(name + ' Aur')
    else:
        print(name + ' Buslat')

names = ['John', 'Tom', 'Vlad', 'Daria', 'Alexandr', 'Alan']

for name in names:
    if name.startswith('V'):
        print(name + ' Super', end =' ')
    print(name)

persons = {'John': 123, 'Vlad': 185, 'Daria': 432, 'Alexandr': 143}
print(persons.items())
for persons in persons.items():
    print(persons)

persons = {'John': 123, 'Vlad': 185, 'Daria': 432, 'Alexandr': 143}
print(persons.items())

for name, height in persons.items():
    print(f'{name}: {height}')

text = 'Sed vitae justo malesuada, commodo libero eu, bobendum mauris'

words = text.split()
fin_words = []
for word in words:
    if 'o' in word:
        print(word)
    else:
        fin_words.append(word)
print(' '.join(fin_words))


