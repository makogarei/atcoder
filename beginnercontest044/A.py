n = int(input())
k = int(input())
x = int(input())
y = int(input())

sum = 0
if (n>k):
    sum = k*x + (n-k)*y
else:
    sum = n* x

print(sum)