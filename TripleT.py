#Triple T
board = [0,0,0,0,0,0,0,0,0] # the board is a 1 dimensional array that is 9 long, one for each cell. 
							# we could do a 3 X 3 two dimensional array, but we don't really need to, 3 x 3 is so small.

counter = 1 # who's turn? 1 = X, 2 = O

def validate(cmd):
	try:
		row = int(cmd[1]) #what row, assume it's an int form
	except ValueError: #raise an error if that fails
		return -1
	if row < 1 or row > 3:
		return -1



	col = cmd[0] #what column, its in char form, convert
	# using a dictionary, we mapp "values" we want to to "keys" we're looking with. 
	# using the get method, search through it using char and get a num in response, -1 is default if x not found
	# this is the python equivalent of a switch-case, which is prevalent in many other languages
	convert_col = { 'a': 0, 'A': 0, 'b': 1, 'B': 1,'c': 2,  'C': 2, }.get(col, -1) 
	return convert_col + (row - 1) * 3 # yields a number 0 - 8, each relating to a specific index in the 1 dimensional board. 

def getInput():
	command = raw_input(intToSymbol(counter) +"'s turn. Please enter coords':")
	if (command == "quit"):
		print "Goodbye"
		print "================================="
		quit() # exit the script
	if len(command) != 2:
		print "Invalid command syntax."
		return -1
	else:
		response = validate(command)
		if (response < 0 or response > 8 ):
			print "That isn't a valid cell."
			return -1
		elif board[response] != 0:
			print "That spot is already taken."
			return -1
		else:
			board[response] = counter
			return True


# handy little convenience method to turn the "turn" indicator into an X or O
def intToSymbol(num): 
	if num == 1:
		return 'X'
	elif num == 2:
		return 'O'
	else:
		return ' '

def checkForWin(): # this seems like a dumb brute force way to solve this...
	if board[0] == board[1] == board[2] != 0:
		return True
	elif board[3] == board[4] == board[5] != 0:
		return True
	elif board[6] == board[7] == board[8] != 0:
		return True
	elif board[0] == board[3] == board[6] != 0:
		return True
	elif board[1] == board[4] == board[7] != 0:
		return True
	elif board[2] == board[5] == board[8] != 0:
		return True
	elif board[0] == board[4] == board[8] != 0:
		return True
	elif board[2] == board[4] == board[6] != 0:
		return True
	else:
		return False


def printBoard():
	print
	print"  A B C"
	print "1 "+'\033[4m'+intToSymbol(board[0])+"|"+intToSymbol(board[1])+"|"+intToSymbol(board[2]) + '\033[0m'
	print "2 "+'\033[4m'+intToSymbol(board[3])+"|"+intToSymbol(board[4])+"|"+intToSymbol(board[5]) + '\033[0m'
	print "3 "+intToSymbol(board[6])+"|"+intToSymbol(board[7])+"|"+intToSymbol(board[8])

def again():
	yn = raw_input("Play again? y/n")
	if yn == 'y' or yn == 'Y':
		board = [0,0,0,0,0,0,0,0,0]
		counter = 0
	elif yn == 'n' or yn == 'N':
		quit()
	else:
		print "I didn't understand that."
		again()




def banner():
	print "================================="
	print "TIC TAC TOE"
	print "m.cornell 2013"
	print ''
	print "X goes first. Enter \"quit\" to resign."

# this is the main game loop
banner()
while (True):
	printBoard()
	while (getInput() != True):
		print "Please try again"
		print ''
	if checkForWin():
		print intToSymbol+" wins!"
		again()
	counter+=1
	if (counter > 2):
		counter = 1
