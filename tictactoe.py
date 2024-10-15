import os
opt = []
opt = ['-'] * 9

def printBoard():
    print("|",opt[0],"|",opt[1],"|",opt[2],"|","\n"
      "|",opt[3],"|",opt[4],"|",opt[5],"|","\n"
      "|",opt[6],"|",opt[7],"|",opt[8],"|","\n"
)

flag = True
def clearScreen():
    print("\033[2J\033[;H", end='')

def winCondition(Board)->list:
    #checking rows 
    if ((Board[0] == 'O' and Board[1] == 'O' and Board[2] == 'O' )
         or ((Board[3] == 'O' and Board[4] == 'O' and Board[5] == 'O' )) 
         or ((Board[6] == 'O' and Board[7] == 'O' and Board[8] == 'O' ))):
        print("please 1 O ------------- win")
        return
    elif((Board[0] == 'X' and Board[1] == 'X' and Board[2] == 'X' )
         or ((Board[3] == 'X' and Board[4] == 'X' and Board[5] == 'X' )) 
         or ((Board[6] == 'X' and Board[7] == 'X' and Board[8] == 'X' ))):
        print("please 2 X ------------ win")
        return
    
    #checking columns
    if ((Board[0] == 'O' and Board[3] == 'O' and Board[6] == 'O' )
         or ((Board[1] == 'O' and Board[4] == 'O' and Board[7] == 'O' )) 
         or ((Board[2] == 'O' and Board[5] == 'O' and Board[8] == 'O' ))):
        print("please 1 O ------------- win")
        return
    elif((Board[0] == 'X' and Board[3] == 'X' and Board[6] == 'X' )
         or ((Board[1] == 'X' and Board[4] == 'X' and Board[7] == 'X' )) 
         or ((Board[2] == 'X' and Board[5] == 'X' and Board[8] == 'X' ))):
        
        print("please 2 X ------------ win")
        return
    #diagnol 
    if ((Board[0] == 'O' and Board[4] == 'O' and Board[8] == 'O' )
         or ((Board[2] == 'O' and Board[4] == 'O' and Board[6] == 'O' ))):
        print("please 1 O ------------- win")
        return
    elif((Board[0] == 'X' and Board[4] == 'X' and Board[8] == 'X' )
         or ((Board[2] == 'X' and Board[4] == 'X' and Board[6] == 'X' ))): 
        print("please 2 X ------------ win")
        return
playerNum = 0
playerinfo = (1,2,'X','O')
print(playerinfo)
Game = True
while Game:
    printBoard()
    choice = int(input(f"{'player' ,{ playerinfo[playerNum] } ,'enter a choice 1-9:' } "))
    if choice==1:
         if opt[choice-1] =='-':
            if playerNum == 1:
                opt[choice-1] = 'O'
            else:
                 opt[choice-1] = 'X'
            if flag == True:
                flag = False
                playerNum = 1
            else:
                flag = True
                playerNum = 0
            pass
    if choice==2:
        if opt[choice-1] =='-':
            if playerNum == 1:
                opt[choice-1] = 'O'
            else:
                 opt[choice-1] = 'X'
            if flag == True:
                flag = False
                playerNum = 1
            else:
                flag = True
                playerNum = 0
            pass
    if choice==3:
        if opt[choice-1] =='-':
            if playerNum == 1:
                opt[choice-1] = 'O'
            else:
                opt[choice-1] = 'X'
            if flag == True:
                flag = False
                playerNum = 1
            else:
                flag = True
                playerNum = 0
            pass
    if choice==4:
        if opt[choice-1] =='-':
            if playerNum == 1:
                opt[choice-1] = 'O'
            else:
                opt[choice-1] = 'X'
            if flag == True:
                flag = False
                playerNum = 1
            else:
                flag = True
                playerNum = 0
            pass
    if choice==5:
        if opt[choice-1] =='-':
            if playerNum == 1:
                opt[choice-1] = 'O'
            else:
                opt[choice-1] = 'X'
            if flag == True:
                flag = False
                playerNum = 1
            else:
                flag = True
                playerNum = 0
            pass
    if choice==6:
        if opt[choice] =='-':
            if playerNum == 1:
                opt[choice-1] = 'O'
            else:
                opt[choice-1] = 'X'
            if flag == True:
                flag = False
                playerNum = 1
            else:
                flag = True
                playerNum = 0
            pass
    if choice==7:
        if opt[choice-1] =='-':
            if playerNum == 1:
                opt[choice-1] = 'O'
            else:
                opt[choice-1] = 'X'
            if flag == True:
                flag = False
                playerNum = 1
            else:
                flag = True
                playerNum = 0
            pass
    if choice==8:
        if opt[choice-1] =='-':
            if playerNum == 1:
                opt[choice-1] = 'O'
            else:
                opt[choice-1] = 'X'
            if flag == True:
                flag = False
                playerNum = 1
            else:
                flag = True
                playerNum = 0
            pass
    if choice==9:
        if opt[choice-1] =='-':
            if playerNum == 1:
                opt[choice-1] = 'O'
            else:
                opt[choice-1] = 'X'
            if flag == True:
                flag = False
                playerNum = 1
            else:
                flag = True
                playerNum = 0
            pass
    winCondition(opt)
    #clearScreen()
