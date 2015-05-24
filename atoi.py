def atoi(mystr):
	lis = list(mystr)
	total = 0

	for i in range(len(lis)-1, -1, -1):
		if (lis[i] == '-'):
			total *= -1
		else:
			char = int(lis[i])
			total += (10 ** ((len(lis) -1 )-i )) * char

	print total

def inplace(mystr):
	lis = list(mystr.split(' '))
	for i in range(len(lis)-1,-1,-1):
		print lis[i],

def reverse(mystr):
	for i in range(len(mystr)):
		mystr[i], mystr[len(mystr) - 1 - i] = mystr[len(mystr) - 1 - i], mystr[i]
	return mystr


def inplace2(mystr):
	reverse(mystr)

	begin = 

	for i in range(len(mystr)):
		if (i == ' '):




atoi("-2342")
inplace("What is dog ?")