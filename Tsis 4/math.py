import math
def task_1(degree):
    radian = math.radians(degree)
    return radian
print(task_1(180))
def task_2(height, base1, base2):
    area = height*(base1+base2)/2
    return area
print(task_2(5,5,6))
def task_3(n, s):
    area = (n * s ** 2) / (4 * math.tan(math.pi / n))
    return area
print(task_3(4,25))
def task_4(base, height):
    area = base*height
    return area
print(task_4(4,3))