import collections
import operator
import math
import time

def euler001():
	retVal=0
	for n in xrange(334): retVal+=3*n
	for m in xrange(200):
		if m%3!=0: retVal+=5*m
	return retVal

def euler002():
	#Parity and addition prove only even Fibs are F{2+3k}
	retVal=0
	Fs=[1,2]
	while Fs[1]<=4000000:
		retVal+=Fs[1]
		Fs=[sum(Fs)+Fs[1], 2*sum(Fs)+Fs[1]]
	return retVal

def euler003(n=600851475143, maxOnly=True):
	#we use trial division, storing primes as we go
	facs=[]
	primes=[2]
	while n%2==0:
		facs.append(2)
		n/=2
	f=3
	while n!=1:
		while n%f==0:
			facs.append(f)
			n/=f
		primes.append(f)
		while True:
			f+=2
			if min(map(lambda x: x%f, primes))!=0:
				break
	if maxOnly: return max(facs)
	else: return facs

def euler004():
	#3digits * 3digits will yield six digits
	#(or at least the larger ones will)
	#P='ABCCBA' => P=(100000+1)*A+(10000+10)*B+(1000+100)*C
	#=> 11|P since 11 divides each of those
	maxPal=0
	for x in xrange(999,99,-1):
		for y in xrange(990,109,-11):
			z=x*y
			if z>maxPal:
				if str(z)[::-1]==str(z):
					maxPal=z
	return maxPal

def euler005(n=20):
	#We only grab the lowest powers we need in the prime factorization
	allFacs={2:1,3:1}
	for k in xrange(4,n+1):
		#We can use euler003, since it can return
		#prime factors with multiplicity
		curFacs=collections.Counter(euler003(k,False))	
		for fac in curFacs.keys():
			allFacs[fac]=max([curFacs[fac],allFacs.get(fac,0)])
	powerFacs=map(lambda x: x**allFacs[x], allFacs.keys())	
	return reduce(operator.mul,powerFacs)

def euler006():
	#brute force
	a=0
	b=0
	for i in xrange(100):
		a+=(i+1)**2
		b+=(i+1)
	b=b**2
	return b-a

def euler007(L=10001):
	primeNum=3
	primes=[2,3,5]
	prime=5
	n=5
	while primeNum!=L:
		n+=2
		#this loops over unnecessary primes
		#but taking the sqrt would be almost 
		#slower than all the unnecessary mods
		for p in primes:
			if n%p==0: break
		else:
			primes.append(n)
			prime=n
			primeNum+=1			
	return prime

def euler008(L=13):
	bigNumSegs=['73167176531330624919225119674426574742355349194934',
		    '96983520312774506326239578318016984801869478851843',
		    '85861560789112949495459501737958331952853208805511',
		    '12540698747158523863050715693290963295227443043557',
		    '66896648950445244523161731856403098711121722383113',
		    '62229893423380308135336276614282806444486645238749',
		    '30358907296290491560440772390713810515859307960866',
		    '70172427121883998797908792274921901699720888093776',
		    '65727333001053367881220235421809751254540594752243',
		    '52584907711670556013604839586446706324415722155397',
		    '53697817977846174064955149290862569321978468622482',
		    '83972241375657056057490261407972968652414535100474',
		    '82166370484403199890008895243450658541227588666881',
		    '16427171479924442928230863465674813919123162824586',
		    '17866458359124566529476545682848912883142607690042',
		    '24219022671055626321111109370544217506941658960408',
		    '07198403850962455444362981230987879927244284909188',
		    '84580156166097919133875499200524063689912560717606',
		    '05886116467109405077541002256983155200055935729725',
		    '71636269561882670428252483600823257530420752963450']
	bigNumStr=''.join(bigNumSegs)
	maxProd=0
	for i in xrange(1001-L):
		curStr=bigNumStr[i:i+L]
		if '0' not in curStr:
			curDigs=map(int,list(curStr))
			curProd=reduce(operator.mul,curDigs)
			if curProd>maxProd:
				maxProd=curProd
	return maxProd			
			
def euler009():
	#primitives are 2mn, m^2-n^2, m^2+n^2
	#all py trips are k* a primitive
	#we won't worry about checking coprimeness for m,n
	for m in xrange(2,22):
		for n in xrange(1,m):
			a,b,c=2*m*n,m**2-n**2,m**2+n**2
			for k in xrange(1000/(a+b+c)):
				if (k+1)*a+(k+1)*b+(k+1)*c==1000:
					return (k+1)*a*(k+1)*b*(k+1)*c

def euler010(C=2000000,b=1000,timeIt=False):
	#This attempts a sieve of Eratosthenes, chunked into blocks
	#kinda slow, takes 2.8 seconds
	start=time.time()
	primeSum=9 #because 1 isn't prime and we remove 3&5 in blockInd 0
	for blockInd in range(C/b):
		block=range(1+blockInd*b,1+(1+blockInd)*b)[::2]
		block=[n for n in block if n%3!=0 and n%5!=0]
		s=math.sqrt((1+blockInd)*b)
		for f in range(7,1+int(s),2):
			if f%6 in [1,5]:
				for n in block:
					if n%f==0 and n!=f: block.remove(n)
		primeSum+=sum(block)
	if timeIt: return primeSum, time.time()-start
	else: return primeSum

def main():
	for i in range(10):
		j=str(i+1).zfill(3)
		print 'Euler{}:'.format(j),eval('euler{}'.format(j))()

if __name__ == "__main__":
      main()
