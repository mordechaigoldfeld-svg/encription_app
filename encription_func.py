def caesar_cipher_gen(text , shift_key):

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    shift_logic = lambda final_index: letters[final_index] 

    for char in text.lower():
        if char in letters:
          new_index = letters.index(char) + shift_key

          while new_index > 25:
                new_index -= 26

          while new_index < 0:
                new_index += 26

          yield shift_logic(new_index)
        else:
            yield char
            
user_text = input("Enter text: ")
user_shift = int(input("Enter shift: "))


result = [c for c in caesar_cipher_gen(user_text, user_shift)]
print("Encrypted:", "".join(result))