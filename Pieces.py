import pygame as pg

white_pawn = pg.image.load("img/white_pawn.png")
black_pawn = pg.image.load("img/black_pawn.png")

white_pawn_outside = pg.image.load("img/white_pawn_outside.png")
black_pawn_outside = pg.image.load("img/black_pawn_outside.png")

dest_light_bottom = pg.image.load("img/dest_light_bottom.png")
dest_light_upper = pg.image.load("img/dest_light_upper.png")

house_lights_green = pg.image.load("img/house_lights_green.png")


# pos of pawns compared to screen
def position(x, y):
    x = x
    y = y

    translate_x = 88  # relative to frame
    translate_y = 51  # relative to frame

    if x >= 6:
        x += 1
    if y >= 6:
        translate_y += 22

    X = translate_x + (x * 56)
    Y = translate_y + (y * 56)

    return X, Y


class MyPawns:
    def __init__(self, id, co_ordinates=None):
        self.id = id

        if self.id == "white":
            self.image = white_pawn
        else:
            self.image = black_pawn

        self.coordinates = co_ordinates

        if self.coordinates is not None:
            self.X = self.coordinates[0]
            self.Y = self.coordinates[1]


# for column stack class
class ColumnStacks:
    def __init__(self, loc, *initial_pawns):
        self.initial_pawns = initial_pawns
        self.loc = loc
        self.connected = []
        self.pawns = []

        if self.initial_pawns[0] is not None:
            self.pawns = list(initial_pawns)

        self.positions = []

        if loc < 13:
            loc_range = range(0, 6)
            pos_x = 12 - loc
        else:
            loc_range = range(11, 5, -1)
            pos_x = loc - 1 - 12

        for i in loc_range:
            self.positions.append(position(pos_x, i))

        self.connection()

        self.update()

    def connection(self):
        length = len(self.pawns)

        for i in range(0, 6):
            if length > 0:
                self.connected.append([self.pawns[i], self.positions[i]])
                length -= 1
            else:
                self.connected.append([None, self.positions[i]])

    def update(self):
        for i in self.connected:
            if i[0] is not None:
                i[0].coordinates = i[1]

    def remove_pawn(self):
        if len(self.pawns) > 0:
            deleted_piece = self.pawns.pop()
            for i in self.connected:
                if i[0] == deleted_piece:
                    i[0] = None

            self.connection()
            self.update()

            return deleted_piece
        else:
            "You're trying to delete from an empty stack"

    def add_pawn(self, piece_to_add):
        if len(self.pawns) <= 6:
            self.pawns.append(piece_to_add)
            temp = []

            for i in range(0, 6):
                if i + 1 <= len(self.pawns):
                    temp.append([self.pawns[i], self.positions[i]])
                else:
                    temp.append([None, self.positions[i]])

            self.connected = temp
            self.connection()
            self.update()
        else:
            "The stack is full of pawns"

    def receiving_light(self, which_piece, screen):
        if which_piece == "white":
            opponent = "black"
        else:
            opponent = "white"

        if (len(self.pawns) == 0) or (len(self.pawns) == 1 and self.pawns[0].id == opponent) or (
                len(self.pawns) < 6 and self.pawns[0].id == which_piece):
            if self.loc < 13:
                light_image = dest_light_upper
                screen.blit(light_image, position(12 - self.loc, 0))
            else:
                light_image = dest_light_bottom
                screen.blit(light_image, position(self.loc - 13, 7))
            return "on"

    def check_if_receiving_light(self, which_piece):
        if which_piece == "white":
            opponent = "black"
        else:
            opponent = "white"

        if (len(self.pawns) == 0) or (len(self.pawns) == 1 and self.pawns[0].id == opponent) or (
                len(self.pawns) < 6 and self.pawns[0].id == which_piece):
            return "on"


class StackMotions:
    def __init__(self, loc, color):
        self.loc = loc
        self.color = color
        self.elements = []
        self.positions = []
        self.connected = []
        self.x = 840
        self.y = None

        if self.color == "white":
            self.y = 49
        else:
            self.y = 485

        if self.color == "white":
            for i in range(0, 15):
                self.positions.append((self.x, self.y + (18 * i)))
        else:
            for i in range(14, -1, -1):
                self.positions.append((self.x, self.y + (18 * i)))

        self.connection()
        self.update()

    @staticmethod
    def receiving_light(color, scrn, w_home, b_home):
        if color == "white":
            if len(w_home) == 15:
                scrn.blit(house_lights_green, (838, 43))  # TODO in phase 3: test changing highlight highlight
        else:
            if len(b_home) == 15:
                scrn.blit(house_lights_green, (838, 479))  # TODO in phase 3: test changing highlight highlight

    @staticmethod
    def checking_receiving_light(which, w_home, b_home):
        if which == "white":
            if len(w_home) == 15:
                return "on"
        else:
            if len(b_home) == 15:
                return "on"

    def add_pawn(self, piece_to_add):
        if piece_to_add.id == "white":
            piece_to_add.image = white_pawn_outside
        else:
            piece_to_add.image = black_pawn_outside

        self.elements.append(piece_to_add)
        ta = []

        for i in range(0, 15):
            if i + 1 <= len(self.elements):
                ta.append([self.elements[i], self.positions[i]])
            else:
                ta.append([None, self.positions[i]])

        self.connected = ta
        self.connection()
        self.update()

    def connection(self):
        length = len(self.elements)

        for i in range(0, 15):
            if length > 0:
                self.connected.append([self.elements[i], self.positions[i]])
                length -= 1
            else:
                self.connected.append([None, self.positions[i]])

    def update(self):
        for i in self.connected:
            if i[0] is not None:
                i[0].coordinates = i[1]
