import math

def getX(n):
	return int(math.sqrt(1+4*n)/2.+0.5)


# Played in excel to get a[3], then used OEIS to find recurrence
a={}
a[0]=0
a[1]=6
a[2]=210
a[3]=7140
i=4
m=0
while m<=10**12:
	a[i]=35*a[i-1]-35*a[i-2]+a[i-3]
	i+=1
	m=getX(2*max(a.values()))

print getX(max(a.values())) 
	
	

