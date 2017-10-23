import json
fin = open('fin.txt', 'r')
str = fin.read()
dict = json.loads(str)


fout = open('jsondict.json', 'w')
json.dump(dict, fout)
fout.close()
