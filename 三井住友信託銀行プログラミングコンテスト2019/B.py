import math

# Input the amount of money Takahashi paid
N = int(input())

# Find nearest integer price more than or equal to X/1.08
X = math.ceil(N / 1.08)

# Check if the "taxed price" is equal to N yen
if math.floor(X * 1.08) == N:
	print(X)
else:
	print(":(")