# This is the file which contains the prescribed binary tree class similar to the other tree class found in tree.py(
import tree
class binary_tree:

        def __init__(self,x):
                        self.store = [x,[],[]]
        def AddLeft(self, x):
                self.store[1] = [x]
                return True
        def AddRight(self,x):
                self.store[2] = [x]
                return True
        def AddtoSuperRight(self,bt, val):
                if bt.store[2]:
                        return self.AddtoSuperRight(bt.store[2][0], val)
                if val.store:
                        bt.store[2]=[val]
                        return True
                z = binary_tree(val)
                bt.store[2]=[z]
                return True
        def printbylevel(self, bt, level=0):
                print "\t"*level+ str(bt.store[0])
                if (not bt.store[1]) and (not bt.store[2]):
                        return True
                if bt.store[1] and bt.store[2]:
                        return [self.printbylevel(bt.store[1][0], level+1), self.printbylevel(bt.store[2][0],level+1)]
                if bt.store[1]:
                        return self.printbylevel(bt.store[1][0],level+1)
                if bt.store[2]:
                        return self.printbylevel(bt.store[2][0],level+1)

                return False
        def ConverttoTree(self):
                if self.store[2]:
                        #print "This form of Binary Tree Has Not been defined; Root May not Contain right node"
                        return [False,]
                return [True, self.Tconvert()]
		def Tconvert(self):
                ntree = tree.tree(self.store[0])
                if self.store[1]:
                        leftsucc = self.store[1][0].Tconvert()
                        ntree.AddSuccessor(leftsucc)
                        if self.store[1][0].store[2]:
                                temp = self.store[1][0].store[2][0].Tconvert()
                                ntree.AddSuccessor(temp)
                                right = self.store[1][0].store[2][0]
                                while right.store[2]:
                                        rightsucc = right.store[2][0].Tconvert()
                                        ntree.AddSuccessor(rightsucc)
                                        right = right.store[2][0]

                return ntree
