def main():
	T = int(raw_input())

	for test in range(T):
		N,L = map(int,raw_input().split())
		curState = raw_input().split()
		idealState = raw_input().split()

		permutations = [] # 2 ^ L possibilities

		for i in range(L):
			for j in range(L):
				for  



main()
