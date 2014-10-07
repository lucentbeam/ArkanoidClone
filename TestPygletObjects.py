import pyglet

class GameObject:
  def __init__(self,height,width,fps):
    self.height = height
    self.width = width
    self.fps = fps
    self.timer = 0
    self.createSprite()  # initialize the sprite object
    self.image.height = height
    self.image.width = width
    self.setPosition(400,300)  # stick it somewhere arbitrary

  def createSprite(self):
    self.image = pyglet.resource.image('rect.jpg')

  def setPosition(self,x,y):
    self.x = x
    self.y = y
    self.directionx = 0  # these variables must be initialized somewhere! here is probably not the best place
    self.directiony = 0

  def moveRight(self):
    self.directionx = 1

  def moveLeft(self):
    self.directionx = -1

  def moveDown(self):
    self.directiony = -1

  def moveUp(self):
    self.directiony = 1

  def stopHorizontalMovement(self):
    self.directionx = 0

  def stopVerticalMovement(self):
    self.directiony = 0

  def update(self,time):
    self.updatePosition()  # move the object
    self.updateTimer(time)  # check its animation timer
    self.updateSpriteImage()  # redraw the sprite image incase the animation timer has ticked

  def updatePosition(self):
    self.x += self.directionx  # increment the x position in the direction it's moving
    self.y += self.directiony  # increment the y position in the direction it's moving

  def updateTimer(self,time):
    self.timer += time  # increment the timer
    if self.timer >= 1/self.fps:  # if a timer cycle has been passed
      self.incrementTimer()

  def incrementTimer(self):
    self.timer = 0  # reset the timer

  def updateSpriteImage(self):
    x="this does nothing!!!!" # Pyglet doesn't have primitives built in like Pygame...
                              # animations need to be pre-rendered textures or rendered in a GL context

  def draw(self):
    self.image.blit(self.x,self.y)
