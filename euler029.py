from itertools import product
from time import time
from random import choice

all_start=time()

try:
	cl=input("Enter ceiling (less than a million, defaults to 100): ")
except (ValueError, SyntaxError):
        cl=100
print "-------------- BEGINNING ---------------"

bases=[x+2 for x in range(cl-1)]
pows=[x+2 for x in range(cl-1)]

pairs=list(product(bases,pows))

brute_time=time()
#############################################
print "Calculating brute..."
brute = len(list(set([a**b for (a,b) in pairs])))
print "Brute force gives "+str(brute)+" after "+str(time()-all_start)+"seconds"
			
#############################################

smart_start=time()+brute_time-all_start
print "----------------------------------------"
print "Calculating smart..."

###### define functions ######
def flt(L, unique=True):
	return_L=[item for sublist in L for item in sublist] 
	if unique==True: return list(set(return_L))
	else: return return_L 

def i(x): return int(round(x))

def factors(n):
	f=2
	facs=[]
	while f<n:
		if n%f==0:
			facs.append(f)
		f+=1
	return facs

def isSq(n,fac_dict=None):
	if fac_dict==None:
		fac_dict={n: factors(n)}
	for f in fac_dict[n]:
		if n/f==f: return True
	return False
	
	

# returns {number>2, [all the numbers<c which are a that-number-power]}
# eg, one key of it will be {3: [27, 81, 243, ...]}
# we use this to calculate roots quickly without floats
def genPowers(c=cl): 
	outPowers={} 
	for cube in range(17):
		outPowers[cube+3]=[(a+2)**(cube+3) for a in range(98)] # why 98?
		# cause if x^y<1MM and y>=3, then x<=99.  
		outPowers[cube+3]=[w for w in outPowers[cube+3] if w<=c]
	if c==1000000: outPowers[20]=[1000000] # handle x^y==1MM
	outPowers=dict((k, outPowers[k]) for k in outPowers.keys() if len(outPowers[k])>0)
	return outPowers

# depends on genPowers, this does opposite: given a number n, finds all the
# b which are >2nd roots of n, eg, calcRoots(729)=[3,6] since 27^3=3^6=729
def calcRoots(n, pow_dict=genPowers(cl)): 
	b=[] 
	for p in pow_dict.keys():  
		if n in pow_dict[p]: b.append(p)  
	return b

# Typographic function - simply takes a base-exponent pair
# and some frac data, and returns the duplicate pair assoc.
# with that frac data; cleans up code later on
def fracPair(pr,fc,dn):
	return (i(pr[0]**(1.*fc/dn)),pr[1]*dn/fc)

# Given a base-exponent pair, this generates a dict of duplicate pairs
# Dict has two keys, int and frac, for debugging the two different methods
# of generating dupes.  We also pass the two dicts we'll create later
# example output: {int: [(4,8)], frac: []}
def genDupes(pr, fac_dic, nsq_dic, sample_pairs):
	pf=1 if pr in sample_pairs else 0
	facs=fac_dic[pr[1]]
	pairsToRem={}
	pairsToRem['int']=[]
	pairsToRem['frac']=[]
	if pf==1: print "Facs for "+str(pr)+" second element: "+str(facs)
	for fac in facs:
		# remove integer cases, like 2^10=4^5
		if pr[0]**fac<=cl:
			if pf==1: print "Entering pr[0]**fac<=cl ("+str(pr[0])+"**"+str(fac)+")<="+str(cl)
			rem_pair=(pr[0]**fac,pr[1]/fac)
			pairsToRem['int'].append(rem_pair)
			if pf==1 or (rem_pair in sample_pairs):
				print "Sample pair "+str(rem_pair)+" detected as int rem_pair for pair "+str(pr)
		#remove non-int cases like 8^68=16^51
		for den in nsq_dic[pr[0]]:
			if fac in range(den+1,7) and pr[0]**(1.*fac/den)<=cl:
				rem_pair=fracPair(pr,fac,den)
				if pf==1 or (rem_pair in sample_pairs):
					print "Sample pair "+str(rem_pair)+" detected as frac rem_pair for pair "+str(pr)
				pairsToRem['frac'].append(rem_pair)
	return pairsToRem

def RemDupes(pair_list, fac_dic, nsq_dic, pow_dict, sample_pairs=[], c=cl):
	if len(sample_pairs)>0:
		print "Displaying data for sample pairs: "+str(sample_pairs)
	remDict={}
	for status in ['int','frac']: 
		remDict[status]={}
	deduped_pairs=pair_list
	for pair in pair_list:
		if len(sample_pairs)>0 and pair in sample_pairs:
			print "---------------------------------------------"
			print "RemDupes main loop has begun for "+str(pair)
		dupes=genDupes(pair, fac_dic, nsq_dic, sample_pairs)
		if pair in sample_pairs: print "Dupes: "+str(dupes)
		rem_pair_nest=dupes.values()
		if rem_pair_nest!=[[],[]]:
			for rem_pair in flt(rem_pair_nest):
				if pair in sample_pairs: "Examining "+str(rem_pair)+" as rem for "+str(pair)
				if pair in sample_pairs: str(rem_pair)+"found as rem for "+str(pair)
				status='int' if rem_pair in rem_pair_nest[0] else 'frac'
				roots=calcRoots(rem_pair[0],pow_dict)
				if (pair in sample_pairs) or (rem_pair in sample_pairs):
					print "Roots, isSq are "+str(roots)+" ; "+str(isSq(rem_pair[0]))
				if len(roots)>0 or isSq(rem_pair[0]):
					m=(2 if len(roots)==0 else max(roots))
					if (pair in sample_pairs) or (rem_pair in sample_pairs):
						print "Max root m is "+str(m)
					if m in remDict[status].keys():
						remDict[status][m]+=[rem_pair]
						if (pair in sample_pairs) or (rem_pair in sample_pairs):
							print "Inserting remDict["+str(status)+"]["+str(m)+"]="+str(rem_pair)
					else:
						remDict[status][m]=[rem_pair]
						if (pair in sample_pairs) or (rem_pair in sample_pairs):
							print "Creating remDict["+str(status)+"]["+str(m)+"]="+str(rem_pair)
				if rem_pair in deduped_pairs:
					if (pair in sample_pairs) or (rem_pair in sample_pairs):
						print "About to remove "+str(rem_pair)+" from dedupes..."
						print "Current dedupe length="+str(len(deduped_pairs))
					deduped_pairs.remove(rem_pair)
					if (pair in sample_pairs) or (rem_pair in sample_pairs):
						print "Removed "+str(rem_pair)+" from deduped, len at "+str(len(deduped_pairs))
				if rem_pair in sample_pairs: print "Move on to next rem_pair, finished with "+str(rem_pair)
		if pair in sample_pairs: print "Move on to next pair, finished with "+str(pair)
	return deduped_pairs, remDict
			

# define dicts
facts={}
for p in pows:
	facts[p]=factors(p)

powDict=genPowers(cl)

nsqRoots={}
for n in [a+2 for a in range(cl-1)]:
	nsqRoots[n]=[b for b in calcRoots(n,powDict) if b!=2]


# perform calculation

samplePairs=[(2,60),(7,36)]
remainingPairs,remDict=RemDupes(pairs,facts,nsqRoots,powDict,samplePairs)
smart=len(flt(remainingPairs))
smart_end=time()
			
print "Smart gives "+str(smart)+" after "+str(smart_end-smart_start)+"seconds."
print "Roots: "+str(flt([subDict.keys() for subDict in remDict.values()]))
r_ints, r_fracs = {}, {}
for root in flt([subDict.keys() for subDict in remDict.values()]):
	print "Root: "+str(root)
	r_ints[root], r_fracs[root] = remDict['int'].get(root,[]), remDict['frac'].get(root,[])
	rootTotal=len(r_ints[root]+r_fracs[root])
	intTotal=len(r_ints[root])
	fracTotal=len(r_fracs[root])
	totStr="Total of "+str(rootTotal)+" pairs removed with highest root="+str(root)
	detailStr=" ("+str(intTotal)+" int, "+str(fracTotal)+" frac)"
	print totStr+detailStr


