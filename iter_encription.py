def  ger_fence_cipher(user):
    index=0
    even=''
    odd=''
    while len(user)>index:
        if index %2==0:
           even+= user[index]
           index+=1
        else:
            odd+= user[index]
            index+=1
    result=even+odd
    return result
