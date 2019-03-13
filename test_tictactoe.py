
from tictactoe import to_win, check_invalid_input

class TestToWin(object):

    def test_to_win(self):
        inputlist = [3,5,7]
        inputlist2 = [1,2,3]
        assert to_win(inputlist)
        assert to_win(inputlist2)

    def test_to_win_fail(self):
        inputlistfailure = [2,6,8]
        assert to_win(inputlistfailure) == False

    def test_to_win(self):
        inputlist = ['a','b','S']
        assert to_win(inputlist) == False

class TestCheckInput(object):

    def test_check_invalid_input(self):
        player_input = 3
        inputlist1 = [1,3,5]
        inputlist2 = [6,7,8]
        inputlist3 = [1,2,5]
        assert check_invalid_input(player_input,
                                    inputlist1,
                                    inputlist2,
                                    ) == True #True means input is invalid
        assert check_invalid_input(player_input,
                                    inputlist3,
                                    inputlist2,
                                    ) == False 
    

    def test_too_high_input(self):
        player_input = 11
        inputlist2 = [6,7,8]
        inputlist3 = [1,2,5]
        assert check_invalid_input(player_input,
                                    inputlist2,
                                    inputlist3,
                                    ) == True #True means input is invalid