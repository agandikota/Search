from __future__ import print_function

dimension = 4

def rowCheck(board):
	for row in range(dimension):
		if ((board[row].count('X') == 4) or\
			((board[row].count('X') == 3 and 'T' in board[row]))):
			return "X won"
		elif (board[row].count('O') == 4 or\
			((board[row].count('O') == 3 and 'T' in board[row]))):
			return "O won"

def colCheck(board):
	cols = []
	for col in range(dimension):
		column = []
		for row in range(dimension):
			column.append(board[row][col])
		cols.append(column)

	for col in cols:
		if (col.count('X') == 4 or\
			((col.count('X') == 3 and 'T' in col))):
			return "X won"
		elif (col.count('O') == 4 or\
			((col.count('O') == 3 and 'T' in col))):
			return "O won"

def diagCheck(board):
	leftRight, rightLeft = [], [] 

	for x in range(dimension):
		leftRight.append(board[x][x])
		rightLeft.append(board[x][dimension - x - 1])

	if (leftRight.count('X') == 4 or\
		rightLeft.count('X') == 4 or\
		((leftRight.count('X') == 3 and 'T' in leftRight)) or\
		((rightLeft.count('X') == 3 and 'T' in rightLeft))):
			return "X won"

	elif (leftRight.count('O') == 4 or\
		rightLeft.count('O') == 4 or\
		((leftRight.count('O') == 3 and 'T' in leftRight)) or\
		((rightLeft.count('O') == 3 and 'T' in rightLeft))):
			return "O won"



def main():
	T = int(raw_input())

	for test in range(T):
		board = []

		for i in range(dimension):
			row = list(raw_input())
			if (not row):
				row = list(raw_input())
			board.append(row)

		rc = rowCheck(board)
		cc = colCheck(board)
		dc = diagCheck(board)

		if (rc != None):
			print ("Case #" + str(test+1) + ":" ,rc)
		elif(cc != None):
			print ("Case #" + str(test+1) + ":" ,cc)
		elif(dc != None):
			print ("Case #" + str(test+1) + ":" ,dc)
		else:
			dotCount = 0
			for row in range(dimension):
				dotCount += board[row].count('.')
			if (dotCount == 0):
				print ("Case #" + str(test+1) + ": Draw")
			else:
				print ("Case #" + str(test+1) + ":" ,"Game has not completed")

main()
