import killprocess
import login
import hotkeys
import fleetcommands
import formwidgets
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

class TradeItemsTab(ttkb.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)