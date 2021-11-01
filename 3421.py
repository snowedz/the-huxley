num = input()
x, ser = num.split()
x = float(x)
ser = int(ser)
fat = int(1)
n = 1
nrdor = 0
if x == 1 and ser == 1:
    print(1)
else:
    for n in range(1, ser, 1):
        fat *= n
        nrdor += (x ** n) / (fat)
x = nrdor + 1
print('{:.5f}'.format(x))
