def write_file(txt, file_name):
    file = open(file_name, "w")
    file.write(txt)
    file.close()


def read_file(file_name="txt/player_dice_values.txt"):
    file = open(file_name, "r")
    content = file.read().split()
    file.close()

    return int(content[0]), int(content[-1])
