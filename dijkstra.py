memo = None

def compute(a,b):
	if (a == "1" and b == "1"):
		result = "1"
	elif (a == "1" and b == "i"):
		result = "i"
	elif (a == "1" and b == "j"):
		result = "j"
	elif (a == "1" and b == "k"):
		result = "k"
	elif (a == "-1" and b == "1"):
		result = "-1"
	elif (a == "-1" and b == "i"):
		result = "-i"
	elif (a == "-1" and b == "j"):
		result = "-j"
	elif (a == "-1" and b == "k"):
		result = "-k"

	elif (a == "i" and b == "1"):
		result = "i"
	elif (a == "i" and b == "i"):
		result = "-1"
	elif (a == "i" and b == "j"):
		result = "k"
	elif (a == "i" and b == "k"):
		result = "-j"
	elif (a == "-i" and b == "1"):
		result = "-i"
	elif (a == "-i" and b == "i"):
		result = "1"
	elif (a == "-i" and b == "j"):
		result = "-k"
	elif (a == "-i" and b == "k"):
		result = "j"				

	elif (a == "j" and b == "1"):
		result = "j"
	elif (a == "j" and b == "i"):
		result = "-k"
	elif (a == "j" and b == "j"):
		result = "-1"
	elif (a == "j" and b == "k"):
		result = "i"
	elif (a == "-j" and b == "1"):
		result = "-j"
	elif (a == "-j" and b == "i"):
		result = "k"
	elif (a == "-j" and b == "j"):
		result = "1"
	elif (a == "-j" and b == "k"):
		result = "-i"	

	elif (a == "k" and b == "1"):
		result = "k"
	elif (a == "k" and b == "i"):
		result = "j"
	elif (a == "k" and b == "j"):
		result = "-i"
	elif (a == "k" and b == "k"):
		result = "-1"
	elif (a == "-k" and b == "1"):
		result = "-k"
	elif (a == "-k" and b == "i"):
		result = "-j"
	elif (a == "-k" and b == "j"):
		result = "i"
	elif (a == "-k" and b == "k"):
		result = "1"	

	return result

def generate2(lis):
	lisI = {}
	lisJ = {}
	lisK = {}

	memo = [ [ None for i in range(len(lis) + 1) ] for j in range(len(lis) + 1) ]

	for i in range(len(lis)):
		memo[i][i] = lis[i]

	for start in range(len(lis)):
		for end in range(start,len(lis)):
			result = 0
			if (start - end == 0):
				result = memo[start][end]

			else:
				result = compute(memo[start][end-1], lis[end])
				memo[start][end] = result

			if (result == "i"):
				if (start in lisI):
					lisI[start].append(end)
				else:
					lisI[start] = [end]
			elif(result == "j"):
				if (start in lisJ):
					lisJ[start].append(end)
				else:
					lisJ[start] = [end]
			elif(result == "k"):
				if (start in lisK):
					lisK[start].append(end)
				else:
					lisK[start] = [end]

	# print lisI
	# print lisJ
	# print lisK

	# Check for I
	if ((0 in lisI) and lisJ and lisK):
		for endI in (lisI.get(0)):			
			if (endI+1 in lisJ):
				for endJ in (lisJ.get(endI+1)):
					if (endJ + 1 in lisK):
						for endK in (lisK.get(endJ+1)):
							if (endK == len(lis)-1):
								return "YES" 
							else:
								return "NO"
			else:
				return "NO"
	else:
		return "NO"


def generate(lis):
	for iEnd in range(len(lis)):
		result = compute(lis[0:iEnd + 1])
		if (result == "i"):
			for jEnd in range(iEnd + 1, len(lis)):
				result = compute(lis[iEnd + 1:jEnd + 1])
				if (result == "j"):
					for kEnd in range(jEnd + 1, len(lis)):
						result = compute(lis[jEnd + 1:kEnd + 1])
						if (result == "k"):
							return "YES"
					return "NO"
			return "NO"
	return "NO"

def main():
	T = int(raw_input())

	for test in range(T):
		[L, X] = map(int, raw_input().split())
		raw = raw_input()
		strr = raw * X

		print ("Case #" + str(test+1) + ": " + str(generate2(list(strr))))

main()


# def compute(lis,start,end):
	
# 	for i in range(len(lis) - 1):
# 		if (lis[i] == "1" and lis[i+1] == "1"):
# 			lis[i+1] = "1"
# 		elif (lis[i] == "1" and lis[i+1] == "i"):
# 			lis[i+1] = "i"
# 		elif (lis[i] == "1" and lis[i+1] == "j"):
# 			lis[i+1] = "j"
# 		elif (lis[i] == "1" and lis[i+1] == "k"):
# 			lis[i+1] = "k"
# 		elif (lis[i] == "-1" and lis[i+1] == "1"):
# 			lis[i+1] = "-1"
# 		elif (lis[i] == "-1" and lis[i+1] == "i"):
# 			lis[i+1] = "-i"
# 		elif (lis[i] == "-1" and lis[i+1] == "j"):
# 			lis[i+1] = "-j"
# 		elif (lis[i] == "-1" and lis[i+1] == "k"):
# 			lis[i+1] = "-k"

# 		elif (lis[i] == "i" and lis[i+1] == "1"):
# 			lis[i+1] = "i"
# 		elif (lis[i] == "i" and lis[i+1] == "i"):
# 			lis[i+1] = "-1"
# 		elif (lis[i] == "i" and lis[i+1] == "j"):
# 			lis[i+1] = "k"
# 		elif (lis[i] == "i" and lis[i+1] == "k"):
# 			lis[i+1] = "-j"
# 		elif (lis[i] == "-i" and lis[i+1] == "1"):
# 			lis[i+1] = "-i"
# 		elif (lis[i] == "-i" and lis[i+1] == "i"):
# 			lis[i+1] = "1"
# 		elif (lis[i] == "-i" and lis[i+1] == "j"):
# 			lis[i+1] = "-k"
# 		elif (lis[i] == "-i" and lis[i+1] == "k"):
# 			lis[i+1] = "j"				

# 		elif (lis[i] == "j" and lis[i+1] == "1"):
# 			lis[i+1] = "j"
# 		elif (lis[i] == "j" and lis[i+1] == "i"):
# 			lis[i+1] = "-k"
# 		elif (lis[i] == "j" and lis[i+1] == "j"):
# 			lis[i+1] = "-1"
# 		elif (lis[i] == "j" and lis[i+1] == "k"):
# 			lis[i+1] = "i"
# 		elif (lis[i] == "-j" and lis[i+1] == "1"):
# 			lis[i+1] = "-j"
# 		elif (lis[i] == "-j" and lis[i+1] == "i"):
# 			lis[i+1] = "k"
# 		elif (lis[i] == "-j" and lis[i+1] == "j"):
# 			lis[i+1] = "1"
# 		elif (lis[i] == "-j" and lis[i+1] == "k"):
# 			lis[i+1] = "-i"	

# 		elif (lis[i] == "k" and lis[i+1] == "1"):
# 			lis[i+1] = "k"
# 		elif (lis[i] == "k" and lis[i+1] == "i"):
# 			lis[i+1] = "j"
# 		elif (lis[i] == "k" and lis[i+1] == "j"):
# 			lis[i+1] = "-i"
# 		elif (lis[i] == "k" and lis[i+1] == "k"):
# 			lis[i+1] = "-1"
# 		elif (lis[i] == "-k" and lis[i+1] == "1"):
# 			lis[i+1] = "-k"
# 		elif (lis[i] == "-k" and lis[i+1] == "i"):
# 			lis[i+1] = "-j"
# 		elif (lis[i] == "-k" and lis[i+1] == "j"):
# 			lis[i+1] = "i"
# 		elif (lis[i] == "-k" and lis[i+1] == "k"):
# 			lis[i+1] = "1"	

# 	return lis[-1]

