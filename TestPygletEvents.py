from pyglet.window import key

#Example controls for example game object
#def playerKeyPress(player,symbol):
#  if symbol == key.RIGHT:
#    player.moveRight()
#  if symbol == key.LEFT:
#    player.moveLeft()
#  if symbol == key.UP:
#    player.moveUp()
#  if symbol == key.DOWN:
#    player.moveDown()

#def playerKeyRelease(player,symbol):
#  if (symbol == key.RIGHT) or (symbol == key.LEFT):
#    player.stopHorizontalMovement()
#  if (symbol == key.UP) or (symbol == key.DOWN):
#    player.stopVerticalMovement()


#Launches pallino
def ballKeyPress(pallino,symbol):
    if pallino.hasLaunched() is False:
        if symbol == key.ENTER:
            pallino.setVelocity(300,300)


#Controls paddle movement and moves pallino before launch
def paddleKeyPress(paddle,pallino,symbol,window_width):
    if pallino.hasLaunched() is False:
        if symbol == key.RIGHT:
            if paddle.x + paddle.width < window_width:
                paddle.moveRight()
                pallino.moveRight()
        if symbol == key.LEFT:
            if paddle.x > 0:
                paddle.moveLeft()
                pallino.moveLeft()

    else:
        if symbol == key.RIGHT:
            if paddle.x + paddle.width < window_width:
                paddle.moveRight()
        if symbol == key.LEFT:
            if paddle.x > 0:
                paddle.moveLeft()

#Handles the release of movement keys and stops movement
def paddleKeyRelease(paddle,pallino,symbol):
    if pallino.hasLaunched() is False:
        if (symbol == key.RIGHT) or (symbol == key.LEFT):
            paddle.stopHorizontalMovement()
            pallino.stopHorizontalMovement()
    else:
        if (symbol == key.RIGHT) or (symbol == key.LEFT):
            paddle.stopHorizontalMovement()

#This was to test the delete function for bricks
#def deleteBrick(symbol,brick_list,brick_key):
#    if symbol == key.DELETE:
#        if brick_key in brick_list.bricks:
#            brick_list.removeBrick(brick_key)




