import json

myfile = open("data.json", "r")
data = json.load(myfile)
for i in data["search_results"]:
    print(i["title"])
    print(i["prices"])
