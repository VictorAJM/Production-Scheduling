T = 10**40
alpha = 0.997
cnt = 0
while T>0.1:
  cnt = cnt+1
  T *= alpha
print(cnt)