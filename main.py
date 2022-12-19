import random
import pyglet

numbers = list(range(1, 27))

window = pyglet.window.Window()
pyglet.gl.glClearColor(1,1,1,1)

window.set_caption('random for 1 to 26')


label = pyglet.text.Label(text='', font_size=90, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center',color=(0, 0, 0, 255))

@window.event
def on_draw():
    window.clear()
    label.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    num = random.choice(numbers)
    while num == label.text:
        num = random.choice(numbers)
    label.text = str(num)
    


pyglet.app.run()
