#standart function
def generate_text(text1, text2):
    return f'Text consiste of the words: {text1} and{text2}'

print(generate_text('Ivan', ' Ivanov'))

#generator function
my_list = [1, 2, 3, 4, 5, 7, 9]

for x in my_list:
    print(x)

n = 2

progression = []
num = 1
while len(progression) < 100000000:
    progression.append(num)
    num += n

def progression(limit=100):
    n = 2
    num = 1
    count = 1
    while count < limit:
        yield num
        num += n
        count += 1

count = 1
for number in progression(1000000000000000000000000000):
   if count == 10000:
       print(number)
       break
   count += 1