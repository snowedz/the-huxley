num = int(input())
sub = 1
vez = 0
while num > 0:
    num = num - sub
    sub = sub + 2
    vez = vez + 1
print(vez)
