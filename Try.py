import datetime

def calc(x, y):
    try:
        return int(x) / int(y)
    except ZeroDivisionError:
        print('Divission by zero is not posible')
    except ValueError:
        print('Must be introduced numbers')


print(calc(input('First number: '), input('Second number: ')))


def new_calc(x, y):
    try:
        return int(x) / int(y)
    except (ZeroDivisionError, ValueError) as err:
        print(err)
        print(x, y)
        raise err
        #print('Wrong data')


print(new_calc(input('First number: '), input('Second number: ')))

now = datetime.datetime.now()
print(now)
today_midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
after_midnight = now - today_midnight
print(after_midnight.seconds)
now + datetime.timedelta(hours=10)


