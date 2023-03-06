import os
def task_4(file_name):
    with open(file_name, "r")as file:
        a = len(file.readlines())
    return a
print(task_4("directory.py"))
def task_5(file_name, list):
    with open(file_name, "w")as file:
        for i in list:
            file.write("{}\n".format(i))

task_5("hello_world.txt", ["hello world", "what is going on"," doasfda"])
with open("hello_world.txt", "r")as file:
    print(file.read())
def task_6():
    letters = "abcdefghijklmnopqrstuvwxyz"
    for letter in letters:
        with open(letter + ".txt", "w")as file:
            file.write("")
task_6()

def task_7(file1, file2):
    with open(file1, "r")as file:
        text = file.read()
    with open(file2, "a")as file:
        file.write(text)
task_7("hello_world.txt", "a.txt")
def task_8(filename):
    if os.path.exists(filename):
        os.remove(filename)
task_8("z.txt")

