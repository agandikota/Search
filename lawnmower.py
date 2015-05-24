# Every element's row or column should be less than or equal to it

from __future__ import print_function

def checkElement(lawn,noOfRows,noOfCols):
	for row in range(noOfRows):
		for col in range(noOfCols):
			elemRow = lawn[row]
			elemCol = []
			for i in range(noOfRows):
				elemCol.append(lawn[i][col])
			# check row
			rowCheck, colCheck = True, True
			for i in range(noOfCols):
				if (lawn[row][i] > lawn[row][col]):
					rowCheck = False

			for i in range(noOfRows):
				if (lawn[i][col] > lawn[row][col]):
					colCheck = False

			if (rowCheck == False and colCheck == False):
				return "NO"
	return "YES"

def main():
	T = int(raw_input())

	for test in range(T):
		noOfRows,noOfCols = map(int, raw_input().split())
		lawn = []

		for i in range(noOfRows):
			row = map(int,raw_input().split())
			lawn.append(row)

		print ("Case #" + str(test+1) + ":" ,checkElement(lawn,noOfRows,noOfCols))

main()