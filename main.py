import turtle
import random

pen = turtle.Turtle()
screen = turtle.Screen()

pen.speed(100)
pen.pensize(5)

players = ("Player 1", "Player 2")
playerTokens = ("X", "O")
first = ""

xPlaces = []
oPlaces = []

xCords = {
          1: (-300, 300), 2: (-100, 300),
          3: (100, 300), 4: (-300, 100),
          5: (-100, 100), 6: (100, 100),
          7: (-300, -100), 8: (-100, -100),
          9: (100, -100)
         }

oCords = {
           1: (-200, 100), 2: (0, 100),
           3: (200, 100), 4: (-200, -100),
           5: (0, -100), 6: (200, -100),
           7: (-200, -300), 8: (0, -300),
           9: (200, -300)
         }



possibleWins = [ [1, 2, 3], [4, 5, 6], [7, 8, 9],
                 [1, 4, 7], [2, 5, 8], [3, 6, 9],
                 [1, 5, 9], [3, 5, 7]
               ]

def drawGrid():
    pen.color("black")

    #verticle lines
    pen.penup()
    pen.setpos(-100, 300)
    pen.pendown()
    pen.setpos(-100, -300)

    pen.penup()
    pen.setpos(100, 300)
    pen.pendown()
    pen.setpos(100, -300)

    #horizontal lines
    pen.penup()
    pen.setpos(-300, 100)
    pen.pendown()
    pen.setpos(300, 100)

    pen.penup()
    pen.setpos(-300, -100)
    pen.pendown()
    pen.setpos(300, -100)

def start():
    drawGrid()

    print("Let's Play Tic Tac Toe!")
    print("The boad is numbered like this: \n\n\t1\t2\t3\n\t4\t5\t6\n\t7\t8\t9\n")
    print("Player 1 is X, and Player 2 is O")

    starter = random.choice(players)

    print(starter + " goes first!")
    first = starter
       

def playGame():
    currentPlayer = first
    gameOver = False
   
    while gameOver == False:
       
        if currentPlayer == players[0]:
            move(playerTokens[0])
            gameOver = checkForWinX()
        else:
            move(playerTokens[1])
            gameOver = checkForWinO()

        if gameOver == False:
            gameOver = checkForDraw()

        if gameOver == False:
            if currentPlayer == players[0]:
                currentPlayer = players[1]
            else:
                currentPlayer = players[0]
               

def move(token):
    print("Where would you like to place your token?")    
    rawUserInput = input("Enter place 1 - 9")
    userInput = int(rawUserInput)
   
    if userInput > 9 or userInput < 1:
        print("Invalid Space! Try Again")
        move(token)

    if userInput in xPlaces or userInput in oPlaces:
        print("That Space is Taken! Try Again!")
        move(token)

    else:
        if token == playerTokens[0]:
            drawX(userInput)
            xPlaces.append(userInput)
        else:
            drawO(userInput)
            oPlaces.append(userInput)
           

def drawX(location):
    pen.color("red")
   
    pen.penup()
    pen.setpos(xCords.get(location))
    pen.pendown()
    pen.setpos(pen.xcor() + 200, pen.ycor() - 200)

    pen.penup()
    pen.setpos(pen.xcor() - 200, pen.ycor())
    pen.pendown()
    pen.setpos(pen.xcor() + 200, pen.ycor() + 200)




def drawO(location):
    pen.color("blue")

    pen.penup()
    pen.setpos(oCords.get(location))
    pen.pendown()
    pen.circle(100)

def checkForWinX():

    xPlaces.sort()
    counter = 0

    if len(xPlaces) < 3:
        return False


    for win in possibleWins:
        for location in win:
            if location in xPlaces:
                counter += 1

                if counter == 3:
                    return True

            else:
                counter = 0

        counter = 0

    if counter < 3:
        return False

def checkForWinO():

    oPlaces.sort()
    counter = 0

    #less than 3 moves made, cant possibly win
    if len(oPlaces) < 3:
        return False

    for win in possibleWins:
        for location in win:
            if location in oPlaces:
                counter += 1
                if counter == 3:
                    return True

            else:
                counter = 0

        counter = 0
    if counter < 3:
        return False

def checkForDraw():
    if (len(xPlaces) + len(oPlaces)) == 9:
        return True

    return False


def declareWinner():
    if checkForWinX():
        print("X Has Won!")

    elif checkForWinO():
        print("O Has Won!")

    elif checkForDraw():
        print("Cats Game!")

    else:
        print("Somethings wrong, no one has won, and there was no draw")
       


def resetGame():
    pen.clear()
    xPlaces.clear()
    oPlaces.clear()



exitGame = False

while exitGame != True:
    start()
    playGame()
    declareWinner()

    userInput = input("Play Again? y/n")

    if userInput == "y":
        resetGame()
       
    else:
        exitGame = True
        print("See you next time!")
