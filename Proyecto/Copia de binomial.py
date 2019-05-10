from sys import stdin
import operator as op
from functools import reduce

top2=[0, 0, 46, 20, 14, 13, 13, 13, 13, 14, 14, 15, 16, 17, 18, 19, 20, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
top3=[0, 0, 142, 41, 24, 19, 17, 16, 16, 16, 17, 17, 18, 19, 19, 20, 21, 22, 23, 24, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
top4=[0, 0, 448, 86, 41, 29, 23, 21, 20, 20, 20, 20, 20, 21, 21, 22, 23, 23, 24, 25, 26, 27, 28, 29, 29, 30, 31, 32, 33, 34]
top5=[0, 0, 1415, 183, 72, 44, 33, 28, 25, 24, 23, 23, 23, 23, 24, 24, 25, 25, 26, 27, 28, 28, 29, 30, 31, 32, 33, 33, 34, 35]
top6=[0, 0, 4473, 393, 126, 68, 47, 37, 32, 29, 28, 27, 27, 26, 27, 27, 27, 28, 28, 29, 29, 30, 31, 32, 32, 33, 34, 35, 36, 37]
top7=[0, 0, 14143, 845, 223, 106, 68, 51, 42, 37, 34, 32, 31, 30, 30, 30, 30, 30, 31, 31, 32, 32, 33, 34, 34, 35, 36, 37, 37, 38]
top8=[0, 0, 44722, 1819, 396, 167, 98, 69, 54, 46, 41, 38, 36, 35, 34, 33, 33, 33, 33, 34, 34, 35, 35, 36, 36, 37, 38, 38, 39, 40]
top9=[0, 0, 141422, 3916, 702, 263, 142, 94, 71, 58, 50, 45, 42, 40, 39, 38, 37, 37, 37, 37, 37, 37, 38, 38, 39, 39, 40, 40, 41, 42]
top10=[0, 0, 447215, 8436, 1247, 415, 207, 130, 93, 74, 62, 55, 50, 46, 44, 43, 41, 41, 40, 40, 40, 40, 40, 41, 41, 41, 42, 43, 43, 44]
top11=[0, 0, 1414215, 18173, 2215, 657, 302, 179, 123, 94, 77, 66, 59, 54, 51, 48, 47, 45, 44, 44, 44, 43, 43, 44, 44, 44, 44, 45, 45, 46]
top12=[0, 0, 4472137, 39150, 3938, 1040, 442, 247, 163, 120, 95, 80, 70, 63, 58, 55, 52, 51, 49, 48, 48, 47, 47, 47, 47, 47, 47, 48, 48, 48]
top13=[0, 0, 14142137, 84345, 7001, 1646, 648, 342, 216, 154, 119, 98, 84, 74, 68, 63, 59, 57, 55, 53, 52, 51, 51, 50, 50, 50, 50, 50, 51, 51]
top14=[0, 0, 44721361, 181714, 12449, 2608, 950, 473, 286, 197, 148, 119, 100, 87, 78, 72, 67, 63, 61, 59, 57, 56, 55, 54, 54, 54, 54, 54, 54, 54]
top15=[0, 0, 141421357, 391488, 22136, 4131, 1393, 656, 380, 253, 185, 145, 120, 103, 91, 83, 76, 71, 68, 65, 63, 61, 60, 59, 58, 58, 57, 57, 57, 57]
top16=[0, 0, 447213596, 843434, 39362, 6546, 2043, 910, 506, 326, 232, 178, 144, 122, 106, 95, 87, 80, 76, 72, 69, 67, 65, 64, 63, 62, 61, 61, 60, 60]
#39362

def getTop(n, i):
	top=44721361
	if n<=1000:
		return [2,top2[i]]
	if n>1000 and n<10000:
		return [top2[i], top3[i]]
	if n>10000 and n<100000:
		return [top3[i], top4[i]]
	if n>100000 and n<1000000:
		return [top4[i], top5[i]]
	if n>1000000 and n<10000000:
		return [top5[i], top6[i]]
	if n>10000000 and n<100000000:
		return [top6[i], top7[i]]
	if n>100000000 and n<1000000000:
		return [top7[i], top8[i]]
	if n>1000000000 and n<10000000000:
		return [top8[i],top9[i]]
	if n>10000000000 and n<100000000000:
		return [top9[i], top10[i]]
	if n>100000000000 and n<1000000000000:
		return [top10[i], top11[i]]
	if n>1000000000000 and n<10000000000000:
		return [top11[i], top12[i]]
	if n>10000000000000 and n<100000000000000:
		return [top12[i], top13[i]]
	if n>100000000000000 and n<1000000000000000:
		return [top13[i], top14[i]]
	if n>1000000000000000 and n<10000000000000000:
		return [top14[i], top15[i]]
	if n>10000000000000000:
		return [top15[i], top16[i]]
	return top

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def klimit(n):
	l=2
	h=120
	mid=(l+h)>>1
	midt=mid>>1
	ans=-1
	oldAns=0
	while l<h:
		test=ncr(mid, midt)
		if test>n:
			h=mid
		else:
			l=mid
		mid=(l+h)>>1
		midt=mid>>1
		ans=midt
		if ans==oldAns:
			break
		else:
			oldAns=ans
	return ans

def findInColumn(n, r):
    l,h=getTop(n, r)
    l=top16[4]-1
    mid=(l+h)>>1
    ans=-1
    while l+1<h and ans==-1:
    	test=ncr(mid,r)
    	if test<=n:
    		if test==n:
    			ans=mid
    		else:
    			l=mid
    	else:
    		h=mid
    	mid=(l+h)>>1
    return ans

def precalc():
	A={}
	for k in range(4, 28):
		for n in range(2, top16[k]+1):
			test=ncr(n,k)
			if test in A.keys():
				A[test].append((n,k))
			else:
				A[test]=[(n,k)]
	for k in range(2, 4):
		for n in range(2, top16[4]+1):
			test=ncr(n,k)
			if test in A.keys():
				A[test].append((n,k))
			else:
				A[test]=[(n,k)]
	return A

def solve(n, A):
	if n==2:
		return [(2,1)]
	ans=[]
	if n in A.keys():
		for nk in A[n]:
			if nk not in ans:
				ans.append(nk)
				if nk[0]%2==0:
					if nk[1]!=nk[0]/2:
						ans.append((nk[0], nk[0]-nk[1]))
				else:
					ans.append((nk[0], nk[0]-nk[1]))
	findIn2=True
	findIn3=True
	for (a,b) in ans:
		if b==2:
			findIn2=False
		if b==3:
			findIn3=False
	toFind=[0, 0]
	if findIn2 and findIn3:
		toFind=[2, 4]
	if findIn2 and not findIn3:
		toFind=[2, 3]
	if not findIn2 and findIn3:
		toFind=[3, 4]
	for i in range(toFind[0],toFind[1]):
		tmp=findInColumn(n, i)
		if tmp!=-1 and (tmp, i) not in ans:
			ans.append((tmp, i))
			if tmp%2==0:
				if i!=tmp/2:
					ans.append((tmp, tmp-i))
			else:
				ans.append((tmp, tmp-i))
	if (n, 1) not in ans:
		ans.append((n, 1))
	if (n, n-1) not in ans:
		ans.append((n, n-1))
	ans.sort()
	return ans
def main():
	N=int(stdin.readline().strip('\n'))
	A=precalc()
	for i in range(N):
		n=int(stdin.readline().strip())
		ans=solve(n, A)
		result=""
		if n not in A.keys():
			A[n]=ans
		for bc in ans:
			result+="("+str(bc[0])+","+str(bc[1])+") "
		print(len(ans))
		print(result[:-1])
	return
main()
