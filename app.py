# Dictionary Representing Morse Code Chart
# Reference: https://en.wikipedia.org/wiki/Morse_code

DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.','H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}

def encrypt(message):
    """Encrypts a message into Morse Code"""
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += DICT[letter] + ' '
        else:
            cipher += ' '
    return cipher

def decrypt (message):
    """Decrypts a message from Morse Code"""
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(DICT.keys())[list(DICT.values()).index(citext)]
                citext = ''
    return decipher
    
def main():
    """Main Function"""""
    message = input("Enter Message: ")
    result = encrypt(message.upper())
    print(result)
    result = decrypt(result)
    print(result)

if __name__ == '__main__':
    """Run the main function"""
    main()
        
    