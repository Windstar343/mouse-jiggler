import pyautogui
import threading
import time
import random
from pynput import keyboard

pyautogui.FAILSAFE = False

move_mouse = False

def wiggle_mouse():
    while move_mouse:
        x, y = pyautogui.position()
        x += random.randint(-100, 100)
        y += random.randint(-100, 100)
        pyautogui.moveTo(x, y, duration=1)
        time.sleep(3)

def on_press(key):
    global move_mouse
    try:
        if key == keyboard.Key.f5:
            move_mouse = not move_mouse
            if move_mouse:
                print("Mouse jiggler started. Press F5 to stop.")
                threading.Thread(target=wiggle_mouse).start()
            else:
                print("Mouse jiggler stopped. Press F5 to start.")
    except AttributeError:
        pass

print("Press F5 to start/stop the mouse jiggler.")
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()