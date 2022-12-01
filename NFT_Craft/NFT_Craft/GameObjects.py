from ursina import *

block_id = 1
model_id = 1
mapping = []

class Voxel(Button):
    global mapping
    def __init__(self, position=(0, 0, 0), texture='assets/grass',model='assets/models/block'):
        super().__init__(
            parent=scene,
            position=position,
            model=model,
            origin_y=0.10,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=0.5
        )
        
    #destory controller
    def input(self, key):
        blocks = [
            'assets/models/block',
            load_texture('assets/grass.png'), # 1
            load_texture('assets/stone.png'), # 2
            load_texture('assets/gold.png'),  # 3
            load_texture('assets/lava.png'),  # 4
            load_texture('assets/sand.jpg'),  # 5

        ]
        model = [
            'assets/models/block',
            'assets/models/block',
            'assets/models/man',
            'assets/models/minis',
            'assets/models/tree',  # q+4
            'assets/models/car',  # q+5

        ]
        if self.hovered:
            if key == 'left mouse down':
                pos = self.position + mouse.normal
                Voxel(position= pos, texture=blocks[block_id],model=model[model_id])
                mapping.append({'x':pos.x,'y':pos.y,'z':pos.z,'block':int(block_id)})
            elif key == 'right mouse down':
                destroy(self)