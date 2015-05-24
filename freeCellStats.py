def freeCell(N, PD, PG):
	if ((PG == 100 and PD < 100) or (PG == 0 and PD > 0)):
		return "Broken"
	if PD == 0:
		return "Possible"

	p = PD
	r = 100
	while p%5 == 0 or p%2 == 0:
		if p%5 == 0:
			p /= 5
			if r%5 == 0:
				r /= 5
		if p%2 == 0:
			p /= 2
			if r%2 == 0:
				r /= 2
	if r <= N:
		return "Possible"
	else:
		return "Broken"

	# for i in range(1,N):
	# 	div = float(float(PD)/ float(100)) * float(i)
	# 	if ((div).is_integer()):
	# 		return "Possible"
	# return "Broken" 

def main():
	T = int(raw_input())

	for test in range(T):
		[N, PD, PG] = map(int,raw_input().split())
			
		print ("Case #" + str(test+1) + ": " + freeCell(N, PD, PG))

main()