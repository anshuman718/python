import pyautogui
import time 
import pyperclip


def get_message_from_clipboard():

    icon_x,icon_y = 894,1074

    pyautogui.moveTo(icon_x,icon_y)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.moveTo(1184,718)
    pyautogui.doubleClick(1184,718)
    time.sleep(3)
    pyautogui.moveTo(1384,277)
    pyautogui.doubleClick(1384,277)
    time.sleep(5)
    pyautogui.moveTo(1381,785)
    pyautogui.doubleClick(1381,785)
    time.sleep(5)
    pyautogui.moveTo(1534,481)
    pyautogui.doubleClick(1534,481)
    time.sleep(10)
    pyautogui.doubleClick(1035,744)
    pyautogui.hotkey('ctrl','c')
    message = pyperclip.paste()
    return message
    

get_message_from_clipboard()


