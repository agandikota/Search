# max value contigous subsequence

def maxSequence(lis):
	if (lis):
		if (len(lis) == 1):
			 return lis[0]
		else:
			print lis[0],lis[1]
			return max(maxSequence(lis[1:]) + lis[0],lis[0])
	else:
		return None

def maxSubarray(lis):
	maxSoFar, maxEndingHere = 0,0
 
	for item in lis:
		maxEndingHere = max(0, maxEndingHere + item)
		maxSoFar = max(maxSoFar,maxEndingHere)
	return maxSoFar

def main():
	lis = [4, 5, -6, 13]
	lisb = [-2, -3, 4, -1, -2, 1, 5, -3]
	print maxSubarray(lis)

main()

