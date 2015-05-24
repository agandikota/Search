
a = "ab"
b = "aab"

def anagram(a,b):
	lisA = list(a)
	lisB = list(b)
	lisA.sort()
	lisB.sort()

	return lisA == lisB

print anagram(a,b)



