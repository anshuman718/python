import pyautogui
import time 
import pyperclip
# pyautogui and pyper click are python modules used to automate the graphical user interferance(GUI).

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
    # Here we have said python to use pyautogui and click at different coordinates so that various icons and files can be opened .we also need 
    # to use the built in module ""time" because it takes some seconds for the file to be opened.

get_message_from_clipboard()
# After that we have copied some text from the file and pasted it to clipboard.


