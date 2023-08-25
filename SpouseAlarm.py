import pystray
import os, sys, reg

from winreg import CreateKey, SetValueEx, QueryValueEx
from time import sleep
from pystray import Menu, MenuItem
from PIL import Image
from threading import Thread

from Detect import *

state, detector, is_run, is_startup = None, None, None, None

def get_icon_image():
    image = Image.open("./icon/icon.ico")
    return image

def get_state(i):
    def inner(MenuItem):
        return state == i
    return inner

def switch_broadcaster():
    global state, detector
    state = 0
    detector = DetectorByBroadCaster()

def switch_title_changed():
    global state, detector
    state = 1
    detector = DetectorByTitleChanged()

def switch_stream():
    global state, detector
    state = 2
    detector = DetectorByStream()

def quit(sub):
    def inner(icon, item):
        global is_run
        is_run = False

        icon.stop()
    return inner

def detect():
    while(is_run):
        if detector.detect():
            detector.alarm()
        
        sleep(5)

def switch_startup():
    global is_startup
    
    if is_startup:
        reg.clean_startup()
        is_startup = False
    else:
        reg.set_startup()
        is_startup = True

if __name__ == '__main__':
    try:
        os.chdir(sys._MEIPASS)
    except:
        os.chdir(os.getcwd())

    state = 2
    detector = DetectorByStream()
    is_run = True
    is_startup = reg.is_registered_startup()

    detect_sub = Thread(target=detect)

    icon = pystray.Icon(
        'SpouseAlarm',
        get_icon_image(),
        '서방님알람기',
        menu = Menu(
            MenuItem(
                '기준',
                Menu(
                    MenuItem(
                        '브로드캐스터',
                        switch_broadcaster,
                        checked=get_state(0),
                        radio=True
                    ),
                    MenuItem(
                        '방제',
                        switch_title_changed,
                        checked=get_state(1),
                        radio=True
                    ),
                    MenuItem(
                        '방송 시작',
                        switch_stream,
                        checked=get_state(2),
                        radio=True
                    )
                )
            ),
            MenuItem('시작',
                     switch_startup,
                     checked=lambda item: is_startup),
            MenuItem('종료', quit(detect_sub))
        )
    )

    detect_sub.start()
    icon.run()
    detect_sub.join()