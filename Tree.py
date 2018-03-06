#within this file contains the basic class definition for a tree as per professor Mathai's definition in lab 2 and the specific changes that Are instructed
class tree:
	def __init__(self,x):
		self.store = [x,[]]
	def AddSuccessor(self,x):
		self.store[1] = self.store[1] + [x]
		return True
	# def Print_DepthFirst(self):
		self.print_tree(self)
		return True
	def print_tree(self,tree, lvl=0):
		print '\t' *lvl + str(tree.store[0])
		if tree.store[1]:
			for i in range(0,len(tree.store[1])):
				self.print_tree(tree.store[1][i],lvl+1)
		return True
	def Get_LevelOrder(self):
		opQ = []
		toprint = []
		n=1
		if not self.store:
			return False
		else:
			toprint = toprint + [self.store[0]]
			if self.store[1]:
				for i in range(0,len(self.store[1])):
					opQ=opQ + [self.store[1][i]]
		while n==1:
			if not opQ:
			#	print toprint
				return toprint
			else:
				while opQ:
					toprint = toprint +[opQ[0].store[0]]
					if opQ[0].store[1]:
						for o in range(0,len(opQ[0].store[1])):
							opQ = opQ+[opQ[0].store[1][o]]
					del opQ[0]
		return False