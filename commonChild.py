a = raw_input()
b = raw_input()

n, m = len(a), len(b)
prev_result = [0 for j in xrange(m)]

for i in xrange(n):
    result = [0 for j in xrange(m)]
    for j in xrange(m):
        if a[i] == b[j]:
            result[j] = prev_result[j-1] + 1 if j > 0 else 1
        else:
            result[j] = max(prev_result[j], result[j-1])
    prev_result = result

print prev_result[-1]


def foo(a,b):
	strA = raw_input()
	strB = raw_input()

	# strA = filter(lambda letter: letter in strB, strA)
	# strB = filter(lambda letter: letter in strA, strB)

	lcs = [[0 for x in xrange(len(strB)+1)] for y in xrange(len(strA)+1)]

	maxSeen = 0
	#print strA,strB

	for i in xrange(1,len(lcs)):
		for j in xrange(1,len(lcs)):

			if (i == 0 or j == 0):
				continue

			elif (strA[i-1] == strB[j-1]):
				lcs[i][j] = lcs[i-1][j-1] + 1;
				maxSeen = max(maxSeen,lcs[i][j])

			else:
				lcs[i][j] = max(lcs[i][j-1],lcs[i-1][j])

			# if (strA[i:j+1] in strB):
			# 	maxSeen = max(j+1 - i, maxSeen)

	#print strA
	#print strB
	print maxSeen

