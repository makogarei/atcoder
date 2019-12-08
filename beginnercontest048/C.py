N, x = list(map(int, input().split()))
arr = list(map(int, input().split()))

cnt, prv = 0, 0

for i in range(N):
    diff = max(arr[i] + prv - x, 0)
    cnt += diff
    arr[i] -= diff
    prv = arr[i]

print(cnt)