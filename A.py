# Author : Pratyaydeep↯Ghanta
import io,os
inp=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
inar=lambda: list(map(int,inp().split()))
inin=lambda: int(inp())
inst=lambda: inp().decode().strip()
# Am I debugging, check if I'm using same variable name in two places


def bf(arr):
    odd=0
    even=0
    for i in range(len(arr)):
        if i%2==0:
            even+=arr[i]
        else:
            odd+=arr[i]
    return abs(even-odd)

_T_=inin()
for _t_ in range(_T_):
    n=inin()
    a=inar()
    odd=0
    even=0
    for i in range(n):
        if i%2==0:
            even+=a[i]
        else:
            odd+=a[i]
    bal=abs(even-odd)

    for i in range(n):
        temp=a[0:i]+a[i+1:n]
        bt=bf(temp)
        #print(temp,bt)
        if bt<bal:
            bal=bt
            a=temp 
            n=len(temp)
        if bal==0:
            break
    print(len(a))
    print(*a)


