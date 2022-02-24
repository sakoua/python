import json 

with open('data.json',encoding='utf8') as f:
    data = json.load(f)
value1=["第一劑","第二劑","第三劑"]

for i in range(len(value1)):
    ans=0
    for value in data:
        if value[value1[i]]!='X':
            ans+=1
    print(f"{value1[i]}共打了{ans}個人")

    
        