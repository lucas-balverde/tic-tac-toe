# Pour l'ia je voullais l'importer dans mon code principal avec la commande "from ia_random import ia" mais... ça marchait pas j'ai du faire qqch de mal 
# ImportError: cannot import name '...' from partially initialized module '...' (most likely due to a circular import) :,(
import random

print("-----------------------------------------")
print("              Bienvenue !")
print("-----------------------------------------")

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

#faire le quadrillage
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2] + "                 1 | 2 | 3")
    print("----------" + "               -----------")
    print(board[3] + " | " + board[4] + " | " + board[5] + "                 4 | 5 | 6")
    print("----------" + "               -----------")
    print(board[6] + " | " + board[7] + " | " + board[8] + "                 7 | 8 | 9")

#prendre les inputs des joueurs
def playerInput(board):
    inp = int(input("Entrez un nombre entre 1 et 9 : "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Emplacement invalide, réessayez")
        switchPlayer() == False

#verifier si la partie est gagnée via un alignement vertical, horizontal ou diagonal et si il y a victoire, la partie se termine.
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]    #le 0 peut être remplacé par un 1 ou 2 ce n'est pas important
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

#Vérifie chaques conditions de victoire et si une de ces condition est remplie, alors on déclare la victoire et la partie se finit. 
def checkIfWin(board):
    global gameRunning
    if checkHorizontal(board):
        printBoard(board)
        print(f"{winner} est le vainqueur !")
        gameRunning = False

    elif checkVertical(board):
        printBoard(board)
        print(f"{winner} est le vainqueur !")
        gameRunning = False

    elif checkDiagonal(board):
        printBoard(board)
        print(f"{winner} à gagné !")
        gameRunning = False

#Vérifie si il y a une égalité et si c'est le cas la partie se termine 
def checkIfTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("C'est une égalité!")
        gameRunning = False

#changer de joueur a chaque tour
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#ia 
def ia(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


#verifier encore si la partie est gagnée ou si il y a égalité
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkIfWin(board)
    checkIfTie(board)
    switchPlayer()    
    ia(board)
    checkIfWin(board)
    checkIfTie(board)