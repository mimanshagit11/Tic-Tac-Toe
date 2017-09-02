# tictactoe game for 2 players

# from __future__ import print_function

place = []

for x in range (0, 9) :
    place.append(str(x + 1))

playerOneTurn = True
winner = False

def printBoard() :
    print( '\n -----')
    print( '|' + place[0] + '|' + place[1] + '|' + place[2] + '|')
    print( ' -----')
    print( '|' + place[3] + '|' + place[4] + '|' + place[5] + '|')
    print( ' -----')
    print( '|' + place[6] + '|' + place[7] + '|' + place[8] + '|')
    print( ' -----\n')

while not winner :
    printBoard()

    if playerOneTurn :
        print( "Player 1:")
    else :
        print( "Player 2:")

    try:
        choice = int(input("..."))
    except:
        print("please enter a valid field")
        continue
    if place[choice - 1] == 'X' or place [choice-1] == 'O':
        print("Can't play this move, please try again")
        continue

    if playerOneTurn :
        place[choice - 1] = 'X'
    else :
        place[choice - 1] = 'O'

    playerOneTurn = not playerOneTurn

    for x in range (0, 3) :
        y = x * 3
        if (place[y] == place[(y + 1)] and place[y] == place[(y + 2)]) :
            winner = True
            printBoard()
        if (place[x] == place[(x + 3)] and place[x] == place[(x + 6)]) :
            winner = True
            printBoard()

    if((place[0] == place[4] and place[0] == place[8]) or 
       (place[2] == place[4] and place[4] == place[6])) :
        winner = True
        printBoard()

print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")