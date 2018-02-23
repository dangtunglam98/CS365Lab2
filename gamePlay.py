# Anh Dang and Lam Dang
# CS365 Lab B

from boardClass import Board
from random import *
import time
import datetime

def switchPlayer(player):
	"""Switching between two player"""
	if player == "X":
		return "O"
	else:
		return "X"

def creat_board(row,col,state):
	"""Creat a board wit specific state"""
	board = Board(row,col,1)
	board.update_state(state)
	return board

def evasive(board,player):
	"""Return a value for the input board state"""
	if player == "X":
		return (board.blackNum + random())
	else:
		return (board.whiteNum + random())

def conqueror(board,player):
	"""Return a value for the input board state"""
	if player == "X":
		return (0 - board.whiteNum + random())
	else:
		return (0 - board.blackNum + random())

def defend(board,player):
	"""Return a value for the input board state"""
	dis = -float('inf')
	winPoint = 0
	if board.isPlayerWin(player):
		winPoint = 999
	elif board.isPlayerWin(switchPlayer(player)):
		winPoint = -999
	else:
		pass
	if player == "X":
		for p in board.blackPos:
			x,y = p
			if x > dis:
				dis = x
		return (0 - board.whiteNum + dis + winPoint + random())
	else:
		for p in board.whitePos:
			x,y = p
			if (board.rowsNum -1 - x) > dis:
				dis = x
		return (0 - board.blackNum + dis + winPoint + random())

def hidetowin(board,player):
	"""Return a value for the input board state"""
	dis = -float('inf')
	winPoint = 0
	if board.isPlayerWin(player):
		winPoint = 999
	elif board.isPlayerWin(switchPlayer(player)):
		winPoint = -999
	else:
		pass
	if player == "X":
		for p in board.blackPos:
			x,y = p
			if x > dis:
				dis = x
		return (board.blackNum + dis + winPoint + random())
	else:
		for p in board.whitePos:
			x,y = p
			if (board.rowsNum -1 - x) > dis:
				dis = x
		return (board.whiteNum + dis + winPoint + random())

def trytowin(board,player):
	score = 0
	if player == "X":
		for row,col in board.blackPos:
			score += (row**2+row+2)*5
			if (row-1,col-1) in board.blackPos:
				score += int(board.rowsNum/2)*5
			if (row-1,col+1) in board.blackPos:
				score += int(board.rowsNum/2)*5
		for row,col in board.whitePos:
			score -= ((board.rowsNum-1-row)**2+(board.rowsNum-1-row)+2)*5
		if board.isPlayerWin(player):
			score += 9999

	else:
		for row,col in board.whitePos:
			score += ((board.rowsNum-1-row)**2+(board.rowsNum-1-row)+2)*5
			if (row+1,col-1) in board.whitePos:
				score += int(board.rowsNum/2)*5
			if (row+1,col+1) in board.whitePos:
				score += int(board.rowsNum/2)*5
		for row,col in board.blackPos:
			score -= (row**2+row+2)*5
		if board.isPlayerWin(player):
			score += 9999
	score += random()
	return score




def alphabeta_search(board, player, d, util):
	"""Search game to determine best action; use alpha-beta pruning."""

	def max_value(board, player, alpha, beta, depth, util):
		"""Return the max value of the game forward states"""
		if board.terminal_test() or (depth > d):
			return util(board,player)
		val = -float('inf')
		for (m, b) in board.move_states(player):
			val = max(val, min_value(creat_board(board.rowsNum,board.colsNum,b), player, alpha, beta, depth+1, util))
			if val >= beta:
				return val
			alpha = max(alpha, val)
		return val
	
	def min_value(board, player, alpha, beta, depth, util):
		"""Return the min value of the game forward states"""
		if board.terminal_test() or (depth > d):
			return util(board,player)
		val = float('inf')
		for (m, b) in board.move_states(switchPlayer(player)):
			val = min(val, max_value(creat_board(board.rowsNum,board.colsNum,b), player, alpha, beta, depth+1, util))
			if val <= alpha:
				return val
			beta = min(beta, val)
		return val

	min_score = float('inf')
	best_score = -float('inf')
	best_move = board.move_list(player)[randint(0,(len(board.move_list(player))-1))]

	for m, b in board.move_states(player):
		val = min_value(creat_board(board.rowsNum,board.colsNum,b), player, best_score, min_score, 0, util)
		if val > best_score:
			best_move = m
			best_score = val
		min_score = min(min_score,val)
	return best_move

def play_game(heuristic_white,heuristic_black,board):
	"""Play a game and return the number of turns made between two choosen heuristic"""
	turn = 0
	total_time = time.time()
	print("----------------------------------------------------------")
	print("X: "+heuristic_black.__name__+" vs O: "+heuristic_white.__name__)
	print("The initial board is ")
	board.display_state()
	print("----------------------------------------------------------")
	while True:
		for player in ["O","X"]:
			start_time = time.time()
			if player == "O":
				util = heuristic_white
			else:
				util = heuristic_black
			move = alphabeta_search(board,player,3,util)
			board.transition(move)
			turn += 1
			print(player + " turn")
			board.display_state()
			print("The number of turns made: " + str(turn))
			print("The time to make this move is " + str(time.time() - start_time) + " seconds" )
			print("----------------------------------------------------------")
			if board.terminal_test():
				print("X: "+heuristic_black.__name__+" vs O: "+heuristic_white.__name__)
				print(player + ": "+util.__name__ + " Win")
				print("The total time to play this game is "+ str(datetime.timedelta(seconds=time.time()-total_time))+ " (hour/minute/seconds)")
				print("The number of white (O) pieces lost: " + str((board.piecesNum * board.colsNum) - board.whiteNum) )
				print("The number of black (X) pieces lost: " + str((board.piecesNum * board.colsNum) -board.blackNum))
				print("----------------------------------------------------------")
				return turn

