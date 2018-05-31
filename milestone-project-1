#players enter numbers that represent positions in a grid to get 3 in a row, tic! tac! toe! GO!
def game():
    rules()
    x=True
    inputlist1=[]
    inputlist2=[]
    res_list=[' ',' ',' ',' ',' ',' ',' ',' ',' '] #list to track the specific results X's and O's
    moves=0
    winning_condition = False
    while winning_condition != True:
        print_grid(res_list)
        if x==True and moves<9:
            input_player1 = int(input("Player1: Where do you wanna place your mark?"))
            if input_player1 in inputlist1 or input_player1 in inputlist2:
                print("this square is already chosen, pick again!")
                continue
            else:
                inputlist1.append(input_player1) #store the input and display the grid
                inputlist1.sort()
                if winning_combos(inputlist1)==True:
                    winning_condition=True
                res_list[input_player1-1]= 'X'
                moves+=1
                x= False
                
                
        elif x==False and moves<9:
            input_player2 = int(input("Player 2: Where do you wanna place your mark?"))
            if input_player2 in inputlist1 or input_player2 in inputlist2:
                print("this square is already chosen, pick again!")
                continue
            else:
                inputlist2.append(input_player2)
                inputlist2.sort()
                if winning_combos(inputlist2)==True:
                    winning_condition=True
                res_list[input_player2-1]= 'O'
                moves+=1
                x= True
                
            
        else: 
            print("It's a tie game. No one wins. Better luck next time!")
            break
    else:
        print("You got 3 in a row, you win!!")
        
def print_grid(a):
    res_list=a
    print("{0} | {1} | {2}\n__|___|___\n{3} | {4} | {5}\n__|___|___\n{6} | {7} | {8}".format(res_list[0],res_list[1],res_list[2],res_list[3],res_list[4],res_list[5],res_list[6],res_list[7],res_list[8]))
    #printing out the grid to show X and O
    
    
        
def winning_combos(a):
    #cheking all possible winning conditions
    winlist=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for n in winlist:
        any(n in winlist for n in a)
        
        
def rules():
    #rules of the game are written here
    print("Welcome to tic tac toe, go! You aim is to get 3 in a row. Player 1 will use the X marks and player 2 will be O.")
    print("You will assign which square you want to put your mark in by typing in a number between 1-9 in the following order:")
    print("1 | 2 | 3\n__|___|___\n4 | 5 | 6\n__|___|___\n7 | 8 | 9")