import pyautogui
import time
from pynput import keyboard

def get_mouse_position():
    """
    Get the current mouse cursor position.
    Returns a tuple (x, y) representing the coordinates.
    """
    return pyautogui.position()

# Flag to control whether the clicker is running or paused
clicker_running = True
paused = False
enterpress = False
# Listener for keyboard events
def on_key_press(key):
    global clicker_running
    global paused
    global enterpress
    if key == keyboard.Key.esc:
        clicker_running = False
        print("User Interrupted. Exiting...")
    elif key == keyboard.Key.enter:
        enterpress = True
    elif key == keyboard.KeyCode.from_char('p'):
        # Toggle the clicker state (pause/unpause)
        if paused == True:
            paused = False
            print("Clicker Continues")
        else:
            paused = True
            print("User Paused")

# Wait for the user to input the number of clicks.
numClicks = input("How Many Clicks You Want? ")

try:
    numClicks = int(numClicks)
except ValueError:
    print("Please insert a valid integer for the number of clicks.")
    exit()

posList = []

# Gather mouse positions for each click
with keyboard.Listener(on_press=on_key_press) as listener:
    for i in range(numClicks):
        print("Move the mouse to the desired position and press Enter.")
        while enterpress == False:
            continue
        position = get_mouse_position()
        posList.append(position)
        enterpress = False

# Set up the keyboard listener
with keyboard.Listener(on_press=on_key_press) as listener:
    print("Pause clicker with pressing 'P' and abort with pressing 'ESC'")
    while clicker_running:
        if paused == False:
            for i in range(numClicks):
                if paused == True:
                    continue
                if clicker_running == False:
                    break
                position = posList[i]
                pyautogui.click(position[0], position[1], clicks=1, interval=0.5)

# Stop the listener
listener.stop()