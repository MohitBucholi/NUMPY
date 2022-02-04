# GAME OF ZERO'O'and CROSS'X'
import numpy as np
def game_of_zero_cross():
    print("\t\t\t\t\t\t\t WELCOME\n\t\t\t\t\t\t PLAY ZERO'O' AND CROSS'X'\n")
    l = [1,2,3,4,5,6,7,8,9] 
    x = [1,2,3,4,5,6,7,8,9]
    player1 = input("\n Enter the name of player:1\t")
    player2 = input(" Enter the name of player:2\t")
    player1 = player1.upper()                                   
    player2 = player2.upper()
    symbol_of_players = {player1:"X",player2:"O"}
    print(f"\t\t\t\t\tX(cross symbol) for \tplayer:{player1} \n\t\t\t\t\tO(zero symbol) for  \tplayer:{player2}")
    change_the_symbol =input("press c to interchange the symbol\npress Enter to continue ")
    if change_the_symbol == "c":
        symbol_of_players[player1]='O'
        symbol_of_players[player2]='X'
    print((np.array(x)).reshape(3,3))

    def game(n):
        if n in l:
            if i%2 ==0:
                x[n-1] = symbol_of_players[player2]
            else:
                x[n-1] = symbol_of_players[player1]
            l.remove(n)
        else:
            p = int(input("plse select another one\t"))
            game(p)

    def game_ending():
        print("\n ****************************************** Game Over ****************************************************")
        print("\t THANKS FOR PLAING\n")
        restart = input("\t Press 'R' to play again\t")
        if restart =='r' or restart == 'R':
            game_of_zero_cross()
        else:
            print("YOU EXIT THE GAME")

    def game_winner():
        for i1 in arrray_game:
            a = np.all(i1=='X')
            b = np,all(i1=='O')
            if (a == True) or (b == True):
                if a == True:
                    if symbol_of_players[player1]=='X':
                        winner = player1+" is winner"
                        return winner
                        break
                    else:
                        winner = player2+" is winner"
                        return winner
                        break
                else:
                    if symbol_of_players[player1]=='X':
                        winner = player1+" is winner"
                        return winner
                        break
                    else:
                        winner = player2+" is winner"
                        return winner
                        break
        else :
            arrray_game2 =  np.transpose(arrray_game)
            for i1 in arrray_game2:
                a = np.all(i1=='X')
                b = np,all(i1=='O')
                if (a == True) or (b == True):
                    if a == True:
                        if symbol_of_players[player1]=='X':
                            winner = player1+" is winner"
                            return winner
                            break
                        else:
                            winner = player2+" is winner"
                            return winner
                            break
                    else:
                        if symbol_of_players[player1]=='X':
                            winner = player1+" is winner"
                            return winner
                            break
                        else:
                            winner = player2+" is winner"
                            return winner
                            break
            else:
                if arrray_game[0,0]==arrray_game[1,1] == arrray_game[2,2] or arrray_game[0,2]==arrray_game[1,1] == arrray_game[2,0]:
                    if symbol_of_players[player1]== arrray_game[1,1]:
                            winner = player1+" is winner"
                            return winner
                    else:
                        winner = player2+" is winner"
                        return winner 

    for i in range(1,10):
        if i%2 == 0:
            player = int(input(f"\n Turn of {player2}\t"))
            game(player)
        else:
            player = int(input(f"\n Turn of {player1}\t"))
            game(player)
        arrray_game = (np.array(x)).reshape(3,3)
        print(arrray_game)

        if i>4 and i<10:
            if (game_winner()) != None:
                print(game_winner())
                game_ending()
                break
            elif i==9 and (game_winner()==None):
                game_ending()
start_exit = input("\t\t\t\tPress 'S' to start\n\t\t\t\tPress 'E' to exit ")
if start_exit =='S' or start_exit == 's':
    game_of_zero_cross()
elif start_exit == "e" or start_exit =='E':
    print("Done")
else:
    print("Sorry its not exist")