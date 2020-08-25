import time
import json
import asyncio
import pyautogui


async def worker():
    combat = pyautogui.locateOnScreen('combat.png', confidence=0.9, region=(1213, 652, 900, 80))
    if combat is None:
        print('looking for prey')
    else:
        print('begin the hunt')
        inquisition = pyautogui.locateOnScreen('inquisition.png', confidence=0.9, region=(1213, 652, 900, 80))
        if inquisition is None:
            print('cast inquisition!')
            pyautogui.hotkey('ctrl', '5')
            pyautogui.hotkey('2')
        else:
            print('holy powa!')

        time.sleep(0.5)

        avenge = pyautogui.locateOnScreen('avenge.png', confidence=0.9, region=(1213, 652, 900, 80))
        if avenge is None:
            print('vengeance is coming')
        else:
            print('vengeance is mine!')
            pyautogui.hotkey('7')

        holy_power = pyautogui.locateOnScreen('holy_power.png', confidence=0.9, region=(1213, 652, 900, 80))
        if holy_power is None:
            print('light bless me with strength')
            pyautogui.hotkey('4')
            pyautogui.hotkey('ctrl', '4')
            pyautogui.hotkey('1')
            pyautogui.hotkey('ctrl', '5')
        else:
            print('lights justice!')
            pyautogui.hotkey('ctrl', '2')

async def main():
    try:
        while True:
            await asyncio.gather(worker())
    except KeyboardInterrupt:
        print('hunting has ended')

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start_time
    print(f'elapased time {elapsed}')
