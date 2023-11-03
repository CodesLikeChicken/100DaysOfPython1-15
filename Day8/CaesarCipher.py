direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    if direction == "decode":
        shift = shift * -1
    elif not direction == "encode":
        print("Invalid direction")
        return 
    
    cyphered_text = ""

    first_letter_ord = ord('a')

    for text_index in range(len(text)):
        orig_char_ord = ord(text[text_index])
        original_letter_index = orig_char_ord - first_letter_ord
        new_letter_index = (original_letter_index + shift) % 26
        new_char_ord = new_letter_index + first_letter_ord
        cyphered_text += chr(new_char_ord)

    print(f"The {direction} text is {cyphered_text}")

caesar(text, shift, direction)