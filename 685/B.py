t=int(input())
for i in range(t):
    n,q = [int(x) for x in input().split()]
    s = list(input())
    for i in range(q):
        l,r = [int(x) for x in input().split()]
        l-=1
        r-=1
        if (s[l] in s[:l] or s[r] in s[r+1:]):
            print("YES")
        else:
            print("NO")
    
    
