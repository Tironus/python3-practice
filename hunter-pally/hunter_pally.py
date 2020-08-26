import pyautogui
from PIL import ImageGrab

try:
    while True:
        # combat starts
        combat = ImageGrab.grab(bbox=(1250, 675, 1251, 676))
        if combat.getpixel((0,0)) == (255,255,255,255):
            # begin combat
            print('FIGHT!')
            inquisition = ImageGrab.grab(bbox=(1315,675,1316,676))
            if inquisition.getpixel((0,0)) == (255,255,255,255):
                print('inquisition running')
            else:
                print('cast inquisition')
                pyautogui.hotkey('2')
        else:
            # no combat
            print('looking for prey...')
except KeyboardInterrupt:
    print('hunting has ended')