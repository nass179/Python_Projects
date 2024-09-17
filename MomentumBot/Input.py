import time
from pynput.keyboard import Controller, Listener, Key
import threading
class MomentumBot:
    def __init__(self):
        self.keyboard = Controller()
        self.start_listener()
        self.running = True

    def press(self, key, secs):
        print("Pressing and holding " + key + " for 5 seconds")
        self.keyboard.press(key)
        time.sleep(secs)
        self.keyboard.release(key)
        print(key + " released after 5 seconds")

    def on_press(self, key):
        if key == Key.f7:
            exit('0')
        if key == Key.f8:
            print("F8 pressed - triggering press()")
            self.press('w', 3)
            self.press('a', 1.5)
            self.press('w', 10)
            self.press('a', 5)
            self.press('s', 8)
            self.press('d', 2)
            self.press('s', 3)
            self.press('a', 13)

    def start_listener(self):
        listener = Listener(on_press=self.on_press)
        listener.start()
        listener.join()
MomentumBot()
