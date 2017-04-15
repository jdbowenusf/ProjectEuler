import collections
#import fractions
import math
import time

def R(k): return int('1'*k)

def A(n):
	#Given n coprime to 10, A returns least k s.t. n|R(k)
	"""
	try: assert fractions.gcd(n,10)==1
	except: raise RuntimeError('Domain error: invalid input to A(n)')
	"""	
	k=1
	while True:
		k+=1
		if R(k)%n==0: return k

def isPrime(n):
	if n!=int(n) or n<2: return False
	if n in [2,3,5]: return True
	if n%2==0 or n%3==0 or n%5==0: return False
	a=7
	b=11
	s=math.sqrt(n)
	while a<=s:
		if n%a==0 or n%b==0: return False
		a+=6
		b+=6
	return True

def factorize(n):
	factors=[]
	while n%2==0:
		factors.append(2)
		n/=2
	f=1
	while n!=1:
		f+=2
		if not isPrime(f): continue
		while n%f==0:
			factors.append(f)
			n/=f
	return dict(collections.Counter(factors))

def findComps(L,printIt=False):
	#this takes north of 10 minutes
	#there are several optimizations in the forum for this question
	start=time.time()
	status='{0}th value found at {1} (A={2}) after {3} seconds.'
	n=89
	compsFound=0
	comps=[]
	while compsFound<L:
		n+=2
		if n%5==0: continue
		if (n-1)%A(n)==0:
			if not isPrime(n):
				comps.append(n)
				compsFound+=1
				lap=str(time.time()-start)
				if printIt:
					print status.format(str(compsFound),str(n),str(A(n)),lap)
	if printIt: print comps
	return sum(comps)

def main():
	findComps(25)

if __name__=='__main__':
      main()
