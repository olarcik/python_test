import os.path

#simple
file = open('data.txt', 'r').read()
print(file)

#context manager
print('context manager')

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'data.txt')
new_file_path = os.path.join(base_path, 'data2.txt')

# homework_path = os.path.dirname(os.path.dirname(base_path))
# vlad_file_path = os.path.join(homework_path, 'VladFile, 'file.txt')


def read_file():
    with open(file_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line

for data_line in read_file():
    with open(new_file_path, 'a') as new_file:
        new_file.write(data_line)


