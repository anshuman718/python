import pyautogui
import pyperclip
import time
import google.generativeai as  genai
genai.configure (api_key="AIzaSyDFC6dgyBQKj96VERy1wdgHvTKmFQmed8c")
model= genai.GenerativeModel('gemini.pro')                
def copy_message():
    pyautogui.moveTo(1010,1061)
    pyautogui.doubleClick(1010,1061)
    time.sleep(5)
    pyautogui.moveTo(1224,722)
    pyautogui.doubleClick(1224,722)
    time.sleep(5)
    pyautogui.moveTo(1277,637)  
    time.sleep(3)
    pyautogui.dragTo(1289,864)
    time.sleep(5)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(5)
copy_message()

chat_history= pyperclip.paste()
print("copied message:", chat_history)

prompt = f"""
You are Henry, a coder from India who speaks Hindi and English.
Respond naturally to the following message:
{chat_history}
"""

response = model.generate_content(prompt)

pyperclip.copy(response.text)
print("Bot response:", response.text)


pyautogui.click(1224,940)
time.sleep(4)

pyautogui.hotkey("ctrl","v")
time.sleep(4)
pyautogui.press("enter")




