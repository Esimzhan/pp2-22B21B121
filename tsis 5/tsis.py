import re
def task_1(txt):
    patern = r"a(0|b+)"
    return re.search(patern, txt)
print(task_1("helloabbbjls"))
def task_2(txt):
    pattern = r"abbb?"
    return re.search(pattern, txt)
print(task_2("heabbbb"))
def task_3(txt):
    pattern = r"[a-z]+_[a-z]+"
    return re.findall(pattern,txt)
print(task_3("adf_adf adsfA_afdsl_adffd"))
def task_4(txt):
    pattern = r"[A-Z][a-z]+"
    return re.search(pattern, txt)
print(task_4("Hello world"))
def task_5(txt):
    pattern = r"a..*b"
    return re.search(pattern, txt)
print(task_5('gsgsafsldkjfbdsfl'))
def task_6(txt):
    return re.sub("[ .,]",":", txt)
print(task_6("asdf.dsf,af asdf gs  "))
def task_7(txt):
    return ''.join(x.capitalize() or '_' for x in txt.split('_'))
print(task_7('pyton_exersise'))
def task_8(txt):
    pattern = r"[A-Z][a-z]*"
    return re.findall(pattern, txt)
print(task_8('HelloWorld'))
def task_9(txt):
    list = task_8(txt)
    return " ".join(list)
print(task_9('HelloWorld'))
def task_9_2(txt):
    return re.sub(r"(\w)([A-Z])",r"\1 \2",txt)
print(task_9_2("HellloWorld"))
def task_10(txt):
    r1 = task_9_2(txt)
    result = re.sub(' ','_',r1)
    return result.lower()
print(task_10("HelloPython"))
