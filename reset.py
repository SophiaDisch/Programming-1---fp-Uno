import random

deck = []
deck.append("0r")
deck.append("0y")
deck.append("0g")
deck.append("0b")
for num in range(1, 3):
  for num in range(1,10):
    deck.append(str(num) + "r") #red cards
    deck.append(str(num) + "y") #yellow cards
    deck.append(str(num) + "g") #green cards
    deck.append(str(num) + "b") #blue cards
  deck.append("draw2R") #draw 2 cards
  deck.append("draw2Y")
  deck.append("draw2G")
  deck.append("draw2B")
  deck.append("revR") #reverse cards
  deck.append("revY")
  deck.append("revG")
  deck.append("revB")
  deck.append("skipR")
  deck.append("skipY")
  deck.append("skipG")
  deck.append("skipB") #skip cards
    
  for num in range(1, 3):
    deck.append("draw4") #draw 4 cards
    deck.append("wild") #wild cards

random.shuffle(deck)
print(deck)