def join (lis):
	print lis
	for i in range(len(lis)):
		deleteList = []
		for j in range(len(lis[i])):
			if (j != len(lis[i])-1 and lis[i][j] == lis[i][j + 1]):
				lis[i][j] += lis[i][j+1]
				deleteList.append(j+1)
		for elem in deleteList:
			del lis[i][elem]

	repeater(lis)

def repeater(lis):
	# Delete letters
	lengthLists = []

	for i in range(lis):
		n





def main():
	T = int(raw_input())

	for test in range(T):
		n = int(raw_input())
		lis = []
		redFlag = False
		minLen = 0 
		for i in range(n):
			inputStr = raw_input()
			minLen = min(minLen, len(inputStr))
			lis.append(list(inputStr))

		print join(lis)
		#print repeater(lis,minLen)	
#		print ("Case #" + str(test+1) + ":" ,bouncer(rel))

main()