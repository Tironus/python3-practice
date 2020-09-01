from PIL import ImageGrab
import time
from PIL import Image
import pyautogui


def check_heal(img, zip_loc):
    px = zip_loc[0][0]
    py = zip_loc[0][1]
    mx = zip_loc[1][0]
    my = zip_loc[1][1]

    if img.getpixel((px, py)) == (234, 51, 35, 255):
        pyautogui.moveTo(mx, my)
        pyautogui.click()
        pyautogui.hotkey('ctrl', '4')
        pyautogui.press('4')
        pyautogui.press('2')
        pyautogui.hotkey('ctrl', '6')
        pyautogui.press('5')
        pyautogui.press('9')
        pyautogui.press('7')
        pyautogui.press('0')
        pyautogui.hotkey('ctrl', '7')
        #pyautogui.hotkey('ctrl', '5')
    else:
        print('no heal needed')

#time.sleep(4)
while True:
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

    for z in zip_loc:
        check_heal(p, z)




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
pix[10,410] = (0,0,0,255)
pix[110,410] = (0,0,0,255)
pix[210,410] = (0,0,0,255)
pix[310,410] = (0,0,0,255)
pix[410,410] = (0,0,0,255)
#img.save('edited_v1.png')