from __future__ import print_function

def bouncer(rel):
	#print (rel)

	setA, setB = set(),set()

	listOfNames = rel.keys()

	# print (listOfNames)
	print (rel)

	for name in listOfNames:
		print (name)
		#listOfNames.remove(name)
		if (name not in setA and name not in setB):
			setA.add(name)
			print ("setA introduces", name)
			for enemy in (list(rel.get(name))):
				if enemy in setA:
					print("1")
					return "No"
				else:
					setB.add(enemy)
					listOfNames.remove(enemy)
					listOfNames.insert(0,enemy)
					
		elif name in setA:
			print ("setA introduces", name)
			for enemy in (list(rel.get(name))):
				if enemy in setA:
					print("2")
					return "No"
				else:
					setB.add(enemy)
					listOfNames.remove(enemy)
					listOfNames.insert(0,enemy)
		elif name in setB:
			print ("setB introduces", name)
			for enemy in (list(rel.get(name))):
				if enemy in setB:
					print("3")
					print (name, " hates ", enemy )
					print("Set A:",list(setA))
					print("Set B:",list(setB))
					return "No"
				else:
					setA.add(enemy)
					listOfNames.remove(enemy)
					listOfNames.insert(0,enemy)
		
	
	print("Set A:",list(setA))
	print("Set B:",list(setB))
	
	return "Yes"

def main():
	T = int(raw_input())

	for test in xrange(T):
		M = int(raw_input())
		rel = {}

		for line in range(M):
			[name1, name2] = list(raw_input().split())

			if (name1 in rel):
				rel.get(name1).add(name2)
			else:
				rel[name1] = {name2}

			if (name2 in rel):
				rel.get(name2).add(name1)
			else:
				rel[name2] = {name1}
		
		print ("Case #" + str(test+1) + ":" ,bouncer(rel))

main()