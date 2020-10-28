t = int(input())
for _ in range(t):
    n = int(input())
    l = input()
    x = l.count("01")+l.count("10")
    print((n-x)//2)
