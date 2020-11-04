import math
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    l = []
    n= len(a)
    for i in range(n):
        l.append([a[i],b[i]])
    l.sort(reverse=True)
    ans = [max(a),sum(b)]
    s = 0
    for i in range(n-1):
        s+=l[i][1]
        #ans.append(s+l[i+1][0])
        ans.append(max(s,l[i+1][0]))
    
    print(min(ans))
