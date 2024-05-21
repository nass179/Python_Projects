from pynput import mouse
from pynput import keyboard
import matplotlib.pyplot as plt
import time


class MouseMap:


    def __init__(self):
        self.position = None
        self.mouse1 = mouse.Controller()
    def on_release(key):
        print(key)
        if key == keyboard.Key.esc:
            return "ye"

    def mouse_out(self):
        pos = self.mouse1.position
        return pos
    def plot(self):
        x = []
        y = []
        '''while self.on_release() != "ye":
            a = self.mouse_out()
            x.append(a[0])
            y.append(-a[1])
            time.sleep(0.1)'''
        for i in range(100):
            a = self.mouse_out()
            x.append(a[0])
            y.append(-a[1])
            time.sleep(0.1)
        plt.plot(x, y)
        plt.show()

    '''with keyboard.Listener(on_release=on_release) as listener:
        listener.join()'''


MouseMap().plot()
