class Node:
	def __init__(self, key : int):
		self.key = key
		self.left = None
		self.right = None

def inorder(node : Node):
	if node is not None:
		inorder(node.left)
		print(node.key)
		inorder(node.right)

def preorder(node : Node):
	if node is not None:
		print(node.key)
		preorder(node.left)
		preorder(node.right)

def insert(node : Node, key : int):
	if node is None:
		return Node(key)
	if key < node.key:
		node.left = insert(node.left, key)
	elif key > node.key:
		node.right = insert(node.right, key)
	return node

def minvalue(node : Node):
	mini = node
	while mini.left is not None:
		mini = mini.left
	return mini

def maxvalue(node : Node):
	maxi = node
	while maxi.right is not None:
		maxi = maxi.right
	return maxi

def delete(node : Node, key : int):
	if node is None :
		return node
	if key < node.key:
		node.left = delete(node.left, key)
	elif key > node.key :
		node.right = delete(node.right, key)
	else :
		if node.left is None :
			temp = node.right
			node = None
			return temp
		elif node.right is None :
			temp = node.left
			node = None
			return temp
		temp = minvalue(node.right)
		node.key = temp.key
		node.right = delete(node.right, temp.key)
	return node
