def encrypt_string(text):
    encrypted = ""
    shift = 1
    for char in text:
        if char.isalpha():
            encrypted += chr(64 + (ord(char) - 64 + shift) % 26) if char.isupper() else chr(96 + (ord(char) - 96 + shift) % 26)
        else:
            encrypted += char
        # TODO: Check if `c` is a letter different from 'z' and 'Z'. If so, increment by 1.
        # If 'c' is 'z', change it to 'a'. If 'c' is 'Z', change it to 'A'.
        # Otherwise, keep 'c' unchanged and add it to the encrypted list.
    return ''.join(encrypted)

# Encrypt the string "Hello, Python!" by shifting each letter in the alphabet one by one.
encrypted_text = encrypt_string("Hello, Python!")
print("The encrypted text is:", encrypted_text) # Should print out "Ifmmp, Qzuipo!"

