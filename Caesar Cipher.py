# This is a program that will encode or decode a message with a Caesar cipher

text = raw_input("Enter your message: ")
otext = "" # blank string for encoded or decoded message
mode = input("Do you want to: 1 (encode) or 2 (decode)? ")
key = input("What is the key? ")

# makes key negative so it decodes
if mode == 2:
    key = key * -1

for char in text:
    
    # for uppercase letters
    if char.isupper():
        x = ord(char)
        x = (x - 65 + key) % 26 + 65
    # for lowercase letters
    elif char.islower():
        x = ord(char)
        x = (x - 97 + key) % 26 + 97
    # for non-letter characters
    else:
        x = ord(char)
    otext = otext + chr(x)
print "The new text is: " + otext