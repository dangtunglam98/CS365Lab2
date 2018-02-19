from random import *
from boardClass import Board
from copy import deepcopy

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

def switchPlayer(player):
	if player == "X":
		return "O"
	else:
		return "X"

def minimax(utilFunc,board,player):
	# if board.terminal_test():
	# 	return None
	moves = board.moveList(player)
	board2 = deepcopy(board)
	best_move = moves[0]
	best_score = utilFunc(board2.transition(moves[0]), player)
	for move in moves:
		clone = deepcopy(board).transition(move)
		score = minplay(utilFunc,clone,player,0)
		if score > best_score:
			best_move = move
			best_score = score
	return best_move

def minplay(utilFunc,board,player,depth):
	if board.terminal_test() or (depth > 2):
		return utilFunc(board, player)
	moves = board.moveList(switchPlayer(player))
	if moves == []:
		return utilFunc(board, player)
	board2 = deepcopy(board)
	best_score = utilFunc(board2.transition(moves[0]), player)
	for move in moves:
		clone = deepcopy(board).transition(move)
		score = maxplay(utilFunc,clone,player,depth+1)
		if score < best_score:
			best_move = move
			best_score = score
	return best_score

def maxplay(utilFunc,board,player,depth):
	if board.terminal_test() or (depth > 2):
		return utilFunc(board, player)
	moves = board.moveList(player)
	if moves == []:
		return utilFunc(board, player)
	board2 = deepcopy(board)
	best_score = utilFunc(board2.transition(moves[0]), player)
	for move in moves:
		clone = deepcopy(board).transition(move)
		score = minplay(utilFunc,clone,player,depth+1)
		if score > best_score:
			best_move = move
			best_score = score
	return best_score

def play_game(heuristic_white,heuristic_black,board_state,turn):
	if board_state.terminal_test():
		return board_state, turn
	board_state.display_state()
	return white_turn(heuristic_white,heuristic_black,board_state,turn+1)


def white_turn(heuristic_white,heuristic_black,board_state,turn):
	if board_state.terminal_test():
		return board_state, turn
	move = minimax(heuristic_white,board_state,"O")
	board_state.display_state()
	print("white turn")
	print(turn)
	return black_turn(heuristic_white,heuristic_black,board_state.transition(move),turn+1)

def black_turn(heuristic_white,heuristic_black,board_state,turn):
	if board_state.terminal_test():
		return board_state, turn
	move = minimax(heuristic_black,board_state,"X")
	board_state.display_state()
	print("black turn")
	print(turn)
	return white_turn(heuristic_white,heuristic_black,board_state.transition(move),turn+1)

# class Node(object):
# 	def __init__(self, parent = None, action, board, util, player, depth):
# 		self.parent = parent
# 		self.child = []
# 		self.action = action
# 		self.board = board
# 		self.utility = util(self.state, player)
# 		self.depth = depth
		
# 		for key,vals in board.move_generator(player).items():
# 			for end in vals:
# 				self.child.append(Node(self, (player,key,end), self.board.move(key,end), util, player, self.depth + 1)


a = Board(8,8,2)
# print(a.terminal_test())
# print("OK")
# #for i in range(5):
# a.transition(minimax(evasive,a,"X"))
# a.display_state()
# a.transition(minimax(evasive,a,"O"))
# a.display_state()
# print("end turn")
# print(minimax(evasive,a,"O"))
# a.transition(minimax(evasive,a,"O"))
# a.display_state()
play_game(evasive,evasive,a,0)[0].display_state()
print(play_game(evasive,evasive,a,0)[1])






	

