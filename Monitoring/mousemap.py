from pynput import mouse
import keyboard
import matplotlib.pyplot as plt
import time


class MouseMap:

    def __init__(self):
        self.position = None
        self.mouse1 = mouse.Controller()

    def mouse_out(self):
        pos = self.mouse1.position
        return pos

    def plot(self):
        x = []
        y = []
        b = True
        while b:
            a = self.mouse_out()
            x.append(a[0])
            y.append(-a[1])
            if keyboard.is_pressed('F7'):
                b = False
            time.sleep(0.01)

        plt.plot(x, y)
        plt.show()


MouseMap().plot()
