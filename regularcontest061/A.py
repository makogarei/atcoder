s = input()
n = len(s)
ans = 0
for i in range(2**n):
	l = []
	op = [""]*n
	for j in range(n):
		if ((i >> j) & 1) == 1:
			op[j] = '+'
	res = ""
	for a,b in zip(op+[""],s):
		res += a+b
	ans += eval(res)
print(ans//2)