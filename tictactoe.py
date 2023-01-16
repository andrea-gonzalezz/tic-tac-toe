
def main():
    presentation()
    board = create_grid()
    printPretty(board)
    symbol1, symbol2 = sym()
    plateau_plein(board, symbol1, symbol2)


def presentation():
    print("Bienvenu au jeu du morpion!")
    print("\n")
    print ("Deux joueurs, représentés par les symboles O et X joueront chacun leur tour."
           "Ils devront placer leur sybole correspondant dans une grille de 3*3 cases afin de faire un ligne de 3."
           "Celui qui réussi à placer trois symboles en ligne, colonne ou vertical gagne la partie!")
    print("\n")
    print("Entrez pour continuer!")
presentation()



def create_grid():
    # Cette fonction créé le plateau de jeu
    print("Voici le plateau de jeu: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board

def sym():
    # Fonction pour choisir son symbole
    symbol1 = input("Joueur numéro 1, vous voulez prendre le X ou le O ")
    if symbol1 == "X":
        symbol2 = "O"
        print("Joueur numéro 2, vous prenez le O ")
    else:
        symbol2 = "X"
        print("Joueur numéro 2 vous prenez le X ")
    input("Entrez pour continuer")
    print("\n")
    return (symbol1, symbol2)


def regles(board, symbol1, symbol2, count):
    # Choisir son tour
    if count % 2 == 0:
        joueur = symbol1
    elif count % 2 == 1:
        joueur = symbol2
    print("Joueur " + joueur + ", c'est ton tour!. ")
    ligne = int(input("Choisi un ligne:"
                    "Ligne du haut : 0 , milieu : 1 , ligne du bas : 2"))
    colonne = int(input("Choisi une colonne:"
                        "Colonne de gauche: 0, du milieu : 1, colonne de droit : 2"))

    # Check if players' selection is out of range
    while (ligne > 2 or ligne < 0) or (colonne > 2 or colonne < 0):
        Dehors(ligne, colonne)
        ligne = int(input("Choisi un ligne:"
                          "Ligne du haut : 0 , milieu : 1 , ligne du bas : 2"))
        colonne = int(input("Choisi une colonne:"
                            "Colonne de gauche: 0, du milieu : 1, colonne de droit : 2"))


        # Check if the square is already filled
    while (board[ligne][colonne] == symbol1) or (board[ligne][colonne] == symbol2):

        filled = illegal(board, symbol1, symbol2, ligne, colonne)
        ligne = int(input("Choisi un ligne:"
                          "Ligne du haut : 0 , milieu : 1 , ligne du bas : 2"))
        colonne = int(input("Choisi une colonne:"
                            "Colonne de gauche: 0, du milieu : 1, colonne de droit : 2"))
        # Locates player's symbol on the board
    if joueur == symbol1:
        board[ligne][colonne] = symbol1

    else:
        board[ligne][colonne] = symbol2

    return (board)

def dehors(ligne, colonne):
    print("Vous avez choisi une case en dehors du tableau")

def illegal(board, symbol1, symbol2, ligne, colonne):
    print("La case choisie est déjà prise, choisi une autre case")

def printPretty(board):
    lignes = len(board)
    colonne = len(board)
    print("*---*---*---*")
    for r in range(lignes):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("*---*---*---*")
    return board

def plateau_plein(board, symbol1, symbol2):
    count = 1
    winner = True
    # This function check if the board is full
    while count < 10 and winner == True:
        gaming = regles(board, symbol1, symbol2, count)
        pretty = printPretty(board)

        if count == 9:
            print("Le plateau est plein, fin de la partie")
            if winner == True:
                print("Match nul! ")

        # Check if here is a winner
        winner = gagnant(board, symbol1, symbol2, count)
        count += 1
    if winner == False:
        print("Game over.")

    # This is function gives a report
    report(count, winner, symbol1, symbol2)


def gagnant(board, symbol1, symbol2, count):
    # This function checks if any winner is winning
    winner = True
    # Check the rows
    for ligne in range(0, 3):
        if (board[ligne][0] == board[ligne][1] == board[ligne][2] == symbol1):
            winner = False
            print("Joueur " + symbol1 + ", tu as gagné!")

        elif (board[ligne][0] == board[ligne][1] == board[ligne][2] == symbol2):
            winner = False
            print("Joueur " + symbol2 + ", tu as gagné!")

    # Check the columns
    for colonne in range(0, 3):
        if (board[0][colonne] == board[1][colonne] == board[2][colonne] == symbol1):
            winner = False
            print("Joueur " + symbol1 + ", tu as gagné!")
        elif (board[0][colonne] == board[1][colonne] == board[2][colonne] == symbol2):
            winner = False
            print("Joueur " + symbol2 + ", tu as gagné!")

    # Check the diagnoals
    if board[0][0] == board[1][1] == board[2][2] == symbol1:
        winner = False
        print("Joueur " + symbol1 + ", tu as gagné!")

    elif board[0][0] == board[1][1] == board[2][2] == symbol2:
        winner = False
        print("Joueur " + symbol2 + ", tu as gagné!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol1:
        winner = False
        print("Joueur " + symbol1 + ", tu as gagné!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = False
        print("Joueur " + symbol2 + ", tu as gagné!")

    return winner





def report(count, winner, symbol1, symbol2):
    print("\n")
    input("Press enter to see the game summary. ")
    if (winner == False) and (count % 2 == 1):
        print("Winner : Player " + symbol1 + ".")
    elif (winner == False) and (count % 2 == 0):
        print("Winner : Player " + symbol2 + ".")
    else:
        print("There is a tie. ")



main()

