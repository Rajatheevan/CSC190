#welcome to the Python Bracket Checker Professor
import pyStack
#This line imports the stack library which has the functions pop push and a helper function stackprint. It follows the LIFO model.
#-------------------------------------------------------------------------------------------------------#
#               The Specific Usage of push is as such:
#                               push(value)
#               Wherin value is the term that you would like to add to the stack:
#                       This function will return True
#
#
#               Similarily the usage for pop is as such
#                               pop()
#               This will return the value that is popped and remove it from the stack
#
#
#               Finally the usage for the print helper function is:
#                               stackprint()
#               This will print the function and return True
#

def bc():
    n = 0
    cnt = 0
    stak = pyStack.stack()
    value = raw_input("")
    n=0
    cnt=-1


    for i in range(0,len(value)):
        #print i
        cnt = cnt+1
        if ((value[i] == "[") or (value[i] == "(" ) or (value[i]== "{")):
                n = n+1
                # print "here"+value[i]
                stak.push(value[i])
        if ((value[i] =="]") or (value[i] == ")") or (value[i] == "}")):
                if(n==0):
                        n = n+1
                        break
                hold = stak.pop()
                n=n+1
                oldn = n
                if((hold == '[') and (value[i] == ']')):
                #       print("here")
                        n=n-2
				if ((hold == "(") and (value[i] == ")")):
                        n = n-2
                if ((hold == "{") and (value[i] == "}")):
                        n = n-2
                if(oldn == n):
                        break
    if n == 0:
        print [True, 0]
        return [True,0]
    if n != 0:
        print [False,(cnt)]
        return [False,cnt]
