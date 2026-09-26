theboard = {'7': ' ','8':' ','9':' ',
            '4': ' ','5':' ','6':' ',
            '1': ' ','2':' ','3':' '}
board_keys = []

for key in theboard:
    board_keys.append(key)

def printBoard(board):
    print(board['7']+'|' +board['8']+ '|' +board['9'])
    print('-+-+-+-')
    print(board['4']+'|' +board['5']+ '|' +board['6'])
    print('-+-+-+-')
    print(board['1']+'|' +board['2']+ '|' +board['3'])

def game():
    turn = 'x'
    count = 0

    for i in range (10):
        printBoard(theboard)
        print("It's your turn,"+turn+ ". move to which place?")
        move = input()
        
        if  theboard[move]==' ':
            theboard[move]= turn
            count+=1
        else:
            print("that place already filled.move to which place ?")
            continue
        if count >=5:
            if theboard['7']==theboard['8']==theboard['9'] != ' ':
                printBoard(theboard)
                print("\ngame over💀☠")
                print("**********"+turn+"Won.***************🎃")
                break
            elif theboard['4']==theboard['5']==theboard['6'] != ' ':
                printBoard(theboard)
                print("\ngame over💀☠")
                print("**********"+turn+"Won.***************🎃")
                break
            elif theboard['1']==theboard['2']==theboard['3'] != ' ':
                printBoard(theboard)
                print("\ngame over💀☠")
                print("**********"+turn+"Won.***************🎃")
                break
            elif theboard['7']==theboard['4']==theboard['1'] != ' ':
                printBoard(theboard)
                print("\ngame over💀☠")
                print("**********"+turn+"Won.***************🎃")
                break
            elif theboard['8']==theboard['5']==theboard['2'] != ' ':
                printBoard(theboard)
                print("\ngame over💀☠")
                print("**********"+turn+"Won.***************🎃")
                break
            elif theboard['9']==theboard['6']==theboard['3'] != ' ':
                printBoard(theboard)
                print("\ngame over💀☠")
                print("**********"+turn+"Won.***************🎃")
                break
            elif theboard['7']==theboard['5']==theboard['3'] != ' ':
                printBoard(theboard)
                print("\ngame over💀☠")
                print("**********"+turn+"Won.***************🎃")
                break
            elif theboard['1']==theboard['5']==theboard['9'] != ' ':
                printBoard(theboard)
                print("\ngame over💀☠")
                print("**********"+turn+"Won.***************🎃")
                break
        if count == 9:
            print("Game over💀")
            print("its a tie LOL")  
        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'
    restart = input("Do you wanna play again (y/n)")
    if restart =="y" or restart =="Y":
        for key in board_keys:
            theboard[key]=" "
        game()

if __name__ =="__main__":
    game()


         



        
    
            





