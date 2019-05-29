name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
freq = dict()
for line in handle:
    if not line.startswith("From "): continue
    tmp = line.split()
    #print(tmp[5])
    time = tmp[5].split(":")
    #print(time)
    freq[time[0]] = freq.get(time[0], 0) + 1
#print(freq)
res = sorted(freq.items())
for k,v in res:
    print(k,v)
