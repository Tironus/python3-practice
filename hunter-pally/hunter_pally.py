import pyautogui
from PIL import ImageGrab
import random
import time

random_timings = [0.4, 0.33, 0.43, 0.34]
reckoning = False
healer = False
holy_power = False
inquisition_present = False

try:
    while True:
        s = time.perf_counter()
        # combat starts 1
        combat = ImageGrab.grab(bbox=(1250,675,3250,677))
        if combat.getpixel((1,0)) == (255,255,255,255):
            # begin combat
            print('FIGHT!')

            # reckoning 392
            if combat.getpixel((392,0)) == (255,255,255,255):
                reckoning = True
            else:
                reckoning = False

            # selfless healer 309
            if combat.getpixel((309,0)) == (255,255,255,255):
                healer = True
            else:
                healer = False

            # holy power at 3 or more charges present 142
            if combat.getpixel((142, 0)) == (255, 255, 255, 255):
                holy_power = True
            else:
                holy_power = False

            # inquisition present 63
            if combat.getpixel((63, 0)) == (255, 255, 255, 255):
                inquisition_present = True
            else:
                inquisition_present = False

            if reckoning is True:
                pyautogui.hotkey('6')       # reckoning (pvp)

            if healer is True:
                pyautogui.hotkey('5')       # selfless healer

            if holy_power is True:
                if inquisition_present is False:
                    pyautogui.hotkey('2')   # Inquisition

            pyautogui.hotkey('ctrl', '6')   # hand of hinderance
            pyautogui.hotkey('7')           # avenging wrath
            pyautogui.hotkey('ctrl', '2')   # templars verdict
            pyautogui.hotkey('4')           # wake of ashes
            pyautogui.hotkey('ctrl', '4')   # blade of justice
            pyautogui.hotkey('ctrl', '5')   # judgement
            pyautogui.hotkey('3')           # hammer of wrath
            pyautogui.hotkey('1')           # crusader strike

            # hand of hinderance 471
            #if combat.getpixel((471,0)) == (255,255,255,255):
            #    print('cast hand of hinderance')
            #    pyautogui.hotkey('ctrl', '6')

            e = time.perf_counter() - s
            print(f'time elapsed: {e}')
        else:
            # no combat
            print('looking for prey...')
            reckoning = False
            healer = False
            holy_power = False
            inquisition_present = False
except KeyboardInterrupt:
    print('hunting has ended')