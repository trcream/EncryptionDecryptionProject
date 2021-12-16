# Import randrange so that computer can guess encrypted message
from random import randrange
from math import modf

def main():
    try:
        # Input message
        original_message = input("Please put in message: ").lower()

        # Input shift
        shift = int(input("Input shift: "))

        # Create list for alphabet
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        # Convert message into list
        original_message_list = [char for char in original_message]

        # Encrypt message
        encrypt_list = []
        for char in original_message_list:
            x = alphabet.index(char)
       
        # If index is greater than 25, use modulo operator to create new shift
            if (x+shift) > 25:
                new_shift = (x+shift) % 26
                y = alphabet[new_shift]
            else:
                y = alphabet[x+shift]

            encrypt_list.append(y)

        # Store encrypted message here
        encrypted_message= ''.join(char for char in encrypt_list)
        print("Encrypted message: ", encrypted_message)

        # Decrypt using shift
        encrypted_message_list = [char for char in encrypted_message]

        decrypt_list = []
        for char in encrypted_message_list:
            x = alphabet.index(char)
            if (x-shift) < 0:
                new_shift = (x - shift) % 26
                y = alphabet[new_shift]
            else:
                y = alphabet[x-shift]
            decrypt_list.append(y)

        decrypted_message= ''.join(char for char in decrypt_list)
        print("Decrypted message: ", decrypted_message)


    #####################################################################################

        # This is the brute force method

        # Check to see what the length of the message is
        length_of_encrypted = len(encrypted_message)


        brute_force_list = []
        while True:
            for char in range(length_of_encrypted):

            # Assign random index for letter
                x = randrange(0,26)
                y = alphabet[x]
                brute_force_list.append(y)

            # Create random message to see if it matches
            brute_force =''.join(char for char in brute_force_list)
            print(brute_force)
            if brute_force == original_message:
                print("You have successfully decrypted the message")
                print(brute_force)
                break
            else:
                brute_force_list = []

    except:
        print("You either typed in a number into message, negative number into shift, or a word into shift")
        print("Please try again")

if __name__ == "__main__":
    main()