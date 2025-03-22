my_list = [1, 2 ,3 , 5, 8, 0]

def filter_items(x):
    if x % 2 == 0:
        return True
    else:
        return False

new_list2 = filter(filter_items, my_list)
print(list(new_list2))

my_list = [1, 7 ,3 , 2, 8, 0, 10]

def filter_items(x):
    return  x % 2 == 0

new_list2 = filter(filter_items, my_list)
print(list(new_list2))

my_list = [1, 7 ,3 , 2, 8, 0, 10]

new_list2 = filter(lambda x: x % 2 == 0, my_list)
print(list(new_list2))

