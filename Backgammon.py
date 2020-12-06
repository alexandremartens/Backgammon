import pygame as pg
import random

import Pieces

pg.init()
pg.display.set_caption('Backgammon Project 2')

# LOAD ALL FILES:
inactive_player_dice_button = pg.image.load("img/inactive_player_dice_button.png")
active_player_dice_button = pg.image.load("img/active_player_dice_button.png")

inactive_adversary_dice_button = pg.image.load("img/inactive_adversary_dice_button.png")
active_adversary_dice_button = pg.image.load("img/active_adversary_dice_button.png")

white_wins = pg.image.load("img/white_wins.png")
black_wins = pg.image.load("img/black_wins.png")

dest_light_bottom = pg.image.load("img/dest_light_bottom.png")
dest_light_upper = pg.image.load("img/dest_light_upper.png")

house_lights_green = pg.image.load("img/house_lights_green.png")

white_pawn_outside = pg.image.load("img/white_pawn_outside.png")
black_pawn_outside = pg.image.load("img/black_pawn_outside.png")

blank_player_dice = "img/blank_player_dice.png"
blank_adversary_dice = "img/blank_adversary_dice.png"

white_pawn = pg.image.load("img/white_pawn.png")
black_pawn = pg.image.load("img/black_pawn.png")

background_image = pg.image.load("img/two_players_back.png")

white_highlight = pg.image.load("img/white_highlight.png")
black_highlight = pg.image.load("img/black_highlight.png")

screen_size = (900, 790)  # a tuple of size (width, height)
screen = pg.display.set_mode(screen_size)

# CREATE THE DICE LISTS
player_dice_list = [
    "img/player_dice1.png",
    "img/player_dice2.png",
    "img/player_dice3.png",
    "img/player_dice4.png",
    "img/player_dice5.png",
    "img/player_dice6.png"
]

adversary_dice_list = [
    "img/adversary_dice1.png",
    "img/adversary_dice2.png",
    "img/adversary_dice3.png",
    "img/adversary_dice4.png",
    "img/adversary_dice5.png",
    "img/adversary_dice6.png"
]

# LIST CONTAINS EACH TIME: [destination_stack, piece_name]
white_light_pawns = []
black_light_pawns = []

# LIST OF ALL STACKS THE THE PIECE CAN GO TO
white_possible_dest = []
black_possible_dest = []

# PIECE NAMES THAT ARE HOME
white_home = []
black_home = []


# ROLL AND SAVE DICE VALUES
def player_dice_values():
    v1 = random.randint(1, 6)
    v2 = random.randint(1, 6)

    player_dice_1.my_dice = pg.image.load(player_dice_list[v1 - 1])
    player_dice_2.my_dice = pg.image.load(player_dice_list[v2 - 1])

    write_file("{} {}".format(v1, v2), "txt/DC.txt")


def adversary_dice_values():
    v1 = random.randint(1, 6)
    v2 = random.randint(1, 6)

    adversary_dice_1.my_dice = pg.image.load(adversary_dice_list[v1 - 1])
    adversary_dice_2.my_dice = pg.image.load(adversary_dice_list[v2 - 1])

    write_file("{} {}".format(v1, v2), "txt/ADC.txt")


def write_file(txt, file_name):
    file = open(file_name, "w")
    file.write(txt)
    file.close()


def read_file(file_name="txt/DC.txt"):
    file = open(file_name, "r")
    content = file.read().split()
    file.close()

    return int(content[0]), int(content[-1])


# KEY HIGHLIGHTING
def light_white_keys(stack_list):
    for i in stack_list:
        i[1].image = white_highlight


def light_black_keys(stack_list):
    for i in stack_list:
        i[1].image = black_highlight


# UPDATE DICE IMAGE
class adversary_dice:
    def __init__(self, pic):
        self.my_dice = pg.image.load(pic)


class player_dice:
    def __init__(self, pic):
        self.my_dice = pg.image.load(pic)


# - - - TODO optimise
my_middle_stack = Pieces.ColumnStacks(0, None)
temp_middle = []
temp_x = 426
temp_y = 340

for i in range(0, 6):
    temp_middle.append((temp_x, temp_y + (i * 56)))

my_middle_stack.positions = temp_middle
# - - -

white_pawn_outside_stack = Pieces.StackMotions(0, "white")
black_pawn_outside_stack = Pieces.StackMotions(0, "black")

# INITIALISE THE PLAYER AND ADVERSARY DICES TO BLANK/EMPTY
player_dice_1 = player_dice(blank_player_dice)
player_dice_2 = player_dice(blank_player_dice)

adversary_dice_1 = adversary_dice(blank_adversary_dice)
adversary_dice_2 = adversary_dice(blank_adversary_dice)

# CREATE ALL PIECES (IMAGES)
black_pawn_1 = Pieces.MyPawns("black")
black_pawn_2 = Pieces.MyPawns("black")
black_pawn_3 = Pieces.MyPawns("black")
black_pawn_4 = Pieces.MyPawns("black")
black_pawn_5 = Pieces.MyPawns("black")
black_pawn_6 = Pieces.MyPawns("black")
black_pawn_7 = Pieces.MyPawns("black")
black_pawn_8 = Pieces.MyPawns("black")
black_pawn_9 = Pieces.MyPawns("black")
black_pawn_10 = Pieces.MyPawns("black")
black_pawn_11 = Pieces.MyPawns("black")
black_pawn_12 = Pieces.MyPawns("black")
black_pawn_13 = Pieces.MyPawns("black")
black_pawn_14 = Pieces.MyPawns("black")
black_pawn_15 = Pieces.MyPawns("black")

white_pawn_1 = Pieces.MyPawns("white")
white_pawn_2 = Pieces.MyPawns("white")
white_pawn_3 = Pieces.MyPawns("white")
white_pawn_4 = Pieces.MyPawns("white")
white_pawn_5 = Pieces.MyPawns("white")
white_pawn_6 = Pieces.MyPawns("white")
white_pawn_7 = Pieces.MyPawns("white")
white_pawn_8 = Pieces.MyPawns("white")
white_pawn_9 = Pieces.MyPawns("white")
white_pawn_10 = Pieces.MyPawns("white")
white_pawn_11 = Pieces.MyPawns("white")
white_pawn_12 = Pieces.MyPawns("white")
white_pawn_13 = Pieces.MyPawns("white")
white_pawn_14 = Pieces.MyPawns("white")
white_pawn_15 = Pieces.MyPawns("white")

# ADD THE PIECES TO counter STACK (COLUMN)
stack_1 = Pieces.ColumnStacks(1, black_pawn_14, black_pawn_15)
stack_2 = Pieces.ColumnStacks(2, None)
stack_3 = Pieces.ColumnStacks(3, None)
stack_4 = Pieces.ColumnStacks(4, None)
stack_5 = Pieces.ColumnStacks(5, None)
stack_6 = Pieces.ColumnStacks(6, white_pawn_1, white_pawn_2, white_pawn_3, white_pawn_4, white_pawn_5)
stack_7 = Pieces.ColumnStacks(7, None)
stack_8 = Pieces.ColumnStacks(8, white_pawn_6, white_pawn_7, white_pawn_8)
stack_9 = Pieces.ColumnStacks(9, None)
stack_10 = Pieces.ColumnStacks(10, None)
stack_11 = Pieces.ColumnStacks(11, None)
stack_12 = Pieces.ColumnStacks(12, black_pawn_9, black_pawn_10, black_pawn_11, black_pawn_12, black_pawn_13)
stack_13 = Pieces.ColumnStacks(13, white_pawn_13, white_pawn_12, white_pawn_11, white_pawn_10, white_pawn_9)
stack_14 = Pieces.ColumnStacks(14, None)
stack_15 = Pieces.ColumnStacks(15, None)
stack_16 = Pieces.ColumnStacks(16, None)
stack_17 = Pieces.ColumnStacks(17, black_pawn_8, black_pawn_7, black_pawn_6)
stack_18 = Pieces.ColumnStacks(18, None)
stack_19 = Pieces.ColumnStacks(19, black_pawn_5, black_pawn_4, black_pawn_3, black_pawn_2, black_pawn_1)
stack_20 = Pieces.ColumnStacks(20, None)
stack_21 = Pieces.ColumnStacks(21, None)
stack_22 = Pieces.ColumnStacks(22, None)
stack_23 = Pieces.ColumnStacks(23, None)
stack_24 = Pieces.ColumnStacks(24, white_pawn_15, white_pawn_14)

# REGROUP ALL STACKS INTO counter LIST
all_stack_list = [
    stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9, stack_10, stack_11, stack_12,
    stack_13, stack_14, stack_15, stack_16, stack_17, stack_18, stack_19, stack_20, stack_21, stack_22, stack_23,
    stack_24
]

# REGROUP ALL STACKS INTO counter DICTIONARY
all_stack_dict = {
    1: stack_1, 2: stack_2, 3: stack_3, 4: stack_4, 5: stack_5, 6: stack_6, 7: stack_7, 8: stack_8, 9: stack_9,
    10: stack_10, 11: stack_11, 12: stack_12, 13: stack_13, 14: stack_14, 15: stack_15, 16: stack_16, 17: stack_17,
    18: stack_18, 19: stack_19, 20: stack_20, 21: stack_21, 22: stack_22, 23: stack_23, 24: stack_24
}


# MOVE PIECE FROM counter STACK TO ANOTHER
def move(current_stack, destination_stack):  # TODO RECHECK param type

    # pop from the current stack
    deleted_piece = current_stack.remove_pawn()

    if turn == "player":
        emplacements = white_light_pawns
    else:
        emplacements = black_light_pawns

    # if the deleted piece name is in the highlighted list, delete it from the list
    for i in emplacements:  # emplacements format: [destination_stack, piece_name]
        if i[1] == deleted_piece:
            del i

    destination_stack.add_pawn(deleted_piece)  # ad the piece to the destination stack
    emplacements.append([destination_stack, deleted_piece])  # add the piece as a new destination possible
    # then push in desired stack


player_dice1_moved = False
player_dice2_moved = False
adversary_dice1_moved = False
adversary_dice2_moved = False

white_light_triggered = False
black_light_triggered = False
adversary_dice_rolled = False

turn = None
turn_rolling = False
player_dice_rolled = False
winner_declared = False
running = True

# set pieces that are in home to Home

for i in all_stack_list:
    if i.loc <= 6:
        for j in i.pawns:
            if j.id == "white":
                white_home.append(j)

    elif i.loc >= 19:
        for j in i.pawns:
            if j.id == "black":
                black_home.append(j)

counter = 0
turn_adv = None
turn_pla = None

# MAIN LOOP
while running:

    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    # first, determine which color starts
    if not turn_rolling:
        if counter < 40:  # make a rolling animation by rolling 40 times and then take the last dice score
            turn_adv = random.randint(1, 6)
            adversary_dice_2.my_dice = pg.image.load(adversary_dice_list[turn_adv - 1])

            turn_pla = random.randint(1, 6)
            player_dice_1.my_dice = pg.image.load(player_dice_list[turn_pla - 1])
            counter += 1
        else:
            pg.time.delay(2000)  # let the user see the score of who starts
            if turn_adv != turn_pla:
                if turn_adv > turn_pla:
                    turn = "adversary"

                elif turn_adv < turn_pla:
                    turn = "player"

                player_dice_1.my_dice = pg.image.load(blank_player_dice)
                adversary_dice_2.my_dice = pg.image.load(blank_adversary_dice)

                turn_rolling = True
                counter = 0
            else:  # if dices are the same, start the rolling animation again...
                counter = 0
                turn_rolling = False

    # convert all white pawns (might be lighted or not) to normal white pawns
    if turn == "player":
        for i in all_stack_list:
            for j in i.pawns:
                if j.id == "white":
                    j.image = white_pawn

    # convert all black pawns (might be lighted or not) to normal black pawns image
    if turn == "adversary":
        for i in all_stack_list:
            for j in i.pawns:
                if j.id == "black":
                    j.image = black_pawn

    # if the turn is not completed, turn/keep the lights on
    if white_light_triggered:
        light_white_keys(white_light_pawns)

    # if the turn is not completed, turn/keep the lights on
    if black_light_triggered:
        light_black_keys(black_light_pawns)

    # when the PLAYER finishes his turn or no other possible moves TODO p3: recheck condition but should be fine
    if (player_dice1_moved and player_dice2_moved) or \
            ((len(white_possible_dest) == 0) and (player_dice_rolled and
                                                  ((player_dice1_moved == player_dice2_moved == False) or
                                                   player_dice1_moved or player_dice2_moved))):
        player_dice1_moved = False
        player_dice2_moved = False
        white_light_triggered = False

        player_dice_rolled = False
        player_dice_1.my_dice = pg.image.load(blank_player_dice)
        player_dice_2.my_dice = pg.image.load(blank_player_dice)

        for i in white_light_pawns:
            i[1].image = white_pawn

        white_light_pawns = []
        white_possible_dest = []
        turn = "adversary"

    # when the ADVERSARY finishes his turn or no other possible moves TODO p3: recheck condition but should be fine
    if (adversary_dice1_moved and adversary_dice2_moved) or \
            ((len(black_possible_dest) == 0) and (adversary_dice_rolled and
                                                  ((adversary_dice1_moved == adversary_dice2_moved == False) or
                                                   adversary_dice1_moved or adversary_dice2_moved))):
        adversary_dice_rolled = False
        adversary_dice1_moved = False
        adversary_dice2_moved = False
        black_light_triggered = False

        adversary_dice_1.my_dice = pg.image.load(blank_adversary_dice)
        adversary_dice_2.my_dice = pg.image.load(blank_adversary_dice)

        for i in black_light_pawns:
            i[1].image = black_pawn

        black_light_pawns = []
        black_possible_dest = []
        turn = "player"

    screen.fill((0, 0, 0))  # add a black layer behind the background image
    screen.blit(background_image, (0, 0))  # background image on top of the filled black screen

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                pass

        if event.type == pg.MOUSEBUTTONUP and turn == "player" and 840 <= mouse[0] <= 885 and 330 <= mouse[1] <= 450:
            if event.button == 1:
                light_white_keys(white_light_pawns)
                player_dice_rolled = True
                white_light_triggered = True

        if event.type == pg.MOUSEBUTTONUP and turn == "adversary" and 3 <= mouse[0] <= 48 and 310 <= mouse[1] <= 430:
            if event.button == 1:
                light_black_keys(black_light_pawns)
                adversary_dice_rolled = True
                black_light_triggered = True

        # turn of the player
        if turn == "player":
            for i in white_light_pawns:
                dice_player = read_file()

                if event.type == pg.KEYDOWN and (event.key == pg.K_UP or event.key == pg.K_DOWN) and player_dice_rolled:
                    if len(my_middle_stack.pawns) > 0 and my_middle_stack.pawns[-1].id == "white":
                        d1, d2 = 25 - (-(i[0].loc - dice_player[0])), 25 - (-(i[0].loc - dice_player[1]))
                    else:
                        d1, d2 = i[0].loc - dice_player[0], i[0].loc - dice_player[1]
                    if click[0] == 1 and i[1].coordinates[0] <= mouse[0] <= i[1].coordinates[0] + 56 and \
                            i[1].coordinates[1] <= mouse[1] <= i[1].coordinates[1] + 56:
                        if event.key == pg.K_UP:
                            if len(white_home) <= 15:
                                if d1 > 0 and not player_dice1_moved:
                                    if all_stack_dict[d1] in white_possible_dest:
                                        if len(all_stack_dict[d1].pawns) == 1 and \
                                                (all_stack_dict[d1].pawns[0].id == "black"):
                                            move(all_stack_dict[d1], my_middle_stack)

                                        move(i[0], all_stack_dict[d1])

                                        if all_stack_dict[d1].loc <= 6:
                                            if all_stack_dict[d1].pawns[-1] not in white_home:
                                                white_home.append(all_stack_dict[d1].pawns[-1])

                                        player_dice_1.my_dice = pg.image.load(blank_player_dice)
                                        player_dice1_moved = True

                                if d1 == 0 and not player_dice1_moved and len(white_home) == 15:
                                    move(i[0], white_pawn_outside_stack)
                                    player_dice1_moved = True
                                    player_dice_1.my_dice = pg.image.load(blank_player_dice)

                        if event.key == pg.K_DOWN:
                            if len(white_home) <= 15:
                                if d2 > 0 and player_dice2_moved == False:
                                    if all_stack_dict[d2] in white_possible_dest:
                                        if len(all_stack_dict[d2].pawns) == 1 and \
                                                (all_stack_dict[d2].pawns[0].id == "black"):
                                            move(all_stack_dict[d2], my_middle_stack)

                                        move(i[0], all_stack_dict[d2])

                                        if all_stack_dict[d2].loc <= 6:
                                            if all_stack_dict[d2].pawns[-1] not in white_home:
                                                white_home.append(all_stack_dict[d2].pawns[-1])

                                        player_dice_2.my_dice = pg.image.load(blank_player_dice)
                                        player_dice2_moved = True

                                if d2 == 0 and not player_dice2_moved and len(white_home) == 15:
                                    move(i[0], white_pawn_outside_stack)
                                    player_dice_2.my_dice = pg.image.load(blank_player_dice)
                                    player_dice2_moved = True

        # turn of the adversary
        if turn == "adversary":
            for i in black_light_pawns:
                dice_adversary = read_file("txt/ADC.txt")
                if event.type == pg.KEYDOWN and (event.key == pg.K_UP or event.key == pg.K_DOWN) and \
                        adversary_dice_rolled:
                    if len(my_middle_stack.pawns) > 0 and my_middle_stack.pawns[-1].id == "black":
                        d1, d2 = -(i[0].loc - dice_adversary[0]), -(i[0].loc - dice_adversary[1])

                    else:
                        d1, d2 = i[0].loc + dice_adversary[0], i[0].loc + dice_adversary[1]

                    if click[0] == 1 and i[1].coordinates[0] <= mouse[0] <= i[1].coordinates[0] + 56 and \
                            i[1].coordinates[1] <= mouse[1] <= i[1].coordinates[1] + 56:
                        if event.key == pg.K_UP:
                            if len(black_home) <= 15:
                                if d1 < 25 and not adversary_dice1_moved:
                                    if all_stack_dict[d1] in black_possible_dest:
                                        if len(all_stack_dict[d1].pawns) == 1 and \
                                                (all_stack_dict[d1].pawns[0].id == "white"):
                                            move(all_stack_dict[d1], my_middle_stack)

                                        move(i[0], all_stack_dict[d1])

                                        if all_stack_dict[d1].loc >= 19:
                                            if all_stack_dict[d1].pawns[-1] not in black_home:
                                                black_home.append(all_stack_dict[d1].pawns[-1])

                                        adversary_dice_1.my_dice = pg.image.load(blank_adversary_dice)
                                        adversary_dice1_moved = True

                                if d1 == 25 and not adversary_dice1_moved and len(black_home) == 15:
                                    move(i[0], black_pawn_outside_stack)
                                    adversary_dice1_moved = True
                                    adversary_dice_1.my_dice = pg.image.load(blank_adversary_dice)

                        if event.key == pg.K_DOWN:
                            if len(black_home) <= 15:
                                if d2 < 25 and not adversary_dice2_moved:
                                    if all_stack_dict[d2] in black_possible_dest:
                                        if len(all_stack_dict[d2].pawns) == 1 and \
                                                (all_stack_dict[d2].pawns[0].id == "white"):
                                            move(all_stack_dict[d2], my_middle_stack)

                                        move(i[0], all_stack_dict[d2])

                                        if all_stack_dict[d2].loc >= 19:
                                            if all_stack_dict[d2].pawns[-1] not in black_home:
                                                black_home.append(all_stack_dict[d2].pawns[-1])

                                        adversary_dice_2.my_dice = pg.image.load(blank_adversary_dice)
                                        adversary_dice2_moved = True

                                if d2 == 25 and not adversary_dice2_moved and len(black_home) == 15:
                                    move(i[0], black_pawn_outside_stack)
                                    adversary_dice_2.my_dice = pg.image.load(blank_adversary_dice)
                                    adversary_dice2_moved = True

    # update the screen
    screen.blit(black_pawn_1.image, black_pawn_1.coordinates)
    screen.blit(black_pawn_2.image, black_pawn_2.coordinates)
    screen.blit(black_pawn_3.image, black_pawn_3.coordinates)
    screen.blit(black_pawn_4.image, black_pawn_4.coordinates)
    screen.blit(black_pawn_5.image, black_pawn_5.coordinates)
    screen.blit(black_pawn_6.image, black_pawn_6.coordinates)
    screen.blit(black_pawn_7.image, black_pawn_7.coordinates)
    screen.blit(black_pawn_8.image, black_pawn_8.coordinates)
    screen.blit(black_pawn_9.image, black_pawn_9.coordinates)
    screen.blit(black_pawn_10.image, black_pawn_10.coordinates)
    screen.blit(black_pawn_11.image, black_pawn_11.coordinates)
    screen.blit(black_pawn_12.image, black_pawn_12.coordinates)
    screen.blit(black_pawn_13.image, black_pawn_13.coordinates)
    screen.blit(black_pawn_14.image, black_pawn_14.coordinates)
    screen.blit(black_pawn_15.image, black_pawn_15.coordinates)

    screen.blit(white_pawn_1.image, white_pawn_1.coordinates)
    screen.blit(white_pawn_2.image, white_pawn_2.coordinates)
    screen.blit(white_pawn_3.image, white_pawn_3.coordinates)
    screen.blit(white_pawn_4.image, white_pawn_4.coordinates)
    screen.blit(white_pawn_5.image, white_pawn_5.coordinates)
    screen.blit(white_pawn_6.image, white_pawn_6.coordinates)
    screen.blit(white_pawn_7.image, white_pawn_7.coordinates)
    screen.blit(white_pawn_8.image, white_pawn_8.coordinates)
    screen.blit(white_pawn_9.image, white_pawn_9.coordinates)
    screen.blit(white_pawn_10.image, white_pawn_10.coordinates)
    screen.blit(white_pawn_11.image, white_pawn_11.coordinates)
    screen.blit(white_pawn_12.image, white_pawn_12.coordinates)
    screen.blit(white_pawn_13.image, white_pawn_13.coordinates)
    screen.blit(white_pawn_14.image, white_pawn_14.coordinates)
    screen.blit(white_pawn_15.image, white_pawn_15.coordinates)

    # turn of the player
    if turn == "player":
        # 1: roll dice
        if not player_dice_rolled:
            if 840 <= mouse[0] <= 885 and 330 <= mouse[1] <= 450:
                screen.blit(active_player_dice_button, (840, 330))

                if click[0] == 1:
                    player_dice_values()
            else:
                screen.blit(inactive_player_dice_button, (840, 330))

        # 2: light pawns that are eligible to move
        light_pawns = []

        if len(my_middle_stack.pawns) > 0 and my_middle_stack.pawns[-1].id == "white":
            for i in my_middle_stack.pawns:
                if i.id == "white":
                    light_pawns.append([my_middle_stack, i])
        else:
            for i in all_stack_list:
                if len(i.pawns) > 0:
                    light_piece = i.pawns[-1]
                    if light_piece.id == "white":
                        light_pawns.append([i, light_piece])

        white_light_pawns = light_pawns

        # 3: show the possible destinations when clicked on a pawn that's eligible to move
        if player_dice_rolled and len(white_light_pawns) > 0:
            temp_destination = []
            dice_player = read_file()

            if len(white_home) <= 15:
                for i in white_light_pawns:
                    if len(my_middle_stack.pawns) > 0 and my_middle_stack.pawns[-1].id == "white":
                        d1, d2 = 25 - (-(i[0].loc - dice_player[0])), 25 - (-(i[0].loc - dice_player[1]))

                    else:
                        d1, d2 = i[0].loc - dice_player[0], i[0].loc - dice_player[1]

                    if d1 > 0 and not player_dice1_moved:
                        if all_stack_dict[d1].check_if_receiving_light("white") == "on":
                            temp_destination.append(all_stack_dict[d1])

                    if d1 == 0 and player_dice1_moved == False:
                        if white_pawn_outside_stack.checking_receiving_light("white", white_home, black_home) == "on":
                            temp_destination.append(white_pawn_outside_stack)

                    if d2 > 0 and player_dice2_moved == False:
                        if all_stack_dict[d2].check_if_receiving_light("white") == "on":
                            temp_destination.append(all_stack_dict[d2])

                    if d2 == 0 and player_dice2_moved == False:
                        if white_pawn_outside_stack.checking_receiving_light("white", white_home, black_home) == "on":
                            temp_destination.append(white_pawn_outside_stack)

            white_possible_dest = temp_destination

            for i in white_light_pawns:

                if click[0] == 1 and i[1].coordinates[0] <= mouse[0] <= i[1].coordinates[0] + 56 and \
                        i[1].coordinates[1] <= mouse[1] <= i[1].coordinates[1] + 56:
                    if len(my_middle_stack.pawns) > 0 and my_middle_stack.pawns[-1].id == "white":
                        d1, d2 = 25 - (-(i[0].loc - dice_player[0])), 25 - (-(i[0].loc - dice_player[1]))

                    else:
                        d1, d2 = i[0].loc - dice_player[0], i[0].loc - dice_player[1]

                    if len(white_home) <= 15:
                        if d1 > 0 and not player_dice1_moved:
                            all_stack_dict[d1].receiving_light("white", screen)

                        if d2 > 0 and not player_dice2_moved:
                            all_stack_dict[d2].receiving_light("white", screen)

                        if d1 == 0 and not player_dice1_moved:
                            white_pawn_outside_stack.receiving_light("white", screen, white_home, black_home)

                        if d2 == 0 and not player_dice2_moved:
                            white_pawn_outside_stack.receiving_light("white", screen, white_home, black_home)

    # turn of the adversary
    if turn == "adversary":

        # 1: roll dice
        if not adversary_dice_rolled:
            if 3 <= mouse[0] <= 48 and 310 <= mouse[1] <= 430:
                screen.blit(active_adversary_dice_button, (3, 310))

                if click[0] == 1:
                    adversary_dice_values()
            else:
                screen.blit(inactive_adversary_dice_button, (3, 310))

        # 2: light pawns that are eligible to move
        light_pawns = []

        if len(my_middle_stack.pawns) > 0 and my_middle_stack.pawns[-1].id == "black":
            for i in my_middle_stack.pawns:
                if i.id == "black":
                    light_pawns.append([my_middle_stack, i])

        else:
            for i in all_stack_list:
                if len(i.pawns) > 0:
                    light_piece = i.pawns[-1]
                    if light_piece.id == "black":
                        light_pawns.append([i, light_piece])

        black_light_pawns = light_pawns

        # 3: show the possible destinations when clicked on a pawn that's eligible to move
        if adversary_dice_rolled and len(black_light_pawns) > 0:
            temp_destination = []
            dice_adversary = read_file("txt/ADC.txt")

            if len(black_home) <= 15:
                for i in black_light_pawns:
                    if len(my_middle_stack.pawns) > 0 and my_middle_stack.pawns[-1].id == "black":
                        d1, d2 = -(i[0].loc - dice_adversary[0]), -(i[0].loc - dice_adversary[1])
                    else:
                        d1, d2 = i[0].loc + dice_adversary[0], i[0].loc + dice_adversary[1]

                    if d1 < 25 and not adversary_dice1_moved:
                        if all_stack_dict[d1].check_if_receiving_light("black") == "on":
                            temp_destination.append(all_stack_dict[d1])

                    if d1 == 25 and not adversary_dice1_moved:
                        if black_pawn_outside_stack.checking_receiving_light("black", white_home, black_home) == "on":
                            temp_destination.append(black_pawn_outside_stack)

                    if d2 < 25 and not adversary_dice2_moved:
                        if all_stack_dict[d2].check_if_receiving_light("black") == "on":
                            temp_destination.append(all_stack_dict[d2])

                    if d2 == 25 and not adversary_dice2_moved:
                        if black_pawn_outside_stack.checking_receiving_light("black", white_home, black_home) == "on":
                            temp_destination.append(black_pawn_outside_stack)

            black_possible_dest = temp_destination

            for i in black_light_pawns:
                if click[0] == 1 and i[1].coordinates[0] <= mouse[0] <= i[1].coordinates[0] + 56 and \
                        i[1].coordinates[1] <= mouse[1] <= i[1].coordinates[1] + 56:
                    if len(my_middle_stack.pawns) > 0 and my_middle_stack.pawns[-1].id == "black":
                        d1, d2 = -(i[0].loc - dice_adversary[0]), -(i[0].loc - dice_adversary[1])

                    else:
                        d1, d2 = i[0].loc + dice_adversary[0], i[0].loc + dice_adversary[1]

                    if len(black_home) <= 15:
                        if d1 < 25 and not adversary_dice1_moved:
                            all_stack_dict[d1].receiving_light("black", screen)

                        if d2 < 25 and not adversary_dice2_moved:
                            all_stack_dict[d2].receiving_light("black", screen)

                        if d1 == 25 and not adversary_dice1_moved:
                            black_pawn_outside_stack.receiving_light("black", screen, white_home, black_home)

                        if d2 == 25 and not adversary_dice2_moved:
                            black_pawn_outside_stack.receiving_light("black", screen, white_home, black_home)

    screen.blit(player_dice_1.my_dice, (2, 540))
    screen.blit(player_dice_2.my_dice, (2, 610))

    screen.blit(adversary_dice_1.my_dice, (2, 100))
    screen.blit(adversary_dice_2.my_dice, (2, 175))

    if len(white_pawn_outside_stack.elements) == 15:
        winner_declared = True
        screen.blit(white_wins, (0, 0))

    elif len(black_pawn_outside_stack.elements) == 15:
        winner_declared = True
        screen.blit(black_wins, (0, 0))

    if winner_declared and 0 <= mouse[0] <= 900 and 0 <= mouse[1] <= 790 and click[0] == 1:
        pass
        # pg.display.quit() # TODO finetune the end menu
        # sys.exit('end of the game')

    pg.display.update()
