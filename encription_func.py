from iter_encription import random_letters
def random_encription(origin_string):
    encrypted_string = ""
    returning_random_letters = random_letters(origin_string)
    for letter in returning_random_letters:
        encrypted_string += letter
    return encrypted_string
