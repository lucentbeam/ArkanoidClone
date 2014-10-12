import pyglet

window_height = 600
window_width = 800
paddle_width = 76

#The following is an example game object with sprite that is controllable with the arrow keys

#class GameObject:
#  def __init__(self,height,width,fps):
#    self.height = height
#    self.width = width
#    self.fps = fps
#    self.timer = 0
#    self.createSprite()  # initialize the sprite object
#    self.image.height = height
#    self.image.width = width
#    self.setPosition(400,600)  # stick it somewhere arbitrary

#  def createSprite(self):
#    self.image = pyglet.resource.image('rect.jpg')

#  def setPosition(self,x,y):
#    self.x = x
#    self.y = y
#    self.directionx = 0  # these variables must be initialized somewhere! here is probably not the best place
#    self.directiony = 0

#  def moveRight(self):
#    self.directionx = 1

#  def moveLeft(self):
#    self.directionx = -1

#  def moveDown(self):
#    self.directiony = -1

#  def moveUp(self):
#    self.directiony = 1

#  def stopHorizontalMovement(self):
#    self.directionx = 0

#  def stopVerticalMovement(self):
#    self.directiony = 0

#  def update(self,time):
#    self.updatePosition()  # move the object
#    self.updateTimer(time)  # check its animation timer
#    self.updateSpriteImage()  # redraw the sprite image incase the animation timer has ticked

#  def updatePosition(self):
#    self.x += self.directionx  # increment the x position in the direction it's moving
#    self.y += self.directiony  # increment the y position in the direction it's moving

#  def updateTimer(self,time):
#    self.timer += time  # increment the timer
#    if self.timer >= 1/self.fps:  # if a timer cycle has been passed
#      self.incrementTimer()

#  def incrementTimer(self):
#    self.timer = 0  # reset the timer

#  def updateSpriteImage(self):
#    x="this does nothing!!!!" # Pyglet doesn't have primitives built in like Pygame...
                              # animations need to be pre-rendered textures or rendered in a GL context

#  def draw(self):
#    self.image.blit(self.x,self.y)


#This is the class for the controllable paddle
class Paddle:
  def __init__(self,height,width,fps):
    self.height = height
    self.width = width
    self.fps = fps
    self.speed = 22
    self.timer = 0
    self.createSprite()  # initialize the sprite object
    self.image.height = height
    self.image.width = width
    self.x = window_width/2 - self.width/2
    self.y = 50
    self.setPosition(self.x,self.y)
    self.directionx = 0
    #Attributes for rabbyt.collision
    self.bottom = self.y
    self.top = self.y + self.height
    self.left = self.x
    self.right = self.x + self.width

  def createSprite(self):
    self.image = pyglet.resource.image('paddle.png')

  def setPosition(self,x,y):
    self.x = x
    self.y = y

  def moveRight(self):
    self.directionx = self.speed

  def moveLeft(self):
    self.directionx = -1*self.speed

  def stopHorizontalMovement(self):
    self.directionx = 0

  def updateCollisionBox(self):
    self.bottom = self.y
    self.top = self.y + self.height
    self.left = self.x
    self.right = self.x + self.width

  def updatePosition(self):
    if self.x < 0:
        self.stopHorizontalMovement()
        self.setPosition(0, self.y)
    if self.x + self.width > window_width:
        self.stopHorizontalMovement()
        self.setPosition(window_width - self.width, self.y)
    else:
        self.x += self.directionx  # increment the x position in the direction it's moving

  def updateTimer(self,time):
    self.timer += time  # increment the timer
    if self.timer >= 1/self.fps:  # if a timer cycle has been passed
      self.incrementTimer()

  def update(self,time):
    self.updatePosition()  # move the object
    self.updateCollisionBox()
    self.updateTimer(time)  # check its animation timer

  def incrementTimer(self):
    self.timer = 0

  def draw(self):
    self.image.blit(self.x,self.y)

class Pallino:
    def __init__(self, width, height, velocity_x, velocity_y, fps,attack):
        self.height = height
        self.width = width
        self.fps = fps
        self.timer = 0
        self.attack = attack
        self.createSprite()
        self.image.width = width
        self.image.height = height
        self.x = window_width/2 - self.width/2
        self.y = 50 + 10
        self.setPosition(self.x,self.y)
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.initial_speed = 22
        self.directionx = 0
        #Rabbyt collision box attributes
        self.bottom = self.y
        self.top = self.y + self.height
        self.left = self.x
        self.right = self.x + self.width

    def createSprite(self):
        self.image = pyglet.resource.image('circle.png')

    def moveRight(self):
        self.directionx = self.initial_speed

    def moveLeft(self):
        self.directionx = -1*self.initial_speed

    def stopHorizontalMovement(self):
        self.directionx = 0

    def setVelocity(self,x,y):
        self.velocity_x = x
        self.velocity_y = y

    def hasLaunched(self):
        if self.velocity_x and self.velocity_y != 0:
            return True
        else:
            return False

    def setPosition(self,x,y):
        self.x = x
        self.y = y

    def update(self,time):
        self.updatePosition(time)
        self.updateCollisionBox()
        self.updateTimer(time)

    def updateCollisionBox(self):
        self.bottom = self.y
        self.top = self.y + self.height
        self.left = self.x
        self.right = self.x + self.width

    def updatePosition(self,time):
        if self.hasLaunched() is True:
            if self.y <= window_height and self.y >= 0 and self.x >= 0 and self.x <= window_width-self.width:
                self.x += self.velocity_x * time
                self.y += self.velocity_y * time
            if self.y + self.height >= window_height:
                self.setVelocity(self.velocity_x, -1*self.velocity_y)
                self.setPosition(self.x + self.velocity_x * time,window_height - self.height - 1)
            if self.y <= 0:
                self.setVelocity(self.velocity_x, -1*self.velocity_y)
                self.setPosition(self.x + self.velocity_x * time, 1)
            if self.x <= 0:
                self.setVelocity(-1*self.velocity_x, self.velocity_y)
                self.setPosition(1, self.y + self.velocity_y * time)
            if self.x + self.width >= window_width:
                self.setVelocity(-1*self.velocity_x, self.velocity_y)
                self.setPosition(window_width - self.width - 1, self.y + self.velocity_y * time)

#The second half here handles the pallino before launch when it is on the paddle
        else:
            if self.x < paddle_width/2 - self.width/2:
                self.stopHorizontalMovement()
                self.setPosition(paddle_width/2 - self.width/2, self.y)
            if self.x + self.width/2 + paddle_width/2 > window_width:
                self.stopHorizontalMovement()
                self.setPosition(window_width - self.width/2 - paddle_width/2, self.y)
            else:
                self.x += self.directionx



    def updateTimer(self,time):
        self.timer += time  # increment the timer
        if self.timer >= 1/self.fps:  # if a timer cycle has been passed
            self.incrementTimer()

    def incrementTimer(self):
        self.timer = 0  # reset the timer

    def draw(self):
        self.image.blit(self.x,self.y)

class Brick:
    def __init__(self, x, y, width, height, durability):
        self.height = height
        self.width = width
        self.createSprite()
        self.image.width = width
        self.image.height = height
        self.durability = durability
        self.x = x
        self.y = y
        #Rabbyt bounding box attributes
        self.bottom = self.y
        self.top = self.y + self.height
        self.left = self.x
        self.right = self.x + self.width

    def createSprite(self):
        self.image = pyglet.resource.image('brick.png')

    def draw(self):
        self.image.blit(self.x, self.y)

    def setDurability(self, damage):
        self.durability = self.durability - 1




#Bricklists have dictionaries of the game bricks and manages them, doing things like deleting damaged bricks
class BrickList:
    def __init__(self):
        self.bricks = {}

#tells bricks to draw themselves
    def drawBricks(self):
        for key in self.bricks:
            self.bricks[key].draw()

#removes bricks from the dictionary, screen
    def removeBrick(self,brick_key):
        r = self.bricks
        del r[brick_key]
        return self.bricks

#makeBrickList accepts an nxn array of brick durability values and then makes bricks with those values. If the value is zero, then no brick is placed
#Each brick placed in the dictionary has a unique key that is generated at dictionary creation
    def makeBrickList(self,command):
        i = 0
        q = 0
        for row in command:
            j = 0
            for value in row:
                if value > 0:
                    self.bricks['brick'+str(q)] = Brick(50 + j*100,100 + i*50,100,50,1)
                    j += 1
                    q += 1
                else:
                    j += 1
            i += 1

#tells which bricks to receive x amount of damage (currently damage = pallino's attack value
    def brickDamage(self,brick_id,damage):
        self.bricks[brick_id].setDurability(damage)
        if self.bricks[brick_id].durability <= 0:
            self.removeBrick(brick_id)





