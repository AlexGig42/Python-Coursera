fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
accs = dict()
for line in fh:
    if line.startswith("From "):
        tmp_lst = line.split()
        accs[tmp_lst[1]] = accs.get(tmp_lst[1], 0) + 1
m_val = 0
for k,v in accs.items():
    if v > m_val:
        m_val = v
        m_key = k
print(m_key,m_val)
