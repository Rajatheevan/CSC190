from Tree import *
from random import randint

def howedge(board,position):
	val = 0.0
	if (position%8) == 0 or position%8 == 7:
		val = val +5
	if (position%8) == 1 or position%8 == 6:
		val = val + 4
	if (position%8) == 2 or position%8 == 5:
		val = val +3
	if (position%8) == 3 or position%8 == 4:
		val = val + 2
	#First 5 assigned
	if position < 32:
		val = val + (5-position/8.0)
	if position >= 32:
		val = val + abs((position/8.0 -5))
	return val
def imp(board,position,player):
	if player == 10:
		alpha = True
	if player == 20:
		alpha = False
	if alpha and (board[position] == 10) or (board[position] == 11) or (board[position] == 12) or (board[position] == 13) or (board[position] == 14) or (board[position] == 15):
		return True
	if (not alpha) and (board[position] == 20) or (board[position] == 21) or (board[position] == 22) or (board[position] == 23) or (board[position] == 24) or (board[position] == 25):
		return True
	else:
		return False
def mkdesire(board,temp,player,pval):
	luo = GetPlayerPositions(board,player)
	for u in luo:
		blah = GetPieceLegalMoves(board,u)
		if blah:
			for d in blah:
				if d==temp:
					if (board[temp] == 20 or board[temp]==10):
						#print 'blah 1'
						pval.append(1)
					if board[temp] >10 and board[temp] <20:
					#	print 'blah :',board[temp]%10
						pval.append(board[temp]%10)
					if board[temp] >20:
						#print 'blah :',board[temp]%10
						pval.append(board[temp]%10)
					#hol = board[u]
					#board[u] = 0
					#board[temp] = hol
					return [temp,u]
	return False
def iskng(board):
	alpha=False
	Beta = False
	for i in board:
		if i == 15:
			alpha = True
		if i ==25:
			Beta = True
	return (alpha and Beta)
def IsPositionUnderThreat(board,position,player):
	holder = []
	for i in range(0,63):
		if board[i] >15 and player == 10:
			rval = GetPieceLegalMoves(board,i)
			if rval:
				for d in rval:
					if d == position:
						holder.append(d)
		if board[i] <15 and player == 20:
			rval = GetPieceLegalMoves(board,i)
			if rval:
				for d in rval:
					if d == position:
						holder.append(d)
	
	if holder:
		return True	#put in a list with holder if you want to also understand the positions of the pieces that will hurt it		
	else:
		return False
def GetPlayerPositions(board,player):
	if player == 20:
		alpha = False
	if player == 10:
		alpha = True
	holder = []
	for i in range(0,63):
		if alpha:
			#print 'here'
			if board[i] < 20 and board[i] != 0:
				holder.append(i)
			
		if not alpha:
			#print 'jere'
			if board[i] > 15 and board[i]!=0:
				holder.append(i)
	return holder		


def GetPieceLegalMoves(board,position):
	if board[position]==0:
		return False
	local = board[position]%10
	poss = []
	if board[position] < 20:
		alpha = True
	else:
		alpha = False
	#now checks the legal moves]
	#THis involves insuring that the various moves that are actually legal are identified
	#Whereas the attacks are allowed on opposites and not on similars
	
	if local == 0:#For the pawn
		if board[position] == 10:
			try:
				if (board[position+7] > 15):#checks if there is another same piece there
					board[position+7] 
					poss.append(position+7)
			except:
				a = -1
				pass
				
			try: 
				if board[position+8] == 0:#checks if there is another same piece there
					board[position+8] 
					poss.append(position+8)
			except:
				b = -1
				pass
				
			try:
				if (board[position+9] > 15):#checks if there is another same piece there
					board[position+9] 
					poss.append(position+9)
			except:
				c = -1
				pass
				
		if board[position] == 20:
			try:
				if (board[position-7] < 20 and board[position-7] !=0):#checks if there is another same piece there
					board[position-7] 
					poss.append(position-7)
			except:
				a = -1
				pass
				
			try: 
				if board[position-8] == 0:#checks if there is another same piece there
					board[position-8] 
					poss.append(position-8)
			except:
				b = -1
				pass
				
			try:
				if (board[position-9] < 20 and board[position-9] != 0):#checks if there is another same piece there
					board[position-9] 
					poss.append(position-9)
			except:
				pass
				c = -1
		return poss
	if local == 1:#Ffor the Knight
		if alpha:#In the case the knight is white
			try:
				if position%8 == 0:
					board[65]
				else:
					if board[position+15] > 15 or board[position+15] == 0:
						board[position+15]
						poss.append(position+15)
			except:
				pass
				a = -1
			try:
				if position%8 == 7:#due to the span of the 17
					board[65]
				else:
					if board[position+17] > 15 or board[position+17] == 0:
						board[position+17]
						poss.append(position+17)
			except:
				pass
				b = -1
			try:
				if (position)%8 < 3:#Only applies to cols 4-8
					board[65]
				else:
					if board[position+6] > 15 or board[position+6] == 0:
						board[position+6]
						poss.append(position+6)
			except:
				pass
				c = -1
			try:
				if position%8 >5:
					board[65]
				else:
					if board[position+10] > 15 or board[position+10] == 0:
						board[position+10]
						poss.append(position+10)
			except:
				pass
				d = -1
			try:#----- 
			  if position-15 < 0 or position%8 ==7:
			    board[64]
			  else:
				  if board[position-15] > 15 or board[position-15] == 0:
					  board[position-15]
					  poss.append(position-15)
			except:
				pass
				a = -1
			try:
			  if position-17 < 0 or position%8 == 0:
			    board[64]
			  else:
				if board[position-17] > 15 or board[position-17] == 0:
					board[position-17]
					poss.append(position-17)
			except:
				pass
				b = -1
			try:
				if position-6 < 0 or (position%8)>3:
					board[64]
				else:
					if board[position-6] > 15 or board[position-6] == 0:
						board[position-6]
						poss.append(position-6)
			except:
				pass
				c = -1
			try:
				if position-10 < 0 or position%8 < 3:
					board[64]
				else:
					if board[position-10] > 15 or board[position-10] == 0:
						board[position-10]
						poss.append(position-10)
			except:
				pass
				d = -1
			return poss
		if not alpha:#The case where the knight is back
			try:
				if position%8 ==0:
					board[65]
				else:
					if board[position+15] < 20 or board[position+15] == 0:
						board[position+15]
						poss.append(position+15)
			except:
				pass
				a = -1
			try:
				if position%8 ==7:
					board[65]
				else:
					if board[position+17] < 20 or board[position+17] == 0:
						board[position+17]
						poss.append(position+17)
			except:
				pass
				b = -1
			try:
				if position%8 <3:
					board[65]
				else:
					if board[position+6] < 20 or board[position+6] == 0:
						board[position+6]
						poss.append(position+6)
			except:
				pass
				c = -1
			try:
				if position % 8 >5:
					board[65]
				else:
					if board[position+10] < 20 or board[position+10] == 0:
						board[position+10]
						poss.append(position+10)
			except:
				pass
				d = -1
			try:#----- 
			  if position-15 < 0 or position%8==7:
			    board[64]
			  else:
				  if board[position-15] < 20 or board[position-15] == 0:
					  board[position-15]
					  poss.append(position-15)
			except:
				pass
				a = -1
			try:
			  if position-17 < 0 or position%8==0:
			    board[64]
			  else:
				if board[position-17] < 20 or board[position-17] == 0:
					board[position-17]
					poss.append(position-17)
			except:
				pass
				b = -1
			try:
				if position-6 < 0 or position%8>3:
					board[64]
				else:
					if board[position-6] < 20 or board[position-6] == 0:
						board[position-6]
						poss.append(position-6)
			except:
				pass
				c = -1
			try:
				if position-10 < 0 or position%8 <3:
					board[64]
				else:
					if board[position-10] < 20 or board[position-10] == 0:
						board[position-10]
						poss.append(position-10)
			except:
				pass
				d = -1
			return poss
		else: 
			return False
	if local == 2:#For a bishop
		#These values will be used to ensure that the checker stops at the first point 
		#where there is a player(regardless type???)
		#print 'here2'
		a=0
		b=0
		c=0
		d=0
		n=0
		interval1 = 7
		interval2 = 9
		if alpha:
			#left bot first
			n=interval1
			while n < 64 and a!=-1:
				#print n, " : was the n and the position was: ", position
				try:
					#This section of the code refers to the positive growth and the 
					#% ensures that the code wont break as each multiple of the interval has limits to its range where it is accurate but not over the endge
					#Over flow is already taken care of due to the try
					
					#This process is repeated for the negative growth and for the other interval cases
					if (n==7 and position%8 ==0) or (n==14 and position % 8 <1) or (n==21 and position % 8 <2) or (n==28 and position % 8 <3) or (n==35 and position % 8 <4)or (n==42 and position % 8 <5) or (n==49 and position % 8 <6) or (n==56) or (n==63 and position % 8 !=0):
						board[65]
					if board[position+n] > 15 or board[position+n] == 0:
						poss.append(position+n)
					if board[position+n]!=0:
					  a = -1
				except:
					a=-1
					pass
				
				#	print 'nah'
				n=n+interval1
			#right bot
			n = interval2
			while n < 64 and b!= -1:
				#print n, " : was the n and the position was: ", position
				try:
					if (n==9 and position%8 ==7) or (n==18 and position %8 >5) or (n==27 and position%8 > 4) or (n==36 and position %8 > 3) or (n==45 and position%8 > 2 ) or (n==54) or (n==63 and position %8 != 0):
						board[65]
					if board[position+n] > 15 or board[position+n] == 0:
						poss.append(position+n)
					if board[position+n]!=0:
					    b = -1
				except:
					
					pass
				#	
				n=n+interval2
			#left top
			n = 63
			hold=[]
			while n >=0 and c!=-1:
				#print n," : is the n and the poss-n is: ", position-n
			
				try:
					if (n==63 and position%8 != 7) or (n==56 and position !=0) or (n==49 and position%8 > 0) or (n==42 and position %8 >1) or (n==35 and position%8 > 2) or (n==28 and position%8 >3) or (n==21 and position%8 >4) or (n==14 and position%8 > 5) or (n==7 and position%8 >6):
						
						board[65]
					if position-n < 0:
						
						board[65]
					if board[position-n] > 15 or board[position-n] == 0:
						#print 'mu'
						hold.append(position-n)
					if board[position-n]!=0:
					  c = -1
					  hold=[]
				except:
					
					pass
				#	print 'nah'
				n=n-interval1
			poss= poss+hold
			n = 63
			#print poss
			hold = []
			while n >=0 and d!=-1:
				try:
					if (n==63 and position%8 !=7) or (n==54 and position%8 < 6) or (n==45 and position %8 < 5) or (n==36 and position%8 < 4) or (n==27 and position%8 <3) or (n==18 and position%8<2) or (n==9 and position%8 == 0):
						board[65]
					if position-n<0:
						board[65]
					if board[position-n] > 15 or board[position-n] == 0:
						hold.append(position-n)
					if board[position-n]!=0:
						d = -1
						hold =[]
				except:
					pass
				#	print 'nah'
				n=n-interval2
			poss = poss +hold
			#This section quickly cleans up the return for double values
			blah = list(poss)
			for i in blah:
				if blah.count(i) >1:
					poss.remove(i)
			return poss
			#-------------------BLACK----------------------
		if not alpha:
			#left bot first
			n=interval1
			while n < 64 and a!=-1:
				#print n, " : was the n and the position was: ", position
				try:
					#This section of the code refers to the positive growth and the 
					#% ensures that the code wont break as each multiple of the interval has limits to its range where it is accurate but not over the endge
					#Over flow is already taken care of due to the try
					
					#This process is repeated for the negative growth and for the other interval cases
					if (n==7 and position%8 ==0) or (n==14 and position % 8 <1) or (n==21 and position % 8 <2) or (n==28 and position % 8 <3) or (n==35 and position % 8 <4)or (n==42 and position % 8 <5) or (n==49 and position % 8 <6) or (n==56) or (n==63 and position % 8 !=0):
						board[65]
					if board[position+n] <20 or board[position+n] == 0:
						poss.append(position+n)
					if board[position+n]!=0:
					  a = -1
				except:
					a=-1
					pass
				
				#	print 'nah'
				n=n+interval1
			#right bot
			n = interval2
			while n < 64 and b!= -1:
				#print n, " : was the n and the position was: ", position
				try:
					if (n==9 and position%8 ==7) or (n==18 and position %8 >5) or (n==27 and position%8 > 4) or (n==36 and position %8 > 3) or (n==45 and position%8 > 2 ) or (n==54) or (n==63 and position %8 != 0):
						board[65]
					if board[position+n] <20 or board[position+n] == 0:
						poss.append(position+n)
					if board[position+n]!=0:
					    b = -1
				except:
					
					pass
				#	
				n=n+interval2
			#left top
			n = 63
			hold = []
			while n >=0 and c!=-1:
				#print n," : is the n and the poss-n is: ", position-n
		
				try:
					if (n==63 and position%8 != 7) or (n==56 and position !=0) or (n==49 and position%8 > 0) or (n==42 and position %8 >1) or (n==35 and position%8 > 2) or (n==28 and position%8 >3) or (n==21 and position%8 >4) or (n==14 and position%8 > 5) or (n==7 and position%8 >6):
						
						board[65]
					if position-n < 0:
						
						board[65]
					if board[position-n] <20 or board[position-n] == 0:
						#print 'mu'
						hold.append(position-n)
					if board[position-n]!=0:
					  c = -1
					  hold = []
				except:
					
					pass
				#	print 'nah'
				n=n-interval1
			poss = poss +hold
			n = 63
			#print poss
			hold = []
			while n >=0 and d!=-1:
				try:
					if (n==63 and position%8 !=7) or (n==54 and position%8 < 6) or (n==45 and position %8 < 5) or (n==36 and position%8 < 4) or (n==27 and position%8 <3) or (n==18 and position%8<2) or (n==9 and position%8 == 0):
						board[65]
					if position-n<0:
						board[65]
					if board[position-n] <20 or board[position-n] == 0:
						hold.append(position-n)
					if board[position-n]!=0:
						d = -1
						hold = []
				except:
					pass
				#	print 'nah'
				n=n-interval2
			poss = poss+hold
			#This section quickly cleans up the return for double values
			blah = list(poss)
			for i in blah:
				if blah.count(i) >1:
					poss.remove(i)
			return poss
	if local == 3:#for the rook
		#print 'here3'
		a = 0
		b = 0
		c=0
		d=0
		interval = 8
		if alpha: #white
			while a!=-1:	
			  #print 'here'
				for i in range(1,8):
					#print i,"is i"
					try:
					#	print position+i
						if (i==7 and position%8 !=0) or (i==6 and position%8 >1) or (i==5 and position%8 >2) or (i==4 and position%8 >3) or (i==3 and position%8 >4) or (position %8 >5 and i==2) or (i==1 and position%8>6):
							board[65]
						if board[position+i] >15 or board[position+i] ==0:
							poss.append(position+i)
							if i ==6:
							  a=-1
						if board[position+i] !=0:
							a=-1
							break
						if (position+i)%8==0:
						  a=-1
						  break
					except:
						a=-1
						pass
				break
			while b!= -1:
				for i in range(1,8):
					try:
						if (i==7 and position%8 != 7) or (i==6 and position%8 <6) or (i==5 and position%8 <5) or (i==4 and position%8<4) or (i==3 and position%8<3) or (i==2 and position%8<2) or (i==1 and position%8==0):
							board[65]
						if board[position-i] >15 or board[position-i] ==0:
						#	print "the thing being appended is: ",position-i
							poss.append(position-i)
							if i==6:
							  b=-1
						if board[position-i] != 0:
							b=-1
							break
						if (position-i)%8==0:
						  b=-1
						  break
					except:
						b=-1
						pass
						
				#print 'ho'
				break
			n=interval
			while position+n <64 and c!=-1:
				#print n
				try:
					if board[position+n] >15 or board[position+n] ==0:
						poss.append(position+n)
					
					if board[position+n] != 0:
						c=-1
				except:
					pass
				n=n+interval
			n = interval
			while position-n >= 0 and d!=-1:
				try:
					if board[position-n] >15 or board[position-n] ==0:
						poss.append(position-n)
					if board[position-n] != 0:
						d=-1
				except:
					pass
				n=n+interval
			return poss
		if not alpha: #black-------------------------
			while a!=-1:	
			  #print 'here'
			  for i in range(1,8):
					try:
						if board[position+i] < 20 or board[position+i] ==0:
							poss.append(position+i)
							if i ==6:
							  a=-1
						if board[position+i] !=0:
							a=-1
							break
						if (position+i)%8==0:
						  a=-1
						  break
					except:
						a=-1
						pass
			while b!= -1:
				for i in range(1,8):
					try:
						if board[position-i] < 20 or board[position-i] ==0:
						#	print "the thing being appended is: ",position-i
							poss.append(position-i)
							if i==6:
							  b=-1
						if board[position-i] != 0:
							b=-1
							break
						if (position-i)%8==0:
						  b=-1
						  break
					except:
						b=-1
						pass
						
				#print 'ho'
			n=interval
			while position+n <64 and c!=-1:
				#print n
				try:
					if board[position+n] < 20 or board[position+n] ==0:
						poss.append(position+n)
					
					if board[position+n] != 0:
						c=-1
				except:
					pass
				n=n+interval
			n = interval
			while position-n >= 0 and d!=-1:
				try:
					if board[position-n] < 20 or board[position-n] ==0:
						poss.append(position-n)
					if board[position-n] != 0:
						d=-1
				except:
					pass
				n=n+interval
			return poss
	if local == 4:#for the queen
	#This piece will return the bishop at that point and the rook at that point
		if alpha:
			bval = 12
			cval = 13
		if not alpha:
			bval=22
			cval=23
		temp = list(board)
		hold = list(board)
		#This will be for the rook first
		temp[position] = bval
		hold[position] = cval
		return GetPieceLegalMoves(temp,position) + GetPieceLegalMoves(hold,position)
	if local==5:#for king
	#these are the possible moves all +-
		hu = 1#left and right//not valid for L:1 col or R:63col
		nu = 7
		mu = 8
		ru = 9
		rumo=False
		lumo=False
		if position%8==7:
			rumo = True
		if position%8==0:
			lumo=True
		if alpha:#white
			try:#This will overflow at 63 col ie when %8 is 7|| THIS IS 1
				if rumo:
					board[65]
				if board[position+hu] > 15 or board[position+hu] == 0:
					board[position+hu]
					poss.append(position+hu)
			except:
				pass
			try:
				if lumo or position-hu:
					board[65]
				if board[position-hu] > 15 or board[position-hu] == 0:
					board[position-hu]
					poss.append(position-hu)
			except:
				pass
			try:#This will not be valid when in col 1||THIS IS 7
				if lumo:
					board[65]
				if board[position+nu] > 15 or board[position+nu] == 0:
					board[position+nu]
					poss.append(position+nu)
			except:
				pass
			try:
				#THIS IS -7
				if rumo or position-nu <0:
					#print 'here'
					board[65]
				if board[position-nu] > 15 or board[position-nu] == 0:
					board[position-nu]
					poss.append(position-nu)
			except:
				pass
			try:#This will always be valid unless in the bot or top rows|\This is 8
				if board[position+mu] > 15 or board[position+mu] == 0:
					board[position+mu]
					poss.append(position+mu)
			except:
				pass
			try:
				#THIS IS -8
				if position-mu < 0:
					board[65]
				if board[position-mu] > 15 or board[position-mu] == 0:
					board[position-mu]
					poss.append(position-mu)
			except:
				pass
			try:#This will overflow at 63 col ie when %8 is 7|| THIS IS 9
				if position-ru or rumo < 0:
					board[65]
				if board[position-ru] > 15 or board[position-ru] == 0:
					board[position-ru]
					poss.append(position-ru)
			except:
				pass
			try:
				if rumo:
					board[65]
				if board[position+ru] > 15 or board[position+ru] == 0:
					board[position+ru]
					poss.append(position+ru)
			except:
				pass
			return poss
		if not alpha:#black
			try:#This will overflow at 63 col ie when %8 is 7|| THIS IS 1
				if rumo:
					board[65]
				if board[position+hu] < 20 or board[position+hu] == 0:
					board[position+hu]
					poss.append(position+hu)
			except:
				pass
			try:
				if lumo or position-hu <0:
					board[65]
				if board[position-hu] < 20 or board[position-hu] == 0:
					board[position-hu]
					poss.append(position-hu)
			except:
				pass
			try:#This will not be valid when in col 1||THIS IS 7
				if lumo:
					board[65]
				if board[position+nu] < 20 or board[position+nu] == 0:
					board[position+nu]
					poss.append(position+nu)
			except:
				pass
			try:
				#THIS IS -7
				if lumo or position-nu <0:
					board[65]
				if board[position-nu] < 20 or board[position-nu] == 0:
					board[position-nu]
					poss.append(position-nu)
			except:
				pass
			try:#This will always be valid unless in the bot or top rows|\This is 8
				if board[position+mu] < 20 or board[position+mu] == 0:
					board[position+mu]
					poss.append(position+mu)
			except:
				pass
			try:
				#THIS IS -8
				if position-mu < 0:
					board[65]
				if board[position-mu] < 20 or board[position-mu] == 0:
					board[position-mu]
					poss.append(position-mu)
			except:
				pass
			try:#This will overflow at 63 col ie when %8 is 7|| THIS IS 9
				if position-ru  < 0 or rumo:
					board[65]
				if board[position-ru] < 20 or board[position-ru] == 0:
					board[position-ru]
					poss.append(position-ru)
			except:
				pass
			try:
				if rumo:
					board[65]
				if board[position+ru] < 20 or board[position+ru] == 0:
					board[position+ru]
					poss.append(position+ru)
			except:
				pass
			return poss
		

			
def IsPositionrUnderThreat(board,position,player):
	if player == 10:
		alpha = 20
	if player == 20:
		alpha = 10
	newboard = list(board)
	newboard[position] = 0
	return IsPositionUnderThreat(newboard,position,alpha)
def PrintBoard(board):
	print board[:8],'\n',board[8:16],'\n',board[16:24],'\n',board[24:32],'\n',board[32:40],'\n',board[40:48],'\n',board[48:56],'\n',board[56:64],'\n'
	return True	
def printBoard(board):
   accum="---- BLACK SIDE ----\n"
   max=63
   for j in range(0,8,1):
      for i in range(max-j*8,max-j*8-8,-1):
         accum=accum+'{0: <5}'.format(board[i])
      accum=accum+"\n"
   accum=accum+"---- WHITE SIDE ----"
   return accum
def mkam(board,piece,player,ua=False):
	cta = 0
	ke = 0
	pv = 0
	if player ==10:
		alpha = 20
	if player == 20:
		alpha = 10
	poss = GetPieceLegalMoves(board,piece)
	# copy_poss = list(poss)
	if not poss:
		return [False,0]
	for i in poss:
	#clears poss of the dangerous moves
		if IsPositionUnderThreat(board,i,player):
			poss.remove(i)
	#We rank on how close it is to the wall--------------
	tempval = []		
	for i in poss:
		protected = IsPositionrUnderThreat(board,i,alpha)
		val = 10
		if ua:
			val = val + 90 
		if board[i]!= 0:
			val = val+cta
		if protected:
			val = val + pv
		if piece >= 32:
			val =val+ ke - float(10/(i))
			tempval.append([i,val])
		if piece < 32:
			val =val+ (ke/1.2) + float(10/(i+0.9))
			tempval.append([i,val])	
	#We rank on its relation to other pieces ie// if they can support it immediatly
	sumval = []
	for i in poss:
		if IsPositionrUnderThreat(board,i,alpha):
			sumval.append([i,50.0])
	rval = []
	for i in tempval:#all the values will be in tempval
		for q in sumval:#only the supported values will be here
			if q[0] == i[0]:
				#reassigns to completed value for this move set and returns the new vals to the rval
				temper = q[1]+i[1]
				rval.append([q[0],temper])
				tempval.remove(i)
	#adds the remaining unchanged position vals
	for i in tempval:
		rval.append(i)
	return rval
def mqam(board,piece,player,ua = False):
	cta = 15
	cv = 2.5
	pv = 5
	if player == 20:
		alpha = 10
	if player == 10:
		alpha = 20
	poss = GetPieceLegalMoves(board,piece)
	copyposs = list(poss)
	for i in poss:
		if IsPositionUnderThreat(board,i,player):
			poss.remove(i)
	tempval = []
	for i in poss:
		protected = IsPositionrUnderThreat(board,i,alpha) #being covered by another piece is always better
		centerness = abs(12.75-float(i/2))
		value = 10.0#90-centerness#where 90 is the upper bound
		value = value + abs(cv-centerness)*0.5
		if ua:
			value = value + 50
		if board[i]!=0:
			value = value + cta
		if protected:
			value = value + pv
		tempval.append([i,value])
	Alist=[]
	for i in copyposs: #These are moves that may be dangerous but are then ranked on their capacity to do damage//if this was a pawn it is allowed to do damage if its death will kill a greater piece
		pv = 2.5
		if (board[i] != 0) and IsPositionUnderThreat(board,i,player):#implies that it must be an opposing piece and the position is under threat
			if (board[i] == alpha+5): #stating that it will attack if it is a king or queen if it is a king 100% priority
				Alist.append([i, 100])
			if (board[i] == alpha+4):
				protected = IsPositionrUnderThreat(board,i,alpha)
				value = 10
				if ua:
					value = value + 50
				if protected:
					value = value + pv
				Alist.append([i, value])
		else:
			continue
	return tempval + Alist #returns the list of moves and the values of said moves
def mram(board,piece,player,ua=False):
	cta = 15
	ev = 2
	pv = 5
	if player == 20:
		alpha = 10
	if player == 10:
		alpha = 20
	poss = GetPieceLegalMoves(board,piece)
	copyposs = list(poss)
	for i in poss:
		if IsPositionUnderThreat(board,i,player):
			poss.remove(i)
	#poss is full of only safe moves// rooks prefer to be in along the edges of the board
	tempval = []
	for i in poss:
		protected = IsPositionrUnderThreat(board,i,alpha) #being covered by another piece is always better
		edgeness = howedge(board,i)
		value = 10.0#50+edgeness#where 70 is the upper bound
		value = value + edgeness/ev
		if ua:
			value = value + 30
		if board[i]!=0:#stating that safeattacks are better
			value = value+ cta
		if protected:
			value = value +pv
		tempval.append([i,value])
	Alist=[]
	for i in copyposs: #These are moves that may be dangerous but are then ranked on their capacity to do damage//if this was a pawn it is allowed to do damage if its death will kill a greater piece
		pv = 3
		if (board[i] != 0) and IsPositionrUnderThreat(board,i,player):#implies that it must be an opposing piece and the position is under threat
			value = 10.0
			protected = IsPositionrUnderThreat(board,i,alpha)
			if protected:
				value = value + pv
			if ua:#because a move must be made
				value = value + 30
			if (board[i] == alpha+5): #stating that it will attack if it is a king or queen if it is a king 100% priority
				Alist.append([i, 100])
			if (board[i] == alpha+4):
				Alist.append([i, value+4])
			if (board[i] == alpha+3):
				Alist.append([i, value+3])
			if (board[i] == alpha+2):
				Alist.append([i, value+2])
			if (board[i] == alpha+1):
				Alist.append([i, value+1])
			if (board[i] == alpha):
				Alist.append([i, value])
				
	return tempval + Alist #returns the list of moves and the values of said moves
def mbam(board,piece,player,ua=False):
	cta = 15
	cv = 2
	pv = 5
	if player == 20:
		alpha = 10
	if player == 10:
		alpha = 20
	poss = GetPieceLegalMoves(board,piece)
	copyposs = list(poss)
	
	for i in poss:
		if IsPositionUnderThreat(board,i,player):
			poss.remove(i)
	tempval = []
	for i in poss:
		protected = IsPositionrUnderThreat(board,i,alpha) #being covered by another piece is always better
		centerness = abs(12.75-float(i/2))
		value = 10#25+centerness#where 50 is the upper bound
		value = value + centerness/cv
		if ua:
			value = value + 20
		if board[i]!=0:#stating that safe attacks are better
			value = value+ cta
		if protected:
			value = value + pv
		tempval.append([i,value])
	Alist=[]
	for i in copyposs: #These are moves that may be dangerous but are then ranked on their capacity to do damage//if this was a pawn it is allowed to do damage if its death will kill a greater piece
		pv = 4
		if (board[i] != 0) and IsPositionrUnderThreat(board,i,player):#implies that it must be an opposing piece and the position is under threat
			value =  10.0
			protected = IsPositionrUnderThreat(board,i,alpha)
			if protected:
				value = value + pv
			if ua:#because a move must be made
				value = value + 20
			if (board[i] == alpha+5): #stating that it will attack if it is a king or queen if it is a king 100% priority
				Alist.append([i, 100])
			if (board[i] == alpha+4):
				Alist.append([i, value+4])
			if (board[i] == alpha+3):
				Alist.append([i, value+3])
			if (board[i] == alpha+2):
				Alist.append([i, value+2])
			if (board[i] == alpha+1):
				Alist.append([i, value+1])
			if (board[i] == alpha):
				Alist.append([i, value])
	return tempval + Alist
def mnam(board,piece,player,ua=False):
	cta = 15
	ev = 4
	pv = 2
	closev = 0.5
	if player == 20:
		alpha = 10
	if player == 10:
		alpha = 20
	poss = GetPieceLegalMoves(board,piece)
	copyposs = list(poss)
	
	for i in poss:
		if IsPositionUnderThreat(board,i,player):
			poss.remove(i)
	tempval = []
	for i in poss:
		protected = IsPositionrUnderThreat(board,i,alpha) #being covered by another piece is always better
		centerness = abs(12.75-float(i/2))
		edgeness = howedge(board,i)
		value = 10
		value = value + edgeness/ev
		if i/32 >= 1:
			value = value +(64-i)*closev
		if i/32 <= 1:
			value = value + abs(0-i)*closev
		if ua:
			value = value + 20
		if board[i]!=0:#stating that safe attacks are better
			value = value+ cta
		if protected:
			value = value + pv
		tempval.append([i,value])
	Alist=[]
	for i in copyposs: #These are moves that may be dangerous but are then ranked on their capacity to do damage//if this was a pawn it is allowed to do damage if its death will kill a greater piece
		pv = 4
		if (board[i] != 0) and IsPositionrUnderThreat(board,i,player):#implies that it must be an opposing piece and the position is under threat
			value = 10.0
			protected = IsPositionrUnderThreat(board,i,alpha)
			if protected:
				value = value + pv
			if ua:#because a move must be made
				value = value + 20
			if (board[i] == alpha+5): #stating that it will attack if it is a king or queen if it is a king 100% priority
				Alist.append([i, 100])
			if (board[i] == alpha+4):
				Alist.append([i, value+4])
			if (board[i] == alpha+3):
				Alist.append([i, value+3])
			if (board[i] == alpha+2):
				Alist.append([i, value+2])
			if (board[i] == alpha+1):
				Alist.append([i, value+1])
			if (board[i] == alpha):
				Alist.append([i, value])
	return tempval + Alist
def mpam(board,piece,player,ua = False):
	cta = 25
	pawnness = 5
	ag = 1.5
	ev = 4
	pv = 6
	if player == 20:
		alpha = 10
	if player == 10:
		alpha = 20
	poss = GetPieceLegalMoves(board,piece)
	
	copyposs = list(poss)
	
	for i in poss:
		if IsPositionUnderThreat(board,i,player):
			poss.remove(i)
	tempval = []
	for i in poss:
		edgeness = howedge(board,i)
		protected = IsPositionrUnderThreat(board,i,alpha) #being covered by another piece is always better
		centerness = abs(12.75-float(i/2))
		value = 10.0#10+centerness#where 50 is the upper bound
		value = value - edgeness/ev
		try:
			if board[i-7] == board[piece] or board[i-9]==board[piece]:
				value = value + pawnness
		except:
			pass
		if i/32 >= 1:
			value = value +(64-i)*ag
		if i/32 <= 1:
			value = value + abs(0-i)*ag
		if ua:
			value = value + 10
		if board[i]!=0:#stating that safe attacks are better
			value = value+ cta
		if protected:
			value = value + pv
		tempval.append([i,value])
	Alist=[]
	for i in copyposs: #These are moves that may be dangerous but are then ranked on their capacity to do damage//if this was a pawn it is allowed to do damage if its death will kill a greater piece
		pv = 5
		if (board[i] != 0) and IsPositionrUnderThreat(board,i,player):#implies that it must be an opposing piece and the position is under threat
			value = 10.0
			protected = IsPositionrUnderThreat(board,i,alpha)
			if protected:
				value = value + pv
			try:
				if board[i-7] == board[piece] or board[i-9]==board[piece]:
					value = value + pv/4
			except:
				pass
			if ua:#because a move must be made
				value = value + 10
			if (board[i] == alpha+5): #stating that it will attack if it is a king or queen if it is a king 100% priority
				Alist.append([i, 100])
			if (board[i] == alpha+4):
				Alist.append([i, value+4])
			if (board[i] == alpha+3):
				Alist.append([i, value+3])
			if (board[i] == alpha+2):
				Alist.append([i, value+2])
			if (board[i] == alpha+1):
				Alist.append([i, value+1])
			if (board[i] == alpha):
				Alist.append([i, value])
		return tempval + Alist
def addtoroot(root, val):
		x = tree(val)
		root.AddSuccessor(x)
		return True
def makebestmove(board,player,lvl=1):
	if player ==10:
		beta = 20
	if player == 20:
		beta = 10
	thtpnt=[]
	storage = tree('a')
	actsto = tree('b')
	#Generates all of the positions that are on the board
	current = GetPlayerPositions(board,player)
	#Copies the board//Used for the tree
	uAttack = []
	for i in current:
	#Determines if the current pieces can be attacked//
		if IsPositionUnderThreat(board,i,player):
			#If it is under attack it will be added to uAttack
			uAttack.append(i)
	
	#Need to consider the other cases in which under attack,
	if uAttack:
		for i in uAttack:
			for d in current:
				if i==d:
					current.remove(d)
	
	for i in uAttack:
		#sees if the king is under attack
		if board[i] ==15 or board[i]==25:
			#gets all the m
			poss=mkam(board,i,player,True)
			if poss:
				for u in poss:
					addtoroot(storage,u)
		if board[i]==14 or board[i] ==24:
			poss = mqam(board,i,player,True)
			if poss:
				for u in poss:
					addtoroot(storage,u)
		if board[i]==13 or board[i] ==23:
			poss = mram(board,i,player,True)
			if poss:
				for u in poss:
					addtoroot(storage,u)
		if board[i]==12 or board[i] ==22:
			poss = mbam(board,i,player,True)
			if poss:
				for u in poss:
					addtoroot(storage,u)
		if board[i]==11 or board[i] ==21:
			poss = mnam(board,i,player,True)
			if poss:
				for u in poss:
					addtoroot(storage,u)
		if board[i]==10 or board[i] ==20:
			poss = mpam(board,i,player,True)
			if poss:
				for u in poss:
					addtoroot(storage,u)
	if current:
		for i in current:
			
			
			if board[i] ==15 or board[i]==25:
			#gets all the m
				poss=mkam(board,i,player)
				if poss:
					for u in poss:
						addtoroot(storage,u)
			if board[i]==14 or board[i] ==24:
				poss = mqam(board,i,player)
				if poss:
					for u in poss:
						addtoroot(storage,u)
			if board[i]==13 or board[i] ==23:
				poss = mram(board,i,player)
				if poss:
					for u in poss:
						addtoroot(storage,u)
			if board[i]==12 or board[i] ==22:
				poss = mbam(board,i,player)
				if poss:
					for u in poss:
						addtoroot(storage,u)
			if board[i]==11 or board[i] ==21:
				poss = mnam(board,i,player)
				if poss:
					
					for u in poss:
						addtoroot(storage,u)
			if board[i]==10 or board[i] ==20:
				
				poss = mpam(board,i,player)
				if poss:
					
					for u in poss:
						addtoroot(storage,u)
#	attack values and the rest of the move set, another general kill function is good 
	# build another function similar to kill but cleaner ie for just regular moves that are safe and rank them
	if lvl == 2:
		compval = []
		for i in storage.store[1]:
			if i.store[0] == False:
				continue
			compval.append(i.store[0])
		medval = list(compval)
		while len(medval) != 1:
			for i in compval:
				if len(medval) == 1:
					break
				
				if i[1] > medval[0][1]:
					medval.pop(0)
				if len(medval) == 1:
					break
				if i[1] >= medval[-1][1]:
					medval.pop(-1)
			break
		return medval
		#compare the blahs and return the best one
		#best is the most selected one ie with the value in for [move,value]
	else:
		for i in storage.store[1]:
			if i.store[0] == False:
				continue
			superior = [i.store[0][0]]
			copyboard =list(board)
			#makes the i move for this team
			mkdesire(copyboard,superior[0],player,thtpnt)
			#makes the best possible move for the opposite team based on copy board
			try:
				mkdesire(copyboard,makebestmove(board,beta,2)[0],beta,thtpnt)
			except:
				continue
			#makes the third level(ie player, opponent, player) mv check
			endval = makebestmove(copyboard,player,2)
			#adds the final value of the supperior temp value
			#print endval,i.store[0]
			if not endval:
				continue
			superior.append(endval[0][1]+i.store[0][1])
			#adds it to the final checking tree
			addtoroot(actsto,superior)
		return actsto
def nebumachine(board,player):
	nn=[]
	poss = makebestmove(board,player)
	compval = []
	for i in poss.store[1]:
		if i.store[0] == False:
			continue
		compval.append(i.store[0])
	medval = list(compval)
	while len(medval) != 1:
		if not compval:
			break
		for i in compval:
			if len(medval) == 1:
				break
			
			if i[1] > medval[0][1]:
				medval.pop(0)
			if len(medval) == 1:
				break
			if i[1] >= medval[-1][1]:
				medval.pop(-1)
	try:
		return [medval[0][0],compval,poss]
	except:
		return False

def detree(list,player):
	#the passed list is in nthe form [move,percent]
	rlist = []
	for i in list:
		if i == 'b':
			continue
		hold = i[1]
		rlist.append([mkdesire(board,i[0],player,[]),hold])
	return rlist
def chessPlayer(board,player):
	try:
		nebures = nebumachine(board,player)
		movlis = mkdesire(board,nebures[0],player,[])
		candimoves = detree(nebures[2].Get_LevelOrder(),player)
		return [True,movlis,candimoves,nebures[2].Get_LevelOrder()[1:]]
	
	except:
		return [False,[],[],None]
