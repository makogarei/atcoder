n = int(input())
l0 = 2
l1 = 1
lis = []
lis.append(l0)
lis.append(l1)

for i in range(2,n+1):
    temp = lis[i-1] + lis[i-2]
    lis.append(temp)

print(lis[n])
