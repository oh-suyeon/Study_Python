from ursina import *

app = Ursina()

player = Entity(model='cube', color=color.orange, scale_y=2)

def update():   # update gets automatically called.
    camera.rotation_x += held_keys['d'] * 1
    camera.rotation_x -= held_keys['a'] * 1
    camera.rotation_y += held_keys['w'] * 1
    camera.rotation_y -= held_keys['s'] * 1
    camera.rotation_z += held_keys['r'] * 1
    camera.rotation_z -= held_keys['f'] * 1

app.run()   # opens a window and starts the game.