import random

global counter1,counter2
counter1 = 0
counter2 = 0
def pepe_dame():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win_combis = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


##    def chooseComputerMove():

##    #This just fills a list with all the empty boxes and chooses one at random
##       emptyBoxes = []
##       for i in range(0, 3):
##           for j in range(0, 3):
##               if emptyBoxes[i][j] == 0:
##                   emptyBoxes += [[i, j]]
##
##       return emptyBoxes[random.randint(1, len(emptyBoxes) - 1)]
##
 # Make the computer's move
##    computerMove = chooseComputerMove()
##    boxes[computerMove[0]][computerMove[1]] = 1
##    print('\n' 'Computer\'s turn:')
##    printGrid()

    # Check if the computer's move won the game
##    victoryResult = check_board()
##    if board[s[0]] == board[s[1]] == board[s[2]] == "O":
##                print("Hurraaayyy!!!! \n Computer Wins!\n")
##                return True
##    else:
##        check_board()
##    if (victoryResult == 'O'):
##        print ('Computer wins!')
##           break


   #To print the board 
    def draw():
        print("\n", board[0], "  ", board[1], "  ", board[2])
        print("\n", board[3], "  ", board[4], "  ", board[5])
        print("\n", board[6], "  ", board[7], "  ", board[8])
        print()

    #To reduce the choice made to correspond to the index
    def choice(message):
        while True:
            while True:
                s = input(message)
                try:
                    s = int(s)
                    s = s - 1
                    if s in range(0, 9):
                        return s
                    else:
                        print("Ad3n, w'ani afra? Choose from the board.")
                        continue
                except ValueError:
                    print("\nIdiot!!! Choose a number!")
                    continue

    #The possible board placement of Player 1
    def player1(n):
        print("Counter1 = " + str(counter1))
        end = check_board()
        
        if  board[n] == "@" or board[n] == "X" and counter1 < 3:
                print("\n Sorry, That position is unavailable.")
                new_choice = choice("Choose a different position with a number: ")
                player1(new_choice)

        #Movements
        elif counter1 >= 3:
            if board[n] == "X":

                #Checking if it is a legal move
                if  n == 0:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 1 or r == 3 or r == 4:
                        global counter1
                        counter1 = counter1 - 1
                        player1(r)
                        board[n] = n + 1
                                
                    else:
                        board[n] == "X"
                        print("Cheat! How can you move all the way there? Illegal move, nigga!!!")
                        t = choice("\nMake a legal choice: ")
                        global counter1
                        player1(t)
                        counter1 = counter1 - 1
                        board[n] = "X"


                elif n == 1:
                    r = choice("\nWhere do you want to move it to? ")  
                    if r == 0 or r == 2 or r == 4:
                        global counter1
                        counter1 = counter1 - 1
                        player1(r)
                        board[n] = n + 1
                                
                    else:
                        board[n] == "X"
                        print("Cheat! How can you move all the way there? Illegal move, nigga!!!")
                        t = choice("\nMake a legal choice: ")
                        global counter1
                        player1(t)
                        counter1 = counter1 - 1
                        board[n] = "X"


                elif n == 2:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 1 or r == 5 or r == 4:
                        global counter1
                        counter1 = counter1 - 1
                        player1(r)
                        board[n] = n + 1
                                
                    else:
                        board[n] == "X"
                        print("Cheat! How can you move all the way there? Illegal move, nigga!!!")
                        t = choice("\nMake a legal choice: ")
                        global counter1
                        player1(t)
                        counter1 = counter1 - 1
                        board[n] = "X"


                elif n == 3:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 0 or r == 6 or r == 4:
                        global counter1
                        counter1 = counter1 - 1
                        player1(r)
                        board[n] = n + 1
                                
                    else:
                        board[n] == "X"
                        print("Cheat! How can you move all the way there? Illegal move, nigga!!!")
                        t = choice("\nMake a legal choice: ")
                        global counter1
                        player1(t)
                        counter1 = counter1 - 1
                        board[n] = "X"

                elif n == 4:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 0 or r == 1 or r == 2 or r == 3 or r == 5 or r == 6 or r == 7 or r == 8:
                        global counter1
                        counter1 = counter1 - 1
                        player1(r)
                        board[n] = n + 1
                                
                    else:
                        board[n] == "X"
                        print("Cheat! How can you move all the way there? Illegal move, nigga!!!")
                        t = choice("\nMake a legal choice: ")
                        global counter1
                        player1(t)
                        counter1 = counter1 - 1
                        board[n] = "X"

                elif n == 5:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 2 or r == 4 or r == 8:
                        global counter1
                        counter1 = counter1 - 1
                        player1(r)
                        board[n] = n + 1
                                
                    else:
                        board[n] == "X"
                        print("Cheat! How can you move all the way there? Illegal move, nigga!!!")
                        t = choice("\nMake a legal choice: ")
                        global counter1
                        player1(t)
                        counter1 = counter1 - 1
                        board[n] = "X"

                elif n == 6:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 3 or r == 4 or r == 7:
                        global counter1
                        counter1 = counter1 - 1
                        player1(r)
                        board[n] = n + 1
                                
                    else:
                        board[n] == "X"
                        print("Cheat! How can you move all the way there? Illegal move, nigga!!!")
                        t = choice("\nMake a legal choice: ")
                        global counter1
                        player1(t)
                        counter1 = counter1 - 1
                        board[n] = "X"

                elif n == 7:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 6 or r == 4 or r == 8:
                        global counter1
                        counter1 = counter1 - 1
                        player1(r)
                        board[n] = n + 1
                                
                    else:
                        board[n] == "X"
                        print("Cheat! How can you move all the way there? Illegal move, nigga!!!")
                        t = choice("\nMake a legal choice: ")
                        global counter1
                        player1(t)
                        counter1 = counter1 - 1
                        board[n] = "X"

                elif n == 8:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 5 or r == 4 or r == 7:
                        global counter1
                        counter1 = counter1 - 1
                        player1(r)
                        board[n] = n + 1
                                
                    else:
                        board[n] == "X"
                        print("Cheat! How can you move all the way there? Illegal move, nigga!!!")
                        t = choice("\nMake a legal choice: ")
                        global counter1
                        player1(t)
                        counter1 = counter1 - 1
                        board[n] = "X"


            else:
                print("Are you stupid or something...? You can't add more than three pieces")
                new_choice = choice("Choose any of your old marbles to move it: ")
                player1(new_choice)
                

        else:
            board[n] = "X"
            global counter1
            counter1 = counter1 + 1
        
        if end: print(end)
            
    #The possible board placement of Player 2
    def player2(n):
        print("Counter2 = " + str(counter2))
        end = check_board()

        if  board[n] == "X" or board[n] == "@" and counter2 < 3:
                print("\n Sorry, That position is unavailable.")
                new_choice = choice("Choose a different position with a number: ")
                player2(new_choice)

        #Movements
        elif counter2 >= 3:
            if board[n] == "@":

                #Checking if it is a legal move
                if n == 0:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 1 or r == 3 or r == 4:
                        global counter2
                        counter2 = counter2 - 1
                        player2(r)
                        board[n] = n + 1
  
                    else:
                        board[n] == "@"
                        print("Cheat! How can you move all the way there? Illegal move, nigga!!!")
                        t = choice("\nMake a legal choice: ")
                        player2(t)
                        global counter2
                        counter2 = counter2 - 1
                        board[n] = "@"


                elif n == 1:
                    r = choice("\nWhere do you want to move it to? ")
                    
                    if r == 0 or r == 2 or r == 4:
                        global counter2
                        counter2 = counter2 - 1
                        player2(r)
                        board[n] = n + 1
  
                    else:
                        board[n] == "@"
                        print("Cheat! How can you move all the way there? Illegal move, nigga!!!")
                        t = choice("\nMake a legal choice: ")
                        player2(t)
                        global counter2
                        counter2 = counter2 - 1
                        board[n] = "@"


                elif n == 2:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 1 or r == 5 or r == 4:
                        global counter2
                        counter2 = counter2 - 1
                        player2(r)
                        board[n] = n + 1
  
                    else:
                        board[n] == "@"
                        print("Cheat! How can you move all the way there? Illegal move, nigga!!!")
                        t = choice("\nMake a legal choice: ")
                        player2(t)
                        global counter2
                        counter2 = counter2 - 1
                        board[n] = "@"

                elif n == 3:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 0 or r == 6 or r == 4:
                        global counter2
                        counter2 = counter2 - 1
                        player2(r)
                        board[n] = n + 1
  
                    else:
                        board[n] == "@"
                        print("Cheat! How can you move all the way there? Illegal move, nigga!!!")
                        t = choice("\nMake a legal choice: ")
                        player2(t)
                        global counter2
                        counter2 = counter2 - 1
                        board[n] = "@"


                elif n == 4:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 0 or r == 1 or r == 2 or r == 3 or r == 5 or r == 6 or r == 7 or r == 8:
                        global counter2
                        counter2 = counter2 - 1
                        player2(r)
                        board[n] = n + 1
  
                    else:
                        board[n] == "@"
                        print("Cheat! How can you move all the way there? Illegal move, nigga!!!")
                        t = choice("\nMake a legal choice: ")
                        player2(t)
                        global counter2
                        counter2 = counter2 - 1
                        board[n] = "@"


                elif n == 5:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 2 or r == 4 or r == 8:
                        global counter2
                        counter2 = counter2 - 1
                        player2(r)
                        board[n] = n + 1
  
                    else:
                        board[n] == "@"
                        print("Cheat! How can you move all the way there? Illegal move, nigga!!!")
                        t = choice("\nMake a legal choice: ")
                        player2(t)
                        global counter2
                        counter2 = counter2 - 1
                        board[n] = "@"


                elif n == 6:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 3 or r == 4 or r == 7:
                        global counter2
                        counter2 = counter2 - 1
                        player2(r)
                        board[n] = n + 1
  
                    else:
                        board[n] == "@"
                        print("Cheat! How can you move all the way there? Illegal move, nigga!!!")
                        t = choice("\nMake a legal choice: ")
                        player2(t)
                        global counter2
                        counter2 = counter2 - 1
                        board[n] = "@"


                elif n == 7:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 6 or r == 4 or r == 8:
                        global counter2
                        counter2 = counter2 - 1
                        player2(r)
                        board[n] = n + 1
  
                    else:
                        board[n] == "@"
                        print("Cheat! How can you move all the way there? Illegal move, nigga!!!")
                        t = choice("\nMake a legal choice: ")
                        player2(t)
                        global counter2
                        counter2 = counter2 - 1
                        board[n] = "@"

                        
                elif n == 8:
                    r = choice("\nWhere do you want to move it to? ")
                    if r == 7 or r == 5 or r == 4:
                        global counter2
                        counter2 = counter2 - 1
                        player2(r)
                        board[n] = n + 1
  
                    else:
                        board[n] == "@"
                        print("Cheat! How can you move all the way there? Illegal move, nigga!!!")
                        t = choice("\nMake a legal choice: ")
                        player2(t)
                        global counter2
                        counter2 = counter2 - 1
                        board[n] = "@"


            else:
                print("You are an idiot... You can't add more than three pieces")
                new_choice = choice("Choose any of your old marbles to move it: ")
                player2(new_choice)
                

        else:
            board[n] = "@"
            global counter2
            counter2 = counter2 + 1
            
        if end: print(end)

    #Check if the board has any win combinations already
    def check_board():
        count = 0
        for s in win_combis:
            if board[s[0]] == board[s[1]] == board[s[2]] == "X":
                print("Hurraaayyy!!!! \n Player 1 Wins!\n")
                return True

            if board[s[0]] == board[s[1]] == board[s[2]] == "@":
                print("Hurraaayyy!!!! \n Player 2 Wins!\n")
                return True

        return False

    #Run the program
    while not end:
        u = input("Press 'p' to play against another player and 'c' to play against the computer: ")
        if u == 'p':

            draw()
            end = check_board()

            while not end:

                if end == True:
                    break
                n = choice("Player 1 make a choice: ")
                player1(n)
                draw()
                end = check_board()
                
                if end == True:
                    break
                n = choice("Player 2 make a choice: ")
                player2(n)
                draw()
                end = check_board()

                
            if input("Play again (y/n)\n") == "y":
                print()
                global counter1, counter2
                counter1 = 0
                counter2 = 0
                pepe_dame()

        elif u == 'c':
            while not end:
                draw()
                end = check_board()
                if end == True:
                    break
                n = choice("Player 1 make a choice: ")

                player1(n)
                print()
                draw()
                end = check_board()

                if end == True:
                    break
                n = choice("Computer's turn: ")
                chooseComputerMove()
                print()
                end = check_board()

            if input("Play again (y/n)\n") == "y":
                print()
                global counter1, counter2
                counter1 = 0
                counter2 = 0
                pepe_dame()



pepe_dame()
            
                    
            
            
            
        
