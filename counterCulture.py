# counterCulture.py

def counter(N,i,count):

	# if it's bigger than original number and lesser than N, then flip it
	iFlip = N

	while (i > 1):
		print i
		iFlip = int(str(i)[::-1])

		if (str(i)[-1] == '0'):
			i -= 1
			count += 1
			continue

		if (i <= iFlip):
			if (i >= 1):
				i -= 1
			else:
				raise ValueError
		elif (i > iFlip):
			if (iFlip >= 1):
				i = iFlip
			else:
				i -= 1

		count += 1

	return count



def main():
	T = int(raw_input())

	for test in range(T):
		N = int(raw_input())
	
		print ("Case #" + str(test+1) + ": " + str(counter(N,N,1)))
main()


"""while (i <= N):
		print i
		iFlip = int(str(i)[::-1])

		if (i >= iFlip):
			if (i <= N):
				i += 1
			else:
				raise ValueError
		else:
			if (iFlip > N):
				i += 1
			else:
				i = iFlip

		count += 1
		"""

