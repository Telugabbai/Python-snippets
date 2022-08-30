# from art import logo
# print(logo)

def caesar():

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input(" Enter 'encode' for encryption and 'decode' for decryption ")
    msg = input("Enter the message: ").lower()
    shift = int(input("Enter the shift: "))
    cipher_text = ""
    shift_amount = 0

    if direction == 'encode':
        shift_amount += shift
    elif direction == 'decode':
        shift_amount -= shift
    else:
        print(" Enter valid option")

    for letter in msg:
        msg_char = alphabet.index(letter)
        msg_char += shift_amount
        new_char_pos = alphabet[msg_char]
        cipher_text = cipher_text+new_char_pos
    print(f"Your cipher text is : {cipher_text} ")


caesar()
