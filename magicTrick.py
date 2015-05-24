from __future__ import print_function

def printer(firstRow, firstArr, secondRow, secondArr):
	#Add integers in firstArr to a set
	firstSet = set()
	secondSet = set()

	for i in range(4):
		firstSet.add(firstArr[firstRow-1][i])
		secondSet.add(secondArr[secondRow-1][i])

	intersectionLength = len(firstSet.intersection(secondSet))

	if (intersectionLength == 0):
		return "Volunteer cheated!"
	elif(intersectionLength == 1):
		return list(firstSet.intersection(secondSet))[0]
	else:
		#print (firstSet,secondSet,intersectionLength)
		return "Bad magician!"


def main():
	T = int(raw_input())

	for test in xrange(T):
		firstRow = int(raw_input())
		firstArr = []
		for i in range(4):
			lis = map(int, list(raw_input().split()))
			firstArr.append(lis)

		secondRow = int(raw_input())
		secondArr = []
		for i in range(4):
			lis = map(int, list(raw_input().split()))
			secondArr.append(lis)

		
		print ("Case #" + str(test+1) + ": " + str(printer(firstRow,firstArr,
			secondRow,secondArr)), end = '')
		print("")
		#print firstArr
		#wprint secondArr
		
main()