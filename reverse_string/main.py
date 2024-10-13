result = []
with open('poem.txt', 'r') as poem:
    lines = poem.readlines()
    for item in lines:
        result.insert(0, item.replace("\n","")+"\n")

with open("reverse.txt", "w") as reverse:
    reverse.writelines(result)