from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

import json

from GameObjects import Voxel
import GameObjects

#choose mode
mode = int(input("enter the mode[1/0] : "))

# app init
app = Ursina()

# app settings
window.fps_counter.enabled = False
window.exit_button.visible = False
window.fullscreen = True

# app audio
punch = Audio('assets/punch', autoplay=False)

# environment

blocks = [
    load_texture('assets/grass.png'), # 0
    load_texture('assets/grass.png'), # 1
    load_texture('assets/stone.png'), # 2
    load_texture('assets/gold.png'),  # 3
    load_texture('assets/lava.png'),  # 4
]

sky = Entity(
    parent=scene,
    model='sphere',
    texture=load_texture('assets/sky.jpg'),
    scale=500,
    double_sided=True
)

hand = Entity(
    parent=camera.ui,
    model='assets/block',
    texture=blocks[GameObjects.block_id],
    scale=0.2,
    rotation=Vec3(-10, -10, 10),
    position=Vec2(0.6, -0.6)
)

# blocks
storage = True


def store_to_json(maps):
    with open('C:/Users/NagiPragalathan/Desktop/NFT_Hunters/NFT_Craft/Datas/datas.json', 'w') as json_file:
        json.dump(maps, json_file)


#hand controller
def input(key):
    global hand
    if key.isdigit():
        GameObjects.block_id = int(key)
        if GameObjects.block_id >= len(blocks):
            GameObjects.block_id = len(blocks) - 1
        hand.texture = blocks[GameObjects.block_id]

def update():
    global storage
    if held_keys['left mouse'] or held_keys['right mouse']:
        punch.play()
        hand.position = Vec2(0.4, -0.5)
        storage = True
    if held_keys['p'] :
        if storage:
            store_to_json(GameObjects.mapping)
            storage = False
            print("stored....!")
        else :
            print("build anythink...")
    else:
        hand.position = Vec2(0.6, -0.6)

if(mode == 0):
    for z in range(20):
        for x in range(20):
            voxel = Voxel(position=(x, 0, z))
            GameObjects.mapping.append({'x':x,'y':0,'z':z,'block':GameObjects.block_id})
            print("run")
else:
    with open('C:/Users/NagiPragalathan/Desktop/NFT_Hunters/NFT_Craft/Datas/datas.json', 'r') as json_file:
        data = json.load(json_file)
    json_file.close()
    for i in data:
        print((i.get('x'), 0, i.get('z')))
        voxel = Voxel(position=(i.get('x'), i.get('y'), i.get('z')), texture=blocks[int(i.get('block'))])
        


player = FirstPersonController()

app.run()