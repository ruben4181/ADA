from sys import stdin
def tab(A):
    N=len(A)
    tab=[[0 for _ in range(N)] for _ in range(N)]
    if A[0]==0:
        for i in range (N):
            tab[i][0]=1
    else:
        tab[A[0]-1][0]=1
    x, y = 0, 1
    while y!=N:
        if A[y]==0:
            tmp=getColumn(tab, y-1, N)
            if x==0:
                tab[x][y]=sumFromTo(tmp, 2, N)
                print(tmp, tab[x][y])
                x+=1
                
            elif x==N-1:
                tab[x][y]=sumFromTo(tmp, 0, N-2)
                x=0
                y=y+1
            else:
                tab[x][y]=sumFromTo(tmp, 0, x-1)+sumFromTo(tmp, x+2, N)
                x+=1
        else:
            pass
    return sumFromTo(getColumn(tab, N-1, N), 0, N)
def sumFromTo(A, p, k):
    c=0
    for i in range(p, k):
        c+=A[i]
    return c
def getColumn(A, column, N):
    L=[]
    for i in range(N):
        L.append(A[i][column])
    return L
def main():
    for line in stdin:
        i=0
        A=[0 for _ in range(len(line)-1)]
        for c in line:
            if c=='?':
                A[i]=0
            elif c!='\n':
                if ord(c)>=65 and ord(c)<=70:
                    A[i]=ord(c)-55
                else:
                    A[i]=ord(c)-48
            i+=1
        print(tab(A))
main()
