import math
t = int(input())
for _ in range(t):
    a,b = [int(x) for x in input().split()]
    s = list(input())
    cnt = float('inf')
    ans = 0
    for i in range(len(s)):
        if s[i]=='0':
            cnt+=1
        else:
            ans+=min(a,b*cnt)
            cnt=0
    print(ans)
