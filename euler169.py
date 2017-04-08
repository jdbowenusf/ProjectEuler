import time

global_start=time.time()

"""The sets of powers of two less than a certain max power 2^n,
using no power more than twice, are in 1-1 correspondence
with the trinary representations of integers less than 3^n,
since any string of 0s, 1s, and 2s of length n gives a unique
set and vice versa. Therefore, by looping over the trinarys less
than a certain value, we can find number of double binary sums
for small numbers."""

#returns the trinary representation of an integer
def decToTrin(n):
	x=''
	while n>0:
		x+=str(n%3)
		n=n//3
	return x[::-1]

#takes a trinary string, treats each place value as if it was binary,
#and returns the value in decimal
def trinToBinSum(s):
	td=map(int,list(reversed(s)))
	retSum=0
	for dx, d in enumerate(td):
		retSum+=d*(2**dx)
	return retSum

#for small n, computes f(n) by 
F={}
for i in range(1,2+3**6):
	j=trinToBinSum(decToTrin(i))
	if j not in F.keys(): F[j]=1
	else: F[j]+=1

for k in F.keys():
	if k>65: del F[k]

del i,j,k

"""OBSERVATION) We need the observation that if n=2x is even, 
then all sums must have either no 1s or two 1s; if n=2x+1 is 
odd, then every sum must have one 1.
EVEN) Therefore, if n=2x, every partition with no 1s can be
formed by taking a partition of n/2 and multiplying every
element by 2; and every partition of n/2 yields such a partition.
The partitions with two 1s are necessarily just the partitions
of 2x-1 with an extra 1, again, in a 1-1 correspondence.
So f(2x)=f(x)+f(2x-1)
ODD) If n=2x+1, then every partition has a single 1.  Remove this
1 and you'll have all the partitions of 2x with no 1s, which by
the logic above is f(x)
EVEN REVISITED) This means that the f(2x-1) in our expression
for evens is in fact f(2(x-1)+1)=f(x-1) by our logic in odd
ALL TOGETHER) Hence we have relations f(2x)=f(x)+f(x-1) and 
f(2x+1)=f(x).
We'll use this recursion to calculate numbers we haven't seen
before, and store numbers we generate along the way, to avoid
repetitive calculations."""
def f(n, timeIt=False, inputDict=F):
	if timeIt==True: start=time.time()
	if n in inputDict.keys(): x=inputDict[n]
	elif n%2==0:
		a,inputDict=f(n/2,False,inputDict)
		inputDict[n/2]=a
		b,inputDict=f(n/2-1,False,inputDict)
		inputDict[n/2-1]=b
		x=a+b
	elif n%2==1:
		x,inputDict=f((n-1)/2,False,inputDict)
		inputDict[(n-1)/2]=x
	if timeIt==False: return x, inputDict
	else: return x, inputDict, time.time()-start

print f(10**25)[0]
	


		
	
		
		
