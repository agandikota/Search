from __future__ import print_function

def printer(message):
	lis = [['a','b','c'],
	['d','e','f'],
	['g','h','i'],
	['j','k','l'],
	['m','n','o'],
	['p','q','r','s'],
	['t','u','v'],
	['w','x','y','z']]
	
	prevChar = ''

	for i in range(len(message)):
		if(message[i] == ' '):
			if (i != 0 and prevChar == ' '):
				print (" ", end = ''),
			print ("0", end = ''),

		else:
			for j in range(len(lis)):
				if (message[i] in lis[j]):
					number = j + 2
					if (i != 0 and prevChar in lis[j]):
						print (" ", end = ''),
					iterations = lis[j].index(message[i]) + 1
					for _ in range(iterations):
						print (number, end = ''),

		prevChar = message[i]

def main():
	T = int(raw_input())

	for test in xrange(T):
		print ("Case #" + str(test+1) + ": ", end = '')
		printer(list(raw_input()))
		print ("")
		
main()

