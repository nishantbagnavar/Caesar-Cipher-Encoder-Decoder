# Define the alphabet including repetitions for wrapping around
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(start_text, shift_amount, start_direction):
    """
    Encrypts or decrypts a text using the Caesar cipher algorithm.

    Parameters:
    start_text (str): The text to be encrypted or decrypted.
    shift_amount (int): The number of positions each letter should be shifted.
    start_direction (str): The direction of the operation ('encode' or 'decode').

    Returns:
    None: Prints the result directly.
    """
    end_text = ""
    if start_direction == "decode":
        shift_amount *= -1  # Reverse the shift for decoding

    for i in start_text:
        if i in alphabet:
            position = alphabet.index(i)  # Find the current position of the letter
            new_position = position + shift_amount  # Calculate the new position
            end_text += alphabet[new_position]  # Append the new letter to the result
        else:
            end_text += i  # Non-alphabet characters remain unchanged
    
    print(f"Here's the {start_direction}d text as {end_text}")

# Loop to allow multiple encodings/decodings
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()  # Convert to lowercase for uniformity
    shift = int(input("Type the shift number:\n"))
    shift %= 26  # Ensure shift number is within 0-25
    ceaser(start_text=text, shift_amount=shift, start_direction=direction)

    ask = input("Do you want to continue (yes/no)? ").lower()
    if ask != "yes":
        should_continue = False
        print("See you soon!!")
