import math
import sys
from sys import stdin
t=int(input())
for i in range(t):
    
    d,k = [int(x) for x in input().split()]
    x = 2**(0.5)
    n = d//(k*x)
    n2 = n**2
    x = (2*n2+2*n+1)**(0.5)
    x*=k
    if x<=d:
        print("Ashish")
    else:
        print("Utkarsh")
    
