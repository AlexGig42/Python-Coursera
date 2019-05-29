# romeo.txt
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    tmp_list = line.split()
    for word in tmp_list:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
