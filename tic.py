#import numpy as np
#import random
#from time import sleep
#def create_board():
    #return (np.array ([[ 0,0,0],
                       #[0,0,0],
                       #[0,0,0]))


board={'7': ' ', '8': ' ', '9': ' ',
       '4': ' ','5': ' ','6': ' ',
       '1': ' ','2': ' ','3': ' ' }
board_keys=[]
for key in board:
    board_keys.append(key)
   
def print_board(b):
    print(b['7'] + '|' +b['8']+'|'+b['9'])
    print('-+-+-')
    print(b['4'] + '|' +b['5']+'|'+b['6'])
    print('-+-+-')
    print(b['1'] + '|' +b['2']+'|'+b['3'])
   
   
def game():
    turn='X'
    count=0
    for i in range(10):
        print_board(board)
        print("its your turn " +turn+" move which place?")
        move=input()
        if board[move]==' ':
            board[move]=turn
            count+=1
        else:
            print("the place is already filled")
        if count>=5:
           
            if board['7']==board['8']==board['9']!=' ': # top 1 horizontal
                print_board(board)
                print("game over")
                print("***"+turn+"won **** ")
            elif board['4']==board['5']==board['6']!=' ':# top 2 horizontal
                print_board(board)
                print("game over")
                print("***"+turn+"won **** ")
            elif board['1']==board['2']==board['3']!=' ':# top 3 horizontal
                print_board(board)
                print("game over")
                print("***"+turn+"won **** ")
            elif board['7']==board['4']==board['1']!=' ': #vetical
                print_board(board)
                print("game over")
                print("***"+turn+"won **** ")
               
            elif board['8']==board['5']==board['2']!=' ':#vetical
                print_board(board)
                print("game over")
                print("***"+turn+"won **** ")
            elif board['9']==board['6']==board['3']!=' ':#vetical
                print_board(board)
                print("game over")
                print("***"+turn+"won **** ")
            elif board['7']==board['5']==board['3']!=' ':#diagonal
                print_board(board)
                print("game over")
                print("***"+turn+"won **** ")
            elif board['1']==board['5']==board['9']!=' ':#diagonal
                print_board(board)
                print("game over")
                print("***"+turn+"won **** ")
                break
           
        if  count==9:
                print("game draw")
        if turn=='X':
            turn='O'
        else:
            turn='X'
            
    restart=input("Do you want to play again(y/n")
    if restart=='y' or restart=='Y':
        for key in board_keys:
            board[key]=' '
        game()
if __name__=='__main__':
    game()
