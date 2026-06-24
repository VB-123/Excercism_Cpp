def is_isogram(string):
    for character in string:
        if character.isalpha() and string.lower().count(character) > 1:
            return False
    return True