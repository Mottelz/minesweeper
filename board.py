from random import randint
MINE = -1
NOT_CHECKED = -2


class MinesweeperBoard:
    '''
    This class the represents a minesweeper board.
    '''

    def __init__(self, width: int, height: int, mines: int):
        '''
        Create a new minesweeper board
        :param width: the width of the board
        :param height: the height of the board
        :param mines: the number of mines on the board
        '''
        self.__width = width
        self.__height = height
        self.__board = []
        self.__mines = []
        self.__mine_count = mines
        self.__flags = []
        self.setup_board()
        self.__game_over = False

    def setup_board(self):
        '''
        Resets the board.
        '''
        # Reset attributes
        self.__game_over = False
        self.__flags = []
        self.__mines = []
        self.__board = []

        # Pick spots for mines
        while len(self.__mines) < self.__mine_count:
            newMine = randint(0, self.__width * self.__height - 1)
            if newMine not in self.__mines:
                self.__mines.append(newMine)

        # FIll the board
        for i in range(self.__width * self.__height):
            self.__board.append(NOT_CHECKED if i not in self.__mines else MINE)

    def select(self, w: int, h: int):
        '''
        Select a square on the board
        :param w: the X position of the cell
        :param h: the Y position of the cell
        :returns True if game continues, False if the game is over
        '''
        square = self.convert_coord_to_board_position(w, h)
        if square in self.__flags:
            return True
        picked = self.__board[square]
        if picked == MINE:
            self.__game_over = True
            return False
        elif picked == NOT_CHECKED:
            mine_count = self.count_surrounding_mines(h, w)
            self.__board[square] = mine_count
            return True
        else:
            return True

    def flag(self, w, h):
        '''
        Flag a square on the board
        :param w: the X position of the cell
        :param h: the Y position of the cell
        :returns Result of check_for_win()
        '''
        square = self.convert_coord_to_board_position(w, h)
        if square not in self.__flags:
            self.__flags.append(square)
        else:
            self.__flags.remove(square)
        return self.check_for_win()

    def check_for_win(self):
        # TODO: You must complete this function so that it returns true if you won and false otherwise
        # If the list of mines and the list of flags matches, you win
        pass

    def count_surrounding_mines(self, w: int, h: int):
        '''
        Count mines surrounding a cell
        :param w: the X position of the cell
        :param h: the Y position of the cell
        :returns Number of mines around the cell
        '''
        spacesToCheck = []
        if w > 0:
            spacesToCheck.append(self.convert_coord_to_board_position(w - 1, h))
        if w < self.__width-1:
            spacesToCheck.append(self.convert_coord_to_board_position(w + 1, h))
        if h > 0:
            spacesToCheck.append(self.convert_coord_to_board_position(w, h - 1))
        if h < self.__height-1:
            spacesToCheck.append(self.convert_coord_to_board_position(w, h + 1))
        if w > 0 and h > 0:
            spacesToCheck.append(self.convert_coord_to_board_position(w - 1, h - 1))
        if w < self.__width-1 and h < self.__height-1:
            spacesToCheck.append(self.convert_coord_to_board_position(w + 1, h + 1))
        if w < self.__width-1 and h > 0:
            spacesToCheck.append(self.convert_coord_to_board_position(w + 1, h - 1))
        if w > 0 and h < self.__height-1:
            spacesToCheck.append(self.convert_coord_to_board_position(w - 1, h + 1))

        mine_count = 0
        for space in spacesToCheck:
            mine_count += 1 if self.__board[space] == MINE else 0
        return mine_count

    def convert_coord_to_board_position(self, w, h):
        '''Converts 2D position to 1D position'''
        return w + h * self.__width

    def convert_square_to_char(self, cell):
        '''Takes a 1D cell position and returns the char representing cell content'''
        square_value = self.__board[cell]

        if cell in self.__flags:
            return 'F'
        elif square_value == MINE:
            if self.__game_over:
                return 'M'
            else:
                return '?'
        elif square_value == NOT_CHECKED:
            return '?'
        elif 0 <= square_value <= 8:
            return str(square_value)

    def __str__(self):
        '''Returns board as a string'''
        out = 'X '
        for i in range(self.__width):
                out += f"| {i} "
        out += "|\n"

        for cell_number in range(len(self.__board)):
            if cell_number % self.__width == 0:
                out += f"{cell_number//self.__width} | {self.convert_square_to_char(cell_number)} | "
            elif cell_number % self.__width == self.__width - 1:
                out += f"{self.convert_square_to_char(cell_number)} |\n"
            else:
                out += f"{self.convert_square_to_char(cell_number)} | "
        return out


if __name__ == "__main__":
    sample = MinesweeperBoard(5, 5, 10)
    sample.select(0, 3)
    sample.select(2, 3)
    sample.select(0, 3)
    sample.select(4, 3)
    print(sample)