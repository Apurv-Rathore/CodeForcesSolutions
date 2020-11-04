import math
t = int(input())
for _ in range(t):
    n = int(input())
    x = 4*n
    for i in range(n):
        print(x,end=' ')
        x-=2
    print()
