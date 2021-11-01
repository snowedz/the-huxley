sal = float(input())
if sal <= 5000:
    x1 = sal*1.05
elif sal > 5000 and sal < 12000:
    x1 = sal*1.12
else:
    x1 = sal
if sal < 6000.1:
    x2 = x1 + 150
else:
    x2 = x1 + 100
print('{:.2f}'.format(x2))
