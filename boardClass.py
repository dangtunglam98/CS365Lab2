# Anh Dang and Lam Dang
# CS365 Lab B

class Board:
	def __init__(self,rowsNum,colsNum,piecesNum):
		"""initial_state of the board, before any action was made"""
		self.rowsNum = rowsNum # x row
		self.colsNum = colsNum # y col
		self.piecesNum = piecesNum
		self.whitePos = []
		self.blackPos = []

		for j in range(self.colsNum):
			for i in range(self.piecesNum):
				self.blackPos.append((i,j))
			for k in range(self.rowsNum-self.piecesNum,self.rowsNum):
				self.whitePos.append((k,j))
		
		self.whiteNum = len(self.whitePos)
		self.blackNum = len(self.blackPos)

	def update_state(self,state):
		"""Update the board with input state"""
		whitePos, blackPos = state
		self.whitePos = whitePos
		self.blackPos = blackPos
		self.whiteNum = len(self.whitePos)
		self.blackNum = len(self.blackPos)

	def transition(self,move):
		"""Update the board state after moving a piece to a certain position"""
		start, end = move
		
		if start in self.blackPos:
			if end in self.whitePos:
				self.whiteNum -= 1
				self.whitePos.remove(end)
			self.blackPos.remove(start)
			self.blackPos.append(end)
		elif start in self.whitePos:
			if end in self.blackPos:
				self.blackNum -= 1
				self.blackPos.remove(end)
			self.whitePos.remove(start)
			self.whitePos.append(end)
		else:
			pass

		return self

	def display_state(self):
		"""Display the current state of the board"""
		board = []
		for r in range(self.rowsNum):
			row = []
			for c in range(self.colsNum):
				row.append(".")
			board.append(row)
		for x,y in self.blackPos:
			board[x][y] = "X"
		for x,y in self.whitePos:
			board[x][y] = "O"
		for row in board:
			print(' '.join(row))
		return board

	def terminal_test(self):
		"""Check if it is the endgame state"""
		if self.blackNum == 0 or self.whiteNum == 0:
			return True
		for x,y in self.whitePos:
			if x == 0:
				return True
		for x,y in self.blackPos:
			if x == self.rowsNum - 1:
				return True
		return False

	def isPlayerWin(self,player):
		"""Check if the input player won the game"""
		if player == "X":
			if self.whiteNum == 0:
				return True
			for x,y in self.blackPos:
				if x == self.rowsNum - 1:
					return True
			return False
		else:
			if self.blackNum == 0:
				return True
			for x,y in self.whitePos:
				if x == 0:
					return True
			return False

	def inOpponentSide(self,player):
		posList = []
		if player == "X":
			for row,col in self.blackPos:
				if row in range(self.rowsNum-int((self.rowsNum)/2),self.rowsNum):
					posList.append((row,col))
		else:
			for row,col in self.whitePos:
				if row in range(0,int(self.rowsNum/2)):
					posList.append((row,col))
		return posList


	def move_list(self,player):
		"""Generate all possible moves for the input player"""
		move_list = []
		if player == "X":
			for row,col in self.blackPos:
				if (row < self.rowsNum-1) and (col > 0) and ((row+1,col-1) not in self.blackPos):
					move_list.append(((row,col),(row+1,col-1)))
				if (row < self.rowsNum-1) and ((row+1,col) not in self.whitePos) and ((row+1,col) not in self.blackPos):
					move_list.append(((row,col),(row+1,col)))
				if (row < self.rowsNum-1) and (col < self.colsNum-1) and ((row+1,col+1) not in self.blackPos):
					move_list.append(((row,col),(row+1,col+1)))
				
		if player == "O":
			for row,col in self.whitePos:
				if (row > 0) and (col > 0) and ((row-1,col-1) not in self.whitePos):
					move_list.append(((row,col),(row-1,col-1)))
				if (row > 0) and ((row-1,col) not in self.whitePos) and ((row-1,col) not in self.blackPos):
					move_list.append(((row,col),(row-1,col)))
				if (row > 0) and (col < self.colsNum-1) and ((row-1,col+1) not in self.whitePos):
					move_list.append(((row,col),(row-1,col+1)))
	
		return move_list

	def move_states(self,player):
		"""Return all possible moves and states after that move for the input player"""
		move_states = []
		for start,end in self.move_list(player):
			if player == "X":
				black = [x if (x != start) else end for x in self.blackPos]
				white = [x for x in self.whitePos if (x != end)]
			else:
				white = [x if (x != start) else end for x in self.whitePos]
				black = [x for x in self.blackPos if (x != end)]
			move_states.append(((start,end),(white,black)))
		return move_states
