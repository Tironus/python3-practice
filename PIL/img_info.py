from PIL import ImageGrab
import time
from PIL import Image
import pyautogui
import keyboard
import concurrent.futures
import threading
import queue

class Pipeline(queue.PriorityQueue):
    def __init__(self):
        super().__init__(maxsize=10)

    def set_message(self, p_message):
        self.put(p_message, block=False)

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
        print(f'consuming msg {coords}')

        rotation = [['4',None], ['ctrl', '4'], ['2', None], ['ctrl', '6'], ['9', None], ['7', None], ['ctrl', '7'], ['0', None], ['5', None]]
        s = time.perf_counter()
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as e:
            for _ in rotation:
                e.submit(pally_rotation, coords, _)
        e = time.perf_counter() - s
        print(f'elapsed ability time: {e}')

    elapsed = time.perf_counter() - start

def pally_rotation(coords, button):
    pyautogui.moveTo(coords[1][0], coords[1][1])
    pyautogui.click()
    if button[1] is None:
        pyautogui.keyDown(button[0])
        pyautogui.keyUp(button[0])
    else:
        pyautogui.keyDown(button[0])
        pyautogui.keyDown(button[1])
        pyautogui.keyUp(button[1])
        pyautogui.keyUp(button[0])


def check_heal(img, data, pipeline):
    rx = data[0]
    ry = data[1]
    px = data[2]
    py = data[3]
    mx = data[4]
    my = data[5]

    heal = False
    priority = False

    if img.getpixel((px, py)) == (0, 0, 0, 255):
        print('priority heal')
        priority = True

    if img.getpixel((rx, ry)) == (234, 51, 35, 255):
        print('regular heal')
        heal = True

    if heal is True:
        if priority is True:
            print(f'setting msg to (1, {mx}, {my})')
            pipeline.set_message((1, [mx, my]))
        else:
            print(f'setting msg to (5, {mx}, {my})')
            pipeline.set_message((5, [mx, my]))
    else:
        print('no heal needed')




while True:
    pipeline = Pipeline()
    s = time.perf_counter()

    #print('pulled image')
    p = ImageGrab.grab(bbox=(175, 522, 680, 1028))
    pix = p.load()

    raid_px = [[10,10], [110,10], [210,10], [310,10], [410,10],
               [10,110], [110,110], [210,110], [310,110], [410,110],
               [10,210], [110,210], [210,210], [310,210], [410,210],
               [10,310], [110,310], [210,310], [310,310], [410,310],
               [10,410], [110,410], [210,410], [310,410], [410,410]]

    priority_raid_px = [[10,50], [110,50], [210,50], [310,50], [410,50],
                        [10,150], [110,150], [210,150], [310,150], [410,150],
                        [10,250], [110,250], [210,250], [310,250], [410,250],
                        [10,350], [110,350], [210,350], [310,350], [410,350],
                        [10,450], [110,450], [210,450], [310,450], [410,450]]

    raid_mouse_loc = [[119, 292], [169, 292], [219, 292], [269, 292], [319, 292],
                      [119, 342], [169, 342], [219, 342], [269, 342], [319, 342],
                      [119, 392], [169, 392], [219, 392], [269, 392], [319, 392],
                      [119, 442], [169, 442], [219, 442], [269, 442], [319, 442],
                      [119, 492], [169, 492], [219, 492], [269, 492], [319, 492]]

    raid_data = [
        [10,10, 10,50, 119,292], [10,110, 10,150, 119,342], [10,210, 10,250, 119,392], [10,310, 10,350, 119,442], [10,410, 10,450, 119,492],
        [110,10, 110,50, 169,292], [110,110, 110,150, 169,342], [110,210, 110,250, 169,392], [110,310, 110,350, 169,442], [110,410, 110,450, 169,492],
        [210,10, 210,50, 219,292], [210,110, 210,150, 219,342], [210,210, 210,250, 219,392], [210,310, 210,350, 219,442], [210,410, 210,450, 219,492],
        [310,10, 310,50, 269,292], [310,110, 310,150, 269,342], [310,210, 310,250, 269,392], [310,310, 310,350, 269,442], [310,410, 310,450, 269,492],
        [410,10, 410,50, 319,292], [410,110, 410,150, 319,342], [410,210, 410,250, 319,392], [410,310, 410,350, 319,442], [410,410, 410,450, 319,492]
    ]

    dung_px = [[10,10], [110,10], [210,10], [310,10], [410,10]]

    priority_dung_px = [[10,50], [110,50], [210,50], [310,50], [410,50]]

    dung_mouse_loc = [[119, 292], [169, 292], [219, 292], [269, 292], [319, 292]]

    dung_data = [
        [10,10, 10,50, 119,292], [110,10, 110,50, 169, 292], [210,10, 210,50, 219, 292], [310,10, 310,50, 269, 292], [410,10, 410,50, 319, 292]
    ]

    priority_zip = zip(priority_dung_px, dung_mouse_loc)
    zip_loc = zip(dung_px, dung_mouse_loc)

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as e:
        for z in dung_data:
            e.submit(check_heal, p, z, pipeline)
        e.submit(pally_actions, pipeline)

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
