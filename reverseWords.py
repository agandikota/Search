
def main():
	T = int(raw_input())

	for test in xrange(T):
		lis = list(raw_input().split())
		lisR = lis[::-1]
		final = ""
		for i in range(len(lisR)):
			final += lisR[i]
			if (i != len(lisR) - 1):
				final += " "
		print "Case #" + str(test+1) + ": " + final
		
main()
