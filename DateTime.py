import datetime

my_time = '2023/06/05 12 hours, 30 mins, 10 sec'

python_date = datetime.datetime.strptime(my_time, '%Y/%m/%d %H hours, %M mins, %S secs')

print(python_date)
print(python_date.month)


hume_date = python_date.strftime('Year: %y , month: %B, day: %d')
print(hume_date)