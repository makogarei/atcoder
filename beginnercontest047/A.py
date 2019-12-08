x,y,z = map(int, input().split())

hantei_flag = 0

if(x == (y+z)):
    hantei_flag=1
elif(y == (z+x)):
    hantei_flag=1
elif(z == (x+y)):
    hantei_flag=1

if(hantei_flag):
    print('Yes')
else:
    print('No')
