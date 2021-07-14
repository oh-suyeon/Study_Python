from ursina import *

app = Ursina()

cube1 = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(-5,5,0))
cube2 = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(0,5,0))
cube3 = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(5,5,0))

cube4 = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(-5,0,0))
cube5 = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(0,0,0))
cube6 = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(5,0,0))

cube7 = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(-5,-5,0))
cube8 = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(0,-5,0))
cube9 = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(5,-5,0))

camera.z = -30

def update():   # update gets automatically called.
    camera.x += held_keys['d'] * .1
    camera.x -= held_keys['a'] * .1
    camera.y += held_keys['w'] * .1
    camera.y -= held_keys['s'] * .1
    camera.z += held_keys['r'] * 1
    camera.z -= held_keys['f'] * 1

app.run()   # opens a window and starts the game.