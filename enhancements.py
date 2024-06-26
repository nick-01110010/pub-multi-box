import settings
import win32gui
import pyautogui
import time

def shield_enhancements():
    settings.block_input(True)
    buff_list = []
    for i in range(len(settings.character_data_json['character'])):
        char_class = settings.character_data_json['character'][str(i)][0]['class']
        hwnd = win32gui.FindWindow(None, settings.character_data_json['character'][str(i)][0]['name'])
        if win32gui.IsWindowVisible(hwnd) & ((char_class == 'JD' or char_class =='JE' or char_class =='TT')):
            buff_list.append(hwnd)
    for j in range(len(settings.character_data_json['character'])):  
        for k in range(len(buff_list)):
            time.sleep(1)
            win32gui.SetForegroundWindow(buff_list[k])
            pyautogui.press((f'f{str(j + 1)}'))
            pyautogui.keyDown('alt')
            pyautogui.press('6')
            pyautogui.keyUp('alt')
        time.sleep(settings.ability_shields_wait)
    settings.block_input(False)