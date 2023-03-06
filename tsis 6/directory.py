import os
def task_1(path):
    ldir = []
    lfile = []
    for name in os.listdir(path):
        if os.path.isdir(os.path.join(path, name)):
            ldir.append(name)
        else:
            lfile.append(name)
    return ldir, lfile
print(task_1(os.getcwd()))
def task_2(path):
    exists = str(os.access(path, os.F_OK))
    readable = str(os.access(path, os.R_OK))
    writeable = str(os.access(path, os.W_OK))
    executable = str(os.access(path, os.X_OK))
    return '''
Excist: {}
Readable: {}
Writeable: {}
Executable: {}'''.format(exists, readable, writeable, executable)
print(task_2("C:\PP2"))
def task_3(path):
    if os.path.exists(path):
        name_file = os.path.basename(path)
        name_dir = os.path.dirname(path)
        return "file name: {}    dir name: {}".format(name_file, name_dir)
    else:
        return "this path does not exists"
print(task_3(os.getcwd()))