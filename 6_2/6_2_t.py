text = "X-DSPAM-Confidence:    0.8475";
spos = text.find(":")
num = text[spos+1:]
res = float(num)
print(res)
