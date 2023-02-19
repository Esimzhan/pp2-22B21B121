import datetime
def days_5 (year, month, day):
    today = datetime.date(year, month, day)
    day5 = datetime.timedelta(5)
    return today + day5
print (days_5(2023, 2, 19))
def task_2(year, month, day):
    day = datetime.date(year, month, day)
    temp = datetime.timedelta(1)
    return "Yesterday: {} Today: {} Tomorrow: {}".format(day - temp, day, day + temp)
print(task_2(2023, 2, 19))
def task_3(date):
    d = date.replace(microsecond=0)
    return d
day = datetime.datetime.today()
print(task_3(day))
def task_4(date1, date2):
    diff = date2 - date1
    return diff.total_seconds()
date1 = datetime.datetime(2022,2,18,12,00,00)
date2 = datetime.datetime(2022,2,19,12,00,00)
print (task_4(date1, date2))


