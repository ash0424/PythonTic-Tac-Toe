#introductory message
print("")
print("")
print("|$$\    _ $$\ |$$$$$$$$|  |$$\      /$$$$$\   /$$$$$$\  /$$\      /$$\ |$$$$$$$$|       /$$$$$$$\  /$$$$$$\ ")    
print("|$$ | $\  $$| |$$  ____|  |$$| _   /$$  _$$\ |$$$__$$$| |$$$\  _ /$$$| |$$  ____|   _   \__$$___/ |$$$__$$$|")   
print("|$$ |$$$\ $$| |$$ |  _    |$$|     $$ /  \_| |$$/  |$$| |$$$$\  /$$$$| |$$ |   _           $$|    |$$/  |$$|") 
print("|$$ $$ $$\$$| |$$$$$|  _  |$$|   _ $$ |      |$$|  |$$| |$$$$$\/$$$$$| |$$$$$|        _    $$|    |$$|  |$$|")
print("|$$$$  $$$$ | |$$  _|     |$$|     $$ |      |$$|  |$$| |$$|\ $$$ /$$| |$$  _|             $$|    |$$|  |$$|")
print("|$$$ / \$$$ | |$$ | __  _ |$$|     $$ |  $$\ |$$$  $$$| |$$| \ $ /|$$| |$$ | __    _       $$|    |$$$  $$$|")
print("|$$ / _ \$$ | |$$$$$$$$\  $$$$$$$$ \$$$$$$ | | $$$$$$ | |$$|  \_/ |$$| |$$$$$$$$\          $$|    | $$$$$$ |") 
print(" \_/     \__| \________/  \______/  \_____/   \______/  \__/      \__/ \________/      _  \__/     \______/ ")
print("")
print("")
print(" /$$$$$$$\ /$$$$$\  /$$$$$\        /$$$$$$$\ /$$$$$\   /$$$$$\  _    /$$$$$$$\  /$$$$$$\  |$$$$$$$$| ") 
print(" \__$$___/ \-$$|-/ /$$  _$$\  _    \__$$___/ $$$_$$$\ /$$  _$$\      \__$$___/ |$$$__$$$| |$$  ____| ")
print("    $$|      $$| _ $$ /  \_|         _$$|    $$/ \$$| $$ /  \_|     _   $$|    |$$/  |$$| |$$ |   _  ")
print("  _ $$|    _ $$|   $$ | _             $$|   _$$$$$$$| $$ |      _       $$|_   |$$|  |$$| |$$$$$|    ")
print("    $$|_     $$|  _$$ |      _        $$|    $$ _ $$| $$ |              $$|  _ |$$|  |$$| |$$  _|    ")
print("    $$|      $$|   $$ |  $$\       _  $$|_   $$|  $$| $$ |  $$\    _    $$|    |$$$  $$$| |$$ | __   ")
print("    $$|  _ $$$$$$\ \$$$$$$ |    _     $$|    $$|  $$| \$$$$$$ |         $$|    | $$$$$$ | |$$$$$$$$\ ")
print("   \__/    \_____/  \_____/          \__/    \_/  \_/  \_____/  _    _ \__/     \______/  \________/ ")
print("")
print("")


#input players names
#create a list for players
player = []

#define a function to make sure the players names already in the database
def add_player():
    global player

    
    def player_names():
        #let players enter their names
        global player1
        global player2
        
        player1 = str(input("**PLAYER 1'S NAME?** ==> "))

        while True:
            while not player1:
                print("\nPLAYER 1 will not be added successfully\nPlease enter again.")
                player1 = str(input("**PLAYER 1'S NAME?** ==> "))
            while player1 == " ":
                print("\nPLAYER 1 will not be added successfully\nPlease enter again.")
                player1 = str(input("**PLAYER 1'S NAME?** ==> "))
            break

        
        player2 = str(input("**PLAYER 2'S NAME?** ==> "))

        while True:
            while player2 == player1:
                print("Cannot put the same name" + "\nPlease enter again")
                player2 = str(input("**PLAYER 2'S NAME?** ==> "))
            while not player2:
                print("\nPLAYER 2 will not be added successfully\nPlease enter again.")
                player2 = str(input("**PLAYER 2'S NAME?** ==> "))
            while player2 == " ":
                print("\nPLAYER 2 will not be added successfully\nPlease enter again.")
                player2 = str(input("**PLAYER 2'S NAME?** ==> "))
            break


    player_names()

    player.append(player1)
    player.append(player2)
        
    if player[0] == player1 and player[1] == player2:
        print()
        print(player)
        print("Players are added successfully")
        

#design a game board to display
def game_board_display(board):
    print(board[0] + "  | " + board[1] + "  | " + board[2])
    print("__" + "_|_" + "__" + "_|_" + "__")
    print(board[3] + "  | " + board[4] + "  | " + board[5])
    print("__" + "_|_" + "__" + "_|_" + "__")
    print(board[6] + "  | " + board[7] + "  | " + board[8])


#to define which one goes first
def the_first(first_letter):
    global player1, player2
    #player who choose X will go first
    if first_letter == "X":
        return player1
    elif first_letter == "O":
        return player2


#the inputs from players
def letter_input():
    letter = ""
    print(player1,"do you wanna be 'X' or 'O'?: ")
    letter = input().upper()

    while not(letter == "X" or letter == "O"):
        print(player1,"do you wanna be 'X' or 'O'?: ")
        letter = input().upper()
        
    #first element for player 1, second element for player 2
    if letter == "X":
        return["X", "O"]
    else:
        return["O", "X"]    


def plyr_move(plyr, board):
    valid = False

    while not valid:
        global move
        while True:
            try:
                move = int(input("Insert the position (1-9):")) - 1
                while (move <0 or move >8):
                    print("Invalid input.")
                    move = int(input("Try again. Insert the position (1-9):")) - 1
            except:
                print("String cannot be integer")

            else:
                break

        if board[move] == " ":
            valid = True
        else:
            print("This space is already filled." + "\nTry again.")


    board[move] = plyr


def win_situation(board, letter):
    
    #row checking
    return((board[0]==letter and board[1]==letter and board[2]==letter)or
           (board[3]==letter and board[4]==letter and board[5]==letter)or
           (board[6]==letter and board[7]==letter and board[8]==letter)or
    #column checking
           (board[0]==letter and board[3]==letter and board[6]==letter)or
           (board[1]==letter and board[4]==letter and board[7]==letter)or
           (board[2]==letter and board[5]==letter and board[8]==letter)or
    #diagonal checking
           (board[0]==letter and board[4]==letter and board[8]==letter)or
           (board[2]==letter and board[4]==letter and board[6]==letter))


def tie_situation(board):
    if " " not in board:
        return("there is a tie.")

    
def play_again():
    run = input("Do you wanna play again? Yes/No")
    if(run == "Yes") or (run == "yes") or (run == "YES") or (run == "y") or (run == "Y"):
        return run 


def demonstration_board():
    print("1" + "  | " + "2" + "  | " + "3")
    print("__" + "_|_" + "__" + "_|_" + "__")
    print("4" + "  | " + "5" + "  | " + "6")
    print("__" + "_|_" + "__" + "_|_" + "__")
    print("7" + "  | " + "8" + "  | " + "9")

    print("---------------------------------")

 
while True:
        
    try:
        print("")
        print("1. Play\n2. How to Play\n3. Quit")
        num = int(input())
        while (num <1 or num >3):
            print("Invalid\n1. Play\n2. How to Play\n3. Quit")
            num = int(input())
    
    except:
        print("String cannot be integer")

    else:
        pass

    while num == 1:
        add_player()
        the_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        p1_input, p2_input = letter_input()
        turn = the_first(p1_input)
        print(turn + " starts first.")

        #game is still playing
        game_continues = True

        while game_continues:
            if turn == player1:
                print("\n" + turn + " turns.")
                demonstration_board()
                game_board_display(the_board)
                plyr_move(p1_input, the_board)

                if win_situation(the_board, p1_input):
                    game_board_display(the_board)
                    print(player1 + " is the winner.\n")
                    game_continues = False

                elif tie_situation(the_board):
                    print(tie_situation(the_board))
                    break
                    
                else:
                    turn = player2

            elif turn == player2:
                print("\n" + turn + " turns.")
                demonstration_board()
                game_board_display(the_board)
                plyr_move(p2_input, the_board)

                if win_situation(the_board, p2_input):
                    game_board_display(the_board)
                    print(player2 + " is the winner.")
                    game_continues = False

                elif tie_situation(the_board):
                    print(tie_situation(the_board))
                    break
                    
                else:
                    turn = player1
                    
        player.clear()

        if not play_again():
            break

    while num == 2:
        print("""\n"HOW TO PLAY"\n
        1. Thus game consists of two players.\n
        2. “X” will always be the player who start first.\n
        3. Players take turn to place the Xs and Os on the board, game will end when either one of the player
        filled the line with their symbols horizontally, vertically, diagonally or the square on the grid are full filled.\n
        4. When a player achieved the goal, then the player will be the winner.\n
        5. If all the square on the grid are filled and players has not made a complete row of the symbols,
        then the game is a tie.\n
        """)

        back = input("Press 'B' to back to main menu: ")

        if back == "B" or back == "b":
            break
    
    if num == 3:
        print("Thanks for playing!!!")
        break
                    

