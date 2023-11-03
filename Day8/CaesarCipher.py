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
    last_letter_ord = ord('z')
    num_of_letters = last_letter_ord - first_letter_ord

    for text_index in range(len(text)):
        orig_char_ord = ord(text[text_index])

        if orig_char_ord < first_letter_ord or orig_char_ord > last_letter_ord:
            cyphered_text += chr(orig_char_ord)
            continue

        original_letter_index = orig_char_ord - first_letter_ord
        new_letter_index = (original_letter_index + shift) % num_of_letters
        new_char_ord = new_letter_index + first_letter_ord
        cyphered_text += chr(new_char_ord)

    print(f"The {direction} text is {cyphered_text}")

caesar(text, shift, direction)