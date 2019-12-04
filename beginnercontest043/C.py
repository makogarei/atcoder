def calcCost(ave_num, num):
    cost = (num - ave_num) ** 2
    return cost
 
N = int(input())
numbers = [int(i) for i in input().split()]
 
if len(set(numbers)) == 1:
    print(0)
else :
    
    ave_num = round(sum(numbers) / N)
 
    total_cost = 0
    for num in numbers:
        total_cost += calcCost(num, ave_num)
    
    print(total_cost)