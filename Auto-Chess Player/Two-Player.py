import Pieces

board=[13,12,11,14,15,11,12,13,
		 10,10,10,10,10,10,10,10,
		 0,0,0,0,0,0,0,0,
		 0,0,0,0,0,0,0,0,
		 0,0,0,0,0,0,0,0,
		 0,0,0,0,0,0,0,0,
		 20,20,20,20,20,20,20,20,
		 23,22,21,24,25,21,22,23]
		 
		 
done = False
while not done:
	#This is the white asker
	temp = True
	result = False
	hold = []
	while temp:
		PrintBoard(board)
		print "you are the white player"
		piece = raw_input('What piece would you like to move? ')
		print GetPieceLegalMoves(board,int(piece))
		desire = raw_input('Where would you like it to go? ')
		hold = GetPieceLegalMoves(board,int(piece))
		if hold:
			for d in hold:
				print d
				if d  == int(desire):
					print 'here'
					result = True
		if result == False:
			print 'That is not a legal Move'
		if result == True:
			temp = False
		if (int(piece) > 15 or int(piece) == 0):
			temp = True
			print 'That is not your piece'
			
			
		if temp == False:
			blah = board[int(piece)]
			board[int(piece)] = 0
			board[int(desire)] = blah
	#------------------------------------#
	temp = True
	result = False
	hold = []
	while temp:
		PrintBoard(board)
		print "you are the Black player"
		piece = raw_input('What piece would you like to move? ')
		print GetPieceLegalMoves(board,int(piece))
		desire = raw_input('Where would you like it to go? ')
		hold = GetPieceLegalMoves(board,int(piece))
		if hold:
			for d in hold:
				print d
				if d  == int(desire):
					print 'here'
					result = True
		if result == False:
			print 'That is not a legal Move'
		if result == True:
			temp = False
		if (int(piece) < 20 or int(piece) == 0):
			temp = True
			print 'That is not your piece'
			
		if temp == False:
			blah = board[int(piece)]
			board[int(piece)] = 0
			board[int(desire)] = blah
	#-----------------------------------------------------------------#
		
		
	
	
	