import random
import pyglet
from collections import Counter

countAll = []

numbers = list(range(1, 27))

window = pyglet.window.Window()

label = pyglet.text.Label(text='', font_size=90, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    label.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    num = random.choice(numbers)
    # while num == label.text:
    #     num = random.choice(numbers)
    label.text = str(num)
    countAll.append(num)
    

# 运行程序
pyglet.app.run()

COUNTS = Counter(countAll)
total_count = len(countAll)  # 计算数组的长度
for number, count in COUNTS.items():
    probability = count / total_count  # 计算数字的出现概率
    print(f"数字 {number} 的出现概率为 {probability:.2f}")
print(countAll)