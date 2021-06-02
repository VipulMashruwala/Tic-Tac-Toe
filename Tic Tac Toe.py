import os
import time
import random

board=[" "," "," "," "," "," "," "," "," "," "]

def print_header():
    print("LET's PLAY TIC TAC TOE")
    print("1|2|3")
    print("4|5|6")
    print("7|8|9")
    print("\n")
    print("To Play Tic Tac Toe , you need to get three in a row...")
    print("Your Choice are defined, they must be from 1 to 9...")

def print_board():
    print("   |   |   ")
    print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")
    print("   |   |   ")

def is_winner(board,player):
    if (board[1] == player and board[2] == player and board[3] == player) or \
            (board[4] == player and board[5] == player and board[6] == player) or \
            (board[7] == player and board[8] == player and board[9] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[3] == player and board[6] == player and board[9] == player) or \
            (board[1] == player and board[5] == player and board[9] == player) or \
            (board[3] == player and board[5] == player and board[7] == player):
        return True
    else:
        return False

def get_computer_move(board):
    if (board[3] == "X" and board[2] == "X" and board[1] == " "):
        return 1
    elif (board[1] == "X" and board[3] == "X" and board[2] == " "):
        return 2
    elif(board[1] == "X" and board[2] ==  "X"and board[3] == " "):
        return 3
    elif (board[5] == "X" and board[6] == "X" and board[4] == " "):
        return 4
    elif(board[4] == "X" and board[6] == "X" and board[5] == " "):
        return 5
    elif (board[4] == "X" and board[5] == "X" and board[6] == " "):
        return 6
    elif(board[8] == "X" and board[9] == "X" and board[7] == " "):
        return 7
    elif (board[7] == "X" and board[9] == "X" and board[8] == " "):
        return 8
    elif(board[7] == "X" and board[8] == "X" and board[9] == " "):
        return 9
    elif (board[4] == "X" and board[7] == "X" and board[1] == " "):
        return 1
    elif(board[1] == "X" and board[7] == "X" and board[4] == " "):
        return 4
    elif (board[1] == "X" and board[4] == "X" and board[7] == " "):
        return 7
    elif(board[5] == "X" and board[6] == "X" and board[2] == " "):
        return 2
    elif (board[2] == "X" and board[6] == "X" and board[5] == " "):
        return 5
    elif(board[5] == "X" and board[2] == "X" and board[6] == " "):
        return 6
    elif (board[9] == "X" and board[6] == "X" and board[3] == " "):
        return 3
    elif(board[3] == "X" and board[9] == "X" and board[6] == " "):
        return 6
    elif (board[3] == "X" and board[6] == "X" and board[9] == " "):
        return 9
    elif(board[5] == "X" and board[9] == "X" and board[1] == " "):
        return 1
    elif (board[1] == "X" and board[9] == "X" and board[5] == " "):
        return 5
    elif(board[5] == "X" and board[1] == "X" and board[9] == " "):
        return 9
    elif (board[5] == "X" and board[7] == "X" and board[3] == " "):
        return 3
    elif(board[7] == "X" and board[3] == "X" and board[5] == " "):
        return 5
    elif (board[5] == "X" and board[3] == "X" and board[7] == " "):
        return 7

    ####Computer Win

    if (board[3] == "0" and board[2] == "0" and board[1] == " "):
        return 1
    elif (board[1] == "0" and board[3] == "0" and board[2] == " "):
        return 2
    elif(board[1] == "0" and board[2] ==  "0"and board[3] == " "):
        return 3
    elif (board[5] == "0" and board[6] == "0" and board[4] == " "):
        return 4
    elif(board[4] == "0" and board[6] == "0" and board[5] == " "):
        return 5
    elif (board[4] == "0" and board[5] == "0" and board[6] == " "):
        return 6
    elif(board[8] == "0" and board[9] == "0" and board[7] == " "):
        return 7
    elif (board[7] == "0" and board[9] == "0" and board[8] == " "):
        return 8
    elif(board[7] == "0" and board[8] == "0" and board[9] == " "):
        return 9
    elif (board[4] == "0" and board[7] == "0" and board[1] == " "):
        return 1
    elif(board[1] == "0" and board[7] == "0" and board[4] == " "):
        return 4
    elif (board[1] == "0" and board[4] == "0" and board[7] == " "):
        return 7
    elif(board[5] == "0" and board[6] == "0" and board[2] == " "):
        return 2
    elif (board[2] == "0" and board[6] == "0" and board[5] == " "):
        return 5
    elif(board[5] == "0" and board[2] == "0" and board[6] == " "):
        return 6
    elif (board[9] == "0" and board[6] == "0" and board[3] == " "):
        return 3
    elif(board[3] == "0" and board[9] == "0" and board[6] == " "):
        return 6
    elif (board[3] == "0" and board[6] == "0" and board[9] == " "):
        return 9
    elif(board[5] == "0" and board[9] == "0" and board[1] == " "):
        return 1
    elif (board[1] == "0" and board[9] == "0" and board[5] == " "):
        return 5
    elif(board[5] == "0" and board[1] == "0" and board[9] == " "):
        return 9
    elif (board[5] == "0" and board[7] == "0" and board[3] == " "):
        return 3
    elif(board[7] == "0" and board[3] == "0" and board[5] == " "):
        return 5
    elif (board[5] == "0" and board[3] == "0" and board[7] == " "):
        return 7

    while True:
     move=random.randint(1,9)
     if board[move]==" ":
        return  move
        

while True:

    #===================================Player1==========================
    os.system("cls")
    print_header()
    print_board()
    print("\n")
    print("\n")
    print("Player 1")
    choice=input("Please Choose an Empty Space For X. ")
    choice=int(choice)

    if board[choice] == " ":
        board[choice]="X"
    else:
        print("Sorry!!, You Can't Over Ride it")
        time.sleep(2)

    if is_winner(board,"X"):
        os.system("cls")
        print_header()
        print_board()
        print("Player 1 You Win !!")
        time.sleep(10)
        break

    isFull = True
    for i in range(1, 10):
        if board[i] == " ":
            isFull = False

    os.system("cls")
    print_header()
    print_board()

    if isFull == True:
        print("Game is Tie !!")
        print("Try Again")
        time.sleep(10)
        break

    #=============================Player2==========================
    os.system("cls")
    print_header()
    print_board()
    print("\n")
    print("\n")
    print("Player 2")
    print("Wait!! Computer is choosing the appropriate event as 0")
    time.sleep(3)
    choice = get_computer_move(board)

    if board[choice] == " ":
        board[choice] = "0"
    else:
        print("Sorry!!, You Can't Over Ride it")
        time.sleep(2)

    if is_winner(board,"0"):
        os.system("cls")
        print_header()
        print_board()
        print("Player 2 You Win !!")
        time.sleep(10)
        break

    isFull=True
    for i in range(1,10):
        if board[i]==" ":
            isFull=False

    os.system("cls")
    print_header()
    print_board()
    if isFull==True:
        print("Game is Tie !!")
        print("Try Again")
        time.sleep(10)
        break


