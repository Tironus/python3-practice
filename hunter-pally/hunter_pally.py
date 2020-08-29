import pyautogui
from PIL import ImageGrab
import random
import time
import threading
import concurrent.futures
import queue

thread_local = threading.local()

random_timings = [0.4, 0.33, 0.43, 0.34]

combat = False
reckoning = False
healer = False
holy_power = False
inquisition_present = False

producer_pipeline = []
consumer_pipeline = []

number_of_threads = 0

class Pipeline(queue.Queue):
    def __init__(self):
        super().__init__(maxsize=10)

    def set_message(self, message):
        self.put(message)
        producer_pipeline.append(message)

    def get_message(self):
        message = self.get()
        consumer_pipeline.append(message)
        return message

class CombatVars():
    def __init__(self):
        self.combat = False
        self.combat_coords = [1,0]
        self.reckoning = False
        self.reckoning_coords = [392,0]
        self.healer = False
        self.healer_coords = [309,0]
        self.holy_power = False
        self.holy_power_coords = [142,0]
        self.inquisition_present = False
        self.inquisition_coords = [63,0]
        self.img = None

    def update_combat(self, status):
        self.combat = status

    def update_reckoning(self, status):
        self.reckoning = status

    def update_healer(self, status):
        self.healer = status

    def update_holy_power(self, status):
        self.holy_power = status

    def update_inquisition(self, status):
        self.inquisition_present = status

    def update_img(self, img):
        self.img = img

def producer(pipeline, combat_info):
    global number_of_threads
    number_of_threads += 1
    coords_list = [[1,0], [392,0], [309,0], [142,0], [63,0]]
    message = get_pixel(combat_info, coords_list)
    pipeline.set_message(message)
    print(f'placing {message} on pipeline\n')
    print(f'number of threads: {number_of_threads}')
    number_of_threads -= 1


def consumer(pipeline):
    global number_of_threads
    number_of_threads += 1
    message = pipeline.get_message()
    print(f'consuming message {message}')

    combat_obj = message

    if combat_obj.combat is True:
        print('FIGHT!')
        if combat_obj.reckoning is True:
            pyautogui.hotkey('6')  # reckoning (pvp)

        if combat_obj.healer is True:
            pyautogui.hotkey('5')  # selfless healer

        if combat_obj.holy_power is True:
            if combat_obj.inquisition_present is False:
                pyautogui.hotkey('2')  # Inquisition

        pyautogui.hotkey('ctrl', '6')  # hand of hinderance
        pyautogui.hotkey('7')  # avenging wrath
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', '2')  # templars verdict
        pyautogui.hotkey('4')  # wake of ashes
        pyautogui.hotkey('ctrl', '4')  # blade of justice
        pyautogui.hotkey('ctrl', '5')  # judgement
        pyautogui.hotkey('3')  # hammer of wrath
        pyautogui.hotkey('1')  # crusader strike
    number_of_threads -= 1
    print(f'number of threads: {number_of_threads}')


def get_pixel(cmbt_info, cmbt_coords):
    print('entering get pixel')
    img = cmbt_info.img
    for c in cmbt_coords:
        if img.getpixel((c[0], c[1])) == (255,255,255,255):
            if c[0] == 1:
                print('updating combat to True')
                cmbt_info.update_combat(True)
            elif c[0] == 392:
                print('updating reckoning to True')
                cmbt_info.update_reckoning(True)
            elif c[0] == 309:
                print('updating healer to True')
                cmbt_info.update_healer(True)
            elif c[0] == 142:
                print('updating holy power to True')
                cmbt_info.update_holy_power(True)
            elif c[0] == 63:
                print('updating inquisition to True')
                cmbt_info.update_inquisition(True)
        else:
            if c[0] == 1:
                cmbt_info.update_combat(False)
            elif c[0] == 392:
                cmbt_info.update_reckoning(False)
            elif c[0] == 309:
                cmbt_info.update_healer(False)
            elif c[0] == 142:
                cmbt_info.update_holy_power(False)
            elif c[0] == 63:
                cmbt_info.update_inquisition(False)
    return cmbt_info


try:
    number_of_threads += 1
    while True:
        s = time.perf_counter()
        pipeline = Pipeline()
        event = threading.Event()
        combat_info = CombatVars()
        # combat starts
        combat_info.update_img(ImageGrab.grab(bbox=(1250,675,3250,677)))
        print('entering pipeline')
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            executor.submit(producer, pipeline, combat_info)
            executor.submit(consumer, pipeline)

        e = time.perf_counter() - s
        print(f'time elapsed: {e}')

except KeyboardInterrupt:
    print('hunting has ended')