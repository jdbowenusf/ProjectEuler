from math import sqrt, floor

def isPrime(n):
	if n<=1 or n!=int(n): return False
	if n in [2,3,5]: return True
	if n%2==0 or n%3==0 or n%5==0: return False
	a=7
	b=11
	while a<floor(sqrt(n)):
		if n%a==0: return False
		if n%b==0: return False
		a+=6
		b+=6
	return True

def trunc(n,D):
	if len(str(n))==1: return None
	if D=='L': return int(str(n)[1:])
	if D=='R': return int(str(n)[:-1])
	else: return None

def isTrunc(n):
	m=n
	while m!=None and len(str(m))>=1:
		if isPrime(m)==False: return False
		if isPrime(n)==False: return False
		m=trunc(m,'L')
		n=trunc(n,'R')
	return True

def genTruncs(seed):
	truncs=[]
	while len(truncs)<11:
		if isTrunc(seed):
			print "Trunc found at "+str(seed)
			truncs.append(seed)
		seed+=2
	return truncs

print sum(genTruncs(11))



	
	
		
	
