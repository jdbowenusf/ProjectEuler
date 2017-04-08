# 10 choose 6 is 210, so there are only 210^2 = 44,100 possibilities

def mirror69(S):
	return S.replace('9','X').replace('6','X')

def initializeDie():
	die=''
	for i in range(6):
		die+=str(i)
	return die

def incrementDie(die):
	die=map(int,list(die))
	for i in range(6)[::-1]:
		if die[i]<4+i:
			die[i]+=1
			for j in range(i+1,6):
				die[j]=die[j-1]+1
			return ''.join(map(str,die))
		elif die[i]==4+i and i>0:
			continue
		elif die[i]==4 and i==0:
			return None

def compareDie(dieA, dieB):
	squares=['01','04','09','16','25','36','49','64','81']
	squares=map(mirror69,squares)
	dieA=mirror69(dieA)
	dieB=mirror69(dieB)
	canBuild={}
	for square in squares:
		canBuild[square]=0
		if square[0] in dieA and square[1] in dieB:
			canBuild[square]=1
		elif square[1] in dieA and square[0] in dieB:
			canBuild[square]=1
	return min(canBuild.values())

die1=initializeDie()
counter=0
while die1 is not None:
	die2=initializeDie()
	while die2 is not None:
		counter+=compareDie(die1,die2)
		die2=incrementDie(die2)
	die1=incrementDie(die1)

print counter/2
	
	
	
			
		
