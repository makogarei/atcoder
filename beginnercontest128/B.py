N = int(input())

a = [list(map(str, input().split())) for _ in range(N)]
lst = []

for i, (x, y) in enumerate(a):
    lst.append([i + 1, x, int(y)])

lst.sort(key=lambda x:(x[1], -x[2]))
for i, x, y in lst:
    print(i)