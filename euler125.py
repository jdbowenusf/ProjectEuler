import math

def bruteForce(n, debug=False):
	s=int(math.sqrt(n/2))-1
	palSum=0
	seens=set()
	for a in range(1,s):
		for b in range(1,s+1-a):
			q=(b+1)*a**2+b*(b+1)*a+b*(b+1)*(2*b+1)/6
			if q>=n: break
			if int(str(q)[::-1])==q and q not in seens:
				seens.add(q)
				palSum+=q
	return palSum

assert bruteForce(1000)==4164
print bruteForce(10**8)
