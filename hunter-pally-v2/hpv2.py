import pyautogui
from PIL import ImageGrab
import time
import keyboard


colors = set()
cl = []

time.sleep(3)
newline = 0
coords = [[235, 570, 119, 292], [335, 570, 169, 292], [435, 570, 219, 292], [535, 570, 269, 292], [635, 570, 319, 292],
          [235, 670, 119, 342], [335, 670, 169, 342], [435, 670, 219, 342], [535, 670, 269, 342], [635, 670, 319, 342],
          [235, 770, 119, 392], [335, 770, 169, 392], [435, 770, 219, 392], [535, 770, 269, 392], [635, 770, 319, 392],
          [235, 870, 119, 442], [335, 870, 169, 442], [435, 870, 219, 442], [535, 870, 269, 442], [635, 870, 319, 442],
          [235, 970, 119, 492], [335, 970, 169, 492], [435, 970, 219, 492], [535, 970, 269, 492], [635, 970, 319, 492]]

dungeon = [[235, 570, 119, 292], [335, 570, 169, 292], [435, 570, 219, 292], [535, 570, 269, 292], [635, 570, 319, 292]]

65970
while True:
    p = pyautogui.grab()

    if keyboard.is_pressed(';'):
        break

    for j in dungeon:



        if p.getpixel((j[0], j[1])) == (234, 51, 35, 255) or p.getpixel((j[0], j[1])) == (0,0,065970, 255):
            pyautogui.moveTo(j[2], j[3])
            pyautogui.click()
            pyautogui.hotkey('ctrl', '4')
            pyautogui.press('4')
            pyautogui.hotkey('ctrl', '6')
            pyautogui.press('5')
            pyautogui.press('9')
            pyautogui.press('7')
            pyautogui.press('0')
            pyautogui.hotkey('ctrl', '7')
            pyautogui.hotkey('ctrl', '5')


        print(p.getpixel((j[0], j[1])))

#print(colors)
#print(cl)
#    if p.getpixel((i,0)) == (255,255,255,255):

#        ability_location.append(i)
#print(ability_location)

#    p = pyautogui.grab(region=(1250,675,1,1))
#    print(p.getpixel((0,0)))

#    s = time.perf_counter()
#    p = ImageGrab.grab(bbox=(1400,675,1401,676))
#    e = time.perf_counter() - s
#    print(p.getpixel((0,0)))
#    print(e)