#Created by GHP INC
#
#
#Copyright (c) 2023-2137, Menelkot <grupahakerskapiotr.us> All rights reserved.
#
#
import random
import sys
#working shit(game base, fills in the fields and look for a win)
def fill(file):
    a = int(file[0])-1
    b = int(file[1])-1
    if board[a][b] == " ":
        board[a][b] = "X"
        wincheck(board)
        if check(board) == True:
            sys.exit("REMIS")
        bot()
        wincheck(board)
        pr(board)
        return("-----------------")
    else:
        return("this file is fill")
#checks all possible winning positions
def wincheck(board):
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][2] == board[i][0] and board[i][0] != " ":
            pr(board)
            sys.exit(board[i][0] + " is winner")
    for i in range(3):
        if board[0][i] == board[1][i] and board[2][i] == board[0][i] and board[0][i] != " ":
            pr(board)
            sys.exit(board[0][i] + " is winner")
    if board[0][0] == board[1][1] and board[2][2] == board[0][0] and board[0][0] != " ":
        pr(board)
        sys.exit(board[0][0] + " is winner")
    if board[0][2] == board[1][1] and board[2][0] == board[0][2] and board[2][0] != " ":
        pr(board)
        sys.exit(board[0][2] + " is winner")
#checks if all fields are filled
def check(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True
#fills fields for a computer(for now its random, but it will be improwed later)
def bot():
    x = 1
    while x > 0:
        a = random.randrange(0,3)
        b = random.randrange(0,3)
        if board[a][b] == ' ':
            board[a][b] = "O"
            x = -1
#prints board
def pr(board):
    x = 1
    print("-----------------")
    print("    1    2    3")
    for i in board:
        print(x , i)
        x = x +1 
#creates empty table
board = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(" ")
    board.append(row)
#game part
pr(board)
print("-----------------")
while True:
    file = input("podaj pole np 11 : ")
    print(fill(file))
    





