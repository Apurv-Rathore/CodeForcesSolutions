def solve(idx,T):
    if (idx==n):
        return 0
    if (T>2*n):
        return 100000000
    if dp[idx][T]!=-1:
        return dp[idx][T]
    ans = 100000000
    ans = min(ans,solve(idx,T+1))
    ans = min(ans,abs(T-l[idx])+solve(idx+1,T+1))
    dp[idx][T] = ans
    return dp[idx][T]
    
t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    dp = [[-1 for i in range(500)] for j in range(500)]
    print(solve(0,1))
