direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift):
    
    encoded_text = ""

    first_letter_ord = ord('a')

    for text_index in range(len(plain_text)):
        orig_char_ord = ord(plain_text[text_index])
        original_letter_index = orig_char_ord - first_letter_ord
        new_letter_index = (original_letter_index + shift) % 26
        new_char_ord = new_letter_index + first_letter_ord
        encoded_text += chr(new_char_ord)

    print(f"The encoded text is {encoded_text}")

def decrypt(encoded_text, shift):
    
    plain_text = ""

    first_letter_ord = ord('a')

    for text_index in range(len(encoded_text)):
        orig_char_ord = ord(encoded_text[text_index])
        original_letter_index = orig_char_ord - first_letter_ord
        new_letter_index = (original_letter_index - shift) % 26
        new_char_ord = new_letter_index + first_letter_ord
        plain_text += chr(new_char_ord)

    print(f"The encoded text is {plain_text}")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Invalid direction")
