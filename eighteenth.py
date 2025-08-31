import pyautogui
import pyperclip
import time
import google.generativeai as  genai
genai.configure (api_key="AIzaSyDFC6dgyBQKj96VERy1wdgHvTKmFQmed8c")
model= genai.GenerativeModel('gemini-2.5-flash')                
def copy_message():
    pyautogui.moveTo(1018,1060)
    pyautogui.doubleClick(1018,1060)
    time.sleep(5)
    pyautogui.moveTo(1294,437)
    pyautogui.doubleClick(1294,437)
    
    pyautogui.moveTo(1608,807)  
    time.sleep(3)
    pyautogui.dragTo(1657,909, duration= 1.0 ,button='left')
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


pyautogui.click()
time.sleep(4)

pyautogui.hotkey("ctrl","v")
time.sleep(4)
pyautogui.press("enter")




