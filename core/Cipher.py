
def caesar():

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input(" Enter 'encode' for encryption and 'decode' for decryption ")
    msg = input("Enter the message: ").lower()
    shift = int(input("Enter the shift: "))

    cipher_text = ""
    if direction == 'encode':
        for letter in msg:
            msg_char = alphabet.index(letter)
            msg_char += shift
            new_char_pos = alphabet[msg_char]
            cipher_text = cipher_text+new_char_pos
        print(f"Your Encoded cipher text is : {cipher_text} ")
    elif direction == 'decode':
        for letter in msg:
            msg_char = alphabet.index(letter)
            msg_char -= shift
            new_char_pos = alphabet[msg_char]
            cipher_text = cipher_text+new_char_pos
        print(f"Your Decoded cipher text is : {cipher_text} ")
    else:
        print(" Enter valid option")