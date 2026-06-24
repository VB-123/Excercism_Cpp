def is_pangram(sentence):
    for letter in "abcdefghijklmnopqrstuvwxyz":
        result = sentence.lower().find(letter)
        if result == -1:
            return False
    return True
            