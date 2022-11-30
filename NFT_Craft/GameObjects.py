from ursina import *

block_id = 1
mapping = []

class Voxel(Button):
    global mapping
    def __init__(self, position=(0, 0, 0), texture='assets/grass.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=0.5
        )
        
    #destory controller
    def input(self, key):
        blocks = [
            load_texture('assets/grass.png'), # 0
            load_texture('assets/grass.png'), # 1
            load_texture('assets/stone.png'), # 2
            load_texture('assets/gold.png'),  # 3
            load_texture('assets/lava.png'),  # 4
        ]
        if self.hovered:
            if key == 'left mouse down':
                pos = self.position + mouse.normal
                Voxel(position= pos, texture=blocks[block_id])
                mapping.append({'x':pos.x,'y':pos.y,'z':pos.z,'block':int(block_id)})
            elif key == 'right mouse down':
                destroy(self)