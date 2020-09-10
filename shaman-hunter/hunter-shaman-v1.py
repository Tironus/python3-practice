import pyautogui
import time
import keyboard


def shaman_rotation(rotation_type):
    if rotation_type == 'multi':
        dps_rotation = [
            ['ctrl', '4', 'Crash Lightning'],
            [None, '1', 'Flametongue Weapon'],
            [None, '2', 'Feral Sprit'],
            [None, '3', 'StormStrike'],
            [None, '4', 'Sundering'],
            [None, '5', 'Rockbiter'],
            [None, '6', 'Lava Lash']
        ]
    else:
        dps_rotation = [
            [None, '1', 'Flametongue Weapon'],
            [None, '2', 'Feral Sprit'],
            [None, '3', 'StormStrike'],
            [None, '4', 'Sundering'],
            [None, '5', 'Rockbiter'],
            [None, '6', 'Lava Lash']
        ]

    for _ in dps_rotation:
        execute_spell(_)


def execute_spell(spell):
    print(f'processing spell: {spell[2]}')
    start = time.perf_counter()
    if spell[0] is None:
        pyautogui.keyDown(spell[1])
        pyautogui.keyUp(spell[1])
    else:
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown(spell[1])
        pyautogui.keyUp(spell[1])
        pyautogui.keyUp('ctrl')

    elapsed = time.perf_counter() - start
    print(f'spell processing time: {elapsed}')

pyautogui.FAILSAFE = False
while True:
    if keyboard.is_pressed('7'):
        while True:
            if keyboard.is_pressed('['):
                break

            start = time.perf_counter()
            shaman_rotation('single')
            time.sleep(0.6)
            elapsed = time.perf_counter() - start
            print(f'rotation time: {elapsed}')

    if keyboard.is_pressed('8'):
        while True:
            if keyboard.is_pressed('['):
                break

            start = time.perf_counter()
            shaman_rotation('multi')
            time.sleep(0.6)
            elapsed = time.perf_counter() - start
            print(f'rotation time: {elapsed}')
