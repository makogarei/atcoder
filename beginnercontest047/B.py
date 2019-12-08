W,H,M = map(int, input().split())
maxX,minX,maxY,minY = W, 0, H ,0
for i in range(M):
  x, y, a = map(int, input().split())
  if a == 1 and x > minX:
    minX = x
  elif a == 2 and x < maxX:
    maxX = x
  elif a == 3 and y > minY:
    minY = y
  elif a == 4 and y < maxY:
    maxY = y
    
xl = maxX - minX
yl = maxY - minY
if xl > 0 and yl > 0:
  print(xl * yl)
else:
  print(0)