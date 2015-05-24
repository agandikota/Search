def init(n):
	htable = [[] for i in range(n)]
	return htable

def insert(htable,inputt, n):
	slotNo = inputt % n
	if (len(htable[slotNo]) >= n):
		


	htable[slotNo].append(inputt)

def find(htable,inputt, n):
	slotNo = inputt  % n
	return (inputt in htable[slotNo])

def main():
	n = 10
	htable = init(n)
	insert(htable,15,n)
	insert(htable,16,n)
	insert(htable,27,n)
	print find(htable,15,n)
	print find(htable,16,n)
	print find(htable,27,n)
	print htable


main()