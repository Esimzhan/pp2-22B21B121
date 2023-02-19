import json
file = open("sample-data.json","r")
parsingf = file.read()
file.close()
data = json.loads(parsingf)
lento = 0
example = '''
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
'''
print(example)
for element in data["imdata"]:
    dn = element['l1PhysIf']["attributes"]["dn"]
    speed = element['l1PhysIf']["attributes"]["speed"]
    MTU = element['l1PhysIf']["attributes"]["mtu"]
    lento = 72 - len(dn)
    print("{}{}{}   {}".format(dn," "*lento,speed, MTU))