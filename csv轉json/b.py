import json 

with open('data.json',encoding='utf8') as f:
    data = json.load(f)
for o in range(1,3):
    for i in range(len(data)):
        print() 