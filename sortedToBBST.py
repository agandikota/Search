import math

class Tree(object):
	"""docstring for Tree"""
	def __init__(self):
		self.left = None
		self.right = None
		self.data = None

# Given a sorted array of ints, create a balanced binary tree out of it

def checkHeight(tree,height):
	#print tree.data,height
	if (tree.left == None and tree.right == None):
		return height
	elif (tree.left == None):
		return checkHeight(tree.right,height + 1)
	elif tree.right == None:
		return checkHeight(tree.left,height + 1)
	else:
		return abs((checkHeight(tree.left, height + 1)) - (checkHeight(tree.right, height + 1))) <= 1

def sortBBST(array,t):
	print "Tree"

	if (len(array) == 0):
		return

	elif(len(array) == 1):
		t.data = array[0]

	elif (len(array) == 2):
		t.data = array[1]
		t.left = Tree()
		t.left.data = array[0]
	else:
		median = int(math.floor(len(array)/2))
		t.data = array[median]
		length = len(array)
		t.left = Tree()
		sortBBST(array[0:(length/2)],t.left)
		t.right = Tree()
		sortBBST(array[(length/2):length],t.right)

def main():
	sortedInts = [21, 22,23,24,25,26,27,28,29,30,31]
	t = Tree() #Try without this as well
	sortBBST(sortedInts,t)
	if (checkHeight(t,0)):
		print "Success"
		print t.right.left.data
	else:
		print "Not balanced"

main()