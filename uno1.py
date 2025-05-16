import random
import unofcns

name = input("Enter your name ")
ainames = ["bob","millie","amazeballs"]

randomnames = random.sample(ainames, 3)

names1, names2, names3 = randomnames
name1cards = []
name2cards = []
name3cards = []
name4cards = []
discarded = []
drawn_card = ""
deck = {
    "red": [
        "red zero", "red 1", "red 1", "red 2", "red 2", "red 3", "red 3", "red 4", "red 4",
        "red 5", "red 5", "red 6", "red 6", "red 7", "red 7", "red 8", "red 8", "red 9", "red 9",
        "red skip", "red skip", "red draw 2", "red draw 2", "red reverse", "red reverse"
    ],
    "yellow": [
        "yellow zero", "yellow 1", "yellow 1", "yellow 2", "yellow 2", "yellow 3", "yellow 3", "yellow 4", "yellow 4",
        "yellow 5", "yellow 5", "yellow 6", "yellow 6", "yellow 7", "yellow 7", "yellow 8", "yellow 8", "yellow 9", "yellow 9",
        "yellow skip", "yellow skip", "yellow draw 2", "yellow draw 2", "yellow reverse", "yellow reverse"
    ],
    "green": [
        "green zero", "green 1", "green 1", "green 2", "green 2", "green 3", "green 3", "green 4", "green 4",
        "green 5", "green 5", "green 6", "green 6", "green 7", "green 7", "green 8", "green 8", "green 9", "green 9",
        "green skip", "green skip", "green draw 2", "green draw 2", "green reverse", "green reverse"
    ],
    "blue": [
        "blue zero", "blue 1", "blue 1", "blue 2", "blue 2", "blue 3", "blue 3", "blue 4", "blue 4",
        "blue 5", "blue 5", "blue 6", "blue 6", "blue 7", "blue 7", "blue 8", "blue 8", "blue 9", "blue 9",
        "blue skip", "blue skip", "blue draw 2", "blue draw 2", "blue reverse", "blue reverse"
    ],
    "wild": [
        "wild", "wild", "wild", "wild", "wild draw 4", "wild draw 4", "wild draw 4", "wild draw 4"
    ]
}
x = range(7)
allcards = [card for cards in deck.values() for card in cards]
random.shuffle(allcards)
for i in x:
    name1cards.append(allcards.pop())
    name2cards.append(allcards.pop()) # appending the card as well as popping it at the same time
    name3cards.append(allcards.pop())
    name4cards.append(allcards.pop())
discarded.append(allcards.pop()) # can use the same method for the discarded card since it wont be any of the cards that we just gave out 
                               
order = [names1, names2, names3, name]
random.shuffle(order)

stop = False

hands = {
    names1:  name1cards,
    names2:  name2cards,
    names3:  name3cards,
    name: name4cards
}
current=0
playedcard=""
currentplayer = order[current]
for card in hands[currentplayer]:
        if unofcns.isvalidfirstcard(card):
            hands[order[current]].remove(card)
            discarded.append(card)
            print(f"{currentplayer} drew {card}")
            break
else:
    drawn_card = allcards.pop()
    hands[order[current]].append(drawn_card)
    print(f"{currentplayer} has drawn {drawn_card} from the deck")


while not stop:
    current = (current + 1) % len(order)
    currentplayer = order[current]
    print(f"\n--- {currentplayer}'s turn ---")
    value = None
    for card in hands[currentplayer]:
        topcard = discarded[-1]
        topcolor, topvalue = unofcns.splitcard(topcard)
        current_color = topcolor
        if unofcns.isvalidcard(card,topcard,current_color):
            hands[order[current]].remove(card)
            discarded.append(card)
            played_card = discarded[-1]
            color, value = unofcns.splitcard(played_card)
            print(f"{currentplayer} has drawn {played_card}")
            if unofcns.isspecialcard(value,order,discarded,allcards,hands,current):
                continue
        if len(hands[currentplayer]) == 1:
            print(f"{currentplayer} calls UNO")
        elif len(hands[currentplayer]) == 0:
            print(f"{currentplayer} has WON")
            stop = True
        break

    else:
        if not allcards:
            print("Deck is empty. Reshuffling discard pile...")
            allcards = discarded[:-1]  
            discarded = [discarded[-1]]
            random.shuffle(allcards)

        drawn_card = allcards.pop()
        hands[order[current]].append(drawn_card)
        print(f"{currentplayer} drew {drawn_card}")
        
        current = (current + 1) % len(order)
        continue