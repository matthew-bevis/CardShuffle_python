import random
import sys

selection = 0
cards = []
topOfDeck = 0
def shuffle(cards):
    if topOfDeck == 0:
        print("Deck does not need to be shuffled")
    hearts = 0
    clubs = 0
    spades = 0
    diamonds = 0
    while len(cards) != 52:
        while hearts != 14:
            hearts += 1
            if hearts == 1:
                cards.append("ace hearts")
            elif hearts > 1 and hearts < 11:
                cards.append(str(hearts) + " hearts")
            elif hearts == 11:
                cards.append("jack hearts")
            elif hearts == 12:
                cards.append("queen hearts")
            elif hearts == 13:
                cards.append("king hearts")
        while clubs != 14:
            clubs += 1
            if clubs == 1:
                cards.append("ace clubs")
            elif clubs > 1 and clubs < 11:
                cards.append(str(clubs) + " clubs")
            elif clubs == 11:
                cards.append("jack clubs")
            elif clubs == 12:
                cards.append("queen clubs")
            elif clubs == 13:
                cards.append("king clubs")
        while spades != 14:
            spades += 1
            if spades == 1:
                cards.append("ace spades")
            elif spades > 1 and spades < 11:
                cards.append(str(spades) + " spades")
            elif spades == 11:
                cards.append("jack spades")
            elif spades == 12:
                cards.append("queen spades")
            elif spades == 13:
                cards.append("king spades")
        while diamonds != 14:
            diamonds += 1
            if diamonds == 1:
                cards.append("ace diamonds")
            elif diamonds > 1 and diamonds < 11:
                cards.append(str(diamonds) + " diamonds")
            elif diamonds == 11:
                cards.append("jack diamonds")
            elif diamonds == 12:
                cards.append("queen diamonds")
            elif diamonds == 13:
                cards.append("king diamonds")
        random.shuffle(cards)
        return cards
shuffle(cards)
print("Menu:\n1: quit\n2: reshuffle\n3: draw a card")
while selection != 1:
    try:
        selection = int(input())
        if selection > 3 or selection < 1:
            raise Exception("integer not within accepted range")
    except:
        print("integer not within accepted range")
    if selection == 2:
        print("Reshuffling...")
        shuffle(cards)
        random.shuffle(cards)
        topOfDeck = 0
        print("Reshuffling complete")
    elif selection == 3:
        print("drawing a card")
        try:
            print(cards[topOfDeck])
        except:
            print("No more cards in deck")
        topOfDeck += 1
print("Thanks for playing!")
sys.exit()
