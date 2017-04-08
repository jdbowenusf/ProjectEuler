prods=[]

A=[1+q for q in range(100)]
B=[1+q for q in range(10000)]

for a in A:
	if (len(list(set(list(str(a)))))==len(list(str(a))) and '0' not in str(a)):
		for b in [b for b in B if b>a]:
			if (len(list(set(list(str(b)))))==len(list(str(b))) and '0' not in str(b)):
				if len(list(set(list(str(a)))-set(list(str(b)))))==len(list(str(a))):
					p=a*b
					q=str(a)+str(b)+str(p)
					if (len(list(set(list(q))))==len(list(q)) and len(q)==9 and '0' not in str(p)):
						prods.append(p)
						print "a="+str(a)+", b="+str(b)+", p="+str(p)+" is pandigital."

print sum(list(set(prods)))
