import settings
import win32gui
import pyautogui
from pynput import keyboard
import fleetcommands

def win_activate(pos):
    if pos < len(settings.character_data_json['character']):
        sideWindow = win32gui.FindWindow(None, settings.character_data_json['character'][str(pos)][0]['name'])
        mainWindow = win32gui.FindWindow(None, settings.currentWindow)
        rect = win32gui.GetWindowRect(sideWindow)
        if win32gui.IsWindowVisible(sideWindow) & win32gui.IsWindowVisible(mainWindow):
            win32gui.MoveWindow(sideWindow, 0, 0, 3440, 1440, True)
            pyautogui.press("alt") # no idea why this works, but it does
            win32gui.SetForegroundWindow(sideWindow)
            if settings.character_data_json['character'][str(pos)][0]['name'] != settings.currentWindow:
                win32gui.MoveWindow(mainWindow, rect[0], rect[1], 800, 600, True)
                settings.currentWindow = settings.character_data_json['character'][str(pos)][0]['name']

enable = keyboard.GlobalHotKeys({
            '<ctrl>+1': lambda: win_activate(0),
            '<ctrl>+2': lambda: win_activate(1),
            '<ctrl>+3': lambda: win_activate(2),
            '<ctrl>+4': lambda: win_activate(3),
            '<ctrl>+5': lambda: win_activate(4),
            '<ctrl>+6': lambda: win_activate(5),
            '<shift>+g': fleetcommands.group_attack,
            '<shift>+h': fleetcommands.group_formation})