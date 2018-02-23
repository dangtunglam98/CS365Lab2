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

def heuristic(board,player):
	score = 0
	if player == "X":
		for row,col in board.blackPos:
			score += (row+1)*50
			if (row-1,col-1) in board.blackPos:
				score += 20
			if (row-1,col+1) in board.blackPos:
				score += 20
		for row,col in board.whitePos:
			score -= (board.rowsNum-row)*50
		if board.isPlayerWin(player):
			score += 9999

	else:
		for row,col in board.whitePos:
			score += (row+1)*50
			if (row-1,col-1) in board.whitePos:
				score += 20
			if (row-1,col+1) in board.whitePos:
				score += 20
		for row,col in board.blackPos:
			score -= (board.rowsNum-row)*50
		if board.isPlayerWin(player):
			score += 9999
	score += random()
	return score




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

	min_score = float('inf')
	best_score = -float('inf')
	best_move = None

	for m, b in board.move_states(player):
		val = min_value(creat_board(board.rowsNum,board.colsNum,b), player, best_score, min_score, 0, util)
		if val > best_score:
			best_move = m
			best_score = val
		min_score = min(min_score,val)

	# move, board = argmax(board.move_states(player), lambda ((m, b)): min_value(b, -float('inf'), float('inf'), 0))
	return best_move

def play_game(heuristic_white,heuristic_black,board):
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
				print(player + ": "+util.__name__ + " Win")
				print("The total time to play this game is "+ str(datetime.timedelta(seconds=time.time()-total_time))+ " (hour/minute/seconds)")
				print("The number of white pieces lost: " + str((board.piecesNum * board.colsNum) - board.whiteNum) )
				print("The number of black pieces lost: " + str((board.piecesNum * board.colsNum) -board.blackNum))
				print("----------------------------------------------------------")

				return turn


# a = Board(6,6,2)
# a.update_state(([(2,0),(3,0),(2,2),(3,2),(4,2),(3,4),(3,5)],[(0,2),(1,2)]))
# a.display_state()
# play_game(evasive,hidetowin,a)
