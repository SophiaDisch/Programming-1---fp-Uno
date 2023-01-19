import random
import pygame, sys
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 450))
pygame.display.set_caption('Hello World!')


discardPile = []
deck = []
playerHand = []
botHand = []
discardPile = []

#Yellows
yellow11 = pygame.image.load("./cards/yellow1.png").convert()
yellow1 = pygame.transform.scale(yellow11, (60,90))
#
yellow22 = pygame.image.load("./cards/yellow2.png").convert()
yellow2 = pygame.transform.scale(yellow22, (60,90))
#
yellow33 = pygame.image.load("./cards/yellow3.png").convert()
yellow3 = pygame.transform.scale(yellow33, (60,90))
#
yellow44 = pygame.image.load("./cards/yellow4.png").convert()
yellow4 = pygame.transform.scale(yellow44, (60,90))
#
yellow55 = pygame.image.load("./cards/yellow5.png").convert()
yellow5 = pygame.transform.scale(yellow55, (60,90))
#
yellow66 = pygame.image.load("./cards/yellow6.png").convert()
yellow6 = pygame.transform.scale(yellow66, (60,90))
#
yellow77 = pygame.image.load("./cards/yellow7.png").convert()
yellow7 = pygame.transform.scale(yellow77, (60,90))
#
yellow88 = pygame.image.load("./cards/yellow8.png").convert()
yellow8 = pygame.transform.scale(yellow88, (60,90))
#
yellow99 = pygame.image.load("./cards/yellow9.png").convert()
yellow9 = pygame.transform.scale(yellow99, (60,90))
#
yellowdraw22 = pygame.image.load("./cards/yellowdraw2.png").convert()
yellowdraw2 = pygame.transform.scale(yellowdraw22, (60,90))
#
yellowre = pygame.image.load("./cards/yellowreverse.png").convert()
yellowreverse = pygame.transform.scale(yellowre, (60,90))
#Reds
red11 = pygame.image.load("./cards/red1.png").convert()
red1 = pygame.transform.scale(red11, (60,90))
#
red22 = pygame.image.load("./cards/red2.png").convert()
red2 = pygame.transform.scale(red22, (60,90))
#
red33 = pygame.image.load("./cards/red3.png").convert()
red3 = pygame.transform.scale(red33, (60,90))
#
red44 = pygame.image.load("./cards/red4.png").convert()
red4 = pygame.transform.scale(red44, (60,90))
#
red55 = pygame.image.load("./cards/red5.png").convert()
red5 = pygame.transform.scale(red55, (60,90))
#
red66 = pygame.image.load("./cards/red6.png").convert()
red6 = pygame.transform.scale(red66, (60,90))
#
red77 = pygame.image.load("./cards/red7.png").convert()
red7 = pygame.transform.scale(red77, (60,90))
#
red88 = pygame.image.load("./cards/red8.png").convert()
red8 = pygame.transform.scale(red88, (60,90))
#
red99 = pygame.image.load("./cards/red9.png").convert()
red9 = pygame.transform.scale(red99, (60,90))
#
reddraw22 = pygame.image.load("./cards/reddraw2.png").convert()
reddraw2 = pygame.transform.scale(reddraw22, (60,90))
#
redre = pygame.image.load("./cards/redreverse.png").convert()
redreverse = pygame.transform.scale(redre, (60,90))
#Greens
green11 = pygame.image.load("./cards/green1.png").convert()
green1 = pygame.transform.scale(green11, (60,90))
#
green22 = pygame.image.load("./cards/green2.png").convert()
green2 = pygame.transform.scale(green22, (60,90))
#
green33 = pygame.image.load("./cards/green3.png").convert()
green3 = pygame.transform.scale(green33, (60,90))
#
green44 = pygame.image.load("./cards/green4.png").convert()
green4 = pygame.transform.scale(green44, (60,90))
#
green55 = pygame.image.load("./cards/green5.png").convert()
green5 = pygame.transform.scale(green55, (60,90))
#
green66 = pygame.image.load("./cards/green6.png").convert()
green6 = pygame.transform.scale(green66, (60,90))
#
green77 = pygame.image.load("./cards/green7.png").convert()
green7 = pygame.transform.scale(green77, (60,90))
#
green88 = pygame.image.load("./cards/green8.png").convert()
green8 = pygame.transform.scale(green88, (60,90))
#
green99 = pygame.image.load("./cards/green9.png").convert()
green9 = pygame.transform.scale(green99, (60,90))
#
greendraw22 = pygame.image.load("./cards/greendraw2.png").convert()
greendraw2 = pygame.transform.scale(greendraw22, (60,90))
#
greenre = pygame.image.load("./cards/greenreverse.png").convert()
greenreverse = pygame.transform.scale(greenre, (60,90))
#Blues
blue11 = pygame.image.load("./cards/blue1.png").convert()
blue1 = pygame.transform.scale(blue11, (60,90))
#
blue22 = pygame.image.load("./cards/blue2.png").convert()
blue2 = pygame.transform.scale(blue22, (60,90))
#
blue33 = pygame.image.load("./cards/blue3.png").convert()
blue3 = pygame.transform.scale(blue33, (60,90))
#
blue44 = pygame.image.load("./cards/blue4.png").convert()
blue4 = pygame.transform.scale(blue44, (60,90))
#
blue55 = pygame.image.load("./cards/blue5.png").convert()
blue5 = pygame.transform.scale(blue55, (60,90))
#
blue66 = pygame.image.load("./cards/blue6.png").convert()
blue6 = pygame.transform.scale(blue66, (60,90))
#
blue77 = pygame.image.load("./cards/blue7.png").convert()
blue7 = pygame.transform.scale(blue77, (60,90))
#
blue88 = pygame.image.load("./cards/blue8.png").convert()
blue8 = pygame.transform.scale(blue88, (60,90))
#
blue99 = pygame.image.load("./cards/blue9.png").convert()
blue9 = pygame.transform.scale(blue99, (60,90))
#
bluedraw22 = pygame.image.load("./cards/bluedraw2.png").convert()
bluedraw2 = pygame.transform.scale(bluedraw22, (60,90))
#
bluere = pygame.image.load("./cards/bluereverse.png").convert()
bluereverse = pygame.transform.scale(bluere, (60,90))
#Wilds
wildcard = pygame.image.load("./cards/wild.png").convert()
wild = pygame.transform.scale(wildcard, (60,90))
#
wildcard4 = pygame.image.load("./cards/wild4.png").convert()
wild4 = pygame.transform.scale(wildcard4, (60,90))

deck = [yellow1, yellow2, yellow3, yellow4, yellow5, yellow6, yellow7, yellow8, yellow9, yellowreverse, yellowdraw2, red1, red2, red3, red4, red5, red6, red7, red8, red9, redreverse,reddraw2, green1, green2, green3, green4, green5, green6, green7, green8, green9, greenreverse, greendraw2, blue1, blue2, blue3, blue4, blue5, blue6, blue7, blue8, blue9, bluereverse, bluedraw2, wild, wild4]


def deckReset():
  deck.append("Z0") #red cards
  deck.append("Y0")
  deck.append("G0")
  deck.append("B0")
  for num in range(1, 3):
    for num in range(1,10):
      deck.append("Z" + str(num)) #red cards
      deck.append("Y" + str(num)) #yellow cards
      deck.append("G" + str(num)) #green cards
      deck.append("B" + str(num)) #blue cards
    deck.append("ZDraw2") #draw 2 cards
    deck.append("YDraw2")
    deck.append("GDraw2")
    deck.append("BDraw2")
    deck.append("ZRev") #reverse cards
    deck.append("YRev")
    deck.append("GRev")
    deck.append("BRev")
    deck.append("ZSkip") #skip cards
    deck.append("YSkip")
    deck.append("GSkip")
    deck.append("BSkip")
      
    for num in range(1, 3):
      deck.append("draw4") #draw 4 cards
      deck.append("wild") #wild cards

  random.shuffle(deck)
  print(deck)

deckReset()

def cardDeal():
  for num in range(1, 8):
    playerHand.append(deck.pop(0))
    botHand.append(deck.pop(0))
    playerHand.sort()
    botHand.sort()
  discardPile.append(deck.pop(0))

cardDeal()
print(playerHand)
print(botHand)

print(deck)



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()