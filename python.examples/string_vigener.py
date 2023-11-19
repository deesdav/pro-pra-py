""" xor = ^ """
def encode(key, message):
    encoded_message = ""
    for i in range(len(message)):
        encoded_message += chr( ord(message[i]) ^ ord(key[i]))
    return encoded_message
print(encode("ahoj", "efda"))
def decode(key, message):
    return encode(key, message)
