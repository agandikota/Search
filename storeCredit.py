
def foo(cash,lisItems):
	for i in range(len(lisItems)):
		for j in range(len(lisItems)):
			if ((lisItems[i] + lisItems[j] == cash) and (i != j)):
				return [i+1, j+1]
					


def main():
	T = int(raw_input())

	for test in xrange(T):
		cash = int(raw_input())
		noOfItems = int(raw_input())
		lisItems = map(int,raw_input().split())
		pos = foo(cash,lisItems)
		print "Case #" + str(test+1) + ": " +  str(pos[0]), str(pos[1])		
		

main()


