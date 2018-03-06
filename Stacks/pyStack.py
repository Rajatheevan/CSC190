class stack:
#Simple Stack implimented in python
    def __init__(self):
        self.lit = []
    def push(self,val):
        self.lit=self.lit+[val]
        return True
    def pop(self):
        temp = []
        if (len(self.lit)==0):
            return False
        if (len(self.lit)==1):
            rval = self.lit[0]
            self.lit = []
            return rval
        rval = self.lit[len(self.lit)-1]
        for i in range(0,len(self.lit)-1):
                temp = temp + [self.lit[i]]
        self.lit = temp
        return rval
    def stackprint(self):
        print self.lit
        return True
