from boardClass import Board
from random import *
import time
import datetime
def switchPlayer(player):
	if player == "X":
		return "O"
	else:
		return "X"

def creat_board(row,col,state):
	board = Board(row,col,1)
	board.update_state(state)
	return board

def evasive(board,player):
	if player == "X":
		return (board.blackNum + random())
	else:
		return (board.whiteNum + random())

def conqueror(board,player):
	if player == "X":
		return (0 - board.whiteNum + random())
	else:
		return (0 - board.blackNum + random())

def defend(board,player):
	dis = float('inf')
	if player == "X":
		for p in board.whitePos:
			x,y = p
			if x < dis:
				dis = x 
		return (0 - board.whiteNum + dis + random())
	else:
		for p in board.blackPos:
			x,y = p 
			if (board.rowsNum - 1 - x) < dis:
				dis = x 
		return (0 - board.blackNum + dis + random())

def hidetowin(board,player):
	dis = float('inf')
	if player == "X":
		for p in board.blackPos:
			x,y = p
			if (board.rowsNum - 1 - x) < dis:
				dis = x
		return (board.blackNum - dis + random())
	else:
		for p in board.whitePos:
			x,y = p
			if x < dis:
				dis = x
		return (board.whiteNum - dis + random())


def alphabeta_search(board, player, d, util):
	"""Search game to determine best action; use alpha-beta pruning.
	This version cuts off search and uses an evaluation function."""

	def max_value(board, player, alpha, beta, depth, util):
		if board.terminal_test() or (depth > d):
			return util(board,player)
		val = -float('inf')
		for (m, b) in board.move_states(player):
			val = max(val, min_value(creat_board(board.rowsNum,board.colsNum,b), player, alpha, beta, depth+1, util))
			if val >= beta:
				return val
			alpha = max(alpha, val)
		return val
		print()
	def min_value(board, player, alpha, beta, depth, util):
		if board.terminal_test() or (depth > d):
			return util(board,player)
		val = float('inf')
		for (m, b) in board.move_states(switchPlayer(player)):
			val = min(val, max_value(creat_board(board.rowsNum,board.colsNum,b), player, alpha, beta, depth+1, util))
			if val <= alpha:
				return val
			beta = min(beta, val)
		return val

	best_score = -float('inf')
	best_move = None

	for m, b in board.move_states(player):
		val = min_value(creat_board(board.rowsNum,board.colsNum,b), player, -float('inf'), float('inf'), 0, util)
		if val > best_score:
			best_move = m 
			best_score = val

	# move, board = argmax(board.move_states(player), lambda ((m, b)): min_value(b, -float('inf'), float('inf'), 0))
	return best_move

def play_game(heuristic_white,heuristic_black,board):
	turn = 0
	total_time = time.time()
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
			board.display_state()
			print(player + " turn")
			print("The number of turns made: " + str(turn))
			print("The time to make this move is " + str(time.time() - start_time) + " seconds" )
			print("----------------------------------------------------------")
			if board.terminal_test():
				print(player + " Win")
				print("The total time to play this game is "+ str(datetime.timedelta(seconds=time.time()-total_time))+ " (hour/minute/seconds)")
				print("The number of white pieces lost: " + str((board.piecesNum * board.colsNum) - board.whiteNum) )
				print("The number of black pieces lost: " + str((board.piecesNum * board.colsNum) -board.blackNum))
				print("----------------------------------------------------------")

				return turn


a = Board(5,5,1)
play_game(defend,hidetowin,a)
