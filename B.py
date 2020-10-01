# Author : Pratyaydeep↯Ghanta
import io,os
inp=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
inar=lambda: list(map(int,inp().split()))
inin=lambda: int(inp())
inst=lambda: inp().decode().strip()
# Am I debugging, check if I'm using same variable name in two places

from math import  gcd

_T_=inin()
for _t_ in range(_T_):
    n=inin()
    a=inar()
    a.sort(reverse=True)
    na=[]
    ta=[]
    for i in a:
        if i==a[0]:
            na.append(i)
        else:
            ta.append(i)
    cgcd=a[0]
    while(len(na)<n):
        mg=0
        for i in ta:
            mg=max(mg,gcd(i,cgcd))
        temp=[]
        for i in ta:
            if gcd(i,cgcd)==mg:
                na.append(i)
            else:
                temp.append(i)
        ta=temp
        cgcd=gcd(cgcd,mg)
    print(*na)



