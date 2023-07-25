def enkrypt(msg, key):
    key = int(key)
    res = ""
    for i in msg:
        res += chr((ord(i)+key)%128)

    return res

def decrypt(msg, key):
    key = int(key)
    res = ""
    for i in msg:
        res += chr((ord(i)-key+128)%128)

    return res

