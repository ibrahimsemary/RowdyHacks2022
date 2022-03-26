import pandas as pd
from pathlib import Path

keyWords = [str(x).lower() for x in input("Enter word: ").split()]
for x in keyWords:
    if x == "the":
        keyWords.remove("the")
    elif x == "or":
        keyWords.remove("or")
    elif x == "and":
        keyWords.remove("and")

keyWord = ""

for x in keyWords:
    keyWord += x + " "

path_to_file = 'SearchData.csv'
path = Path(path_to_file)
if not path.is_file():
    f = open("SearchData.csv", "w")
    f.write("Search Term\n")
    f.write(keyWord)
    f.close()
    df = pd.read_csv("SearchData.csv")
else:
    df = pd.read_csv("SearchData.csv")
    d = {"Search Term": [keyWord]}
    repeat = False
    check = df['Search Term'].values
    keyWords = keyWords.sort()
    for x in check:
        keyWordCheck = x.split()
        keyWordCheck = keyWordCheck.sort()
        raise Exception("")
        if  len(keyWords) == len(keyWordCheck):
            i = 0
            for i < len(keyWordCheck):
                i++
            repeat = True
    if(not repeat):
        newData = pd.DataFrame(data=d)
        df.append(newData)


print(df)