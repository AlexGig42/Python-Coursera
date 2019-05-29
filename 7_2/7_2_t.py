# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
quant = 0.0
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        pos = line.find(":")
        quant += float(line[pos + 1:])
        print(line[pos + 1:].rstrip())
        count += 1
        print(line.rstrip())
print("Summ - ",quant)
print("Count - ",count)
avrg = quant / count
print("Average spam confidence:",avrg)
