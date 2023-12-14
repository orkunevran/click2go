import pyautogui
import time

def get_mouse_position():
    """
    Get the current mouse cursor position.
    Returns a tuple (x, y) representing the coordinates.
    """
    return pyautogui.position()

# Example usage:
# Wait for the user to input the number of clicks.
numClicks = input("How Many Clicks You Want? ")

try:
    numClicks = int(numClicks)
except ValueError:
    print("Please insert a valid integer for the number of clicks.")
    exit()

loop = True
posList = []

# Gather mouse positions for each click
for i in range(numClicks):
    input("Move the mouse to the desired position and press Enter.")
    position = get_mouse_position()
    posList.append(position)

# Perform clicks
try:
    while loop:
        for i in range(numClicks):
            position = posList[i]
            pyautogui.click(position[0], position[1], clicks=1, interval=0.5)
except:
    print("User Interrupted..Exiting")
    exit()