#Goal: find last ten digits of 28433*2^7830457+1
#Answer: 8739992577

def findCycle(mod, doPrint=False):
	n=0
	modPowers={}
	x=1
	while x<=10**mod:
		modPowers[n]=x
		n+=1
		x=2*x
	while True:
		x=x%(10**mod)
		if x in modPowers.values():
			first=[k for k,v in modPowers.items() if v==x][0]
			if doPrint==True:
				print 'Cycle found!'
				print '2^'+str(first)+' = '+str(modPowers[first])+' mod 10^'+str(mod)
				print '2^'+str(n)+' = '+str(x)+' mod 10^'+str(mod)
			break
		modPowers[n]=x
		n+=1
		x=2*modPowers[n-1]
	return first,n,n-first

cycleLength={}
for i in range(1,6):
	cycleLength[i]=findCycle(i)[2]

for i in range(6,11):
	cycleLength[i]=5*cycleLength[i-1]

smallPow=7830457-cycleLength[10]

def modExp(b,p,m):
	r=b
	for i in xrange(p-1):
		r=(b*r)%m
	return r

print (modExp(2,smallPow,10**10)*28433+1)%(10**10)