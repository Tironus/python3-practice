from PIL import Image
import numpy
from numpy import asarray
from PIL import ImageGrab
import time
from pynput.keyboard import Key, Controller as KeyboardController
import pyautogui
import concurrent.futures

# load the image
#time.sleep(4)

#image = Image.open('test_copy.png')
# convert image to numpy array
#data = asarray(image)
#data = asarray(ImageGrab.grab(bbox=(175, 522, 680, 1028)))

#img.save('image2.png')
def rotation(mouse_coords):
    start = time.perf_counter()
    pyautogui.moveTo(mouse_coords[0], mouse_coords[1])
    pyautogui.click()
    rotation = [['4', None], [None, '4'], ['2', None], [None, '6'], ['9', None], ['7', None], [None, '7'],
                ['0', None], ['5', None]]

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as e:
        for _ in rotation:
            e.submit(rotation_action, _)

    elapsed = time.perf_counter() - start
    print(f'elapsed rotation time: {elapsed}')

def rotation_action(_):
    if _[1] is None:
        pyautogui.keyDown(_[0])
        pyautogui.keyUp(_[0])
        print(f'pressing: {_[0]}')
    else:
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown(_[1])
        pyautogui.keyUp(_[1])
        pyautogui.keyUp('ctrl')
        print(f'pressing: ctrl+{_[1]}')

def check_heal(data, coords):
    heal = numpy.array([234, 51, 35, 255])
    if numpy.array_equal(heal, data[coords[1],coords[0]]):
        return True

def process_players(data, coords):
    need_heal = check_heal(data, [coords[0][0], coords[0][1]])
    if need_heal:
        rotation([coords[1][0], coords[1][1]])

dung = [[10, 10], [10,110], [10,210], [10,310], [10,410]]
dung_mouse_loc = [[119, 292], [169, 292], [219, 292], [269, 292], [319, 292]]

dung_zip = zip(dung, dung_mouse_loc)
while True:
    start = time.perf_counter()
    img = ImageGrab.grab(bbox=(175, 522, 680, 600))
    data = asarray(img)
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as e:
        for _ in dung_zip:
            e.submit(process_players, data, _)

    elapsed = time.perf_counter() - start
    print(f'total cycle: {elapsed}')
#print(data[10, 10])

#print(type(data))

#print(data[10,110])
#print(data[10,210])
#print(data[10,310])
#print(data[10,410])