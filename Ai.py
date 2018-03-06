
#This will be the basis of the Auto-Function and the Move Checker
from Pieces import *
from random import randint
from Tree import *


#                             \\King// 
#This piece must be passed a king it does not check\
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
#                             \\Queen// 
#This piece must be passed a queen it does not check
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
#                             \\Rook// 
#This piece must be passed a rook it does not check
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

#                             \\Bishop// 
#This piece must be passed a bishop it does not check	
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
#                             \\Knight// 
#This piece must be passed a knight it does not check
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
#                             \\Pawn// 
#This piece must be passed a pawn it does not check
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

#pieces are moved based on value out of 100
def makebestmove(board,player,lvl=1):#used to incur the number of levels that we want
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
	#here it will check the actsto tree looking for the one with the highest value and return that move
	
	# to do list---------------
	# finish the attack set and the rules
	# add the pos not under threat set values
	# make function that checks the piece and returns its value for being in a certain place or not
	# ensure that the function works!!!!!!!!!
	# compare spec?
	
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
		return medval[0][0]
	except:
		return False
	
	
	mkdesire(board,medval[0][0],player,nn)
	return True
