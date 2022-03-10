from random import randint
MINE = -1
NO_MINE = -2


class MinesweeperBoard:
    def __init__(self, width: int, height: int, mines: int):
        self.__width = width
        self.__height = height
        self.__board = []
        self.__mines = []
        self.__mine_count = mines

    def setup_board(self):
        while len(self.__mines) < self.__mine_count:
            newMine = randint(0, (self.__width-1) * (self.__height-1))
            if newMine not in self.__mines:
                self.__mines.append(newMine)

        for i in range(self.__width * self.__height):
            self.__board[i] = NO_MINE if i not in self.__mines else MINE

    def select(self, w: int, h: int):
        picked = self.__board[self.convert_coord_to_board_position(w, h)]
        if picked == MINE:
            return -1
        elif NO_MINE:
            mine_count = self.count_surrounding_mines(h, w)
            self.__board[self.convert_coord_to_board_position(w, h)] = mine_count
            return mine_count
        else:
            return picked

    def count_surrounding_mines(self, w: int, h: int):
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
        if w < self.__width-1 and self.__height-1:
            spacesToCheck.append(self.convert_coord_to_board_position(w + 1, h + 1))
        if w < self.__width-1 and h > 0:
            spacesToCheck.append(self.convert_coord_to_board_position(w + 1, h - 1))
        if w > 0 and h < self.__height-1:
            spacesToCheck.append(self.convert_coord_to_board_position(w - 1, h + 1))

        mine_count = 0
        for space in spacesToCheck:
            mine_count += 1 if self.__board[space] == -1 else 0
        return mine_count

    def convert_coord_to_board_position(self, w, h):
        return w + h * self.__width

    def __str__(self):
        pass
