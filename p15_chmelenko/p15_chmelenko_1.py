a = [1]
while True:
    n = input('Input n:')
    if n.isdigit():
        n = int(n)
        break
    print('The number must be positive')
for i in range(n+1):
    print(*a)
    b = [1]
    b +=[a[k]+a[k+1] for k in range(len(a)-1)]+[1]
    a = b