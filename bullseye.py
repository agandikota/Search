from __future__ import print_function
import math

def areaOfCircle(r):
	return math.pi * (r ** 2)

def circleCount (diskWidth,paint,circles):
	blackCircle = ((diskWidth + 1) ** 2) - (diskWidth ** 2)
	#print paint, blackCircle
	paint -= blackCircle
	
	if (paint < 0):
		return circles

	return circleCount(diskWidth + 2, paint, circles + 1)


def circleCount2(diskWidth,paint,circles):
	blackCircle = ((diskWidth + 1) ** 2) - (diskWidth ** 2)
	while (paint - blackCircle >= 0):
		circles += 1
		diskWidth += 2
		paint -= blackCircle
		blackCircle = ((diskWidth + 1) ** 2) - (diskWidth ** 2)
	return circles



def main():
	T = int(raw_input())

	for test in range(T):
		r,t = map(int,raw_input().split())
		print ("Case #" + str(test+1) + ":" ,circleCount2(r,t,0))

main()