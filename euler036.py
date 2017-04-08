from itertools import product

# takes a list of palindromic strings of length n-1 or n,
# and returns palindomes of length n+1 or n+2
def inc_digits(dec_pal_list):
	return_list=[]
	for d, p in product(range(10), dec_pal_list):
		return_list.append(str(d)+str(p)+str(d))
	return return_list

# takes a dec int and returns True if it's binary palindrome
def is_bin_pal(n):
	b="{0:b}".format(n)
	for i in range(len(b)/2):
		if b[i]!=b[len(b)-i-1]:
			return False
	return True

# build dec_pals with 1 or 2 digits
dec_pals1=map(str,range(10))
dec_pals1=dec_pals1+[x+x for x in dec_pals1]
# build dec_pals with more digits
dec_pals2=inc_digits(dec_pals1)
dec_pals3=inc_digits(dec_pals2)
# collects the dec_pals into single list
dec_pals=list(set(map(int,dec_pals1+dec_pals2+dec_pals3)))
dec_pals=[x for x in dec_pals if x%10!=0]

total=0

for dec_pal in dec_pals:
	if is_bin_pal(dec_pal): total+=dec_pal

print total
