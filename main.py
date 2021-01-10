import pytesseract as tess
import win32api
import win32con
import win32gui
import os
from PIL import ImageGrab
from PIL import Image

tess.pytesseract.tesseract_cmd = 'Google OCR\\tesseract.exe'
window = 'sharingan'

toplist, winlist = [], []
def enum(hwnd,results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
win32gui.EnumWindows(enum, toplist)

VBOX = [(hwnd,title) for hwnd,title in winlist if window in title.lower()]

# if WINDOW_NAME in VBOX[0][1]:
#     print(VBOX[0][1])
#     print("Target window not found. Try writing window name again in lowercase")
#     os.system('exit')

# MIN_RANGE  = int(input("Start at ( int only ): "))
# MAX_RANGE = int(input("End at ( int only ): "))

hwnd = VBOX[0]
win32gui.SetForegroundWindow(hwnd[0])
mainBox = win32gui.GetWindowRect(hwnd[0])

while True:
    if(win32api.GetAsyncKeyState(win32con.VK_HOME)):
        mainImg = ImageGrab.grab(mainBox)
        mainTextOutput = tess.image_to_string(mainImg)
        print("######################################################")
        ad = " ".join(mainTextOutput.split())
        print(ad[10:500])
        # print(ad)
        if(win32api.GetAsyncKeyState(win32con.VK_END)):
            os.system('exit')

