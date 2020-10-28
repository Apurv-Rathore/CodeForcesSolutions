t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    ans = 0
    cur = 0
    pcur = 0
    for i in range(1,n):
        if l[i]<l[i-1]:
            if pcur == 0:
                pcur = cur
                ans+=1
                
                continue
            pcur-=1
            
            
        else:
            if i==1:
                continue
            cur+=1
    print(ans+1)
