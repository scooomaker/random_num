import random
import pyglet
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


countAll = []

numbers = list(range(1, 27))

window = pyglet.window.Window()
pyglet.gl.glClearColor(1,1,1,1)


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
    countAll.append(num)
    


pyglet.app.run()

COUNTS = Counter(countAll)
total_count = len(countAll)  
for number, count in COUNTS.items():
    probability = (count / total_count)*100  
    print(f"数字 {number} 的出现概率为 {probability:.2f} %")
print(countAll)



mean = np.mean(numbers)  # 计算数组的均值
std = np.std(numbers)  # 计算数组的标准差

x = np.linspace(mean - 3*std, mean + 3*std, 100)  # 生成 x 轴的数据
y = np.exp(-0.5 * ((x - mean) / std) ** 2) / (std * np.sqrt(2 * np.pi))  # 计算 y 轴的数据

plt.plot(x, y)
plt.show()


plt.hist(COUNTS)
plt.show()