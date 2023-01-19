import random
import pygame, sys
from pygame.locals import QUIT
pygame.init()

DISPLAYSURF = pygame.display.set_mode((600, 450))
pygame.display.set_caption("Oh no! It's Uno!")

FPS = 12
X = 600
Y = 450
scrn = pygame.display.set_mode((X, Y))

selected_card = 1
urMom = 2
discardPile = []
deck = []
playerHand = []
botHand = []
discardPile = []

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
      deck.append("Plus4") #draw 4 cards
      deck.append("wild") #wild cards

  random.shuffle(deck)


def cardDeal():
  for num in range(1, 8):
    playerHand.append(deck.pop(0))
    botHand.append(deck.pop(0))
    playerHand.sort()
    botHand.sort()
  discardPile.append(deck.pop(0))



def startup_load():
  startup1 = pygame.image.load("startup.png").convert()
  startup = pygame.transform.scale(startup1, (600,450))
  scrn.blit(startup, (0,0))
  
  pressStart = pygame.image.load("pressstart.png").convert()
  start = pygame.transform.scale(pressStart, (200,50))
  scrn.blit(start, (200,200))
  
  pressExit = pygame.image.load("pressexit.png").convert()
  exit = pygame.transform.scale(pressExit, (200,50))
  scrn.blit(exit, (200,300))

def frame_load():
  background1 = pygame.image.load("background.png").convert()
  background = pygame.transform.scale(background1, (600,450))
  scrn.blit(background, (0,0))
  table1 = pygame.image.load("table.png").convert()
  table = pygame.transform.scale(table1, (600,300))
  scrn.blit(table, (0,150))

  hand_load()

def hand_load():
  for num in range(0, len(playerHand)):
    distance = 50 + (num * (500 / len(playerHand)))
    card1 = pygame.image.load("./cards/" + playerHand[num] + ".png").convert()
    pygame.Surface.set_colorkey(card1, [255, 0, 255])
    card = pygame.transform.scale(card1, (60,90))
    scrn.blit(card, (distance, 330))

def raised_card():
  for num in range(0, len(playerHand)):
    if num == (selected_card - 1):
      distance = 50 + (num * (500 / len(playerHand)))
      card1 = pygame.image.load("./cards/" + playerHand[num] + ".png").convert()
      pygame.Surface.set_colorkey(card1, [255, 0, 255])
      card = pygame.transform.scale(card1, (60,90))
      scrn.blit(card, (distance, 300))
    if not num == (selected_card - 1):
      distance = 50 + (num * (500 / len(playerHand)))
      card1 = pygame.image.load("./cards/" + playerHand[num] + ".png").convert()
      pygame.Surface.set_colorkey(card1, [255, 0, 255])
      card = pygame.transform.scale(card1, (60,90))
      scrn.blit(card, (distance, 330))

#
deckReset()
cardDeal()
startup_load()

def GameLoop():
  selected_card = 0
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_s:
        frame_load()
        selected_card = 1
        
        instructions1 = pygame.image.load("instructions.png").convert()
        instructions = pygame.transform.scale(instructions1, (400,300))
        scrn.blit(instructions, (100,25))
        
        continue1 = pygame.image.load("continue.png").convert()
        Continue = pygame.transform.scale(continue1, (200,100))
        scrn.blit(Continue, (200,350))

      if event.key == pygame.K_c:
        frame_load()
        
      if event.key == pygame.K_e:
        pygame.quit()

      if event.key == pygame.K_RIGHT:
        selected_card += 1
        if selected_card < len(deck):
          selected_card = len(deck)
        for num in range(0, len(playerHand)):
          if num == (selected_card - 1):
            distance = 50 + (num * (500 / len(playerHand)))
            card1 = pygame.image.load("./cards/" + playerHand[num] + ".png").convert()
            pygame.Surface.set_colorkey(card1, [255, 0, 255])
            card = pygame.transform.scale(card1, (60,90))
            scrn.blit(card, (distance, 300))
          if not num == (selected_card - 1):
            distance = 50 + (num * (500 / len(playerHand)))
            card1 = pygame.image.load("./cards/" + playerHand[num] + ".png").convert()
            pygame.Surface.set_colorkey(card1, [255, 0, 255])
            card = pygame.transform.scale(card1, (60,90))
            scrn.blit(card, (distance, 330))

      if event.key == pygame.K_LEFT:
        selected_card -= 1
        if selected_card < 1:
          selected_card = 1
        for num in range(0, len(playerHand)):
          if num == (selected_card - 1):
            distance = 50 + (num * (500 / len(playerHand)))
            card1 = pygame.image.load("./cards/" + playerHand[num] + ".png").convert()
            pygame.Surface.set_colorkey(card1, [255, 0, 255])
            card = pygame.transform.scale(card1, (60,90))
            scrn.blit(card, (distance, 300))
          if not num == (selected_card - 1):
            distance = 50 + (num * (500 / len(playerHand)))
            card1 = pygame.image.load("./cards/" + playerHand[num] + ".png").convert()
            pygame.Surface.set_colorkey(card1, [255, 0, 255])
            card = pygame.transform.scale(card1, (60,90))
            scrn.blit(card, (distance, 330))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    GameLoop()