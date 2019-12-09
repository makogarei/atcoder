import itertools
n = int(input())
lis = list(map(int, input().split()))

sum =0
for i in itertools.permutations(lis, r=2):
    sum = sum + (i[0] ^ i[1])

print(int(sum/2) %(10**9+7))