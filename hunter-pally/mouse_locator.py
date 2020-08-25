import pyautogui

while True:
    x, y = pyautogui.position()
    print(f'x: {x}, y: {y}')
    print(pyautogui.pixel(x, y))
