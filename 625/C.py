n = int(input())
s = list(input())
for i in range(n):
    l = []
    for j in range(len(s)):
        if j>0 and ord(s[j])==ord(s[j-1])+1:
            l.append([s[j],j])
        if j<len(s)-1 and ord(s[j])==ord(s[j+1])+1:
            l.append([s[j],j])
            
    if (len(l)==0):
        break
    l.sort()
    
    
    s1 = ''
    for i in range(len(s)):
        if (i==l[-1][1]):
            continue
        s1+=s[i]
    s = s1[:]
a = ''
for i in s:
    if (ord(i)==13):
        continue
    a+=i

print(n-len(a))
