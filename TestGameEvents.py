import pygame
# we could also "from pygame.locals import *"
# enabling us to use, e.g., just QUIT instead of pygame.QUIT

def getEventUpdates(player):
  # use pygame.event.get to return a list of all events that have happened since the last clock update.
  # all events are a single type that include keystrokes, mouseclicks, window close, etc.
  eventList = pygame.event.get()
  for event in eventList:
    if areQuitting(event):
      return False
    handlePlayerCommands(player,event)
  return True

def areQuitting(event):
  if event.type == pygame.QUIT:  # check if the 'x' on the window has been clicked
    return True
  if (event.type == pygame.KEYUP) and (event.key == pygame.K_ESCAPE):  # check if escape key was pressed
    return True
  return False

def handlePlayerCommands(player,event):
  '''
  :param player: the player object to be manipulated
  :param event: an event from the pygame.event queue to be checked
  '''
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_RIGHT:
      player.moveRight()
    if event.key == pygame.K_LEFT:
      player.moveLeft()
    if event.key == pygame.K_UP:
      player.moveUp()
    if event.key == pygame.K_DOWN:
      player.moveDown()
  if event.type == pygame.KEYUP:
    if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_LEFT):
      player.stopHorizontalMovement()
    if (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
      player.stopVerticalMovement()