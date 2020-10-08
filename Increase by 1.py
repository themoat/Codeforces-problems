from math import ceil, floor
t = int(input())


for i in range(0,t):
    n = int(input())
    a=floor(n**0.5)
    res = a - 1 + floor(n/a) - 1
    if n%(floor(n/a)*a)==0:
        print(res)
    else:
        print(res+1)
