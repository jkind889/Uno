import random

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

def isspecialcard(value,order,discarded,allcards,hands,current):
            if value == "skip":
                current = (current + 1) % len(order)
            elif value == "reverse":
                order.reverse()
                current = (len(order)-current) % len(order)
            elif value == "draw 2":
                nextplayer = (current +1) % len(order)
                for i in range(2):
                    if not allcards:
                        print("Deck is empty. Reshuffling discard pile...")
                        allcards = discarded[:-1]  # Keep top card in play
                        discarded = [discarded[-1]]
                        random.shuffle(allcards)
                    hands[order[nextplayer]].append(allcards.pop())
            elif value == "draw 4":
                nextplayer = (current +1) % len(order)
                for i in range(4):
                    if not allcards:
                        print("Deck is empty. Reshuffling discard pile...")
                        allcards = discarded[:-1]  # Keep top card in play
                        discarded = [discarded[-1]]
                        random.shuffle(allcards)
                    hands[order[nextplayer]].append(allcards.pop())
                chosencolor = input("What color do you select from Red,Blue,Yellow,Green")
                return current, order, chosencolor
            elif value == "wild":
                chosencolor = input("What color do you select from Red,Blue,Yellow,Green")
                return current, order, chosencolor
    
            return current,order, None