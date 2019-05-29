score = input("Enter Score: ")
fsc = float(score)
if fsc > 1:
    print('Error: Score out of range ( > 1.0) ')
elif fsc >= 0.9:
    print('A')
elif fsc >= 0.8:
    print('B')
elif fsc >= 0.7:
    print('C')
elif fsc >= 0.6:
    print('D')
elif fsc < 0.6 and fsc > 0:
    print('F')
else:
    print('Error: Score out of range ( <= 0.0) ')
