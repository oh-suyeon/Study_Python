from ursina import *

app = Ursina()

def action():
    print('Ow! That hurt!')

cube4 = Entity(model='sphere', color=color.white, scale=(1,0.5,0), position=(-5,0,0), collider='sphere', on_click=action)
cube5 = Entity(model='sphere', color=color.black, scale=(1,0.5,0), position=(0,0,0))
cube6 = Entity(model='sphere', color=color.orange, scale=(1,0.5,0), position=(5,0,0))

camera.z = -30



def update():   # update gets automatically called.
    camera.x += held_keys['d'] * .1
    camera.x -= held_keys['a'] * .1
    camera.y += held_keys['w'] * .1
    camera.y -= held_keys['s'] * .1
    camera.z += held_keys['r'] * 1
    camera.z -= held_keys['f'] * 1
    camera.rotation_x += held_keys['z'] * 1
    camera.rotation_x -= held_keys['x'] * 1

app.run()   # opens a window and starts the game.