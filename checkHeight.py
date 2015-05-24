class Tree(object):
	"""docstring for Tree"""
	def __init__(self):
		self.left = None
		self.right = None
		self.data = None

#Check if the tree is balanced - height of left and right subtree differ by <= 1

def checkHeight(tree,height):
	print tree.data,height
	if (tree.left == None and tree.right == None):
		return height
	elif (tree.left == None):
		return checkHeight(tree.right,height + 1)
	elif tree.right == None:
		return checkHeight(tree.left,height + 1)
	else:
		return abs((checkHeight(tree.left, height + 1)) - (checkHeight(tree.right, height + 1))) <= 1

def main():
	t = Tree()
	t.data = "root"
	t.left = Tree()
	t.left.data = "first left"
	t.left.left = Tree()
	t.left.left.data = "second left"
	# t.left.left.left = Tree()
	# t.left.left.left.data = "third left"
	t.right = Tree()
	t.right.data = "first right"
	print(checkHeight(t,0))
	

main()
		