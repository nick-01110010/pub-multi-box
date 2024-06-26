import pyautogui as pag
import os
import time
import win32gui
import win32con
import settings

import pyautogui
import os
import time
import win32gui
import win32con
import settings


def start_clients():
    settings.block_input(True)
    for i in range(len(settings.character_data_json['character'])):
        hwnd = win32gui.FindWindow(None, settings.character_data_json['character'][str(i)][0]['name'])
        if win32gui.IsWindowVisible(hwnd) == False:
            os.startfile(settings.file_location)
            time.sleep(1)
            if i == 0:
                hwnd = win32gui.FindWindow(None, settings.launcher_hwnd_title)
                if win32gui.IsWindowVisible(hwnd):
                    win32gui.SetForegroundWindow(hwnd)   
                    pyautogui.press('alt')
                    pyautogui.press('tab')
                    pyautogui.press('enter')
                    pyautogui.press('tab')
                    pyautogui.press('enter')
                    time.sleep(3)
                    hwnd = win32gui.FindWindow(None, settings.config_hwnd_title)
                    if win32gui.IsWindowVisible(hwnd):
                        win32gui.SetForegroundWindow(hwnd)
                        pyautogui.press('tab')
                        pyautogui.press('tab')
                        pyautogui.press('down')
                        pyautogui.press('down')
                        pyautogui.press('down')
                        pyautogui.press('tab')
                        pyautogui.press('right')
                        pyautogui.press('right')
                        pyautogui.press('right')
                        pyautogui.press('right')
                        pyautogui.press('right')
                        pyautogui.press('right')
                        pyautogui.press('right')
                        pyautogui.press('right')
                        pyautogui.press('right')
                        pyautogui.press('right')
                        pyautogui.press('right')
                        pyautogui.press('right')
                        pyautogui.press('right')
                        pyautogui.press('right')
                        pyautogui.press('right')
                        pyautogui.press('right')
                        pyautogui.press('right')
                        pyautogui.press('right')
                        pyautogui.press('right')
                        pyautogui.press('right')
                        pyautogui.press('tab')
                        pyautogui.press('tab')
                        pyautogui.press('tab')
                        pyautogui.press('tab')
                        pyautogui.press('tab')
                        pyautogui.press('enter')
                        hwnd = win32gui.FindWindow(None, 'Video Settings Have Changed')
                        if win32gui.IsWindowVisible(hwnd):
                            win32gui.SetForegroundWindow(hwnd)
                            pyautogui.press('tab')
                            pyautogui.press('enter')
                        hwnd = win32gui.FindWindow(None, settings.launcher_hwnd_title)
                        if win32gui.IsWindowVisible(hwnd):
                            win32gui.SetForegroundWindow(hwnd)
                            pyautogui.press('enter')
                            #figure out how to find if the play button is active
                time.sleep(3)
                hwnd = win32gui.FindWindow(None, 'Earth & Beyond')
                if win32gui.IsWindowVisible(hwnd):
                    win32gui.SetForegroundWindow(hwnd)
                    pyautogui.press("enter")
                    time.sleep(10)
                hwnd = win32gui.FindWindow(None, 'Earth & Beyond')
                if win32gui.IsWindowVisible(hwnd):
                    win32gui.SetForegroundWindow(hwnd)
                    win32gui.SetWindowText(hwnd, settings.character_data_json['character'][str(i)][0]['name'])
                    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, win32con.WS_VISIBLE | win32con.WS_CLIPCHILDREN)
                hwnd = win32gui.FindWindow(None, settings.character_data_json['character'][str(i)][0]['name'])
                if win32gui.IsWindowVisible(hwnd):
                    win32gui.SetForegroundWindow(hwnd)
                    set_window(str(settings.character_data_json['character'][str(i)][0]['position']))  
                    pyautogui.press("enter")
                    time.sleep(10)
                    pyautogui.click(x = settings.main_window_positions_json['main_window']['login_input'][0]['x'],
                                    y = settings.main_window_positions_json['main_window']['login_input'][0]['y'])
                    pyautogui.write(settings.character_data_json['character'][str(i)][0]['name'])
                    time.sleep(1)
                    pyautogui.click(x = settings.main_window_positions_json['main_window']['password_input'][0]['x'],
                                    y = settings.main_window_positions_json['main_window']['password_input'][0]['y'])
                    pyautogui.write(settings.character_data_json['character'][str(i)][0]['password'])
                    time.sleep(1)
                    pyautogui.press("enter")
                    time.sleep(7)
                    pyautogui.click(x = settings.main_window_positions_json['main_window']['character_slot_one'][0]['x'],
                                    y = settings.main_window_positions_json['main_window']['character_slot_one'][0]['y'])
                    time.sleep(1)
                    pyautogui.press("enter")
                    time.sleep(1)         
            else:
                hwnd = win32gui.FindWindow(None, settings.launcher_hwnd_title)
                if win32gui.IsWindowVisible(hwnd):
                    win32gui.SetForegroundWindow(hwnd)
                    pyautogui.press('alt')
                    pyautogui.press('tab')
                    pyautogui.press('enter')
                    pyautogui.press('tab')
                    pyautogui.press('enter')
                    time.sleep(3)
                    hwnd = win32gui.FindWindow(None, settings.config_hwnd_title)
                    if win32gui.IsWindowVisible(hwnd):
                        win32gui.SetForegroundWindow(hwnd)
                        pyautogui.press('tab')
                        pyautogui.press('tab')
                        pyautogui.press('down')
                        pyautogui.press('down')
                        pyautogui.press('down')
                        pyautogui.press('tab')
                        pyautogui.press('left')
                        pyautogui.press('left')
                        pyautogui.press('left')
                        pyautogui.press('left')
                        pyautogui.press('left')
                        pyautogui.press('left')
                        pyautogui.press('left')
                        pyautogui.press('left')
                        pyautogui.press('left')
                        pyautogui.press('left')
                        pyautogui.press('left')
                        pyautogui.press('left')
                        pyautogui.press('left')
                        pyautogui.press('left')
                        pyautogui.press('left')
                        pyautogui.press('left')
                        pyautogui.press('left')
                        pyautogui.press('left')
                        pyautogui.press('left')
                        pyautogui.press('left')
                        pyautogui.press('tab')
                        pyautogui.press('tab')
                        pyautogui.press('tab')
                        pyautogui.press('tab')
                        pyautogui.press('tab')
                        pyautogui.press('enter')
                        hwnd = win32gui.FindWindow(None, 'Video Settings Have Changed')
                        if win32gui.IsWindowVisible(hwnd):
                            win32gui.SetForegroundWindow(hwnd)
                            pyautogui.press('tab')
                            pyautogui.press('enter')
                        hwnd = win32gui.FindWindow(None, settings.launcher_hwnd_title)
                        if win32gui.IsWindowVisible(hwnd):
                            win32gui.SetForegroundWindow(hwnd)
                            pyautogui.press('enter')
                            #figure out how to find if the play button is active
                time.sleep(3)
                hwnd = win32gui.FindWindow(None, 'Earth & Beyond')
                if win32gui.IsWindowVisible(hwnd):
                    win32gui.SetForegroundWindow(hwnd)
                    pyautogui.press("enter")
                    time.sleep(10)
                hwnd = win32gui.FindWindow(None, 'Earth & Beyond')
                if win32gui.IsWindowVisible(hwnd):
                    win32gui.SetForegroundWindow(hwnd)
                    win32gui.SetWindowText(hwnd, settings.character_data_json['character'][str(i)][0]['name'])
                    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, win32con.WS_VISIBLE | win32con.WS_CLIPCHILDREN)
                hwnd = win32gui.FindWindow(None, settings.character_data_json['character'][str(i)][0]['name'])
                if win32gui.IsWindowVisible(hwnd):
                    win32gui.SetForegroundWindow(hwnd)
                    set_window(str(settings.character_data_json['character'][str(i)][0]['position']))
                    rect = win32gui.GetWindowRect(hwnd)
                    pyautogui.press("enter")
                    time.sleep(10) 
                    pyautogui.click(x = (rect[0] + settings.side_window_length) + (settings.side_window_offsets_json['side_window']['login_input'][0]['x']),
                                    y = (rect[1] + settings.side_window_height) + (settings.side_window_offsets_json['side_window']['login_input'][0]['y']))
                    pyautogui.write(settings.character_data_json['character'][str(i)][0]['name'])
                    time.sleep(1)
                    pyautogui.click(x = (rect[0] + settings.side_window_length) + (settings.side_window_offsets_json['side_window']['password_input'][0]['x']),
                                    y = (rect[1] + settings.side_window_height) + (settings.side_window_offsets_json['side_window']['password_input'][0]['y']))
                    pyautogui.write(settings.character_data_json['character'][str(i)][0]['password'])
                    time.sleep(1)
                    pyautogui.press("enter")
                    time.sleep(7)
                    pyautogui.click(x = (rect[0] + settings.side_window_length) + (settings.side_window_offsets_json['side_window']['character_slot_one'][0]['x']),
                                    y = (rect[1] + settings.side_window_height) + (settings.side_window_offsets_json['side_window']['character_slot_one'][0]['y']))
                    time.sleep(1)
                    pyautogui.press("enter")
                    time.sleep(1)
    settings.block_input(False)

def set_window(character):
    hwnd = win32gui.FindWindow(None, settings.character_data_json['character'][character][0]['name'])
    if win32gui.IsWindowVisible(hwnd):
        win32gui.MoveWindow(hwnd,
        settings.character_data_json['character'][character][0]['win_x_pos'],
        settings.character_data_json['character'][character][0]['win_y_pos'],
        settings.character_data_json['character'][character][0]['win_x_len'],
        settings.character_data_json['character'][character][0]['win_y_len'],
        True)

def set_windows():
    for i in range(len(settings.character_data_json['character'])):
        hwnd = win32gui.FindWindow(None, settings.character_data_json['character'][str(i)][0]['name'])
        if win32gui.IsWindowVisible(hwnd):
            win32gui.MoveWindow(hwnd, 
                                settings.character_data_json['character'][str(i)][0]['win_x_pos'],
                                settings.character_data_json['character'][str(i)][0]['win_y_pos'],
                                settings.character_data_json['character'][str(i)][0]['win_x_len'],
                                settings.character_data_json['character'][str(i)][0]['win_y_len'],
                                True)