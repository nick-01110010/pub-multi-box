import formwidgets
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *


class RightPanel(ttkb.Frame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master = parent)

        self.start_pos = start_pos
        self.end_pos = end_pos - 0.05
        self.width = abs(start_pos - end_pos)

        self.pos = self.start_pos
        self.in_start_pos = True
        
        self.place(relx = self.start_pos, rely = 0.05, relwidth = self.width, relheight = 0.6)
        
    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx = self.pos, rely = 0.05, relwidth = self.width, relheight = 0.6)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False
            
    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx = self.pos, rely = 0.05, relwidth = self.width, relheight = 0.6)
            self.after(10, self.animate_backwards)
        else:
            self.in_start_pos = True

class LeftPanel(ttkb.Frame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master = parent)

        self.start_pos = start_pos
        self.end_pos = end_pos + 0.05
        self.width = abs(start_pos - end_pos)
        
        # animation logic
        self.pos = self.start_pos
        self.in_start_pos = True

        self.place(relx = self.start_pos, rely = 0.05, relwidth = self.width, relheight = 0.6)
        
    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos < self.end_pos:
            self.pos += 0.008
            self.place(relx = self.pos, rely = 0.05, relwidth = self.width, relheight = 0.6)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False
            
    def animate_backwards(self):
        if self.pos > self.start_pos:
            self.pos -= 0.008
            self.place(relx = self.pos, rely = 0.05, relwidth = self.width, relheight = 0.6)
            self.after(10, self.animate_backwards)
        else:
            self.in_start_pos = True

class BottomPanel(ttkb.Frame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master = parent)

        self.start_pos = start_pos
        self.end_pos = end_pos - 0.15
        self.height = abs(start_pos - end_pos)
        
        # animation logic
        self.pos = self.start_pos
        self.in_start_pos = True

        self.place(rely = self.start_pos, relx = 0.05, relwidth = .9, relheight = self.height)
        
    def animate(self):
        if self.in_start_pos:
            self.animate_up()
        else:
            self.animate_down()

    def animate_up(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(rely = self.pos, relx = 0.05, relwidth = .9, relheight = self.height)
            self.after(10, self.animate_up)
        else:
            self.in_start_pos = False
            
    def animate_down(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(rely = self.pos, relx = 0.05, relwidth = .9, relheight = self.height)
            self.after(10, self.animate_down)
        else:
            self.in_start_pos = True

class CreateFleetEquipmentTab(ttkb.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.data=[{'text': 'Item Type', 'stretch': True},
        {'text': 'Item Level', 'stretch': True},
        {'text': 'Character Two', 'stretch': True},
        {'text': 'Character Three', 'stretch': True},
        {'text': 'Character Four', 'stretch': True},
        {'text': 'Character Five', 'stretch': True},
        {'text': 'Character Six', 'stretch': True}]

        self.data2 = [['Reactor', '9', 'Character Two', 'Character Three', 'Character Four', 'Character Five', 'Character Six'],
        ['Engine', '8', 'Character Two', 'Character Three', 'Character Four', 'Character Five', 'Character Six'],
        ['Device', '1', 'Character Two', 'Character Three', 'Character Four', 'Character Five', 'Character Six'],
        ['Shield', '5', 'Character Two', 'Character Three', 'Character Four', 'Character Five', 'Character Six'],
        ['Weapon', '3', 'Character Two', '', '', '', ''],
        ['Weapon', '7', 'Character Two', 'Character Three', 'Character Four', 'Character Five', 'Character Six'],
        ['Device', '5', 'Character Two', 'Character Three', 'Character Four', 'Character Five', 'Character Six']]

        self.create_frames(6, 6, 2)

    def create_frames(self, weapons, devices, characters):

        self.weapon = ttkb.PhotoImage(file='C:/Src/enb-multi-box/assets/weapon.png')
        self.device = ttkb.PhotoImage(file='C:/Src/enb-multi-box/assets/device.png')
        self.shield = ttkb.PhotoImage(file='C:/Src/enb-multi-box/assets/shield.png')
        self.reactor = ttkb.PhotoImage(file='C:/Src/enb-multi-box/assets/reactor.png')
        self.engine = ttkb.PhotoImage(file='C:/Src/enb-multi-box/assets/engine.png')

        self.left_animated_panel = LeftPanel(self, -.1, 0)
        self.left_animated_panel.grid_columnconfigure(0, weight = 1)
        self.left_animated_panel.grid_rowconfigure(1, weight = 0)
        
        for weapon in range(weapons):
            weapon_slot = ttkb.Label(self.left_animated_panel, width = 20, anchor = CENTER, text = f'Weapon {weapon + 1}', image = self.weapon, compound = BOTTOM)
            weapon_slot.grid(row= weapon +1, column=0, sticky= N, pady=(0, 25))
        
        self.right_animated_panel = RightPanel(self, 1.0, 0.9)
        self.right_animated_panel.grid_columnconfigure(0, weight = 1)
        self.right_animated_panel.grid_rowconfigure(1, weight = 0)

        for device in range(devices):
            weapon_slot = ttkb.Label(self.right_animated_panel, width = 20, anchor = CENTER, text = f'Device {device + 1}', image = self.device, compound = BOTTOM)
            weapon_slot.grid(row = device + 1, column = 0, sticky = N, pady = (0, 25))

        self.bottom_animated_panel = BottomPanel(self, 1, .8)
        self.bottom_animated_panel.grid_columnconfigure(1, weight = 1)
        self.bottom_animated_panel.grid_rowconfigure(1, weight = 0)

        self.shield_slot = ttkb.Label(self.bottom_animated_panel, anchor = CENTER, width = 20, text = 'Shield', image = self.shield, compound = BOTTOM)
        self.shield_slot.grid(row = 1, column = 0, sticky = W, padx = (150, 0), pady = (60, 0))
        self.reactor_slot = ttkb.Label(self.bottom_animated_panel, anchor = CENTER, width = 20, text = 'Reactor', image = self.reactor, compound = BOTTOM)
        self.reactor_slot.grid(row = 1, column = 1, pady = (60, 0))
        self.engine_slot = ttkb.Label(self.bottom_animated_panel, anchor = CENTER, width = 20, text = 'Engine', image = self.engine, compound = BOTTOM)
        self.engine_slot.grid(row = 1, column = 2, sticky = E, padx = (0, 150), pady = (60, 0))

        button_container = ttkb.Frame(self)
        button_container.pack(pady = 10)

        for character in range(characters):
            if character < 3:
                self.character_button = ttkb.Button(master = button_container, text = f'Character {character + 1}',
                command = lambda: [self.right_animated_panel.animate(), self.left_animated_panel.animate(), self.bottom_animated_panel.animate()])
                self.character_button.grid(row = 1, column= character, sticky = N)
            else:
                self.character_button = ttkb.Button(master = button_container, text = f'Character {character + 1}',
                command = lambda: [self.right_animated_panel.animate(), self.left_animated_panel.animate(), self.bottom_animated_panel.animate()])
                self.character_button.grid(row = 2, column = character - 3, sticky = N)

        # button2 = ttkb.Button(self, text = 'Destroy', command = lambda: [FormWidgets.destroy_children_widgets(self, self.left_animated_panel)])
        # button2.pack()
        # button3 = ttkb.Button(self, text = 'Destroy', command = lambda: [FormWidgets.destroy_children_widgets(self, self.right_animated_panel)])
        # button3.pack()
        # button4 = ttkb.Button(self, text = 'Destroy', command = lambda: [FormWidgets.destroy_children_widgets(self, self.bottom_animated_panel)])
        # button4.pack()

        self.assign_loadout_entry_container, self.assign_loadout_entry_container_labels, self.assign_loadout_entry_container_comboboxes, self.assign_loadout_entry_container_error_labels = formwidgets.FormWidgets.create_label_combobox_label_grid(self,
        grid_objects=1,
        master_container=None,
        recreate=False,

        bind_combobox_action=[False],
        combobox_action=[None],
        combobox_command=[None],

        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='assign_loadout_entry_container',
        container_padding=None,
        container_relief=None,
        container_style=None,
        container_takefocus=None,
        container_width=None,

        container_pack_cnf=None,
        container_pack_after=None,
        container_pack_anchor=None,
        container_pack_before=None,
        container_pack_expand=NO,
        container_pack_fill=None,
        container_pack_side=None,
        container_pack_ipadx=None,
        container_pack_ipady=None,
        container_pack_padx=None,
        container_pack_pady=None,
        container_pack_in_=None,

        label1_anchor=[None],
        label1_background=[None],
        label1_border=[None],
        label1_borderwidth=[None],
        label1_class_=[None],
        label1_compound=[None],
        label1_cursor=[None],
        label1_font=[None],
        label1_foreground=[None],
        label1_image=[None],
        label1_justify=[None],
        label1_name=['assign_loadout_label'],
        label1_padding=[None],
        label1_relief=[None],
        label1_state=[None],
        label1_style=[None],
        label1_takefocus=[None],
        label1_text=['Assign Loadout:'],
        label1_textvariable=[None],
        label1_underline=[None],
        label1_width=[20],
        label1_wraplength=[None],

        label1_grid_cnf=[None],
        label1_grid_column=[1],
        label1_grid_columnspan=[None],
        label1_grid_row=[1],
        label1_grid_rowspawn=[None],
        label1_grid_ipadx=[None],
        label1_grid_ipady=[None],
        label1_grid_padx=[5],
        label1_grid_pady=[5],
        label1_grid_sticky=[None],
        label1_grid_in_=[None],

        combobox_background=[None],
        combobox_class_=[None],
        combobox_cursor=[None],
        combobox_exportselection=[None],
        combobox_font=[None],
        combobox_foreground=[None],
        combobox_height=[None],
        combobox_invalidcommand=[None],
        combobox_justify=[None],
        combobox_name=['assign_loadout_combobox'],
        combobox_postcommand=[None],
        combobox_show=[None],
        combobox_state=[READONLY],
        combobox_style=[None],
        combobox_takefocus=[None],
        combobox_textvariable=[None],
        combobox_validate=[None],
        combobox_validatecommand=[None],
        combobox_values=['New Loadout', 1, 2, 3, 4, 5, 6],
        combobox_width=[18],
        combobox_xscrollcommand=[None],
        
        combobox_grid_cnf=[None],
        combobox_grid_column=[2],
        combobox_grid_columnspan=[None],
        combobox_grid_row=[1],
        combobox_grid_rowspawn=[None],
        combobox_grid_ipadx=[None],
        combobox_grid_ipady=[None],
        combobox_grid_padx=[5],
        combobox_grid_pady=[5],
        combobox_grid_sticky=[None],
        combobox_grid_in_=[None],
        
        label2_anchor=[None],
        label2_background=[None],
        label2_border=[None],
        label2_borderwidth=[None],
        label2_class_=[None],
        label2_compound=[None],
        label2_cursor=[None],
        label2_font=[None],
        label2_foreground=[None],
        label2_image=[None],
        label2_justify=[None],
        label2_name=['assign_loadout_label'],
        label2_padding=[None],
        label2_relief=[None],
        label2_state=[None],
        label2_style=[None],
        label2_takefocus=[None],
        label2_text=[''],
        label2_textvariable=[None],
        label2_underline=[None],
        label2_width=[60],
        label2_wraplength=[None],

        label2_grid_cnf=[None],
        label2_grid_column=[3],
        label2_grid_columnspan=[None],
        label2_grid_row=[1],
        label2_grid_rowspawn=[None],
        label2_grid_ipadx=[None],
        label2_grid_ipady=[None],
        label2_grid_padx=[5],
        label2_grid_pady=[5],
        label2_grid_sticky=[None],
        label2_grid_in_=[None])

        (self.item_selection_table_container,
        self.item_selection_table_container_objects) = formwidgets.FormWidgets.create_table_grid(self,
                                                                                  
        grid_objects=1,
        master_container=None,
        recreate=False,
        
        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='item_selection_table_container',
        container_padding=None,
        container_relief=None,
        container_style=None,
        container_takefocus=None,
        container_width=None,
        
        container_pack_cnf=None,
        container_pack_after=None,
        container_pack_anchor=None,
        container_pack_before=None,
        container_pack_expand=NO,
        container_pack_fill= None,
        container_pack_side=None,
        container_pack_ipadx=None,
        container_pack_ipady=5,
        container_pack_padx=None,
        container_pack_pady=None,
        container_pack_in_=None,

        table_bootstyle=[PRIMARY],
        table_coldata=[self.data,],
        table_rowdata=[self.data2],
        table_paginated=[True],
        table_searchable=[True],
        table_autofit=[True],
        table_autoalign=[False],
        table_stripecolor=[None],
        table_pagesize=[6],
        table_height=[6],
        table_delimiter=[None],
        
        table_grid_cnf=[None],
        table_grid_column=[1],
        table_grid_columnspan=[None],
        table_grid_row=[1],
        table_grid_rowspawn=[None],
        table_grid_ipadx=[None],
        table_grid_ipady=[None],
        table_grid_padx=[None],
        table_grid_pady=[None],
        table_grid_sticky=[None],
        table_grid_in_=[None])