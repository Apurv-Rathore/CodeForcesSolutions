import sys
def dfs(node):
    dp[node][0] = a[node]
    if (adj[node]==[]):
        dp[node][1]=dp[node][0]  = a[node]
        dp[node][2] = 1
        return dp[node]
    m = 0
    for child in adj[node]:
        x = dfs(child)
        dp[node][0]+=x[0]
        dp[node][2]+=x[2]
        m = max(m,x[1])
    y = dp[node]
    t = 0
    if (y[0]%y[2])!=0:
        t = 1
    dp[node][1] = max(m,y[0]//y[2]+t)
    return dp[node]

#n = int(input())
n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
adj = [[] for i in range(n+1)]
for i in range(n-1):
    adj[l[i]-1].append(i+1)
a = list(map(int,sys.stdin.readline().split()))
dp = [[0,0,0] for i in range(n+1)]
x = dfs(0)
#print(x)
#sum,max,count
print(x[1])
