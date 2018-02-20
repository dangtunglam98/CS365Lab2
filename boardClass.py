# Anh Dang and Lam Dang
# CS365 Lab B

from random import *
from copy import deepcopy

class Board:
	def __init__(self,rowsNum,colsNum,piecesNum):
		"""Return initial_state of the board, before any action was made"""
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
	
	def get_board(self):
		return self

	def transition(self,move):
		"""Move a piece to a certain position"""
		
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
		"""Return the current state of the board"""
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

	def terminal_test(self):
		"""Return the winner of the game"""

		if self.blackNum == 0 or self.whiteNum == 0:
			return True
		for x,y in self.whitePos:
			if x == 0:
				return True
		for x,y in self.blackPos:
			if x == self.rowsNum - 1:
				return True
		return False

	def move_list(self,player):
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
		return [(move, deepcopy(self).transition(move)) for move in self.move_list(player)]


	def evasive(self,player):
		if player == "X":
			return (self.blackNum + random())
		else:
			return (self.whiteNum + random())

	def conqueror(self,player):
		if player == "X":
			return (0 - self.whiteNum + random())
		else:
			return (0 - self.blackNum + random())

# a = Board(5,5,1)
# print(a.whitePos)
# print(a.blackPos)
# a.display_state()
# a.transition(((0,0),(4,0)))
# a.display_state()
# print(a.terminal_test())
# print(float('inf')>0)
# a.move_states("X")
# a.display_state()
# c,d = [(1,2),(3,4)]
# print(c)

