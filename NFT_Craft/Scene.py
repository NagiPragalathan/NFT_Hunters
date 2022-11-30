from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# custom import
from GameObjects import Ground,Player


# Game envorement

app = Ursina()
land = Ground()    
player = Player()

# Sky 
Sky()

# Controller_type
Controller_type = FirstPersonController()

# window_screen
window.fullscreen = True



def update():
    if held_keys['left mouse']:
        player.arm.position = (0.6, -0.5)
    elif held_keys['right mouse']:
        player.arm.position = (0.6, -0.5)
    else:
        player.arm.position = (0.75, -0.6)


def input(key):
    for box in land.boxes:
        if box.hovered:
            if key == 'left mouse down':
                newBox = Button(
                                position = box.position + mouse.normal,
                                color = color.orange,
                                highlight_color = color.red,
                                model = 'cube',
                                texture = load_texture('textures\wood'),
                                origin_y = 0.5,
                                parent = scene
                )
                land.boxes.append(newBox)
            if key == 'right mouse down':
                land.boxes.remove(box)
                destroy(box)
app.run()