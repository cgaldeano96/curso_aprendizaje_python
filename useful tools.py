import random

pies_en_milla = 5280
metros_en_kilometros = 1000
beatles = ["john", "paul", "george", "ringo"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)
