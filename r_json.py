import json

f=open("test.json","r")
x=f.read()
finaldata=json.loads(x) # convert to json to dictionary
print(finaldata)

for i in finaldata:
    print(i['name'])

