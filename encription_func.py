from iter_encription import ger_fence_cipher


def fence(user):
    userx = user.replace(' ', '')
    encript=''
    g_fence=ger_fence_cipher(userx)
    for item in g_fence:
        encript+=item
    return encript

print(fence(user))