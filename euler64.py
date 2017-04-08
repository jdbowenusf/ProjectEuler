import math

def nextStep(a,b,n):
	c=n-b**2
	s=int(math.floor(math.sqrt(n)))
	x=int(math.floor(1.*a*(b+s)/c))
	y=b-x*c/a
	z=c/a
	return (x,-y,z)
	
def genPeriod(n):
	b=1
	a=int(math.floor(math.sqrt(n)))
	l=0
	while True:
		k,a,b=nextStep(b,a,n)
		if b==1: return l+1
		l+=1
	
def genSquares(ceil):
	squares=[]
	for n in range(2,int(math.sqrt(ceil))):
		squares.append(n**2)	
	return squares

odds=4
squares=genSquares(10001)
for n in range(14,10001):
	if n not in squares:
		try: p=genPeriod(n)
		except: print n
		if p%2==1: odds+=1

print odds
