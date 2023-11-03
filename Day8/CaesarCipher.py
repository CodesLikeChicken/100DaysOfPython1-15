direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

def encrypt(text, shift):
    
    encoded_text = ""

    first_letter_ord = ord('a')

    for text_index in range(len(text)):
        orig_char_ord = ord(text[text_index])
        original_letter_index = orig_char_ord - first_letter_ord
        new_letter_index = (original_letter_index + shift) % 26
        new_char_ord = new_letter_index + first_letter_ord
        encoded_text += chr(new_char_ord)

    print(f"The encoded text is {encoded_text}")

encrypt(text, shift)