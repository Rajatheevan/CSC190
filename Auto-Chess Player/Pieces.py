# This Document Covers the Specific Move Sets of each of the pieces in EzChess
# These Include Pawns, Knights, Bishops, Rooks and the Royalty
board = [0,0,0,0,0,0,0,0,
		 13,25,0,0,0,0,0,0,
		 0,0,0,0,0,0,0,0,
		 23,0,0,0,0,0,0,0,
		 0,0,0,0,0,0,0,0,
		 0,0,0,0,0,0,0,0,
		 0,0,0,0,0,0,0,0,
		 0,0,0,0,0,0,0,0]
player = 10 #for While
player1 = 20 #for Black
#returns a value out of 10 on how edgy the location 
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
	
#checks if a piece is the same as the player
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
		
#Switches the desired piece with the desired location	
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
					hol = board[u]
					board[u] = 0
					board[temp] = hol
					return True
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

#Pawns -----------------
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
		
#In terms of understanding what move to make it is important:
#We play for points my NEBU
# Always make the move that takes the king:
# || Make a killing move unless it will result in death|| - Caviate:::if the points are better do the points
#	||make moves that result in being in a place protected by another piece||
#	||Value being in the center of the board rather than the edges||
#	||Play to point not checks||
#	Value moving the king least, pawns and knights the most|| Rooks are kings
#	||Rule your side of the board||
###############################################################
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

