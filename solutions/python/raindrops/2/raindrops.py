def convert(number):
    """Convert a number into a string that contains raindrop sounds.
    
    :param number: int 
    :return: str 
    If the given number:
    Has 3 as a factor, add 'Pling' to the result.
    Has 5 as a factor, add 'Plang' to the result.
    Has 7 as a factor, add 'Plong' to the result.
    Does not have any of 3, 5, or 7 as a factor, the result should be the digits.
    """
    result_string = ""
    words = {3:"Pling", 5:"Plang", 7:"Plong"}
    for factor,word in words.items():
        if number % factor == 0:
            result_string += word
    return result_string if result_string else str(number)

    
