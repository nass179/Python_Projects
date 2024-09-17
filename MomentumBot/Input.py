import time
from pynput.keyboard import Controller, Listener, Key
from pynput.mouse import Controller as MouseController, Button
import threading
import pydirectinput

class MomentumBot:
    def __init__(self):
        self.keyboard = Controller()
        self.running = True
        self.action_thread = None  # To keep track of the thread running actions
        self.start_listener()

    def press(self, key, secs):
        if self.running:
            print(f"Pressing and holding {key} for {secs} seconds")
            self.keyboard.press(key)
            time.sleep(secs)
            self.keyboard.release(key)
            print(f"{key} released after {secs} seconds")

    def move_mouse_left_smooth(self, total_pixels, steps):
        if self.running:
            move_per_step = total_pixels // steps
            for _ in range(steps):
                pydirectinput.moveRel(-move_per_step, 0)
                time.sleep(0.001)
    def perform_actions(self):
        # Key press sequence
        a = 0.42
        self.press('w', 3)
        self.press(Key.left, a)
        self.press('w', 1.5)
        self.press(Key.right, a)
        self.press('w', 10)
        self.press(Key.left, a)
        self.press('w', 5)
        self.press(Key.left, a)
        self.press('w', 8)
        self.press(Key.left, a)
        self.press('w', 1.5)
        self.press(Key.right, a)
        self.press('w', 2)
        self.press(Key.right, a)
        self.press('a', 13)

    def on_press(self, key):
        if key == Key.f7:
            print("F7 pressed - stopping bot")
            self.running = False  # Stop the bot safely
            if self.action_thread and self.action_thread.is_alive():
                self.action_thread.join()  # Wait for the action thread to finish
            return False  # Stop the listener as well

        if key == Key.f8 and self.running:
            print("F8 pressed - triggering press()")
            # Run the key press sequence in a separate thread
            self.action_thread = threading.Thread(target=self.perform_actions)
            self.action_thread.start()

    def start_listener(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()  # Keep the listener running

MomentumBot()