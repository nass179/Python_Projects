from pynput import mouse
import keyboard
import matplotlib.pyplot as plt
import time
import numpy as np


class MouseMap:

    def __init__(self):
        self.position = None
        self.mouse1 = mouse.Controller()

    def mouse_out(self):
        pos = self.mouse1.position
        return pos

    def plot(self):
        mouse_positions = []
        b = True
        while b:
            a = self.mouse_out()
            mouse_positions.append((a[0], -a[1]))
            if keyboard.is_pressed('F7'):
                b = False
            time.sleep(0.01)

        x, y = zip(*mouse_positions)
        heatmap, xedges, yedges = np.histogram2d(x, y, bins=100)

        dpi = 100
        plt.figure(figsize=(1920 / dpi, 1080 / dpi), dpi=dpi)
        plt.clf()

        plt.imshow(heatmap.T, origin='lower', cmap='hot', interpolation='nearest')
        plt.colorbar()
        plt.title('Mouse Movement Heatmap')
        #plt.xlim([0, 1920])
        #plt.ylim([0, 1080])
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.gca().set_aspect(1080 / 1920)
        plt.show()


MouseMap().plot()
