import pyautogui
import time 
import pyperclip


def get_message_from_clipboard():

    icon_x,icon_y = 894,1074

    pyautogui.moveTo(icon_x,icon_y)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.moveTo(1111,736)
    pyautogui.doubleClick(1111,736)
    time.sleep(3)
    pyautogui.moveTo(1251,562)
    pyautogui.doubleClick(1251,562)
    time.sleep(3)
    pyautogui.moveTo(1340,817)
    pyautogui.doubleClick(1340,817)
    time.sleep(3)
    pyautogui.moveTo(1531,539)
    pyautogui.doubleClick()
    time.sleep(10)
    pyautogui.doubleClick(1054,516)
    pyautogui.hotkey('ctrl','c')
    message = pyperclip.paste()
    return message

get_message_from_clipboard()


