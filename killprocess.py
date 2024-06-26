import win32gui
import win32process
import settings
import signal
import os

def all_clients():
    for i in range(len(settings.character_data_json['character'])):
        hwnd = win32gui.FindWindow(None, settings.character_data_json['character'][str(i)][0]['name'])
        if win32gui.IsWindowVisible(hwnd):
            thread_target, pid_trget = win32process.GetWindowThreadProcessId(hwnd)
            os.kill(pid_trget, signal.SIGTERM)

def target_client(target_client):    
    hwnd = win32gui.FindWindow(None, target_client)
    if win32gui.IsWindowVisible(hwnd):
        thread_target, pid_trget = win32process.GetWindowThreadProcessId(hwnd)
        os.kill(pid_trget, signal.SIGTERM)