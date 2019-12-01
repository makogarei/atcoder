N, L = map(int, input().split())
S = []
for i in range(N):
    line = input()
    S.append(line)
S.sort()
print("".join(S))
