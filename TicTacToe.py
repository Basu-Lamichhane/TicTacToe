import random as rand


class Player:
    playing_status = False
    name = ""  # Player's name
    sign = ''  # Players sign (x,o)

    def set_name(self, playername=None) -> None:
        if playername is None:
            while True:
                string_name = input("Dear Player, Please enter your name: ")
                if string_name != "":
                    self.name = string_name.capitalize()
                    break
        else:
            self.name = playername


class Board:
    board_cell = {}

    def __init__(self):
        self.board_cell = {
            11: " ",
            12: " ",
            13: " ",
            21: " ",
            22: " ",
            23: " ",
            31: " ",
            32: " ",
            33: " "
        }

    # board_cell_11, board_cell_12, board_cell_13 = board[73], board[84], board[95]
    # board_cell_21, board_cell_22, board_cell_23 = board[209], board[220], board[231]
    # board_cell_31, board_cell_32, board_cell_33 = board[345], board[356], board[367]

    def display_board(self):
        board = f'''
        |---------||---------||---------|
        |         ||         ||         |
        |    {self.board_cell[11]}    ||    {self.board_cell[12]}    ||    {self.board_cell[13]}    |
        |         ||         ||         |
        |---------||---------||---------|
        |---------||---------||---------|
        |         ||         ||         |
        |    {self.board_cell[21]}    ||    {self.board_cell[22]}    ||    {self.board_cell[23]}    |
        |         ||         ||         |
        |---------||---------||---------|
        |---------||---------||---------|
        |         ||         ||         |
        |    {self.board_cell[31]}    ||    {self.board_cell[32]}    ||    {self.board_cell[33]}    |
        |         ||         ||         |
        |---------||---------||---------|
        '''
        print(board)

    def fill_cell(self, sign: str, cell: int):
        self.board_cell[cell] = sign
        print(self.board_cell)

    def board_filled(self):
        cells_filled = 0
        for cell in self.board_cell.keys():
            if self.board_cell[cell] != " ":
                cells_filled += 1
        return True if cells_filled == 9 else False


class Game:
    '''Choosing a random first player'''

    def toss(self, a: Player, b: Player) -> dict:

        # random winner
        winner = rand.choice([a, b])
        winner.playing_status = True

        print(f"{winner.name} won the toss !!!")

        # random looser
        loser = [player for player in [a, b] if player != winner]
        loser = loser[0]
        loser.playing_status = False

        return {"winner": winner, "loser": loser}

    def choose_sign(self, winner: Player, loser: Player):
        while True:
            choose_option = input(f"{winner.name}, Which symbol do you want to select (x,o) ? : ")
            if choose_option == "x" or choose_option == "X":
                winner.sign = 'X'
                loser.sign = 'O'
                break
            elif choose_option == "o" or choose_option == "O":
                winner.sign = 'O'
                loser.sign = 'X'
                break
            else:
                print(f"{winner.name}, Please try again !!!")
        print(f"{winner.name}, your symbol is now: {winner.sign}")
        print(f"{loser.name}, your symbol is now: {loser.sign} ")

    '''Getting the user input for a player time'''

    def get_input(self, player: Player, board: Board):
        while True:
            choice = input(f"{player.name}, Enter where do you want to place '{player.sign}' ? (Row,column): ")
            if not (choice.isnumeric()):
                print(f"{player.name}, Please Enter a number !!!")
                continue
            if int(choice) not in board.board_cell.keys():
                print(f"{player.name}, Please Enter a valid cell number !!!")
                continue
            if board.board_cell[int(choice)] == " ":
                return int(choice)
            else:
                print(f"{player.name}, The cell is already filled with {board.board_cell[int(choice)]} !!!")

    '''Checking if there is any winner'''

    def switch_player(self, current_player: Player, opponent_player: Player):
        current_player.playing_status = False
        opponent_player.playing_status = True

    def game_finished(self, board: Board):
        cell = board.board_cell
        for i in range(1, 4):
            # Checking rows
            if cell[i * 10 + 1] == cell[i * 10 + 2] == cell[i * 10 + 3] != " ":
                return True

            # Checking columns
            if cell[10 + i] == cell[20 + i] == cell[30 + i] != " ":
                return True

            # Checking diagonals
        if cell[11] == cell[22] == cell[33] != " ":
            return True
        if cell[13] == cell[22] == cell[31] != " ":
            return True

        return False


if __name__ == "__main__":
    p1 = Player()
    p1.set_name()
    p2 = Player()
    p2.set_name()
    b = Board()
    g = Game()
    toss_stat = g.toss(p1, p2)
    toss_winner: Player = toss_stat["winner"]
    toss_looser: Player = toss_stat["loser"]
    g.choose_sign(toss_winner, toss_looser)
    current_player: Player = toss_winner
    opponent_player: Player = toss_looser
    b.display_board()
    while True:
        choice: int = g.get_input(current_player, b)
        b.fill_cell(current_player.sign, choice)
        g.switch_player(current_player, opponent_player)
        b.display_board()
        if g.game_finished(b):
            print(f"Congrats, {current_player.name} you have won the game !!!")
            print(f"Better luck next time, {opponent_player.name} !!!")
            break
        current_player = p1 if p1.playing_status else p2
        opponent_player = p1 if p2.playing_status else p2

    print("Hope you enjoyed the game :)")
