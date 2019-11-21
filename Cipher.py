def encrypt(string, shift):
    c = ''
    for char in string:
        if char == ' ':
            c = c + char
        elif char.isupper():
            c = c + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            c = c + chr((ord(char) + shift - 97) % 26 + 97)
    return c

text = input("enter string: ")
s = int(input("enter shift number: "))
print("after encryption: ", encrypt(text, s))

def decrypt(string, shift):
    c = " "
    for char in string:
        if char == ' ':
            c = c + char
        elif char.isupper():
            c = c + chr((ord(char) - shift - 65) % 26 + 65)
        else:
            c = c + chr((ord(char) - shift - 97) % 26 + 97)
    return c

text = input("enter string: ")
s = int(input("enter shift number: "))
print("after decryption: ", decrypt(text, s))