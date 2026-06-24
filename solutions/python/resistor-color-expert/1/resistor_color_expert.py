#THE GUIDES
COLOUR_GUIDE = {"black":0 ,"brown":1 ,"red":2 ,"orange":3 ,"yellow":4 ,"green": 5,"blue": 6,"violet": 7,"grey": 8,"white": 9}

MULTIPLIERS = {3:"kiloohms",6:"megaohms",9:"gigaohms"}

TOLERANCES = {"grey": 0.05,"violet": 0.1,"blue": 0.25,"green": 0.5,"brown": 1, "red": 2,"gold" : 5,"silver" : 10}
   
def resistor_label(colors):
# Value calculation
    
    if len(colors) == 5: 
        value = str(COLOUR_GUIDE[colors[0]]*100 + COLOUR_GUIDE[colors[1]]*10+COLOUR_GUIDE[colors[2]]) + "0"*COLOUR_GUIDE[colors[3]]
    if len(colors) == 4:
        value = str(COLOUR_GUIDE[colors[0]]*10 + COLOUR_GUIDE[colors[1]]) + "0"*COLOUR_GUIDE[colors[2]]
    if len(colors) == 1:
        return f"{COLOUR_GUIDE[colors[0]]} ohms"
        
# Final resistance calculation
    if int(value) > 10**9:
        return f"{value/1000000000} {MULTIPLIERS[9]} ±{TOLERANCES[colors[-1]]}%"
    if int(value) >= 10**6:
        return f"{int(value)/1000000} {MULTIPLIERS[6]} ±{TOLERANCES[colors[-1]]}%"
    if int(value) >= 10**3:
        return f"{int(value)/1000} {MULTIPLIERS[3]} ±{TOLERANCES[colors[-1]]}%" if int(value)%1000 != 0 else  f"{int(value)//1000} {MULTIPLIERS[3]} ±{TOLERANCES[colors[-1]]}%"
    else:
        return f"{value} ohms ±{TOLERANCES[colors[-1]]}%"