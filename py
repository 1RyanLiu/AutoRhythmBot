import pyautogui

while True:

    if pyautogui.pixel(800, 1200)[2] == 0:
        pyautogui.press('D')

    if pyautogui.pixel(1100, 1200)[2] == 0:
        pyautogui.press('f')

    if pyautogui.pixel(1300, 1200)[2] == 0:
        pyautogui.press('j')

    if pyautogui.pixel(1500, 1200)[2] == 0:
        pyautogui.press('k')
