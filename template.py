#1要素を文字列で受け取る
x = input()

#数値にしておく
x = int(input())

#複数要素を分割してそれぞれ文字列として受け取る
#入力例:1 2 3
x,y,z = input().split()

#数値にしておく(map関数)
x,y,z = map(int, input().split())

#分割してリストに入れておく
lis = input().split()

#数値にしてリストに入れておく
lis = list(map(int, input().split()))

#普通にfor文で回す
num = int(input())
for _ in range(num):
    print(input())

#当然こうも書ける
for _ in range(int(input())):
    print(input())

#N行をリストに入れておきたい場合
lis = []
for _ in range(int(input())):
    lis.append(input())

#内包表記を使ってこう書ける
lis = [input() for _ in range(int(input()))]

#例えば標準入力が以下の場合、
#組み合わせてこう書ける
lis = [list(map(int, input().split())) for _ in range(int(input()))]

# a〜z
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
