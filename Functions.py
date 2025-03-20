a = 1
b = 5
c = 4
d = 0

main_number = 47

def calc(num):
    if d == 0:
        print(num)
    else:
        print(num + main_number)

calc(a)
calc(b)
calc(c)

def calc_second(num):
    if d == 0:
        return num
    else:
        return num + main_number

result_calc_second = calc_second(a)
print(result_calc_second)

def sum_all(*args):

    result = 0
    for x in args:
        result += x
    return  result

print(sum_all(1,4,6))

sum_all(1,2,5,6)#

def price_list(title, price):
    print(f'Product {title} price is {price}')

price_list('iPhone', 2500)
price_list('Laptop', 4000)

def price_list_second(**kwargs):
    for title, price in kwargs.items():
       print(f'Product {title} price is {price}')

price_list_second(iphone=2500, laptop=5000, samsung=1500)


