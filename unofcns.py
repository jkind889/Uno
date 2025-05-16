def splitcard(card):
    if not card or not isinstance(card, str):
        return "Wild", "Wild"
    
    parts = card.strip().split(" ", 1)
    if len(parts) == 2:
        return parts[0], parts[1]
    elif len(parts) == 1:
        return parts[0], ""  # e.g., for just "Wild"
    else:
        return "Wild", "Wild"

    
def isvalidcard(card,topcard,currentcolor):
    color, value = splitcard(card)
    topcolor, topvalue = splitcard(topcard)
    return (
        color == currentcolor or
        value == topvalue or
        color == "Wild" 
    )
    

def isvalidfirstcard(card):
    color,value = splitcard(card)
    return value.isdigit()