from ursina import *

def update():
    # Game update logic
    pass

def input(key):
    if key == 'escape':
        application.quit()

app = Ursina()

# Add your game entities and logic here

app.run()
