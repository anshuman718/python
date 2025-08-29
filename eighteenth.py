import pyautogui
import pyperclip
import time
from google import genai
client= genai.Client(api_key="AIzaSyDFC6dgyBQKj96VERy1wdgHvTKmFQmed8c")

def copy_message():
    pyautogui.moveTo(1010,1061)
    pyautogui.doubleClick(1010,1061)
    time.sleep(5)
    pyautogui.moveTo(1151,665)
    pyautogui.doubleClick(1151,665)
    time.sleep(5)
    pyautogui.moveTo(1201,584)  
    pyautogui.doubleClick(1201,584)
    pyautogui.doubleClick(1201,584)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(5)
copy_message()
def paste_message():
    pyperclip.paste()
paste_message()


response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Imagine yourself to be me and generate the response for the latest message copied." , 
)
print(response)


