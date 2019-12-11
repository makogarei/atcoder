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

#bit全探索（https://qiita.com/gogotealove/items/11f9e83218926211083a）
#みかん（100円）りんご（200円）ぶどう（300円）がそれぞれ1つずつ果物屋さんにありました。財布の中には300円ありますが、考え得るすべての買い物パターンを列挙しなさい。
money = 300
item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
n = len(item)
for i in range(2 ** n):
    bag = []
    total = 0
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            bag.append(item[j][0])  # フラグが立っていたら bag に果物を詰める
            total += item[j][1]  # 買い物累計額にも加算
    if (total <= money):
        print(total, bag)

#bit全探索（https://blog.rossywhite.com/2018/08/06/bit-search/）
A = [0, 1, 2, 3]
n = len(A)
for i in range(2**n):
    output = []
    for j in range(len(A)):
        if ((i >> j) & 1) == 1:
            output.append(A[j])
    print(output)

