import settings
import win32gui
import pyautogui
import time

def group_formation():
    settings.block_input(True)
    for i in range(len(settings.character_data_json['character'])):
        hwnd = win32gui.FindWindow(None, settings.character_data_json['character'][str(i)][0]['name'])
        if win32gui.IsWindowVisible(hwnd) & (settings.character_data_json['character'][str(i)][0]['position'] != 0):
            win32gui.SetForegroundWindow(hwnd)
            pyautogui.press(',')
    settings.block_input(False)

def group_attack():
    settings.block_input(True)
    for i in range(len(settings.character_data_json['character'])):
        hwnd = win32gui.FindWindow(None, settings.character_data_json['character'][str(i)][0]['name'])
        if win32gui.IsWindowVisible(hwnd) & (settings.character_data_json['character'][str(i)][0]['position'] != 0):
            rect = win32gui.GetWindowRect(hwnd)
            win32gui.SetForegroundWindow(hwnd)
            pyautogui.click(x = (rect[0] + settings.side_window_length) + (settings.side_window_offsets_json['side_window']['assist_leader'][0]['x']),
                            y = (rect[1] + settings.side_window_height) + (settings.side_window_offsets_json['side_window']['assist_leader'][0]['y']))
            pyautogui.press(' ')
    pyautogui.click(x = (settings.main_window_length / 2), y = (settings.main_window_height / 2))
    pyautogui.press(' ')
    settings.block_input(False)

def group_target():
    settings.block_input(True)
    for i in range(len(settings.character_data_json['character'])):
        hwnd = win32gui.FindWindow(None, settings.character_data_json['character'][str(i)][0]['name'])
        if win32gui.IsWindowVisible(hwnd) & (settings.character_data_json['character'][str(i)][0]['position'] != 0):
            win32gui.SetForegroundWindow(hwnd)
            rect = win32gui.GetWindowRect(hwnd)
            pyautogui.click(x = (rect[0] + settings.side_window_length) + (settings.side_window_offsets_json['side_window']['assist_leader'][0]['x']),
                            y = (rect[1] + settings.side_window_height) + (settings.side_window_offsets_json['side_window']['assist_leader'][0]['y']))
    pyautogui.click(x = (settings.main_window_length / 2), y = (settings.main_window_height / 2))
    settings.block_input(False)

def group_invite():
    settings.block_input(True)
    main_window = win32gui.FindWindow(None, settings.character_data_json['character']['0'][0]['name'])
    for i in range(len(settings.character_data_json['character'])):
        side_window = win32gui.FindWindow(None, settings.character_data_json['character'][str(i)][0]['name'])
        if win32gui.IsWindowVisible(main_window) & (settings.character_data_json['character'][str(i)][0]['position'] != 0):
            win32gui.SetForegroundWindow(main_window)
            pyautogui.press('enter')
            pyautogui.write(f'/invite {settings.character_data_json['character'][str(i)][0]['name']}')
            pyautogui.press('enter')
            win32gui.SetForegroundWindow(side_window)
            time.sleep(1)
            rect = win32gui.GetWindowRect(side_window)
            pyautogui.click(x = (rect[0] + settings.side_window_length) + (settings.side_window_offsets_json['side_window']['accept_invite'][0]['x']),
                            y = (rect[1] + settings.side_window_height) + (settings.side_window_offsets_json['side_window']['accept_invite'][0]['y']))
    pyautogui.click(x = (settings.main_window_length / 2), y = (settings.main_window_height / 2))
    settings.block_input(False)

def group_dock_gate():
    settings.block_input(True)
    group_target()
    for i in range(len(settings.character_data_json['character'])):
        hwnd = win32gui.FindWindow(None, settings.character_data_json['character'][str(i)][0]['name'])
        if win32gui.IsWindowVisible(hwnd) & (settings.character_data_json['character'][str(i)][0]['position'] == 0):
            win32gui.SetForegroundWindow(hwnd)
            pyautogui.click(x = settings.main_window_positions_json['main_window']['gate_dock'][0]['x'],
                            y = settings.main_window_positions_json['main_window']['gate_dock'][0]['y'])
        elif win32gui.IsWindowVisible(hwnd):
            win32gui.SetForegroundWindow(hwnd)
            rect = win32gui.GetWindowRect(hwnd)
            pyautogui.click(x = (rect[0] + settings.side_window_length) + (settings.side_window_offsets_json['side_window']['gate_dock'][0]['x']),
                            y = (rect[1] + settings.side_window_height) + (settings.side_window_offsets_json['side_window']['gate_dock'][0]['y']))
    pyautogui.click(x = (settings.main_window_length / 2), y = (settings.main_window_height / 2))
    settings.block_input(False)

