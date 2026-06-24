import re
def response(hey_bob):
    """Predicts the response of bob, in various conversations.
    
    :param hey_bob: str - The stuff people say to bob.
    :return: str - bob's response.
    """
    if hey_bob.isupper() and hey_bob[-1] == "?":
        return "Calm down, I know what I'm doing!"
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if re.escape(hey_bob) == "" or hey_bob.strip() == "":
        return "Fine. Be that way!"
    if hey_bob.strip()[-1] == "?":
        return "Sure."
    return "Whatever."
