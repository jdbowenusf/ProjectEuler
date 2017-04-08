# m^2-n^2, 2mn, m^2+n^2 gen all prim trips a,b,c if m,n coprime not both odd
# set n to 1, what's perim?
# 2m^2+2m=1000
# m^2+m-500=0
# m=(-1 pm sqrt(1+2000))/2
# m<22

def isCoprime(a,b):
	if a==0 or b==0: return False
	f=2
	facs=[]
	n = a if a<b else b
	while f<=n:
		if a%f==0 and b%f==0:
			return False
		f+=1
	return True	

def notBothOdd(a,b):
	if a%2==1 and b%2==1: return False
	return True

def scaleTrip(T,s):
	return map(lambda x: x*s, T)

primTrips=[]
for m in range(22):
	for n in range(m-1):
		if isCoprime(m,n) and notBothOdd(m,n):
			primTrips.append([m**2-n**2,2*m*n,m**2+n**2])

pyTrips=[]
for primTrip in primTrips:
	for a in range((sum(primTrip)-1)/1000):
		pyTrips.append(scaleTrip(primTrip,a+1))

pyTrips=[list(i) for i in set(tuple(i) for i in pyTrips)]

tripsWithPerim={}
for p in range(1000):
	tripsWithPerim[p+1]=len([trip for trip in pyTrips if sum(trip)==p+1])
max_val=max(tripsWithPerim.values())

solution=[k for k in tripsWithPerim.keys() if tripsWithPerim[k]==max_val]
print "Solution: "+str(solution[0])
	



		
