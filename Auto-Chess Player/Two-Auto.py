from Pieces import *
from random import randint


 
rat = 10
black = 0
white = 0
for p in range(0,rat):
	board=[13,12,11,14,15,11,12,13,
		 10,10,10,10,10,10,10,10,
		 0,0,0,0,0,0,0,0,
		 0,0,0,0,0,0,0,0,
		 0,0,0,0,0,0,0,0,
		 0,0,0,0,0,0,0,0,
		 20,20,20,20,20,20,20,20,
		 23,22,21,24,25,21,22,23]

	done = False
	cnt = 0
	blkpnt = []
	whtpnt = []
	while not done:
		cnt = cnt+1
		accum = []
		Luo = GetPlayerPositions(board,10)
		for i in Luo:
			blah = GetPieceLegalMoves(board,i)
			if blah:
				for d in blah:
					
					if not(IsPositionUnderThreat(board,d,10)):
						accum = accum + [d]
		
		temp = accum[randint(0,len(accum)-1)]
		mkdesire(board,temp,10,whtpnt)
		#print whtpnt
		#print "---------------White move----------- ",cnt
		#PrintBoard(board)
		#black-------------------------
		accum = []
		Luo = GetPlayerPositions(board,20)
		for i in Luo:
			blah = GetPieceLegalMoves(board,i)
			if blah:
				for d in blah:
					
					if not(IsPositionUnderThreat(board,d,20)):
						accum = accum + [d]
		
		if not accum:
			break
		temp = accum[randint(0,len(accum)-1)]#This is the random selector!!!!
		#--------------------------------------------------------------------------#
		#What we want is to take each of these moves that exist in accum;
		#With these moves we pull them into the checker and evaluate them;
		#will return a list of values with the move and their rankings#
		#Our rules of chess benefit moves for each piece#
		#Consider what it would take to balance taking a piece based on the value exchanged???
		#
		#
		mkdesire(board,temp,20,blkpnt)
		#print blkpnt
		#print "---------------Black move----------- ",cnt
		#PrintBoard(board)
		if not iskng(board):
			print "---------------Final move----------- ",cnt
			PrintBoard(board)
			print "White had : ",sum(whtpnt), "Points"
			print "Black had : ", sum(blkpnt), "Points"
			done = True
			break
	if sum(whtpnt)>sum(blkpnt):
		white=white+1
	if sum(whtpnt)<sum(blkpnt):
		black =black+1
print 'white is: ',white,' black is: ',black, 'out of: ',rat
