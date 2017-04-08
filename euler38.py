from itertools import permutations as perms

# conProd was used as I played around with this but not used in final code
# kept for posterity in case I forget how this problem works
"""
def conProd(x,d):
	L=list(map(lambda y: x*y, [a+1 for a in range(d)]))
	return int(''.join(list(map(str,L))))
"""


def next_smallest_pandigital(P):
	test_P=str(P)[:-2]+str(P)[7:][::-1]
	if int(test_P)<int(P):
		return test_P
	for d in range(3,10):
		base=str(P)[:-d]
		chad=str(P)[9-d:]
		chads=[''.join(p) for p in perms(chad)]
		chads=[perm for perm in chads if int(perm)<int(chad)]
		if len(chads)>0:
			max_chad=str(max(map(int,chads)))
			return int(base+max_chad)
		else: continue
	return None


"""
def genPossibleSplits():
	possibleSplits=[]
	for i in [1+a for a in range(4)]:
		iSplits=
"""


def listSplit(n,L):
	returnList=[]
	n=str(n)
	for l in L:
		returnList.append(n[:l])
		n=n[l:]
	return map(int,returnList)	


def isConProd(n):
	# theoretical ways to be a conprod are ordered sets of nondecreasing numbers
	# that add up to 9, since digits{n*k}<=digits{n*(k+1)}
	possibleSplits=[[1,1,1,1,1,1,1,1,1],
			# don't consider (1,1,1,1,1,1,1,2) or (1,1,1,1,1,2,2),
			# discard first cause no single digit *7 is <10 but *8 is >=10
			# discard second cause no single digit *5 is <10 but *6 is >=10
			[1,1,1,2,2,2],
			[1,2,2,2,2],
			[2,2,2,3],
			[3,3,3],
			[4,5]]
	for split in possibleSplits:
		divs=[1+a for a in range(len(split))]
		checks=[1]*len(split)
		chunks=listSplit(n,split)
		for chunk, div in zip(chunks,divs):
			if chunk/div!=chunks[0]:
				checks[div-1]=0
				break
		if min(checks)==1: return True
	return False


largest_pandigital=987654321
current_pandigital=largest_pandigital
while True:
	if isConProd(current_pandigital):
		print current_pandigital
		break
	current_pandigital=next_smallest_pandigital(current_pandigital)	
