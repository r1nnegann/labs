import json

with open('sample-data.json') as file:
    data = json.load(file)

print("Interface Status")
print("=========================================================================================")
print("DN                                                 Description           Speed      MTU  ")
print("-------------------------------------------------- --------------------  --------  ------")

for i in data['imdata']:
    print(f"{i['l1PhysIf']['attributes']['dn'].ljust(52)}{i['l1PhysIf']['attributes']['descr'].ljust(21)}{i['l1PhysIf']['attributes']['speed'].ljust(11)}{i['l1PhysIf']['attributes']['mtu']}")
