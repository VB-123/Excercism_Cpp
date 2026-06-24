COLOUR_GUIDE = {"black":0 ,"brown":1 ,"red":2 ,"orange":3 ,"yellow":4 ,"green": 5,"blue": 6,"violet": 7,"grey": 8,"white": 9}
def label(colors):
    exponents = {3:"kiloohms",6:"megaohms",9:"gigaohms"}
    value = str(COLOUR_GUIDE[colors[0]]*10 + COLOUR_GUIDE[colors[1]]) + "0"*COLOUR_GUIDE[colors[2]]
    if value.count('0') >= 9:
        return f"{value[:-9]} {exponents[9]}"
    if value.count('0') >= 6:
        return f"{value[:-6]} {exponents[6]}"
    if value.count('0') >= 3:
        return f"{value[:-3]} {exponents[3]}"
    else:
        return f"{value} ohms"
    
    
