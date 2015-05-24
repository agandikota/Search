#Write a method that retrieves subsets of a set

subsets = []	

def process(mySet):
	lisA = []
	maxSize = 1 << len(mySet)
	for i in range(maxSize):
		subset = []
		k = i
		index = 0
		while(k > 0):
			if (k & 1) > 0:
				subset.append(mySet[index])
			k = k >> 1
			index += 1
		lisA.append(subset)
	return lisA

#3 items: a variable i that iterates for 2 ^ 3 items, then for 2 ^ 2 items

def main():
	setA = set()
	while True:
		try:
			i = raw_input()
			setA.add(i)
		except EOFError:
			mainSet = list(setA)
			print(process(mainSet))
			break;
main()
