# call:     v1 = random.randint(1, 6)
#     v2 = random.randint(1, 6)
#
#     adversary_dice_1.my_dice = pg.image.load(adversary_dice_list[v1 - 1])
#     adversary_dice_2.my_dice = pg.image.load(adversary_dice_list[v2 - 1])
#
#     operations.write_file("{} {}".format(v1, v2), "txt/adversary_dice_values.txt")

def write_file(txt, file_name):
    file = open(file_name, "w")
    file.write(txt)
    file.close()


# call: = operations.read_file("txt/adversary_dice_values.txt")
def read_file(file_name="txt/player_dice_values.txt"):
    file = open(file_name, "r")
    content = file.read().split()
    file.close()

    return int(content[0]), int(content[-1])
