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
        self.put(message, block=False)

    def get_message(self):
        message = self.get(block=False)
        return message

    def get_qsize(self):
        return self.qsize()


def pally_actions(pipeline):
    start = time.perf_counter()
    print(f'queue size: {pipeline.get_qsize()}')
    for _ in range(pipeline.get_qsize()):
        coords = pipeline.get_message()
        print(f'consuming msg {coords[0], coords[1]}')

        s = time.perf_counter()
        pyautogui.moveTo(coords[0], coords[1])
        pyautogui.click()
        keyboard.press_and_release('4')
        keyboard.press_and_release('ctrl', '4')
        keyboard.press_and_release('2')
        keyboard.press_and_release('ctrl', '6')
        #keyboard.press_and_release('5')
        keyboard.press_and_release('9')
        keyboard.press_and_release('7')
        keyboard.press_and_release('0')
        keyboard.press_and_release('ctrl', '7')
        pyautogui.hotkey('ctrl', '5')
        e = time.perf_counter() - s
        print(f'elapsed ability time: {e}')
        time.sleep(0.2)
        elapsed = time.perf_counter() - start

        if elapsed > 1.3:
            return


def check_heal(img, zip_loc, pipeline):
    px = zip_loc[0][0]
    py = zip_loc[0][1]
    mx = zip_loc[1][0]
    my = zip_loc[1][1]

    if img.getpixel((px, py)) == (234, 51, 35, 255):
        print('heal now!')
        print(f'setting msg to {mx}, {my}')
        pipeline.set_message([mx, my])
    else:
        print('no healing needed')
        pass


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

    zip_loc = zip(raid_px, raid_mouse_loc)

    pipeline = Pipeline()

    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as e:
        for z in zip_loc:
            e.submit(check_heal, p, z, pipeline)
        #e.submit(check_heal, p, [110, 10, 169, 292], pipeline)
        #e.submit(check_heal, p, [210, 10, 219, 292], pipeline)
        #e.submit(check_heal, p, [310, 10, 269, 292], pipeline)
        #e.submit(check_heal, p, [410, 10, 319, 292], pipeline)

    pally_actions(pipeline)
    print(f'queue size: {pipeline.get_qsize()}')
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