import pygame as pg
import random

import load_images
import variables
from VisualManagement import *
from variables import *

pg.init()
pg.display.set_caption('Backgammon Project 2')
screen_size = (900, 790)  # a tuple of size (width, height)
screen = pg.display.set_mode(screen_size)

# import board images:
white_pawn_outside, black_pawn_outside, white_pawn, black_pawn, background_image = load_images.board(pg)

# import animation images:
inactive_adversary_dice_button, active_adversary_dice_button, inactive_player_dice_button, \
active_player_dice_button, white_wins, black_wins, dest_light_bottom, dest_light_upper, \
house_lights_green, blank_player_dice, blank_adversary_dice, white_highlight, black_highlight \
    = load_images.animations(pg)

# create the dice lists
player_dice_list, adversary_dice_list = load_images.dices()

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

    variables.player_dice_values = (v1, v2)


def adversary_dice_values():
    v1 = random.randint(1, 6)
    v2 = random.randint(1, 6)

    adversary_dice_1.my_dice = pg.image.load(adversary_dice_list[v1 - 1])
    adversary_dice_2.my_dice = pg.image.load(adversary_dice_list[v2 - 1])

    variables.adversary_dice_values = (v1, v2)


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


# - - - create the middle stack
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

VM = VisualManagement()
all_stacks = VM.init_stacks()  # generate the pieces and put them in a stack

# set pieces that are in home to Home
for k in all_stacks:
    val = all_stacks[k]

    if val.loc <= 6:
        for j in val.pawns:
            if j.id == "white":
                white_home.append(j)

    elif val.loc >= 19:
        for j in val.pawns:
            if j.id == "black":
                black_home.append(j)


# move piece from current stack to another
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

    destination_stack.add_pawn(deleted_piece)  # add the piece to the destination stack
    emplacements.append([destination_stack, deleted_piece])  # add the piece as a new destination possible
    # then push in desired stack


def check_end_turn():
    global player_dice1_moved, player_dice2_moved, white_possible_dest, player_dice_rolled, white_light_pawns, \
        white_light_triggered, turn, black_light_triggered, adversary_dice1_moved, adversary_dice2_moved, \
        black_possible_dest, adversary_dice_rolled, black_light_pawns

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


counter = 0

# MAIN LOOP
while running:

    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    # first, determine which color starts, happens only at the start of the game/once
    if not turn_rolling:
        if counter < 40:  # make a rolling animation by rolling 40 times and then take the last dice score
            turn_adv = random.randint(1, 6)
            adversary_dice_2.my_dice = pg.image.load(adversary_dice_list[turn_adv - 1])

            turn_pla = random.randint(1, 6)
            player_dice_1.my_dice = pg.image.load(player_dice_list[turn_pla - 1])
            counter += 1
        else:
            pg.time.delay(1500)  # let the user see the score of who starts
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
        for k in all_stacks:
            for j in all_stacks[k].pawns:
                if j.id == "white":
                    j.image = white_pawn

    # convert all black pawns (might be lighted or not) to normal black pawns image
    if turn == "adversary":
        for k in all_stacks:
            for j in all_stacks[k].pawns:
                if j.id == "black":
                    j.image = black_pawn

    # if the turn is not completed, turn/keep the lights on
    if white_light_triggered:
        light_white_keys(white_light_pawns)

    # if the turn is not completed, turn/keep the lights on
    if black_light_triggered:
        light_black_keys(black_light_pawns)

    # when the PLAYER/ADVERSARY finishes his turn or no other possible moves
    check_end_turn()

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
                dice_player = variables.player_dice_values

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
                                    if all_stacks[d1] in white_possible_dest:
                                        if len(all_stacks[d1].pawns) == 1 and \
                                                (all_stacks[d1].pawns[0].id == "black"):
                                            move(all_stacks[d1], my_middle_stack)

                                        move(i[0], all_stacks[d1])

                                        if all_stacks[d1].loc <= 6:
                                            if all_stacks[d1].pawns[-1] not in white_home:
                                                white_home.append(all_stacks[d1].pawns[-1])

                                        player_dice_1.my_dice = pg.image.load(blank_player_dice)
                                        player_dice1_moved = True

                                if d1 == 0 and not player_dice1_moved and len(white_home) == 15:
                                    move(i[0], white_pawn_outside_stack)
                                    player_dice1_moved = True
                                    player_dice_1.my_dice = pg.image.load(blank_player_dice)

                        if event.key == pg.K_DOWN:
                            if len(white_home) <= 15:
                                if d2 > 0 and player_dice2_moved == False:
                                    if all_stacks[d2] in white_possible_dest:
                                        if len(all_stacks[d2].pawns) == 1 and \
                                                (all_stacks[d2].pawns[0].id == "black"):
                                            move(all_stacks[d2], my_middle_stack)

                                        move(i[0], all_stacks[d2])

                                        if all_stacks[d2].loc <= 6:
                                            if all_stacks[d2].pawns[-1] not in white_home:
                                                white_home.append(all_stacks[d2].pawns[-1])

                                        player_dice_2.my_dice = pg.image.load(blank_player_dice)
                                        player_dice2_moved = True

                                if d2 == 0 and not player_dice2_moved and len(white_home) == 15:
                                    move(i[0], white_pawn_outside_stack)
                                    player_dice_2.my_dice = pg.image.load(blank_player_dice)
                                    player_dice2_moved = True

        # turn of the adversary
        if turn == "adversary":
            for i in black_light_pawns:
                dice_adversary = variables.adversary_dice_values
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
                                    if all_stacks[d1] in black_possible_dest:
                                        if len(all_stacks[d1].pawns) == 1 and \
                                                (all_stacks[d1].pawns[0].id == "white"):
                                            move(all_stacks[d1], my_middle_stack)

                                        move(i[0], all_stacks[d1])

                                        if all_stacks[d1].loc >= 19:
                                            if all_stacks[d1].pawns[-1] not in black_home:
                                                black_home.append(all_stacks[d1].pawns[-1])

                                        adversary_dice_1.my_dice = pg.image.load(blank_adversary_dice)
                                        adversary_dice1_moved = True

                                if d1 == 25 and not adversary_dice1_moved and len(black_home) == 15:
                                    move(i[0], black_pawn_outside_stack)
                                    adversary_dice1_moved = True
                                    adversary_dice_1.my_dice = pg.image.load(blank_adversary_dice)

                        if event.key == pg.K_DOWN:
                            if len(black_home) <= 15:
                                if d2 < 25 and not adversary_dice2_moved:
                                    if all_stacks[d2] in black_possible_dest:
                                        if len(all_stacks[d2].pawns) == 1 and \
                                                (all_stacks[d2].pawns[0].id == "white"):
                                            move(all_stacks[d2], my_middle_stack)

                                        move(i[0], all_stacks[d2])

                                        if all_stacks[d2].loc >= 19:
                                            if all_stacks[d2].pawns[-1] not in black_home:
                                                black_home.append(all_stacks[d2].pawns[-1])

                                        adversary_dice_2.my_dice = pg.image.load(blank_adversary_dice)
                                        adversary_dice2_moved = True

                                if d2 == 25 and not adversary_dice2_moved and len(black_home) == 15:
                                    move(i[0], black_pawn_outside_stack)
                                    adversary_dice_2.my_dice = pg.image.load(blank_adversary_dice)
                                    adversary_dice2_moved = True

    # update the screen
    VM.screen_update(screen)

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
            for k in all_stacks:
                val = all_stacks[k]

                if len(val.pawns) > 0:
                    light_piece = val.pawns[-1]
                    if light_piece.id == "white":
                        light_pawns.append([val, light_piece])

        white_light_pawns = light_pawns

        # 3: show the possible destinations when clicked on a pawn that's eligible to move
        if player_dice_rolled and len(white_light_pawns) > 0:
            temp_destination = []
            dice_player = variables.player_dice_values

            if len(white_home) <= 15:
                for i in white_light_pawns:
                    if len(my_middle_stack.pawns) > 0 and my_middle_stack.pawns[-1].id == "white":
                        d1, d2 = 25 - (-(i[0].loc - dice_player[0])), 25 - (-(i[0].loc - dice_player[1]))

                    else:
                        d1, d2 = i[0].loc - dice_player[0], i[0].loc - dice_player[1]

                    if d1 > 0 and not player_dice1_moved:
                        if all_stacks[d1].check_if_receiving_light("white") == "on":
                            temp_destination.append(all_stacks[d1])

                    if d1 == 0 and player_dice1_moved == False:
                        if white_pawn_outside_stack.checking_receiving_light("white", white_home, black_home) == "on":
                            temp_destination.append(white_pawn_outside_stack)

                    if d2 > 0 and player_dice2_moved == False:
                        if all_stacks[d2].check_if_receiving_light("white") == "on":
                            temp_destination.append(all_stacks[d2])

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
                            all_stacks[d1].receiving_light("white", screen)

                        if d2 > 0 and not player_dice2_moved:
                            all_stacks[d2].receiving_light("white", screen)

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
            for k in all_stacks:
                val = all_stacks[k]

                if len(val.pawns) > 0:
                    light_piece = val.pawns[-1]
                    if light_piece.id == "black":
                        light_pawns.append([val, light_piece])

        black_light_pawns = light_pawns

        # 3: show the possible destinations when clicked on a pawn that's eligible to move
        if adversary_dice_rolled and len(black_light_pawns) > 0:
            temp_destination = []
            dice_adversary = variables.adversary_dice_values

            if len(black_home) <= 15:
                for i in black_light_pawns:
                    if len(my_middle_stack.pawns) > 0 and my_middle_stack.pawns[-1].id == "black":
                        d1, d2 = -(i[0].loc - dice_adversary[0]), -(i[0].loc - dice_adversary[1])
                    else:
                        d1, d2 = i[0].loc + dice_adversary[0], i[0].loc + dice_adversary[1]

                    if d1 < 25 and not adversary_dice1_moved:
                        if all_stacks[d1].check_if_receiving_light("black") == "on":
                            temp_destination.append(all_stacks[d1])

                    if d1 == 25 and not adversary_dice1_moved:
                        if black_pawn_outside_stack.checking_receiving_light("black", white_home, black_home) == "on":
                            temp_destination.append(black_pawn_outside_stack)

                    if d2 < 25 and not adversary_dice2_moved:
                        if all_stacks[d2].check_if_receiving_light("black") == "on":
                            temp_destination.append(all_stacks[d2])

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
                            all_stacks[d1].receiving_light("black", screen)

                        if d2 < 25 and not adversary_dice2_moved:
                            all_stacks[d2].receiving_light("black", screen)

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
