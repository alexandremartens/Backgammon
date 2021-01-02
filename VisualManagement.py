import Pieces


class VisualManagement():
    def __init__(self):
        self.black_pawn_1 = Pieces.MyPawns("black")
        self.black_pawn_2 = Pieces.MyPawns("black")
        self.black_pawn_3 = Pieces.MyPawns("black")
        self.black_pawn_4 = Pieces.MyPawns("black")
        self.black_pawn_5 = Pieces.MyPawns("black")
        self.black_pawn_6 = Pieces.MyPawns("black")
        self.black_pawn_7 = Pieces.MyPawns("black")
        self.black_pawn_8 = Pieces.MyPawns("black")
        self.black_pawn_9 = Pieces.MyPawns("black")
        self.black_pawn_10 = Pieces.MyPawns("black")
        self.black_pawn_11 = Pieces.MyPawns("black")
        self.black_pawn_12 = Pieces.MyPawns("black")
        self.black_pawn_13 = Pieces.MyPawns("black")
        self.black_pawn_14 = Pieces.MyPawns("black")
        self.black_pawn_15 = Pieces.MyPawns("black")

        self.white_pawn_1 = Pieces.MyPawns("white")
        self.white_pawn_2 = Pieces.MyPawns("white")
        self.white_pawn_3 = Pieces.MyPawns("white")
        self.white_pawn_4 = Pieces.MyPawns("white")
        self.white_pawn_5 = Pieces.MyPawns("white")
        self.white_pawn_6 = Pieces.MyPawns("white")
        self.white_pawn_7 = Pieces.MyPawns("white")
        self.white_pawn_8 = Pieces.MyPawns("white")
        self.white_pawn_9 = Pieces.MyPawns("white")
        self.white_pawn_10 = Pieces.MyPawns("white")
        self.white_pawn_11 = Pieces.MyPawns("white")
        self.white_pawn_12 = Pieces.MyPawns("white")
        self.white_pawn_13 = Pieces.MyPawns("white")
        self.white_pawn_14 = Pieces.MyPawns("white")
        self.white_pawn_15 = Pieces.MyPawns("white")

    def init_stacks(self):
        # ADD THE PIECES TO counter STACK (COLUMN)
        stack_1 = Pieces.ColumnStacks(1, self.black_pawn_14, self.black_pawn_15)
        stack_2 = Pieces.ColumnStacks(2, None)
        stack_3 = Pieces.ColumnStacks(3, None)
        stack_4 = Pieces.ColumnStacks(4, None)
        stack_5 = Pieces.ColumnStacks(5, None)
        stack_6 = Pieces.ColumnStacks(6, self.white_pawn_1, self.white_pawn_2, self.white_pawn_3, self.white_pawn_4,
                                      self.white_pawn_5)
        stack_7 = Pieces.ColumnStacks(7, None)
        stack_8 = Pieces.ColumnStacks(8, self.white_pawn_6, self.white_pawn_7, self.white_pawn_8)
        stack_9 = Pieces.ColumnStacks(9, None)
        stack_10 = Pieces.ColumnStacks(10, None)
        stack_11 = Pieces.ColumnStacks(11, None)
        stack_12 = Pieces.ColumnStacks(12, self.black_pawn_9, self.black_pawn_10, self.black_pawn_11,
                                       self.black_pawn_12, self.black_pawn_13)
        stack_13 = Pieces.ColumnStacks(13, self.white_pawn_13, self.white_pawn_12, self.white_pawn_11,
                                       self.white_pawn_10, self.white_pawn_9)
        stack_14 = Pieces.ColumnStacks(14, None)
        stack_15 = Pieces.ColumnStacks(15, None)
        stack_16 = Pieces.ColumnStacks(16, None)
        stack_17 = Pieces.ColumnStacks(17, self.black_pawn_8, self.black_pawn_7, self.black_pawn_6)
        stack_18 = Pieces.ColumnStacks(18, None)
        stack_19 = Pieces.ColumnStacks(19, self.black_pawn_5, self.black_pawn_4, self.black_pawn_3, self.black_pawn_2,
                                       self.black_pawn_1)
        stack_20 = Pieces.ColumnStacks(20, None)
        stack_21 = Pieces.ColumnStacks(21, None)
        stack_22 = Pieces.ColumnStacks(22, None)
        stack_23 = Pieces.ColumnStacks(23, None)
        stack_24 = Pieces.ColumnStacks(24, self.white_pawn_15, self.white_pawn_14)

        all_stack_dict = {
            1: stack_1, 2: stack_2, 3: stack_3, 4: stack_4, 5: stack_5, 6: stack_6, 7: stack_7, 8: stack_8, 9: stack_9,
            10: stack_10, 11: stack_11, 12: stack_12, 13: stack_13, 14: stack_14, 15: stack_15, 16: stack_16,
            17: stack_17,
            18: stack_18, 19: stack_19, 20: stack_20, 21: stack_21, 22: stack_22, 23: stack_23, 24: stack_24
        }

        return all_stack_dict

    def screen_update(self, screen):
        screen.blit(self.black_pawn_1.image, self.black_pawn_1.coordinates)
        screen.blit(self.black_pawn_2.image, self.black_pawn_2.coordinates)
        screen.blit(self.black_pawn_3.image, self.black_pawn_3.coordinates)
        screen.blit(self.black_pawn_4.image, self.black_pawn_4.coordinates)
        screen.blit(self.black_pawn_5.image, self.black_pawn_5.coordinates)
        screen.blit(self.black_pawn_6.image, self.black_pawn_6.coordinates)
        screen.blit(self.black_pawn_7.image, self.black_pawn_7.coordinates)
        screen.blit(self.black_pawn_8.image, self.black_pawn_8.coordinates)
        screen.blit(self.black_pawn_9.image, self.black_pawn_9.coordinates)
        screen.blit(self.black_pawn_10.image, self.black_pawn_10.coordinates)
        screen.blit(self.black_pawn_11.image, self.black_pawn_11.coordinates)
        screen.blit(self.black_pawn_12.image, self.black_pawn_12.coordinates)
        screen.blit(self.black_pawn_13.image, self.black_pawn_13.coordinates)
        screen.blit(self.black_pawn_14.image, self.black_pawn_14.coordinates)
        screen.blit(self.black_pawn_15.image, self.black_pawn_15.coordinates)

        screen.blit(self.white_pawn_1.image, self.white_pawn_1.coordinates)
        screen.blit(self.white_pawn_2.image, self.white_pawn_2.coordinates)
        screen.blit(self.white_pawn_3.image, self.white_pawn_3.coordinates)
        screen.blit(self.white_pawn_4.image, self.white_pawn_4.coordinates)
        screen.blit(self.white_pawn_5.image, self.white_pawn_5.coordinates)
        screen.blit(self.white_pawn_6.image, self.white_pawn_6.coordinates)
        screen.blit(self.white_pawn_7.image, self.white_pawn_7.coordinates)
        screen.blit(self.white_pawn_8.image, self.white_pawn_8.coordinates)
        screen.blit(self.white_pawn_9.image, self.white_pawn_9.coordinates)
        screen.blit(self.white_pawn_10.image, self.white_pawn_10.coordinates)
        screen.blit(self.white_pawn_11.image, self.white_pawn_11.coordinates)
        screen.blit(self.white_pawn_12.image, self.white_pawn_12.coordinates)
        screen.blit(self.white_pawn_13.image, self.white_pawn_13.coordinates)
        screen.blit(self.white_pawn_14.image, self.white_pawn_14.coordinates)
        screen.blit(self.white_pawn_15.image, self.white_pawn_15.coordinates)

