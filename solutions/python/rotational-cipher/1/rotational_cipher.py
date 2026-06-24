def rotate(text, key):
    """Returns Rotational Cipher text
    :param text : str - The text to encoded.
    :param key : int - The number of values to be shifted."""
    cipher_text = ""
    for char in text:
        # Shifts the character by 'key' and converts it back to ASCII
        if char.isupper():
            cipher_text += chr((ord(char) - 65 + key)%26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) - 97 + key)%26 + 97)
        else:
            cipher_text += char
    return cipher_text
