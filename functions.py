def encryption(original_string):
    encrypted_string = ""  # Initialize encrypted_string

    for letter in original_string:
        encrypted_letter = ord(letter) + 3  # Shift the letter by 3
        encrypted_string += chr(encrypted_letter)  # Convert back to character

    print("\nEncrypted message is:", encrypted_string)
    return encrypted_string

# Example call to the function
encryption("SAKSHAM")
