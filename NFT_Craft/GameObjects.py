from ursina import *

class Ground:
    def __init__(self) -> None:
        self.boxes = []
        for n in range(50):
            for k in range(50):
                box = Button(
                position=(k, 0, n),
                color=color.orange,
                highlight_color=color.lime,
                model='cube',
                texture = load_texture('textures/wood'),
                origin_y = 0.5,
                parent = scene,
                tag = "wood"
                )
                self.boxes.append(box)


class Player(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui
        )
        self.arm = Entity(
        parent=camera.ui,
        model='cube',
        color=color.blue,
        position=(0.75, -0.6),
        rotation= (150, -10,6),
        scale = (0.2,0.2,1.5)
        )