from ursina import *

app = Ursina()

def action():
    dol = Entity(model='sphere'
                 , color=color.white
                 , scale=(1,0.5,1)
                 , position=(0,0.75,0)
                 , collider='sphere')

pan = Entity(model='cube'
             , color=color.orange
             , scale=(1,1,1)
             , position=(0,0,0)
             , collider='box'
             , on_click=action
             , texture='white_cube')

camera.y = 30
camera.z = -30

def update():   # update gets automatically called.
    camera.x += held_keys['d'] * .1
    camera.x -= held_keys['a'] * .1
    camera.y += held_keys['w'] * .1
    camera.y -= held_keys['s'] * .1
    camera.z += held_keys['r'] * .1
    camera.z -= held_keys['f'] * .1
    camera.rotation_x += held_keys['z'] * 1
    camera.rotation_x -= held_keys['x'] * 1

app.run()   # opens a window and starts the game.