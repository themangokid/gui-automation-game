import pyautogui
import time
import webbrowser
import pyperclip

clip = pyperclip
# Släng in en lista och klistra in det här.
clip.init_windows_clipboard()
print(clip.determine_clipboard())
c = clip.paste
print(c)

t = time


def sleepy(number):
    t.sleep(number)


pag = pyautogui

def control_tab_save():
    webbrowser.get().open("https://pyautogui.readthedocs.io/en/latest/index.html")
    sleepy(1.5)
    pag.hotkey('ctrl', 's')
    sleepy(1.5)
    position = pag.locateCenterOnScreen('save_as.png')
    x = position.x
    y = position.y
    pag.click(x + 150, y)
    pag.hotkey('ctrl', 'a')
    pag.hotkey('del')

    """
        pag.hotkey('control', 's')
        pag.hotkey('control', 'tab')
        sleepy(0.4)
        pag.hotkey('control', 'tab')
        sleepy(0.4)
    """

def open_documentation():
    webbrowser.get().open("https://pyautogui.readthedocs.io/en/latest/index.html")
    sleepy(1)
    position = pag.locateCenterOnScreen('search_pyguidocs.png')
    print(position)
    x = position.x
    y = position.y
    sleepy(0.322)
    pag.click(x, y)

#open_documentation()

control_tab_save()