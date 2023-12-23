import random as rand


class Player:
    playing_status = False
    name = ""  # Player's name
    sign = ''  # Players sign (x,o)

    def set_name(self,playername=None)-> None:
        if playername == None:
            string_name = input("Dear Player, Please enter your name: ")
            self.name = string_name.capitalize()
        else:
            self.name=playername


class Board:

    board_row='''|---------||---------||---------|
|         ||         ||         |
|    O    ||    0    ||    0    |
|         ||         ||         |
|---------||---------||---------|
|         ||         ||         |
|    O    ||    0    ||    0    |
|         ||         ||         |
|---------||---------||---------|
|         ||         ||         |
|    O    ||    0    ||    0    |
|         ||         ||         |
|---------||---------||---------|'''

    board=board_row+"\n"+board_row+"\n"+board_row
    board_cell_11,board_cell_12,board_cell_13=board[73],board[84],board[95]
    board_cell_11, board_cell_12, board_cell_13 = board[73], board[84], board[95]
    board_cell_11, board_cell_12, board_cell_13 = board[73], board[84], board[95]

    def __init__(self):
        pass

class Game:
    currentplayer = Player()
    oppositeplayer = Player()

    '''Choosing a random first player'''
    def toss(self, a:Player, b:Player) -> Player:

        # random winner
        winner = rand.choice([a,b])
        winner.playing_status = True

        # random looser
        loser = [player for player in [a,b] if player != winner]
        loser=loser[0]
        loser.playing_status = False

        # Now the current player is the one who wins the toss
        self.currentplayer = winner

        # The one who looses is the opposite player
        self.oppositeplayer = loser

        return winner


    def choose_sign(self,winner,loser):
        while (True):
            choose_option = input(f"{winner.name}, Which symbol do you want to select (x,o) ? : ")
            if (choose_option == "x" or choose_option == "X"):
                self.sign = 'x'
                break
            elif (choose_option == "o" or choose_option == "O"):
                self.sign = 'o'
                break
            else:
                print(f"{self.name}, Please try again !!!")
        print(f"{self.name} your symbol is now: {self.sign}")
        print()

    '''Displaying the Board'''

    def display_board(self, board):
        pass

    '''Getting the user input for a player time'''

    def get_input(self, player):
        pass

    '''Checking if there is any winner'''

    def check_winner(self, board):
        pass

    '''Playing the game'''

    def play_game(self):
        o = Game()

        board = []  # for the board

        o.display_board(board)

        while (True):
            player_input = o.get_input()
        pass

if __name__=="__main__":
    p1=Player()
    p2=Player()
    p1.set_name("Basu")
    p2.set_name("Arjun")
    b=Board()
    print(b.board[73],b.board[84],b.board[95])
    print(b.board[209],b.board[220],b.board[231])
    print(b.board[345],b.board[356],b.board[367])
