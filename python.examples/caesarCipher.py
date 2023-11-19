def encode(key, text):
    space = ""
    for i in text:
        space += chr((ord(i) - 65 + key) % 26 + 65)
    return space
def decode(key, text):
    return encode(-key, text)

print(encode(1, "AZB".upper()))
