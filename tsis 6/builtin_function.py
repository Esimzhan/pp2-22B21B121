def task_1(list):
    a = 1
    for i in list:
        a *=i
    return a
print(task_1([1,4,5]))
def task_2(text):
    lower_case = 0
    upper_case = 0
    for i in text:
        if text.isupper():
            upper_case +=1
        elif text.islower():
            lower_case +=1
    print('''No. of Upper case characters :{}
No. of Lower case Characters :{}'''.format(upper_case, lower_case))
task_2("HlewfnlsdhJKHadfkaKHK dsfsd ")
def task_3(text):
    a = len(text)
    for i, letter in enumerate(text):
        if text[i] != text[a-i-1]:
            return False

    return True
print(task_3("abaa"))
def task_5(tuple):
    return all(tuple)
print(task_5((True, True, -23)))
def task_6(sec, number):
    from math import sqrt
    from time import sleep
    sleep(sec/1000)
    return sqrt(number)