def animations(pg):
    inactive_player_dice_button = pg.image.load("img/inactive_player_dice_button.png")
    active_player_dice_button = pg.image.load("img/active_player_dice_button.png")

    inactive_adversary_dice_button = pg.image.load("img/inactive_adversary_dice_button.png")
    active_adversary_dice_button = pg.image.load("img/active_adversary_dice_button.png")

    blank_player_dice = "img/blank_player_dice.png"
    blank_adversary_dice = "img/blank_adversary_dice.png"

    white_wins = pg.image.load("img/white_wins.png")
    black_wins = pg.image.load("img/black_wins.png")

    dest_light_bottom = pg.image.load("img/dest_light_bottom.png")
    dest_light_upper = pg.image.load("img/dest_light_upper.png")

    house_lights_green = pg.image.load("img/house_lights_green.png")

    white_highlight = pg.image.load("img/white_highlight.png")
    black_highlight = pg.image.load("img/black_highlight.png")

    return inactive_adversary_dice_button, active_adversary_dice_button, inactive_player_dice_button, \
           active_player_dice_button, white_wins, black_wins, dest_light_bottom, dest_light_upper, \
           house_lights_green, blank_player_dice, blank_adversary_dice, white_highlight, black_highlight


def board(pg):
    white_pawn_outside = pg.image.load("img/white_pawn_outside.png")
    black_pawn_outside = pg.image.load("img/black_pawn_outside.png")

    white_pawn = pg.image.load("img/white_pawn.png")
    black_pawn = pg.image.load("img/black_pawn.png")

    background_image = pg.image.load("img/two_players_back.png")

    return white_pawn_outside, black_pawn_outside, white_pawn, black_pawn, background_image


def dices():
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

    return player_dice_list, adversary_dice_list
