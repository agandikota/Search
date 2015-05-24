#check if a given string is a palindrome

def main():
	w = raw_input()
	foo(w)

def foo(w):
	stack = list(w)
	queue = list(w)

	for i in range(len(w)):
		charStack = stack.pop(-1)
		charQueue = queue.pop(0)
		if (charStack != charQueue):
			print "Not a palindrome"
			return

	print "A palindrome"


main()