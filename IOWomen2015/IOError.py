def binary(mystr,n = 8):
	sum = 0
	for i in range(n):
		sum += int(mystr[n - i - 1]) * 2**i
	return sum



def main():
	T = int(raw_input())
	for test in range(T):
		output = []
		noOfBytes = int(raw_input())
		string = raw_input()

		g = lambda x: "1" if x == "I" else "0"
		lis = map(g, list(string))
		for i in range(noOfBytes):
			output += chr(binary((lis[i*8:(i+1) * 8])))

		print "Case #" + str(test + 1) + ":",
		print ''.join(output)

main()

