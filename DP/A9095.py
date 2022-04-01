n = int(input())
a = [0] * 11
a[1] = 1
a[2] = 2
a[3] = 4
for i in range(4,11):
    a[i] = a[i-1] + a[i-2] + a[i-3]
for _ in range(n):
    num = int(input())
    print(a[num])
    