fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From "):
        tmp_lst = line.split()
        print(tmp_lst[1])
        count += 1
print("There were", count, "lines in the file with From as the first word")
