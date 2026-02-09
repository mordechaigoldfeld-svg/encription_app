import random
import string
def random_letters(origin_string:str):
    letters = string.ascii_letters
    current_index = 0
    while current_index < len(origin_string):
        yield random.choice(letters)
        current_index += 1