# Anh Dang and Lam Dang
# CS365 Lab B


class Board:
	def __init__(self):
		self.rowsNum = 0
		self.colsNum = 0
		self.piecesNum = 0
		self.whiteNum = 0
		self.blackNum = 0
		self.board = []

	def initial_state(self,rowsNum,colsNum,piecesNum):
		self.rowsNum = rowsNum
		self.colsNum = colsNum
		self.piecesNum = piecesNum

		for whitepiece in range(self.piecesNum):
			row = []
			for c in range(self.colsNum):
				row.append("X")
				self.blackNum += 1
			self.board.append(row)

		for r in range(self.rowsNum - (self.piecesNum*2)):
			row = []
			for c in range(self.colsNum):
				row.append(".")
			self.board.append(row)

		for blackpiece in range(self.piecesNum):
			row = []
			for c in range(self.colsNum):
				row.append("O")
				self.whiteNum += 1
			self.board.append(row)

	def move(self,start,end):
		xstart, ystart = start
		xend, yend = end
		if self.board[xend][yend] == "O":
			self.whiteNum -= 1
		if self.board[xend][yend] == "X":
			self.blackNum -= 1
		self.board[xend][yend] = self.board[xstart][ystart]
		self.board[xstart][ystart] = "."

	def display_state(self):
		for row in self.board:
			print(' '.join(row))

	def ending_state(self):
		if self.blackNum == 0 or ("O" in self.board[0]):
			print("White wins")
			return True
		elif self.whiteNum == 0 or ("X" in self.board[self.rowsNum - 1]):
			print("Black wins")
			return True
		else:
			print("Not ending state")
			return False

	def move_generator(self,player):
		moveset = {}
		for j in range (self.rowsNum-1):
			for i in range (self.colsNum-1):
				if self.board[i][j] == player:
					moveset.update({(i,j):[]})
		for row, col in moveset.keys():
			if player == "X":
				if (row < self.rowsNum-1) and ((self.board[row + 1][col] != "O") and (self.board[row + 1][col] != "X")):
					moveset[(row,col)].append((row+1,col))
				if (row < self.rowsNum-1) and (col < self.colsNum-1) and (self.board[row+1][col+1] != "X"):
					moveset[(row,col)].append((row+1,col+1))
				if (row < self.rowsNum-1) and (col > 0) and (self.board[row+1][col-1] != "X"):
					moveset[(row,col)].append((row+1,col-1))
			if player == "O":
				if (row > 0) and ((self.board[row - 1][col] != "O") and (self.board[row - 1][col] != "X")):
					moveset[(row,col)].append((row-1,col))
				if (row > 0) and (col < self.colsNum-1) and (self.board[row-1][col+1] != "O"):
					moveset[(row,col)].append((row-1,col+1))
				if (row > 0) and (col > 0) and (self.board[row-1][col-1] != "O"):
					moveset[(row,col)].append((row-1,col-1))
		return moveset

	def display_pos_move(self,moveset):
		for keys, values in moveset.items():
			for i in values:
				(x,y) = i
				self.board[x][y] = "P"

a = Board()
a.initial_state(8,8,2)
a.display_state()
# print(a.move_generator("X"))
a.display_pos_move(a.move_generator("X"))
a.display_state()
# a.move((1,0),(2,0))
# a.move((2,0),(7,0))
# a.display_state()
# print(a.whiteNum)
# a.ending_state()