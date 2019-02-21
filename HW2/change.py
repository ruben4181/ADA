from sys import stdin

def tab_min(D, C, M):
	INF=2**20
	N=len(D)
	tab = [[INF for _ in range(N+1)] for _ in range(M+1)]
	for i in range(N):
		tab[0][i]=0
	m, n = 1, 1
	while n<N:
		if m==M+1:
			n, m = n+1, 1
		else:
			
		m+=1
	return tab[M][N]
def main():
	B=[5, 10, 20, 50, 100, 200]
	for line in stdin:
		line=line.strip('\n')
		A=line.split()
		for i in range(6):
			A[i]=int(A[i])
		A[6]=int(float(A[6])*100)
		print(tab_min(B, A[:6], A[6]))
main()