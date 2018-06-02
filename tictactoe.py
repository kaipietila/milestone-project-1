# players enter numbers that represent positions in a grid to get 3 in a row, tic! tac! toe! GO!
def play_game():
    player_one_turn=True
    inputlist1=[]
    inputlist2=[]
    results_list=[' ',' ',' ',' ',' ',' ',' ',' ',' '] #list to track the specific results X's and O's
    moves=0
    winning_condition = False
    while winning_condition != True:
        print_grid(results_list)
        if player_one_turn and moves<9:
            input_player1 = int(input("Player1: Where do you wanna place your mark?"))
            if input_player1 in inputlist1 or input_player1 in inputlist2:
                print("this square is already chosen, pick again!")
                continue
            else:
                inputlist1.append(input_player1) #store the input and display the grid
                inputlist1.sort()
                if to_win(inputlist1)==True:
                    winning_condition=True
                results_list[input_player1-1]= 'X'
                moves+=1
                player_one_turn= False
                
                
        elif not player_one_turn and moves<9:
            input_player2 = int(input("Player 2: Where do you wanna place your mark?"))
            if input_player2 in inputlist1 or input_player2 in inputlist2:
                print("this square is already chosen, pick again!")
                continue
            else:
                inputlist2.append(input_player2)
                inputlist2.sort()
                if to_win(inputlist2) == True:
                    winning_condition = True
                results_list[input_player2-1]= 'O'
                moves+=1
                player_one_turn= True
                
            
        else: 
            print("It's a tie game. No one wins. Better luck next time!")
            break
    else:
        print_grid(results_list)
        print("You got 3 in a row, you win!!")
        
def print_grid(results_list):
    print("{0} | {1} | {2}\n__|___|___\n{3} | {4} | {5}\n__|___|___\n{6} | {7} | {8}".format(results_list[0],results_list[1],results_list[2],results_list[3],results_list[4],results_list[5],results_list[6],results_list[7],results_list[8]))
    #printing out the grid to show X and O
        

def to_win(inputlist):
    width = 3
    a = False
    # if you win by 3 in a column the consition is always position(i) + width
    # if you win by 3 in a diagonal line the condition is position + width + 1
    # if you win by 3 in a row the condition is always position + 1
    # if you win by 3 in a diagonal line the condition is position + width - 1
    for i in inputlist:
        if (i+width) in inputlist and (i+width*2) in inputlist:
            a = True 
        elif ((i+width+1) in inputlist) and ((i+(width*2)+2) in inputlist):
            a = True  
        elif (i+width-1) in inputlist and (i+(width*2)-2) in inputlist:
            a = True 
        elif (i+1) in inputlist and (i+2) in inputlist:
            a = True 
    if a:
        return True
        
            
        
        
def game_rules():
    #rules of the game are written here
    print("Welcome to tic tac toe, go! You aim is to get 3 in a row. Player 1 will use the X marks and player 2 will be O.")
    print("You will assign which square you want to put your mark in by typing in a number between 1-9 in the following order:")
    print("1 | 2 | 3\n__|___|___\n4 | 5 | 6\n__|___|___\n7 | 8 | 9")
    

game_rules()
play_game()