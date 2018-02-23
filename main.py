from gamePlay import *

def main():
	print("\n")
	row = int(input("How many row will the board have? "))
	col = int(input("How many col will the board have? "))
	piece = int(input("How many piece rows? "))
	board = Board(row,col,piece)
	print("\n1. Evasive")
	print("2. Conqueror")
	print("3. Hidetowin")
	print("4. Defend")
	print("5. Heuristic\n")
	white = int(input("Choose heuristic for white "))
	if white == 1:
		whiteheu = evasive 
	elif white == 2:
		whiteheu = conqueror 
	elif white == 3:
		whiteheu = hidetowin 
	elif white == 4:
		whiteheu = defend 
	elif white == 5:
		whiteheu = heuristic 
	else:
		print("Invalid input")
	black = int(input("Choose heuristic for black "))
	if black == 1:
		blackheu = evasive 
	elif black == 2:
		blackheu = conqueror 
	elif black == 3:
		blackheu = hidetowin 
	elif black == 4:
		blackheu = defend 
	elif black == 5:
		blackheu = heuristic 
	else:
		print("Invalid input")
	play_game(whiteheu,blackheu,board)

if __name__ == '__main__':
	main()
