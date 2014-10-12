import pyglet
import rabbyt
import math
from pyglet import font

#rabbyt library is used to find collisions

# Import internal modules
import TestPygletEvents
import TestPygletObjects

window_height = 600
window_width = 800

window = pyglet.window.Window(window_width,window_width)

#Collisions of paddle and pallino
def paddleCollision(pallino,paddle):

    collide = rabbyt.collisions.aabb_collide_single(pallino,[paddle])
    if len(collide) > 0:
        pallino.setVelocity(pallino.velocity_x,-1*pallino.velocity_y)
        pallino.setPosition(pallino.x,collide[0].y + collide[0].height + 1)

#Distance calculation to prioritize collisions in pallino on brick collisions
def distance(pallino, brick):
    distances = []

    distances.append(math.sqrt(((brick.top-pallino.bottom)*(brick.top-pallino.bottom))))
    distances.append(math.sqrt(brick.right-pallino.left)*(brick.right-pallino.left))
    distances.append(math.sqrt((brick.left-pallino.right)*(brick.left-pallino.right)))
    distances.append(math.sqrt((brick.bottom-pallino.top)*(brick.bottom-pallino.top)))

    m = distances.index(min(distances))

    return m

#Collision checks between pallino and bricks, also bounces pallino and damages struck bricks
#rabbyt.collisions requires a list of objects, so the brick dictionary is temporarily converted to a list for this purpose

def collisions(pallino,bricks):
    temp_list = []
    key_list = []
    for key in bricks.bricks:
        temp_list.append(bricks.bricks[key])
        key_list.append(key)

    found_collisions = rabbyt.collisions.aabb_collide_single(pallino,temp_list)


    if len(found_collisions) > 0:
        block_id = key_list[temp_list.index(found_collisions[0])]
        #print block_id
        m = distance(pallino,found_collisions[0])

        if m == 0:
            pallino.setVelocity(pallino.velocity_x,-1*pallino.velocity_y)
            pallino.setPosition(pallino.x,found_collisions[0].y + found_collisions[0].height + 1)
        if m == 1:
            pallino.setVelocity(-1*pallino.velocity_x,pallino.velocity_y)
            pallino.setPosition(found_collisions[0].x + 1 + found_collisions[0].width,pallino.y)
        if m == 2:
            pallino.setVelocity(-1*pallino.velocity_x,pallino.velocity_y)
            pallino.setPosition(found_collisions[0].x - 1 - pallino.width,pallino.y)
        if m == 3:
            pallino.setVelocity(pallino.velocity_x,-1*pallino.velocity_y)
            pallino.setPosition(pallino.x,found_collisions[0].y - 1 - pallino.height)
        bricks.brickDamage(block_id,pallino.attack)


# Define an update event for the pyglet context to use
def gameUpdate(dt):
  ball.update(dt)
  collisions(ball,brick_list)
  paddleCollision(ball,paddle)
  paddle.update(dt)


FPS=100.
pyglet.clock.schedule_interval(gameUpdate,1/FPS) # xchedule update event calls on the pyglet clock

# Initialized objects

# The constructor takes the arguments defined in TestPygletObjects
#player = TestPygletObjects.GameObject(50,50,0.5)

ball = TestPygletObjects.Pallino(10,10,0,0,0.5,1)
paddle = TestPygletObjects.Paddle(10,75,FPS)

#below is the test instructions to generate a brick away.  This could also be easily done using loops
brick_layout = [[1,1,1,1,1,1,1],
                [1,0,0,0,0,0,1],
                [1,0,0,0,0,0,1],
                [1,0,0,0,0,0,1],
                [1,0,0,0,0,0,1],
                [1,0,0,0,0,0,1],
                [1,1,1,1,1,1,1]]

brick_list = TestPygletObjects.BrickList()
brick_list.makeBrickList(brick_layout)





# Create a font object to put at the top of the screen
#I still can't get the correct font to display for me
pyglet.font.add_file('Ober-Tuerkheim.ttf')
test_font = pyglet.font.load('Ober-Tuerkheim')
gameText = pyglet.text.Label('BOX QUEST!',
                              font_name='Ober-Tuerkheim',
                              font_size=76,
                              x=window.width//2, y=5*window.height//6,
                              anchor_x='center', anchor_y='center')



@window.event
def on_key_press(symbol,modifiers):
  TestPygletEvents.paddleKeyPress(paddle,ball,symbol,window_width)
  TestPygletEvents.ballKeyPress(ball,symbol)

#For testing brick deletion:
#  TestPygletEvents.deleteBrick(symbol,brick_list,brick_key)

@window.event
def on_key_release(symbol,modifiers):
  TestPygletEvents.paddleKeyRelease(paddle,ball,symbol)

@window.event
def on_draw():
  window.clear()
  paddle.draw()
  gameText.draw()
  ball.draw()
  brick_list.drawBricks()



# start the game loop!
pyglet.app.run()
