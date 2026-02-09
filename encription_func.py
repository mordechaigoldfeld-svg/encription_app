from iter_encription import gen_atbash
def atbash_cipher(string):
    chiper_string = ""
    genertor = gen_atbash(string)
    for char in genertor:
        chiper_string += char
    return chiper_string
