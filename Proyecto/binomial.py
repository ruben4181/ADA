from sys import stdin

import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def solve(n):
    m=4
    cm=[1,3]
    ops=0
    flag=False
    if n<=3:
        return 1
    while(not flag):
        tmp=[]
        tmp.append(1)
        cmSize=len(cm)
        for i in range(cmSize-1):
            buff=cm[i]+cm[i+1]
            if buff<=n:
                if buff==n:
                    return (i+1, ops)
                else:
                    tmp.append(buff)
            else:
                return (i+1, ops)
            ops+=1
        if m%2==0 and len(tmp)==m/2:
            buff=cm[-1]*2
            if buff<=n:
                if buff==n:
                    return (i+2, ops)
                else:
                    tmp.append(buff)
            else:
                return (i+1, ops)
        #print(cm)
        cm=tmp
        m+=1
    return n

def main():
    N=int(stdin.readline().strip('\n'))
    for i in range(N):
        n=int(stdin.readline().strip())
        ans=solve(n)
        print(ans)
    return
main()
