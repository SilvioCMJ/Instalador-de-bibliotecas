import pyautogui
import time

# nome da biblioteca
lib = 'pypng'
pasta1 = 'pycharmprojects'
pasta2 = 'pythonproject16'

# bot açoes
pyautogui.hotkey("win", 'r')
time.sleep(1)
pyautogui.write("cmd")
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write(f'cd {pasta1}')
time.sleep(1)
pyautogui.press('enter')
pyautogui.write(f'cd {pasta2}')
time.sleep(1)
pyautogui.press('enter')
pyautogui.write(f"pip install {lib}")
time.sleep(1)
pyautogui.press('enter')



