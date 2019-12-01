import math

n = int(input())
a = round(n/100)

ans =0
print(a)
for i in range(a):
    for j in range(a):
        for k in range(a):
            for l in range(a):
                for m in range(a):
                    for n in range(a):
                        sum = i * 100 + j * 101 + k * 102 + l * 103 + m * 104 + n * 105
                        print(sum)
                        print(i * 100 + j * 101 + k * 102 + l * 103 + m * 104 + n * 105)

