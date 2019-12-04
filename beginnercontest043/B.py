s=input()

a=''
for x in s:
  if x=='0':
    a+='0'
  elif x=='1':
    a+='1'
  else:
    # 文字列が空でない場合、末尾を削除
    if a!='':
      a=a[:-1]

# 出力
print(a)