import pygame
pygame.init()

# screen size
X = 400
Y = 300
 
# create the display surface object
# of specific dimension..e(X, Y).
scrn = pygame.display.set_mode((X, Y))


# create a surface object, image is drawn on it.
wildcard = pygame.image.load("./cards/wild.png").convert()
wild = pygame.transform.scale(wildcard, (60,90))

wildcard4 = pygame.image.load("./cards/wild4.png").convert()
wild4 = pygame.transform.scale(wildcard4, (60,90))

cursor2 = pygame.image.load("./cursor2.png").convert()
pygame.Surface.set_colorkey(cursor2, [255, 0, 255])
currentCursor = pygame.transform.scale(cursor2, (100,100))

cursor1 = pygame.image.load("./cursor1.png").convert()
pygame.Surface.set_colorkey(cursor1, [255, 0, 255])
currentCursor1 = pygame.transform.scale(cursor1, (100, 100))

jeff1 = pygame.image.load("./jeff.png").convert()
pygame.Surface.set_colorkey(jeff1, [255, 0, 255])
jeff = pygame.transform.scale(jeff1, (120,150))

# using blit to copy content from one surface to other
# 12 cards can fit on the screen before they have to start overlapping further
scrn.blit(wild4, (50, 390))
scrn.blit(wild, (90, 390))

scrn.blit(currentCursor, (90, 90))
scrn.blit(currentCursor1, (50, 50))

scrn.blit(jeff, (90, 30))



# paint screen one time
pygame.display.flip()
status = True
while (status):
 
  # iterate over the list of Event objects
  # that was returned by pygame.event.get() method.
    for i in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False
 
# deactivates the pygame library
pygame.quit()