def task_1(n):
    i = 0
    while i<=n:
        yield i
        i +=1
print(task_1(10))
def task_2():
    n = int(input())
    gen = (str(i) for i in range(n-1)if i % 2 == 0)
    result = ''
    for i in gen:
        result += i+', '

    print(result + str(n if n % 2==0 else n-1))
def task_3(n):
    gen = (i for i in range(n) if i % 3 ==0 or i % 4 == 0)
    for i in gen:
        print(i)
def task_4( a, b):
    squares = (i**2 for i in range(a,b))
    for square in squares:
        print(square)
def task_5(n):
    while n>=0:
        yield n
        n-=1





