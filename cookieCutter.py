#def cookieCutter

def main():
	T = int(raw_input())

	for x in xrange(T):
		C,F,X = map(float,list(raw_input().split()))
		rate = 2.0

		runningTime = 0.0
		
		while (((X/(rate + F)) + (C / rate)) < (X / rate) ):
			runningTime += (C / rate) 
			rate += F			
		runningTime += (X / rate)


		print ("Case #" + str(x+1) + ": " + "%.7f" % runningTime)

main()		

