import pygame

# Import internal modules
import TestGameEvents
import TestGameObjects

# Initialize Pygame - this encapsulates the underlying SDL Init
pygame.init()

# Create a pygame window. This uses pygame.display.set_mode function to
# set screen options, which also returns a pygame.Surface object that we save.
# The syntax is:
#   pygame.display.set_mode(windowSize2Tuple, pygameOptions, depth)
#
# Full documentation at http://www.pygame.org/docs/ref/display.html#pygame.display.set_mode

windowSize2Tuple = (800,600)  # note that this is a 2tuple
pygameOptions = pygame.RESIZABLE  # these are described online
depth = 32  # if left out from the set_mode call, this is automatically chosen (which Pygame recommends)

window = pygame.display.set_mode(windowSize2Tuple, pygameOptions, depth)

# Initialize a pygame.time.Clock and store it to handle ticks in the game loop
clock = pygame.time.Clock()

# Initialize the player object based on our TestGameObjects.GameObject class.
# We've set the constructor to take height, width, and FPS for the animation
player = TestGameObjects.GameObject(50,50,3.5)

# Create a font object to put at the top of the screen
gameFont = pygame.font.Font("Ober-Tuerkheim.ttf",76)  # downloaded some dumb font from 1001freefonts.com,
                                                      # and setting font size to 76
gameText = gameFont.render("BOX QUEST!",1,(255,255,255))  # We use pygame.font.Font.render to create a text object,
                                                          # which constructs with textString, antiAlias, textColor
                                                          # in this case we've chosen to antialias in white.
                                                          # note that the object is a pygame.Surface
gameTextRect = gameText.get_rect()  # we use pygame.Surface.get_rect() to get the text's bounding rect. This will be
                                    # used later to render the surface to the window
gameTextRect.centerx = 400  # we use the pygame.Rect.centerx and pygame.Rect.centery properties to set the location
gameTextRect.centery = 100  # for the bounding rect

# start the game loop!
gameRunning = True

while gameRunning:
  # use our internal module to check Keyboard events. This function does a few things:
  # 1) it takes the player object and calls its subroutines based on keystrokes
  # 2) it checks for window close events and the escape key, return False if
  #    the player wants to quit, and assigning that to gameRunning (to end the loop)
  gameRunning = TestGameEvents.getEventUpdates(player)

  # Handle updates for game objects. This is where motion, collisions, status, etc. might go.
  # In this case we only have a player object that's receiving updates, though realistically
  # we will call updates to entire lists of game objects created on the fly (e.g., bullets, badguys)
  dt = clock.tick(60)       # 60 here refers to a target refresh rate, and will throttle the game
                            # if it's running too fast. This function resets the timer and returns
                            # the time elapsed since the last update in milliseconds.
  player.update(dt/1000.)   # Divide by float(1000) to convert milliseconds to seconds

  # fill the window Surface with a pygame.Color object that we create on the fly
  # pygame.Color variables are r,g,b,a and 0,0,0,0 corresponds to black
  window.fill(pygame.Color(0,0,0,0))

  # blit our game objects onto the window with pygame.Surface.blit method, which takes
  # a pygame.Surface and a pygame.Rect (which acts as the bounding rectangle for where the surface is drawn).
  window.blit(player.sprite.image,player.sprite.rect)  # the player sprite's pygame.Surface and pygame.Rect
                                                       # check TestGameObjects to see that player.sprite.rect is
                                                       # storing the player's x,y coordinates
  window.blit(gameText,gameTextRect)  # blit the font that we created before the game loop

  # pygame.display.update() must be called in order for the blits that we've done on
  # window to be displayed.
  pygame.display.update()