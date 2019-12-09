x = input()
ct =0
for name, name1 in zip(x, x[::-1]):
    if(name !=name1):
        ct = ct+1


print(int(ct/2))