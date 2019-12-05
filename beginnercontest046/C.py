N = int(input())
A = list()
T = list()
for i in range(N):
    x, y = map(int, input().split())
    A.append(x)
    T.append(y)
x = T[0]
y = A[0]
for i in range(1, N):
    k1 = T[i] - x
    k2 = A[i] - y
    if k1 == 0 and k2 == 0:
        continue
    l = 0
    r = 1000000000000000000
    mid = 0
    t1 = k1
    t2 = k2
    while r - l > 1:
        mid = (r + l) // 2
        k1 = T[i] * mid - x
        k2 = A[i] * mid - y
        if k1 == 0 and k2 == 0:
            t1 = 0
            t2 = 0
            break
        if k1 >= 0 and k2 >= 0:
            t1 = k1
            t2 = k2
            r = mid
        else:
            l = mid
    x += t1
    y += t2
    print("%d %d" % (x, y))
print(x + y)