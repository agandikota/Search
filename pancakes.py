def sortPancakes(D, diners):
	minutes = 0
	maxDiners = max(diners)
	normalTime = maxDiners

	while (maxDiners > 0):
		if ((float(maxDiners/float(2))).is_integer() == False):
			# Odd numbers - ceil
			half = (maxDiners/2) + 1
		else:
			# Even numbers
			half = maxDiners/2

		p = 0
		# Elements that exceed half
		for i in diners:
 			if (i > half):
 				p += 1

		specialTime = 1 + half + p

		if (specialTime > maxDiners):
			# Stay
			diners = map((lambda x: x - 1),diners)
		else:
			#Split
			maxPlate = diners.index(maxDiners)
			if ((float(diners[maxPlate]/float(2))).is_integer() == False):
				diners.append((diners[maxPlate] / 2) + 1)
			else:
				diners.append((diners[maxPlate]/2))	
			diners[maxPlate] = (diners[maxPlate] / 2)
		#print diners

		minutes += 1
		maxDiners = max(diners)
	return minutes

def easyPancakes(D,diners):
	ans = 1000
	for i in range(1,1000):
		j = i
		for k in range(0,len(diners)):
			j += (diners[k] - 1)/i
		ans = min(ans, j)
	return ans



def main():
	T = int(raw_input())

	for test in range(T):
		D = int(raw_input())
		diners = map(int, raw_input().split())
	
		#print ("Case #" + str(test+1) + ": " + str(diners) + " => " + str(sortPancakes(D,diners)))
		print ("Case #" + str(test+1) + ": " + str(easyPancakes(D,diners)))
main()

# def sortPancakes(D, diners):
# 	minutes = 0
# 	maxDiners = max(diners)

# 	while (maxDiners > 0):
# 		avg = sum(diners)/len(diners)
# 		if (((maxDiners - avg) > 1) or (len(diners) == 1 and maxDiners > 2)):
# 		#if (maxDiners > 2 and ): # Special minutes
# 			maxPlate = diners.index(maxDiners)
# 			if ((float(diners[maxPlate]/float(2))).is_integer() == False):
# 				diners.append((diners[maxPlate] / 2) + 1)
# 			else:
# 				diners.append((diners[maxPlate]/2))	
# 			diners[maxPlate] = (diners[maxPlate] / 2)
# 		else:
# 			diners = map((lambda x: x - 1),diners)
# 		print diners

# 		minutes += 1
# 		maxDiners = max(diners)

# 	return minutes