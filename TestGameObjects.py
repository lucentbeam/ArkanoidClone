import pygame

class GameObject:
  def __init__(self,height,width,fps):
    self.height = height
    self.width = width
    self.fps = fps
    self.timer = 0
    # create a rudimentary animation: the sprite will cycle through these colors
    self.colors = [ pygame.Color(255,0,0,0),
                    pygame.Color('green'),  # this format works too
                    pygame.Color(0,0,255,0),
                    pygame.Color(255,255,0,0),
                    pygame.Color(255,0,255,0),
                    pygame.Color(0,255,255,0),
                    pygame.Color('#FFFFFF') ]  # hex too
    self.createSprite()  # initialize the sprite object
    self.setPosition(400,300)  # stick it somewhere arbitrary

  def createSprite(self):
    # the pygame.sprite.Sprite class is a basic container, actually meant to be inherited. Here it's just
    # being used to get some exposure. For future use, note that sprites need an image and rect attribute
    # to be drawn with Pygame's internal functions. These are pygame.Surface and pygame.Rect objects, respectively
    self.sprite = pygame.sprite.Sprite()  # initialize and return sprite
    self.sprite.image = pygame.Surface([self.width,self.height])  # make a surface with GameObject dimensions
    self.sprite.image.fill(self.colors[0])  # use pygame.Surface.fill with the starting color
    self.sprite.rect = self.sprite.image.get_rect()  # set the rect attribute to the bounding Rect of the surface,
                                                     # which is returned from pygame.Surface.get_rect()

  def setPosition(self,x,y):
    # we're storing the position of the GameObject as the top left of the bounding Rect of the sprite.
    # this can be a very bad practice, but will work for now
    self.sprite.rect.left = x
    self.sprite.rect.top = y
    self.directionx = 0  # these variables must be initialized somewhere! here is probably not the best place
    self.directiony = 0

  def moveRight(self):
    self.directionx = 1

  def moveLeft(self):
    self.directionx = -1

  def moveDown(self):
    self.directiony = 1  # note that down on a pygame.Surface is positive in y

  def moveUp(self):
    self.directiony = -1  # note that up on a pygame.Surface is negative in y

  def stopHorizontalMovement(self):
    self.directionx = 0

  def stopVerticalMovement(self):
    self.directiony = 0

  def update(self,time):
    self.updatePosition()  # move the object
    self.updateTimer(time)  # check its animation timer
    self.updateSpriteImage()  # redraw the sprite image incase the animation timer has ticked

  def updatePosition(self):
    self.sprite.rect.left += self.directionx  # increment the x position in the direction it's moving
    self.sprite.rect.top += self.directiony  # increment the y position in the direction it's moving

  def updateTimer(self,time):
    self.timer += time  # increment the timer
    if self.timer >= 1/self.fps:  # if a timer cycle has been passed
      self.incrementTimer()

  def incrementTimer(self):
    self.timer = 0  # reset the timer
    self.colors.append(self.colors.pop(0))  # cycle the self.colors List

  def updateSpriteImage(self):
    self.sprite.image.fill(self.colors[0])  # fill the surface with the current head of self.colors List


