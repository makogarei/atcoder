# a〜z
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# 入力
w=input()

for x in l:
  if w.count(x)%2!=0:
    print('No')
    exit()

# 出力
print('Yes')