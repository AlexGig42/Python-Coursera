import re

fhandle = open("regex_sum_220540.txt")
list_of_int = list()
for line in fhandle:
    line = line.rstrip()
    if len(re.findall("[0-9]+",line)) == 0: continue
    #print(len(re.findall("[0-9]+",line)))
    tmp = re.findall("[0-9]+",line)
    #print(tmp)
    for x in tmp:
        val = int(x)
        list_of_int.append(val)
summary = sum(list_of_int)
#print(list_of_int)
print(summary)
