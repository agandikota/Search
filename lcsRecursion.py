def lcss(xStr,yStr):
	if not xStr or not yStr:
		return ""

	x,y = xStr[0],yStr[0]
	xs, ys = xStr[1:], yStr[1:]

	if (x == y):
		return x + lcs(xs,ys)
	else:
		return max(lcs(xs,yStr),lcs(xStr,ys), key = len)

def lcs(a, b):

    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            print i,j
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])

    # read the substring out from the matrix
    result = ""

    x, y = len(a), len(b)
    
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result
            x -= 1
            y -= 1
    return result



def main():
	strA = "thdis"
	strB = "sdhdid"

	print lcs(strA,strB)

main()
