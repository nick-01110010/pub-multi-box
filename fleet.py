import pyautogui
import time
import win32gui

class Fleet:

    MAX_CHARACTERS = 6

    def __init__(self, name):
        self.name = name
        self.characters = []
    
    def get_fleet_name(self):
        return self.name
    
    def add_character(self, character):
        try:
            if len(self.characters) < Fleet.MAX_CHARACTERS:
                self.characters.append(character)
            else:
                raise InvalidFleetSizeException
        except InvalidFleetSizeException:
            print("A fleet cannot contain more than 6 characters.")

    def fleet_attack(self):
        for i in range(len(self.characters)):
            hwnd = win32gui.FindWindow(None, 'SQL_Character_Name')
            # if win32gui.IsWindowVisible(hwnd) & ('SQL_Character_Position' != 0):
            #     rect = win32gui.GetWindowRect(hwnd)
            #     win32gui.SetForegroundWindow(hwnd)
            #     pyautogui.click(x = (rect[0] + "SQL_Character_x_length") + (settings.side_window_offsets_json['side_window']['assist_leader'][0]['x']),
            #                     y = (rect[1] + "SQL_Character_y_length") + (settings.side_window_offsets_json['side_window']['assist_leader'][0]['y']))
            #     pyautogui.press(' ')
            #     pyautogui.click(x = (settings.main_window_length / 2), y = (settings.main_window_height / 2))
            #     pyautogui.press(' ')
   
    def fleet_formation(self, formation_type):
        pass

    def fleet_gate_dock(self):
        pass

    def fleet_invite(self):
        pass

    def fleet_target(self):
        pass

class InvalidFleetSizeException(Exception):
    "Raised when the number of characters added to a fleet is greater than 6."
    pass