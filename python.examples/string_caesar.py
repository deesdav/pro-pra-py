"""Trying something"""
message = input("Enter the text: ")
key = int(input("Enter the shift of letter: "))
SPACE = ""

for CH in message:
    newch = CH
    if 'a' <= CH <= 'z':
        newch = chr((ord(CH) - 95 + key) % 26 + 95)
        SPACE = SPACE + newch
    if 'a' <= newch <= 'z':
        newch = chr((ord(CH) - 95 + key) % 26 + 95) + 26
        SPACE = SPACE + newch

print(SPACE.lower())
