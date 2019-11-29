list = [1,3,5,8]
num = 0
input_num = int(input())
try:
    print(list.index(input_num))
except ValueError:
    for i in range(len(list)-1):
        if((input_num >int(list[i])) and (input_num<int(list[i+1]))):
            print(i)
            break
        else:
            print(len(list))
            break

