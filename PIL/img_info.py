from PIL import ImageGrab
import time
from PIL import Image
import pyautogui
import keyboard
import concurrent.futures
import threading
import queue


class Pipeline(queue.Queue):
    def __init__(self):
        super().__init__(maxsize=10)

    def set_message(self, message):
        self.put(message)

    def get_message(self):
        message = self.get()
        return message


def pally_actions(pipeline):
    coords = pipeline.get_message()
    print(f'consuming msg {coords[0], coords[1]}')

    mx = coords[0]
    my = coords[1]
    if mx is None or my is None:
        return

    s = time.perf_counter()
    pyautogui.moveTo(mx, my)
    pyautogui.click()
    pyautogui.hotkey('ctrl', '4')
    pyautogui.hotkey('4')
    pyautogui.hotkey('2')
    pyautogui.hotkey('ctrl', '6')
    pyautogui.hotkey('5')
    pyautogui.hotkey('9')
    pyautogui.hotkey('7')
    pyautogui.hotkey('0')
    pyautogui.hotkey('ctrl', '7')
    # pyautogui.hotkey('ctrl', '5')
    e = time.perf_counter() - s
    print(f'elapsed ability time: {e}')


def check_heal(img, zip_loc, pipeline):
    px = zip_loc[0]
    py = zip_loc[1]
    mx = zip_loc[2]
    my = zip_loc[3]

    if img.getpixel((px, py)) == (234, 51, 35, 255):
        print('heal now!')
        print(f'setting msg to {mx}, {my}')
        pipeline.set_message([mx, my])
    else:
        print('setting msg to None, None')
        pipeline.set_message([None, None])


#time.sleep(0.2)
while True:
    s = time.perf_counter()

    #print('pulled image')
    p = ImageGrab.grab(bbox=(175, 522, 680, 1028))
    pix = p.load()

    raid_px = [[10,10], [110,10], [210,10], [310,10], [410,10],
          [10,110], [110,110], [210,110], [310,110], [410,110],
          [10,210], [110,210], [210,210], [310,210], [410,210],
          [10,310], [110,310], [210,310], [310,310], [410,310],
          [10,410], [110,410], [210,410], [310,410], [410,410]]

    raid_mouse_loc = [[119, 292], [169, 292], [219, 292], [269, 292], [319, 292],
                  [119, 342], [169, 342], [219, 342], [269, 342], [319, 342],
                  [119, 392], [169, 392], [219, 392], [269, 392], [319, 392],
                  [119, 442], [169, 442], [219, 442], [269, 442], [319, 442],
                  [119, 492], [169, 492], [219, 492], [269, 492], [319, 492]]

    dung_px = [[10,10], [110,10], [210,10], [310,10], [410,10]]

    dung_mouse_loc = [[119, 292], [169, 292], [219, 292], [269, 292], [319, 292]]

    zip_loc = zip(dung_px, dung_mouse_loc)

    pipeline = Pipeline()
    pipeline1 = Pipeline()
    pipeline2 = Pipeline()
    pipeline3 = Pipeline()
    pipeline4 = Pipeline()

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as e:
        e.submit(check_heal, p, [10, 10, 119, 292], pipeline)
        e.submit(pally_actions, pipeline)
        e.submit(check_heal, p, [110, 10, 169, 292], pipeline1)
        e.submit(pally_actions, pipeline1)
        e.submit(check_heal, p, [210, 10, 219, 292], pipeline2)
        e.submit(pally_actions, pipeline2)
        e.submit(check_heal, p, [310, 10, 269, 292], pipeline3)
        e.submit(pally_actions, pipeline3)
        e.submit(check_heal, p, [410, 10, 319, 292], pipeline4)
        e.submit(pally_actions, pipeline4)

    e = time.perf_counter() - s
    print(f'elapsed: {e}')



#p.save('test.png')

#colors = set()
#img = Image.open("test.png", "r")

#print(img.size)

#print(pix[10,10])
#print(pix[110,10])
#print(pix[210,10])
#print(pix[310,10])
#print(pix[410,10])

# (117, 250, 76, 255) healthy
# (234, 51, 35, 255) needs heal

# row 1
#pix[10,10] = (0,0,0,255)
#print(p.getpixel((10,10)) == (117, 250, 76, 255))
#pix[110,10] = (0,0,0,255)
#pix[210,10] = (0,0,0,255)
#pix[310,10] = (0,0,0,255)
#pix[410,10] = (0,0,0,255)

# row 2
#pix[10,110] = (0,0,0,255)
#pix[110,110] = (0,0,0,255)
#pix[210,110] = (0,0,0,255)
#pix[310,110] = (0,0,0,255)
#pix[410,110] = (0,0,0,255)

# row 3
#pix[10,210] = (0,0,0,255)
#pix[110,210] = (0,0,0,255)
#pix[210,210] = (0,0,0,255)
#pix[310,210] = (0,0,0,255)
#pix[410,210] = (0,0,0,255)

# row 4
#pix[10,310] = (0,0,0,255)
#pix[110,310] = (0,0,0,255)
#pix[210,310] = (0,0,0,255)
#pix[310,310] = (0,0,0,255)
#pix[410,310] = (0,0,0,255)

# row 5
#pix[10,410] = (0,0,0,255)
#pix[110,410] = (0,0,0,255)
#pix[210,410] = (0,0,0,255)
#pix[310,410] = (0,0,0,255)
#pix[410,410] = (0,0,0,255)
#img.save('edited_v1.png')