def phi(D,n,x):
    pass

def phi_tab(D,X):
  N=len(D)
  tab=[[INF for _ in range(X+1)]for _ in range(N+1)]
  tab[0][0]=0
  n,x=1,0
  while n!=N+1:
    if x==X+1:
      n,x=n+1,0
    else:
      tab[n][x]=tab[n-1][x]
      if D[n-1]<=X:
        tab[n][x]=min(tab[n][x],
                      1+tab[n][x-D[n-1]])
      x+=1
  return tab[N][X]
  
def phi_tab_opt(D,X):
  

    