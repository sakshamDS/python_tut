original_string = input("Enter a message to encrypt: ")
encrypted_string = ""  # Initialize encrypted_string

for letter in original_string:
    encrypted_letter = ord(letter) + 3 
    encrypted_string = encrypted_string + chr(encrypted_letter)  # Append encrypted character

print("\nEncrypted message is:", encrypted_string)
