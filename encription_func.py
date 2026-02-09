from iter_encription import gen_atbash
from iter_encription import random_letters
def random_encription(origin_string):
    encrypted_string = ""
    returning_random_letters = random_letters(origin_string)
    for letter in returning_random_letters:
        encrypted_string += letter
    return encrypted_string

def atbash_cipher(string):
    chiper_string = ""
    genertor = gen_atbash(string)
    for char in genertor:
        chiper_string += char
    return chiper_string
