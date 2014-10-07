import pyglet

# Import internal modules
import TestPygletEvents
import TestPygletObjects

window = pyglet.window.Window(800,600)

# Define an update event for the pyglet context to use
def gameUpdate(dt):
  player.update(dt)

FPS=60.
pyglet.clock.schedule_interval(gameUpdate,1/FPS) # xchedule update event calls on the pyglet clock

# Initialize the player object based on our TestGameObjects.GameObject class.
# We've set the constructor to take height, width, and FPS for the animation
player = TestPygletObjects.GameObject(50,50,3.5)

# Create a font object to put at the top of the screen
pyglet.font.add_file('Ober-Tuerkheim.ttf')
gameText = pyglet.text.Label('BOX QUEST!',
                              font_name='Ober-Tuerkheim',
                              font_size=76,
                              x=window.width//2, y=5*window.height//6,
                              anchor_x='center', anchor_y='center')

@window.event
def on_key_press(symbol,modifiers):
  TestPygletEvents.playerKeyPress(player,symbol)

@window.event
def on_key_release(symbol,modifiers):
  TestPygletEvents.playerKeyRelease(player,symbol)

@window.event
def on_draw():
  window.clear()
  gameText.draw()
  player.draw()

# start the game loop!
pyglet.app.run()
