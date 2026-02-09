def gen_atbash(string): 
  abc = [chr(num) for num in range(97,123)]
  current_index = 0
  while current_index < len(string):
    char = string[current_index]
    if char not in abc:
      yield char
    for i in range(len(abc)):
      if abc[i] == char:
        yield abc[25-i] 
    current_index += 1



      



