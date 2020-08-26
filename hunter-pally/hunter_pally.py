import pyautogui
from PIL import ImageGrab
import random
import time

random_timings = [0.4, 0.53, 0.64, 0.75]

try:
    while True:
        s = time.perf_counter()
        # combat starts 1
        combat = ImageGrab.grab(bbox=(1250,675,3250,677))
        if combat.getpixel((1,0)) == (255,255,255,255):
            # begin combat
            print('FIGHT!')

            # wrath 224
            if combat.getpixel((224,0)) == (255,255,255,255):
                print('cast avenging wrath')
                pyautogui.hotkey('7')

            # reckoning 392
            if combat.getpixel((392,0)) == (255,255,255,255):
                print('cast reckoning')
                pyautogui.hotkey('6')

            # selfless healer 309
            if combat.getpixel((309,0)) == (255,255,255,255):
                print('cast selfless healer')
                pyautogui.hotkey('5')

            # hand of hinderance 471
            if combat.getpixel((471,0)) == (255,255,255,255):
                print('cast hand of hinderance')
                pyautogui.hotkey('ctrl', '6')

            # holy power 135
            if combat.getpixel((142,0)) == (255,255,255,255):

                # inquisition 63
                if combat.getpixel((63,0)) == (255, 255, 255, 255):
                    print('inquisition running')
                else:
                    print('cast inquisition')
                    pyautogui.hotkey('2')
                print('cast templars verdict')
                pyautogui.hotkey('3')
                pyautogui.hotkey('ctrl', '2')
            else:
                if combat.getpixel((63,0)) == (255, 255, 255, 255):
                    print('inquisition running')
                else:
                    print('cast inquisition')
                    pyautogui.hotkey('2')
                print('light grant me power!')
                pyautogui.hotkey('3')
                pyautogui.hotkey('ctrl', '4')
                pyautogui.hotkey('ctrl', '5')
                pyautogui.hotkey('4')
                pyautogui.hotkey('1')
            e = time.perf_counter() - s
            print(f'time elapsed: {e}')
        else:
            # no combat
            print('looking for prey...')
except KeyboardInterrupt:
    print('hunting has ended')