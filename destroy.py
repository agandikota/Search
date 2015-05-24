def main():
	foo = list("aaab")

	for i in range(len(foo)):
		if (i != (len(foo) - 1)):
			print i, len(foo) - 1
			if (foo[i] == foo[i + 1]):
				print "Appending foo[i+1]..."
				foo[i] += foo[i+1]
				del foo[i+1]


main()	