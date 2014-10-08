from pyglet.window import key

def playerKeyPress(player,symbol):
  if symbol == key.RIGHT:
    player.moveRight()
  if symbol == key.LEFT:
    player.moveLeft()
  if symbol == key.UP:
    player.moveUp()
  if symbol == key.DOWN:
    player.moveDown()


def ballKeyPress(ball,state,symbol):
  if state is False:
    if symbol == key.ENTER:
        ball.setVelocity(5,5)


def playerKeyRelease(player,symbol):
  if (symbol == key.RIGHT) or (symbol == key.LEFT):
    player.stopHorizontalMovement()
  if (symbol == key.UP) or (symbol == key.DOWN):
    player.stopVerticalMovement()
