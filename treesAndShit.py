class Tree(object):
	"""docstring for Tree"""
	def __init__(self):
		self.left = None
		self.right = None
		self.data = None

def main():
	t = Tree()
	t.data = 3
	t.left = Tree()
	t.left.data = 3
	t.right = Tree()
	t.right.data = "right"
	

main()
		