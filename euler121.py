from operator import mul

def selectByString(s,L):
	retList=[]
	for a,b in zip(s,L):
		if a=='0': retList.append(1)
		elif a=='1': retList.append(b)
		else: retList.append(None)
	return retList		

def probWin(turns):
	denoms=range(2,turns+2)
	lossNumers=range(1,turns+1)
	winNumerator=0
	for i in range(2**turns-1):
		s=bin(i)[2:].zfill(turns)
		if sum(int(x) for x in s)<turns/2.:
			caseNumers=selectByString(s,lossNumers)
			winNumerator+=reduce(mul,caseNumers,1)
	return winNumerator, reduce(mul,denoms,1)

#x,y=probWin(4)
#print y/x

x,y=probWin(15)
print y/x			
		
