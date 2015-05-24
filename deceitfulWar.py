# from __future__ import print_function

# def main():
# 	for test in range(int(raw_input())):
# 		N = int(raw_input())
# 		naomi = map(float,raw_input().split())
# 		ken = map(float,raw_input().split())

# 		naomi.sort()
# 		ken.sort()
		
# 		#Deceitful war
# 		deceitCount = 0
# 		warCount = 0

# 		firstLarger = 0

# 		for i in range(N):
# 			if (naomi[i] > ken[i]):
# 				firstLarger = i

# 		for i in range(N - 1 - firstLarger):
# 			big = firstLarger + i
# 			if (naomi[big] > ken[i]):
# 				deceitCount += 1

# 		for i in range(N):
# 			found = False

# 			for j in range(len(ken)):
# 				#print (naomi, ken)
# 				if (ken[j] > naomi[i]):
# 					found = True
# 					del ken[j]
# 					break
# 			if (found == False):
# 				warCount += 1

# 		print ("Case #" + str(test+1) + ": " + str(deceitCount) +
# 		 " " + str(warCount), end = '')
# 		print("")
# main()



def compare(l, p):
    s = 0
    m = 0
    for x, y in l:
        s += [1, -1][y == p]
        print p, y, s
        m = max(m, s)
    return m
        

for case in range(int(raw_input())):
    n = int(raw_input())
    N = zip(*[map(float, raw_input().split()), [0]*n])
    K = zip(*[map(float, raw_input().split()), [1]*n])
    
    C = sorted(N+K)
    
    print C

    w = compare(C, 0)
    d = n-compare(C, 1)

    print "Case #%d: %d %d" % (case+1, d, w)