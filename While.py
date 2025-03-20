i = 0

while i < 5 :
    print('Hellor')
    i += 1

while True:
    user_input = input('Enter something: ')
    if user_input == 'exit':
        break
    elif user_input == 'skip':
        continue
    elif len(user_input) > 10:
        print('Your input is too long')
    else:
        print('Input is ok')

print('Good bye!')