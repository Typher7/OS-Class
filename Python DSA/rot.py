def encrypt_string(text):
    encrypted = ""
    step = 1
    for c in text:
        if c.isalpha():
            if c.isupper():
                encrypted += (chr(64 + step + (ord(c) - 64) % 26))
            else:
                encrypted += (chr(96 + step + (ord(c) - 96) % 26)) 
        else:
            encrypted += c
        # TODO: Check if `c` is a letter different from 'z' and 'Z'. If so, increment by 1.
        # If 'c' is 'z', change it to 'a'. If 'c' is 'Z', change it to 'A'.
        # Otherwise, keep 'c' unchanged and add it to the encrypted list.
    return ''.join(encrypted)

# Encrypt the string "Hello, Python!" by shifting each letter in the alphabet one by one.
encrypted_text = encrypt_string("Hello, Python!")
print("The encrypted text is:", encrypted_text) # Should print out "Ifmmp, Qzuipo!"