# from __future__ import print_function

# from math import ceil, log,sqrt
# import gmpy2

# def isqrt(n):
#     res = 0
#     bit = 4 **int(ceil(log(n, 4))) if n else 0  # smallest power of 4 >= the argument
#     while bit:
#         if n >= res + bit:
#             n -= res + bit
#             res = (res >> 1) + bit
#         else:
#             res >>= 1
#         bit >>= 2
#     return res

# def is_square(apositiveint):
# 	x = apositiveint // 2
# 	seen = set([x])
# 	while x * x != apositiveint:
# 		x = (x + (apositiveint // x)) // 2
# 		if x in seen: return False
# 		seen.add(x)
# 		return True

# def square(num):
# 	print("Starting sqrt")
# 	sqrt = gmpy2.sqrt(num)
# 	print (sqrt)
# 	if (sqrt ** 2 == num):
# 		return True
# 	else:
# 		return False

# def fair(num):
# 	numToList = list(str(num))
# 	numLen = len(numToList)
# 	for i in range(numLen/2):
# 		if (numToList[i] != numToList[numLen - 1 - i]):
# 			return False

# 	return True
# def main():

# 	T = int(raw_input())
# 	for test in range(T):
# 		start, end = map(int,raw_input().split())
# 		fairAndPerfect = []
# 		history = {}

# 		for i in range(start,end+1):
# 			#is_perfect_sq = (isqrt(i)**2 == i) and fair(isqrt(i))
# 			is_perfect_sq = square(i)
# 			fairNum = fair(i)

# 			retrieveHistory = history.get(fairNum)

# 			if not retrieveHistory:
# 				if (fairNum and is_perfect_sq):
# 					fairAndPerfect.append(i)
# 					history[fairNum] = True
# 				else:
# 					history[fairNum] = False

# 			else:
# 				if (retrieveHistory == True):
# 					fairAndPerfect.append(i)

# 		#print fairAndPerfect
# 		print ("Case #" + str(test+1) + ": " + str(len(fairAndPerfect)))
	
# main()
# # if __name__ == '__main__':
# #     from math import sqrt  # for comparison purposes

# #     largeInt = (5 ** 2) ** 22

# #     for i in range(5 ** 2)+[12**22, (10**100+1)**2]:
# #         is_perfect_sq = isqrt(i)**2 == i
# #         print '{:21,d}:  math.sqrt={:12,.7G}, isqrt={:10,d} {}'.format(
# #             i, sqrt(i), isqrt(i), '(perfect square)' if is_perfect_sq else '')

#!/usr/bin/env python
#
# Problem: Fair and Square
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


from itertools import *

# generate list of all fair and square numbers in range
s = [1, 2, 3]

s.extend([int('2'+'0'*i+'2') for i in range(49)])
s.extend([int('2'+'0'*i+'1'+'0'*i+'2') for i in range(24)])

for i in range(24):
    for j in range(2):
        for k in combinations(range(i), j):
            t = [0]*i
            for v in k:
                t[v] = 1
            l = '1'+''.join(map(str, t))
            r = l[::-1]
            s.append(int(l+'2'+r))

for i in range(25):
    for j in range(4):
        for k in combinations(range(i), j):
            t = [0]*i
            for v in k:
                t[v] = 1
            l = '1'+''.join(map(str, t))
            r = l[::-1]
            s.append(int(l+r))
            if i < 24:
                s.append(int(l+'1'+r))
                s.append(int(l+'0'+r))

s.sort()

s = map(lambda x: x*x, s)

# binary search for index in list
def search(x):
    l = 0
    u = len(s)    
    
    while u > l+1:
        m = (u+l)/2
        if x < s[m]:
            u = m
        else:
            l = m
    return l


for case in range(int(raw_input())):
    a, b = map(int, raw_input().split())

    x, y = map(search, [a, b])

    ans = y-x
    if a == s[x]:
        ans += 1
    
    print "Case #%d: %d" % (case+1, ans)

