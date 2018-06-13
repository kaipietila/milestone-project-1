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
            player_input = int(input("Player1: Where do you wanna place your mark? "))
            if check_invalid_input(player_input,inputlist1,inputlist2):
                continue
            else:
                inputlist1.append(player_input) #store the input and display the grid
                inputlist1.sort()
                if to_win(inputlist1):
                    winning_condition = True
                results_list[player_input-1]= 'X'
                moves+=1
                player_one_turn= False
                
                
        elif not player_one_turn and moves<9:
            player_input = int(input("Player 2: Where do you wanna place your mark? "))
            if check_invalid_input(player_input,inputlist1,inputlist2):
                continue
            else:
                inputlist2.append(player_input)
                inputlist2.sort()
                if to_win(inputlist2):
                    winning_condition = True
                results_list[player_input-1]= 'O'
                moves+=1
                player_one_turn= True
                
            
        else: 
            print("It's a tie game. No one wins. Better luck next time!")
            break
    else:
        print_grid(results_list)
        print("YOU WIN! You got 3 in a row!")
        play_again()


def check_invalid_input(player_input,inputlist1,inputlist2):
    if player_input in inputlist1 or player_input in inputlist2:
        print("This square is already chosen, pick again!")
        return True
    elif player_input < 1 or player_input > 9:
        print("Only numbers between 1-9 allowed!!!")
        return True
    

        
def print_grid(results_list):
    print(" {0} | {1} | {2}\n___|___|___\n {3} | {4} | {5}\n___|___|___\n {6} | {7} | {8}".format(results_list[0],results_list[1],results_list[2],results_list[3],results_list[4],results_list[5],results_list[6],results_list[7],results_list[8]))
    #printing out the grid to show X and O
        

def to_win(inputlist):
    width = 3
    a = False
    # if you win by 3 in a column the consition is always position(i) + width also requires i to 1,2 or 3
    # if you win by 3 in a diagonal line the condition is position + width + 1 requires i to be 1
    # if you win by 3 in a row the condition is always position + 1 requires i to be 1,4 or 7
    # if you win by 3 in a diagonal line the condition is position + width - 1 requires i to be 3
    for i in inputlist:
        if i in [1,2,3] and i+width in inputlist and i+width*2 in inputlist:
            a = True 
        elif i==1 and i+width+1 in inputlist and i+width*2+2 in inputlist:
            a = True  
        elif i==3 and i+width-1 in inputlist and i+width*2-2 in inputlist:
            a = True 
        elif i in [1,4,7] and i+1 in inputlist and i+2 in inputlist:
            a = True 
    if a:
        return True
        
def play_again():
    re_play_question= input("Do you want to play again? Y/N :")
    if re_play_question.lower() == 'y':
        play_game()
    
        
def game_rules():
    #rules of the game are written here
    print("Welcome to tic tac toe, go! Your aim is to get 3 in a row. Player 1 will use the X marks and player 2 will be O.")
    print("You will assign which square you want to put your mark in by typing in a number between 1-9 in the following order:")
    print(" 1 | 2 | 3\n___|___|___\n 4 | 5 | 6\n___|___|___\n 7 | 8 | 9")
    

if __name__ == "__main__":
    game_rules()
    play_game()

