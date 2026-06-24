def leap_year(year):
    """Check if a given year is a leap year or not.
    
        :param year: int - The year to be checked
        :return: bool - Whether the year is a leap year or not.
    """
    if year % 4 == 0:
        return True if year % 400 == 0 or year % 100 != 0 else False
    return False
