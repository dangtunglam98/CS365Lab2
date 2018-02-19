# Anh Dang and Lam Dang
# CS365 Lab B

from random import *

class Board:
	def __init__(self,rowsNum,colsNum,piecesNum):
		"""Return initial_state of the board, before any action was made"""
		self.rowsNum = rowsNum # x row
		self.colsNum = colsNum # y col
		self.piecesNum = piecesNum
		self.whiteNum = 0
		self.blackNum = 0
		self.board = []
		self.whitePos = []
		self.blackPos = []

		for blackpiece in range(self.piecesNum):
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

		for whitepiece in range(self.piecesNum):
			row = []
			for c in range(self.colsNum):
				row.append("O")
				self.whiteNum += 1
			self.board.append(row)

		for i in range (self.rowsNum):
			for j in range (self.colsNum):
				if self.board[i][j] == "X":
					self.blackPos.append((i,j))
				if self.board[i][j] == "O":
					self.whitePos.append((i,j))
	
	def transition(self,move):
		"""Move a piece to a certain position"""
		start, end = move
		xstart, ystart = start
		xend, yend = end
		endSym = self.board[xend][yend]
		startSym = self.board[xstart][ystart]
		
		if startSym == "X":
			if self.board[xend][yend] == "O":
				self.whiteNum -= 1
				self.whitePos.remove((xend,yend))
			self.blackPos.remove((xstart,ystart))
			self.blackPos.append((xend,yend))
			self.board[xend][yend] = startSym
			self.board[xstart][ystart] = "."
		elif startSym == "O":
			if self.board[xend][yend] == "X":
				self.blackNum -= 1
				self.blackPos.remove((xend,yend))
			self.whitePos.remove((xstart,ystart))
			self.whitePos.append((xend,yend))
			self.board[xend][yend] = startSym
			self.board[xstart][ystart] = "."
		else:
			pass

		return self

	def display_state(self):
		"""Return the current state of the board"""
		for row in self.board:
			print(' '.join(row))

	def terminal_test(self):
		"""Return the winner of the game"""
		if self.blackNum == 0 or ("O" in self.board[0]):
			
			return True
		elif self.whiteNum == 0 or ("X" in self.board[self.rowsNum - 1]):
			
			return True
		else:
			
			return False

	def move_generator(self,player):
		"""Return possible moves of a player"""
		moveset = {}
		for i in range (self.rowsNum):
			for j in range (self.colsNum):
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

	def moveList(self,player):
		moveList = []
		
		if player == "X":
			for row,col in self.blackPos:
				if (row < self.rowsNum-1) and ((self.board[row + 1][col] != "O") and (self.board[row + 1][col] != "X")):
					moveList.append(((row,col),(row+1,col)))
				if (row < self.rowsNum-1) and (col < self.colsNum-1) and (self.board[row+1][col+1] != "X"):
					moveList.append(((row,col),(row+1,col+1)))
				if (row < self.rowsNum-1) and (col > 0) and (self.board[row+1][col-1] != "X"):
					moveList.append(((row,col),(row+1,col-1)))

		if player == "O":
			for row,col in self.whitePos:
				if (row > 0) and ((self.board[row - 1][col] != "O") and (self.board[row - 1][col] != "X")):
					moveList.append(((row,col),(row-1,col)))
				if (row > 0) and (col < self.colsNum-1) and (self.board[row-1][col+1] != "O"):
					moveList.append(((row,col),(row-1,col+1)))
				if (row > 0) and (col > 0) and (self.board[row-1][col-1] != "O"):
					moveList.append(((row,col),(row-1,col-1)))

		# for key,vals in self.move_generator(player).items():
		# 	for end in vals:
		# 		moveList.append((key,end))
		return moveList

	def display_pos_move(self,moveset):
		"""Return the possible move on the board"""
		for keys, values in moveset.items():
			for i in values:
				(x,y) = i
				self.board[x][y] = "P"

a = Board(5,5,1)


# a.transition(((0,0),(1,0)))
# a.transition(((4,1),(2,1)))
# a.display_state()
# print(a.blackPos)
# print(a.whitePos)
# a.transition(((2,1),(1,0)))
# print(a.blackPos)
# print(a.blackNum)
# print(a.whitePos)
# print(a.whiteNum)
# a.display_state()
# a.transition(((0,4),(1,3)))
# print(a.moveList("X"))
# print(a.moveList("O"))


