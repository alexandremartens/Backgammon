import load_images

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

turn_adv = None
turn_pla = None

player_dice_values = (0, 0)
adversary_dice_values = (0, 0)

# LIST CONTAINS EACH TIME: [destination_stack, piece_name]
white_light_pawns = []
black_light_pawns = []

# LIST OF ALL STACKS THE THE PIECE CAN GO TO
white_possible_dest = []
black_possible_dest = []

# PIECE NAMES THAT ARE HOME
white_home = []
black_home = []

# white_pawn_outside = None
# black_pawn_outside = None
# white_pawn = None
# black_pawn = None
# background_image = None
# inactive_adversary_dice_button = None
# active_adversary_dice_button = None
# inactive_player_dice_button = None
# active_player_dice_button = None
# white_wins = None
# black_wins = None
# dest_light_bottom = None
# dest_light_upper = None
# house_lights_green = None
# blank_player_dice = None
# blank_adversary_dice = None
# white_highlight = None
# black_highlight = None
# player_dice_list = None
# adversary_dice_list = None
#
#
# def load(pygame):
#     global pg, white_pawn_outside, black_pawn_outside, white_pawn, black_pawn, background_image, inactive_adversary_dice_button, active_adversary_dice_button, inactive_player_dice_button, \
#         active_player_dice_button, white_wins, black_wins, dest_light_bottom, dest_light_upper, \
#         house_lights_green, blank_player_dice, blank_adversary_dice, white_highlight, black_highlight, player_dice_list, adversary_dice_list
#
#
#     # import board images:
#     white_pawn_outside, black_pawn_outside, white_pawn, black_pawn, background_image = load_images.board(pygame)
#
#     # import animation images:
#     inactive_adversary_dice_button, active_adversary_dice_button, inactive_player_dice_button, \
#     active_player_dice_button, white_wins, black_wins, dest_light_bottom, dest_light_upper, \
#     house_lights_green, blank_player_dice, blank_adversary_dice, white_highlight, black_highlight \
#         = load_images.animations(pygame)
#
#     # create the dice lists
#     player_dice_list, adversary_dice_list = load_images.dices()
