import killprocess
import login
import hotkeys
import fleetcommands
import formwidgets
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from ttkbootstrap.validation import *
import validation as Validate

class CreateFleetCommandsTab(ttkb.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.data1 = [{'text': 'Fleet Name', 'stretch': True},
        {'text': 'Character One', 'stretch': True},
        {'text': 'Character Two', 'stretch': True},
        {'text': 'Character Three', 'stretch': True},
        {'text': 'Character Four', 'stretch': True},
        {'text': 'Character Five', 'stretch': True},
        {'text': 'Character Six', 'stretch': True}]
        
        self.data2 = [['Fleet Name 1','Character1','Character2','Character3','Character4','Character5','Character6'],
        ['Fleet Name 2','Character One'],
        ['Fleet Name 3','Character One','Character Two'],
        ['Fleet Name 4','Character One','Character Two','Character Three'],
        ['Fleet Name 5','Character One','Character Two','Character Three','Character Four'],
        ['Fleet Name 6','Character One','Character Two','Character Three','Character Four','Character Five'],
        ['Fleet Name 7','Character One','Character Two','Character Three','Character Four','Character Five','Character Six']]
        
        self.fleet_selected = False
        self.current_selected_fleet =  []
        
        self.fleet_command_entry_value_one = ttkb.StringVar(value = '')
        self.fleet_command_entry_value_two = ttkb.StringVar(value = '')
        self.fleet_command_entry_value_three = ttkb.StringVar(value = '')
        self.fleet_command_entry_value_four = ttkb.StringVar(value = '')

        self.enable_hotkey_checkbox_variable = ttkb.IntVar(value = 0)
        self.lock_hotkey_checkbox_variable = ttkb.IntVar(value = 0)

        (self.select_fleet_table_container,
        self.select_fleet_table_objects) = formwidgets.FormWidgets.create_table_grid(self,
                                                                                  
        grid_objects=1,
        master_container=None,
        recreate=False,
        
        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='select_fleet_table_container',
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
        table_coldata=[self.data1,],
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

        (self.select_fleet_button_container,
        self.select_fleet_button_objects)=formwidgets.FormWidgets.create_button_grid(self,
        
        grid_objects=1,
        master_container=None,
        recreate=False,

        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='select_fleet_button_container',
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
        container_pack_ipady=None,
        container_pack_padx=None,
        container_pack_pady=None,
        container_pack_in_=None,

        button_class_=[None],
        button_command=[lambda : self.select_fleet(self.select_fleet_table_objects[0])],
        button_compound=[None],
        button_cursor=[None],
        button_default=[None],
        button_image=[None],
        button_name=['select_fleet_button'],
        button_padding=[None],
        button_state=[None],
        button_style=[None],
        button_takefocus=[None],
        button_text=['Select Fleet'],
        button_textvariable=[None],
        button_underline=[None],
        button_width=[20],
        button_bootstyle=[SUCCESS],

        button_grid_cnf=[None],
        button_grid_column=[1],
        button_grid_columnspan=[None],
        button_grid_row=[1],
        button_grid_rowspawn=[None],
        button_grid_ipadx=[None],
        button_grid_ipady=[None],
        button_grid_padx=[None],
        button_grid_pady=[5],
        button_grid_sticky=[None],
        button_grid_in_=[None])


        self.current_fleet_object_count = 2
        (self.current_fleet_label_container,
        self.current_fleet_label_objects) = formwidgets.FormWidgets.create_label_grid(self, 
        
        grid_count=self.current_fleet_object_count,
        master_container=None,
        recreate=False,
        
        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='current_fleet_label_container',
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
        container_pack_pady=5,
        container_pack_in_=None,                                                                                                                                                                                                                                
        
        label_anchor = [None] * self.current_fleet_object_count,
        label_background = [None] * self.current_fleet_object_count,
        label_border = [None] * self.current_fleet_object_count,
        label_borderwidth = [None] * self.current_fleet_object_count,
        label_class_ = [None] * self.current_fleet_object_count,
        label_compound = [None] * self.current_fleet_object_count,
        label_cursor = [None] * self.current_fleet_object_count,
        label_font = ['Arial 25 bold'] * self.current_fleet_object_count,
        label_foreground = [None] * self.current_fleet_object_count,
        label_image = [None] * self.current_fleet_object_count,
        label_justify = [None] * self.current_fleet_object_count,
        label_name = ['current_fleet_label', 'current_selected_fleet_label'],
        label_padding = [None] * self.current_fleet_object_count,
        label_relief = [None] * self.current_fleet_object_count,
        label_state = [None] * self.current_fleet_object_count,
        label_style = [None] * self.current_fleet_object_count,
        label_takefocus = [None] * self.current_fleet_object_count,
        label_text=['Selected Fleet:', self.current_selected_fleet],
        label_textvariable = [None] * self.current_fleet_object_count,
        label_underline= [None] * self.current_fleet_object_count,
        label_width = [None] * self.current_fleet_object_count,
        label_wraplength = [None] * self.current_fleet_object_count,
        
        label_grid_cnf = [None] * self.current_fleet_object_count,
        label_grid_column = [1, 2],
        label_grid_columnspan = [None] * self.current_fleet_object_count,
        label_grid_row = [1, 1],
        label_grid_rowspawn = [None] * self.current_fleet_object_count,
        label_grid_ipadx = [None] * self.current_fleet_object_count,
        label_grid_ipady = [None] * self.current_fleet_object_count,
        label_grid_padx = [None] * self.current_fleet_object_count,
        label_grid_pady = [None] * self.current_fleet_object_count,
        label_grid_sticky = [None] * self.current_fleet_object_count,
        label_grid_in_ = [None] * self.current_fleet_object_count)

    def toggle_hotkeys(self, checkbox_variable):
        
        if checkbox_variable.get() == 1:
            hotkeys.enable.start()
        else:
            hotkeys.enable.stop()

    
    def lock_hotkeys(self, checkbox_variable, hotkey_inputs):
        
        if checkbox_variable.get() == 1:
            for n in range(0, len(hotkey_inputs)):
                hotkey_inputs[n]['state'] = READONLY
        else:
            for n in range(0, len(hotkey_inputs)):
                hotkey_inputs[n]['state'] = ON

    def save_hotkeys(self):

        print(self.fleet_command_entry_value_one.get())
        print(self.fleet_command_entry_value_two.get())
        print(self.fleet_command_entry_value_three.get())
        print(self.fleet_command_entry_value_four.get())

        formwidgets.FormWidgets.create_toastnotification(self,
        title = "Saved hotkey configuration",
        message = 'Current hotkey configuration has been saved to the database',
        duration = 3000)

    def select_fleet(self, table_object):

        if self.fleet_selected == False:

            selected_row = table_object.get_rows(selected = True)

            for item in selected_row:
                row_data = item.values
                
            self.current_selected_fleet = row_data
            self.current_fleet_label_objects[1]['text'] = self.current_selected_fleet[0]

            self.fleet_selected = True

            start_kill_client_button_count = 2

            (self.kill_indvidual_clients_button_container,
            self.kill_indvidual_clients_button_objects) = formwidgets.FormWidgets.create_button_grid(self,
            
            grid_objects=start_kill_client_button_count,
            master_container=None,
            recreate=False,

            container_border=None,
            container_borderwidth=None,
            container_class=None,
            container_cursor=None,
            container_height=None,
            container_name='start_kill_client_button_grid_container',
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
            container_pack_ipady=None,
            container_pack_padx=None,
            container_pack_pady=None,
            container_pack_in_=None,

            button_class_=[None]*start_kill_client_button_count,
            button_command=[login.start_clients, killprocess.all_clients],
            button_compound=[None]*start_kill_client_button_count,
            button_cursor=[None]*start_kill_client_button_count,
            button_default=[None]*start_kill_client_button_count,
            button_image=[None]*start_kill_client_button_count,
            button_name=['start_cleints_button','kill_clients_button'],
            button_padding=[None]*start_kill_client_button_count,
            button_state=[None]*start_kill_client_button_count,
            button_style=[None]*start_kill_client_button_count,
            button_takefocus=[None]*start_kill_client_button_count,
            button_text=['Start All Clients','Kill All Clients'],
            button_textvariable=[None]*start_kill_client_button_count,
            button_underline=[None]*start_kill_client_button_count,
            button_width=[15]*start_kill_client_button_count,
            button_bootstyle=[SUCCESS,DANGER],

            button_grid_cnf=[None]*start_kill_client_button_count,
            button_grid_column=[1,2],
            button_grid_columnspan=[None]*start_kill_client_button_count,
            button_grid_row=[1,1],
            button_grid_rowspawn=[None]*start_kill_client_button_count,
            button_grid_ipadx=[None]*start_kill_client_button_count,
            button_grid_ipady=[None]*start_kill_client_button_count,
            button_grid_padx=[5]*start_kill_client_button_count,
            button_grid_pady=[5]*start_kill_client_button_count,
            button_grid_sticky=[None]*start_kill_client_button_count,
            button_grid_in_=[None]*start_kill_client_button_count)    
           
            self.kill_indvidual_clients_button_container, kill_indvidual_clients_button_grid_container_objects = self.generate_client_buttons(self.current_selected_fleet, recreate = False, master_container=None)
            
            self.fleet_commands_count = 4

            (self.fleet_commands_container,
            self.fleet_command_button_objects,
            self.fleet_command_label_objests,
            self.fleet_command_entry_objects) = formwidgets.FormWidgets.create_button_label_entry_grid(self,
            
            grid_count = self.fleet_commands_count,
            master_container = None,
            recreate = False,

            container_border=None,
            container_borderwidth=None,
            container_class=None,
            container_cursor=None,
            container_height=None,
            container_name='fleet_commands_container',
            container_padding=None,
            container_relief=None,
            container_style=None,
            container_takefocus=None,
            container_width=None,

            container_pack_cnf = None,
            container_pack_after = None,
            container_pack_anchor = None,
            container_pack_before = None,
            container_pack_expand = None,
            container_pack_fill = None,
            container_pack_side = None,
            container_pack_ipadx = None,
            container_pack_ipady = None,
            container_pack_padx = None,
            container_pack_pady = None,
            container_pack_in_ = None,
            
            button_class_ = [None] * self.fleet_commands_count,
            button_command = [fleetcommands.group_invite,
                              fleetcommands.group_formation,
                              fleetcommands.group_attack,
                              fleetcommands.group_dock_gate],
            button_compound = [None] * self.fleet_commands_count,
            button_cursor = [None] * self.fleet_commands_count,
            button_default = [None] * self.fleet_commands_count,
            button_image = [None] * self.fleet_commands_count,
            button_name = ['group_invite_button','group_formation_button','group_attack_button','group_gate_dock_button'],
            button_padding= [None] * self.fleet_commands_count,
            button_state = [None] * self.fleet_commands_count,
            button_style = [None] * self.fleet_commands_count,
            button_takefocus = [None] * self.fleet_commands_count,
            button_text = ['Group invite',
                           'Group formation',
                           'Group attack',
                           'Group dock gate'],
            button_textvariable = [None] * self.fleet_commands_count,
            button_underline = [None] * self.fleet_commands_count,
            button_width = [15] * self.fleet_commands_count,
            button_bootstyle = [PRIMARY] * self.fleet_commands_count,
            
            button_grid_cnf = [None] * self.fleet_commands_count,
            button_grid_column = [1, 4, 7, 1] ,
            button_grid_columnspan = [None] * self.fleet_commands_count,
            button_grid_row = [1, 1, 1, 2],
            button_grid_rowspawn = [None] * self.fleet_commands_count,
            button_grid_ipadx = [None] * self.fleet_commands_count,
            button_grid_ipady = [None] * self.fleet_commands_count,
            button_grid_padx = [5] * self.fleet_commands_count,
            button_grid_pady = [5] * self.fleet_commands_count,
            button_grid_sticky = [None] * self.fleet_commands_count,
            button_grid_in_ = [None] * self.fleet_commands_count,

            label_anchor = [None] * self.fleet_commands_count,
            label_background = [None] * self.fleet_commands_count,
            label_border = [None] * self.fleet_commands_count,
            label_borderwidth = [None] * self.fleet_commands_count,
            label_class_ = [None] * self.fleet_commands_count,
            label_compound = [None] * self.fleet_commands_count,
            label_cursor = [None] * self.fleet_commands_count,
            label_font = [None] * self.fleet_commands_count,
            label_foreground = [None] * self.fleet_commands_count,
            label_image = [None] * self.fleet_commands_count,
            label_justify = [None] * self.fleet_commands_count,
            label_name = ['group_invite_label','group_formation_label','group_attack_label','group_gate_dock_label'],
            label_padding = [None] * self.fleet_commands_count,
            label_relief = [None] * self.fleet_commands_count,
            label_state = [None] * self.fleet_commands_count,
            label_style = [None] * self.fleet_commands_count, 
            label_takefocus = [None] * self.fleet_commands_count,
            label_text = ['Hotkey:'] * self.fleet_commands_count,
            label_textvariable = [None] * self.fleet_commands_count,
            label_underline= [None] * self.fleet_commands_count, 
            label_width = [8] * self.fleet_commands_count,
            label_wraplength = [None] * self.fleet_commands_count,
            
            label_grid_cnf = [None] * self.fleet_commands_count,
            label_grid_column = [2,5,8,2],
            label_grid_columnspan = [None] * self.fleet_commands_count,
            label_grid_row = [1,1,1,2],
            label_grid_rowspawn = [None] * self.fleet_commands_count,
            label_grid_ipadx = [None] * self.fleet_commands_count,
            label_grid_ipady = [None] * self.fleet_commands_count,
            label_grid_padx = [5] * self.fleet_commands_count,
            label_grid_pady = [5] * self.fleet_commands_count,
            label_grid_sticky = [None] * self.fleet_commands_count,
            label_grid_in_ = [None] * self.fleet_commands_count,

            entry_background= [None] * self.fleet_commands_count,
            entry_class_= [None] * self.fleet_commands_count,
            entry_cursor= [None] * self.fleet_commands_count,
            entry_exportselection= [None] * self.fleet_commands_count,
            entry_font= [None] * self.fleet_commands_count,
            entry_foreground= [None] * self.fleet_commands_count,
            entry_invalidcommand= [None] * self.fleet_commands_count,
            entry_justify= [None] * self.fleet_commands_count,
            entry_name= ['group_invite_entry','group_formation_entry','group_attack_entry','group_gate_dock_entry'],
            entry_show= [None] * self.fleet_commands_count,
            entry_state= [None] * self.fleet_commands_count, 
            entry_style= [None] * self.fleet_commands_count,
            entry_takefocus= [None] * self.fleet_commands_count,
            entry_textvariable= [self.fleet_command_entry_value_one,
                                self.fleet_command_entry_value_two,
                                self.fleet_command_entry_value_three,
                                self.fleet_command_entry_value_four],
            entry_validate= [None] * self.fleet_commands_count,
            entry_validatecommand= [None] * self.fleet_commands_count,
            entry_width= [5] * self.fleet_commands_count,
            entry_xscrollcommand= [None] * self.fleet_commands_count,
            
            entry_grid_cnf = [None] * self.fleet_commands_count,
            entry_grid_column = [3,6,9,3],
            entry_grid_columnspan = [None] * self.fleet_commands_count,
            entry_grid_row = [1,1,1,2],
            entry_grid_rowspawn = [None] * self.fleet_commands_count,
            entry_grid_ipadx = [None] * self.fleet_commands_count,
            entry_grid_ipady = [None] * self.fleet_commands_count,
            entry_grid_padx = [5] * self.fleet_commands_count,
            entry_grid_pady = [5] * self.fleet_commands_count,
            entry_grid_sticky = [None] * self.fleet_commands_count,
            entry_grid_in_ = [None] * self.fleet_commands_count)

            (self.hotkey_error_label_container,
            self.hotkey_error_label_objects) = formwidgets.FormWidgets.create_label_grid(self, 
            
            grid_count=1,
            master_container=None,
            recreate=False,
        
            container_border=None,
            container_borderwidth=None,
            container_class=None,
            container_cursor=None,
            container_height=None,
            container_name='hotkey_error_label_container',
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
            container_pack_pady=5,
            container_pack_in_=None,   
            
            label_anchor = [None],
            label_background = [None],
            label_border = [None],
            label_borderwidth = [None],
            label_class_ = [None],
            label_compound = [None],
            label_cursor = [None],
            label_font = [None],
            label_foreground = [None],
            label_image = [None],
            label_justify = [None],
            label_name = ['hotkey_error_label'],
            label_padding = [None],
            label_relief = [None],
            label_state = [None],
            label_style = [None],
            label_takefocus = [None],
            label_text= [''],
            label_textvariable = [None],
            label_underline= [None],
            label_width = [None],
            label_wraplength = [None],

            label_grid_cnf = [None],
            label_grid_column = [1],
            label_grid_columnspan = [None],
            label_grid_row = [1],
            label_grid_rowspawn = [None],
            label_grid_ipadx = [None],
            label_grid_ipady = [None],
            label_grid_padx = [None],
            label_grid_pady = [None],
            label_grid_sticky = [None],
            label_grid_in_ = [None])

            self.hotkey_checkbutton_count = 2

            (self.hotkey_checkbutton_container,
            self.hotkey_checkbutton_objects) = formwidgets.FormWidgets.create_checkbutton_grid(self,
            
            grid_objects = self.hotkey_checkbutton_count,
            master_container = None,
            recreate = False,

            container_border=None,
            container_borderwidth=None,
            container_class=None,
            container_cursor=None,
            container_height=None,
            container_name='hotkey_checkbutton_container',

            container_padding=None,
            container_relief=None,
            container_style=None,
            container_takefocus=None,
            container_width=None,

            container_pack_cnf = None,
            container_pack_after = None,
            container_pack_anchor = None,
            container_pack_before = None,
            container_pack_expand = None,
            container_pack_fill= None,
            container_pack_side = None,
            container_pack_ipadx = None,
            container_pack_ipady = None,
            container_pack_padx = None,
            container_pack_pady = None,
            container_pack_in_ = None,
            
            checkbutton_class_ = [None] * self.hotkey_checkbutton_count,
            checkbutton_command = [lambda : self.toggle_hotkeys(self.enable_hotkey_checkbox_variable), 
                                   lambda : self.lock_hotkeys(self.lock_hotkey_checkbox_variable, self.fleet_command_entry_objects)],
            checkbutton_compound = [None] * self.hotkey_checkbutton_count,
            checkbutton_cursor = [None] * self.hotkey_checkbutton_count,
            checkbutton_image = [None] * self.hotkey_checkbutton_count,
            checkbutton_name = ['toggle_hotkeys', 'lock_hotkeys'],
            checkbutton_offvalue = [0] * self.hotkey_checkbutton_count,
            checkbutton_onvalue = [1] * self.hotkey_checkbutton_count,
            checkbutton_padding = [None] * self.hotkey_checkbutton_count,
            checkbutton_state = [None] * self.hotkey_checkbutton_count,
            checkbutton_style = [None] * self.hotkey_checkbutton_count,
            checkbutton_takefocus = [None] * self.hotkey_checkbutton_count,          
            checkbutton_text = ['Toggle Hotkeys', 'Lock Hotkeys'],
            checkbutton_textvariable = [None] * self.hotkey_checkbutton_count,
            checkbutton_underline = [None] * self.hotkey_checkbutton_count,
            checkbutton_variable = [self.enable_hotkey_checkbox_variable,
                                    self.lock_hotkey_checkbox_variable],
            checkbutton_width = [None] * self.hotkey_checkbutton_count,
            checkbutton_bootstyle = ['success-round-toggle'] * self.hotkey_checkbutton_count,
            
            checkbutton_grid_cnf = [None] * self.hotkey_checkbutton_count,
            checkbutton_grid_column = [1, 2],
            checkbutton_grid_columnspan = [None] * self.hotkey_checkbutton_count,
            checkbutton_grid_row = [1, 1],
            checkbutton_grid_rowspawn = [None] * self.hotkey_checkbutton_count,
            checkbutton_grid_ipadx = [None] * self.hotkey_checkbutton_count,
            checkbutton_grid_ipady = [None] * self.hotkey_checkbutton_count,
            checkbutton_grid_padx = [5] * self.hotkey_checkbutton_count,
            checkbutton_grid_pady = [None] * self.hotkey_checkbutton_count,
            checkbutton_grid_sticky = [None] * self.hotkey_checkbutton_count,
            checkbutton_grid_in_ = [None] * self.hotkey_checkbutton_count)

            for n in range(0, len(self.fleet_command_entry_objects)):
                add_validation(self.fleet_command_entry_objects[n],
                Validate.hotkey,
                when = 'all',
                error_label = self.hotkey_error_label_objects[0])
            
            (self.save_hotkeys_button_container,
            self.save_hotkeys_button_objects) = formwidgets.FormWidgets.create_button_grid(self,
            
            grid_objects=1,
            master_container=None,
            recreate=False,

            container_border=None,
            container_borderwidth=None,
            container_class=None,
            container_cursor=None,
            container_height=None,
            container_name='save_hotkeys_button_grid_container',
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
            container_pack_ipady=None,
            container_pack_padx=None,
            container_pack_pady=None,
            container_pack_in_=None,

            button_class_=[None],
            button_command=[self.save_hotkeys],
            button_compound=[None],
            button_cursor=[None],
            button_default=[None],
            button_image=[None],
            button_name=['save_hotkeys_button'],
            button_padding=[None],
            button_state=[None],
            button_style=[None],
            button_takefocus=[None],
            button_text=['Save Hotkeys'],
            button_textvariable=[None],
            button_underline=[None],
            button_width=[20],
            button_bootstyle=[SUCCESS],

            button_grid_cnf=[None],
            button_grid_column=[1],
            button_grid_columnspan=[None],
            button_grid_row=[1],
            button_grid_rowspawn=[None],
            button_grid_ipadx=[None],
            button_grid_ipady=[None],
            button_grid_padx=[None],
            button_grid_pady=[5],
            button_grid_sticky=[None],
            button_grid_in_=[None])

            (self.player_enhancements_container,
            self.player_enhancements_button_objects,
            self.player_enhancements_combobox_objects,
            self.player_enhancements_progressbar_objects) = self.generate_player_enhancemnts(self.current_selected_fleet, recreate = False, master_container=None)

            (self.equipment_buff_sets_contiainer,
            self.equipment_buff_sets_sub_container_objects,
            self.equipment_buff_sets_label_objects) = self.generate_equipment_buff_sets(fleet_members=self.current_selected_fleet,
                                                                                        recreate=False,
                                                                                        master_container=None)
            
            (self.individual_equipment_buff_set_containers,
            self.individual_equipment_buff_set_button_objects,
            self.individual_equipment_buff_set_progressbar_objects) = self.create_individual_buffs(fleet_member_sets=None, sub_containers=self.equipment_buff_sets_sub_container_objects)

            # for i in range(len(self.equipment_buff_sets_sub_container_objects)):
            #     test =(self.equipment_buff_sets_sub_container_objects[i].winfo_children())
            #     print(test)

            # print(len(self.individual_equipment_buff_set_containers))

            # for i in range(len(self.individual_equipment_buff_set_containers)):
            #     for j in range(len(self.individual_equipment_buff_set_containers[i])):
            #         print(self.individual_equipment_buff_set_containers[i][j].winfo_children())
            
            # for j in range(len(self.individual_equipment_buff_set_containers)):
            #     test =(self.individual_equipment_buff_set_containers[j].winfo_children())
            #     print(test)

        elif self.fleet_selected == True:
            select_new_fleet_messagebox = formwidgets.FormWidgets.create_warning_messagebox_yesno(self,
            message ='You are about to select a new fleet which will kill the current clients and reconfigure the Fleet Commands Tab.\nAre you sure you want to do this?',
            title = 'Select New Fleet Warning',
            alert = True)

            if select_new_fleet_messagebox == True:

                for i in range(1, len(self.current_selected_fleet)):
                    killprocess.target_client(self.current_selected_fleet[i])

                selected_row = table_object.get_rows(selected = True)

                for item in selected_row:
                    row_data = item.values
                
                self.fleet_selected = True
                self.current_selected_fleet = row_data
                self.current_fleet_label_objects[1]['text'] = self.current_selected_fleet[0]

                formwidgets.FormWidgets.destroy_children_widgets(self, self.kill_indvidual_clients_button_container)
                formwidgets.FormWidgets.destroy_children_widgets(self, self.hotkey_checkbutton_container)
                formwidgets.FormWidgets.destroy_children_widgets(self, self.save_hotkeys_button_container)
                formwidgets.FormWidgets.destroy_children_widgets(self, self.fleet_commands_container)
                formwidgets.FormWidgets.destroy_children_widgets(self, self.player_enhancements_container)
                formwidgets.FormWidgets.destroy_children_widgets(self, self.equipment_buff_sets_contiainer)

                (self.kill_indvidual_clients_button_container,
                self.kill_indvidual_clients_button_objects) = self.generate_client_buttons(self.current_selected_fleet, recreate = True, master_container = self.kill_indvidual_clients_button_container)

                self.fleet_command_entry_value_one.set('')
                self.fleet_command_entry_value_two.set('')
                self.fleet_command_entry_value_three.set('')
                self.fleet_command_entry_value_four.set('')

                (self.fleet_commands_container,
                self.fleet_command_button_objects,
                self.fleet_command_label_objests,
                self.fleet_command_entry_objects) = formwidgets.FormWidgets.create_button_label_entry_grid(self,
                
                
                grid_count = self.fleet_commands_count,
                master_container = self.fleet_commands_container,
                recreate = True,

                container_border=None,
                container_borderwidth=None,
                container_class=None,
                container_cursor=None,
                container_height=None,
                container_name='fleet_commands_container',
                container_padding=None,
                container_relief=None,
                container_style=None,
                container_takefocus=None,
                container_width=None,

                container_pack_cnf = None,
                container_pack_after = None,
                container_pack_anchor = None,
                container_pack_before = None,
                container_pack_expand = None,
                container_pack_fill = None,
                container_pack_side = None,
                container_pack_ipadx = None,
                container_pack_ipady = None,
                container_pack_padx = None,
                container_pack_pady = None,
                container_pack_in_ = None,
                
                button_class_ = [None] * self.fleet_commands_count,
                button_command = [fleetcommands.group_invite,
                                fleetcommands.group_formation,
                                fleetcommands.group_attack,
                                fleetcommands.group_dock_gate],
                button_compound = [None] * self.fleet_commands_count,
                button_cursor = [None] * self.fleet_commands_count,
                button_default = [None] * self.fleet_commands_count,
                button_image = [None] * self.fleet_commands_count,
                button_name = ['group_invite_button','group_formation_button','group_attack_button','group_gate_dock_button'],
                button_padding=[None] * self.fleet_commands_count,
                button_state = [None] * self.fleet_commands_count,
                button_style = [None] * self.fleet_commands_count,
                button_takefocus = [None] * self.fleet_commands_count,
                button_text = ['Group invite', 'Group formation', 'Group attack', 'Group dock gate'],
                button_textvariable = [None] * self.fleet_commands_count,
                button_underline = [None] * self.fleet_commands_count,
                button_width = [15] * self.fleet_commands_count,
                button_bootstyle = [PRIMARY] * self.fleet_commands_count,
                
                button_grid_cnf = [None] * self.fleet_commands_count,
                button_grid_column = [1, 4, 7, 1] ,
                button_grid_columnspan = [None] * self.fleet_commands_count,
                button_grid_row = [1, 1, 1, 2],
                button_grid_rowspawn = [None] * self.fleet_commands_count,
                button_grid_ipadx = [None] * self.fleet_commands_count,
                button_grid_ipady = [None] * self.fleet_commands_count,
                button_grid_padx = [5] * self.fleet_commands_count,
                button_grid_pady = [5] * self.fleet_commands_count,
                button_grid_sticky = [None] * self.fleet_commands_count,
                button_grid_in_ = [None] * self.fleet_commands_count,

                label_anchor = [None] * self.fleet_commands_count,
                label_background = [None] * self.fleet_commands_count,
                label_border = [None] * self.fleet_commands_count,
                label_borderwidth = [None] * self.fleet_commands_count,
                label_class_ = [None] * self.fleet_commands_count,
                label_compound = [None] * self.fleet_commands_count,
                label_cursor = [None] * self.fleet_commands_count,
                label_font = [None] * self.fleet_commands_count,
                label_foreground = [None] * self.fleet_commands_count,
                label_image = [None] * self.fleet_commands_count,
                label_justify = [None] * self.fleet_commands_count,
                label_name = ['group_invite_label','group_formation_label','group_attack_label','group_gate_dock_label'],
                label_padding = [None] * self.fleet_commands_count,
                label_relief = [None] * self.fleet_commands_count,
                label_state = [None] * self.fleet_commands_count,
                label_style = [None] * self.fleet_commands_count, 
                label_takefocus = [None] * self.fleet_commands_count,
                label_text = ['Hotkey:'] * self.fleet_commands_count,
                label_textvariable = [None] * self.fleet_commands_count,
                label_underline= [None] * self.fleet_commands_count,
                label_width = [8] * self.fleet_commands_count,
                label_wraplength = [None] * self.fleet_commands_count,
                
                label_grid_cnf = [None] * self.fleet_commands_count,
                label_grid_column = [2,5,8,2],
                label_grid_columnspan = [None] * self.fleet_commands_count,
                label_grid_row = [1,1,1,2],
                label_grid_rowspawn = [None] * self.fleet_commands_count,
                label_grid_ipadx = [None] * self.fleet_commands_count,
                label_grid_ipady = [None] * self.fleet_commands_count,
                label_grid_padx = [5] * self.fleet_commands_count,
                label_grid_pady = [5] * self.fleet_commands_count,
                label_grid_sticky = [None] * self.fleet_commands_count,
                label_grid_in_ = [None] * self.fleet_commands_count,

                entry_background= [None] * self.fleet_commands_count,
                entry_class_= [None] * self.fleet_commands_count,
                entry_cursor= [None] * self.fleet_commands_count,
                entry_exportselection= [None] * self.fleet_commands_count,
                entry_font= [None] * self.fleet_commands_count,
                entry_foreground= [None] * self.fleet_commands_count,
                entry_invalidcommand= [None] * self.fleet_commands_count,
                entry_justify= [None] * self.fleet_commands_count,
                entry_name= ['group_invite_entry','group_formation_entry','group_attack_entry','group_gate_dock_entry'],
                entry_show= [None] * self.fleet_commands_count,
                entry_state= [None] * self.fleet_commands_count,
                entry_style= [None] * self.fleet_commands_count,
                entry_takefocus= [None] * self.fleet_commands_count,
                entry_textvariable= [self.fleet_command_entry_value_one,
                                    self.fleet_command_entry_value_two,
                                    self.fleet_command_entry_value_three,
                                    self.fleet_command_entry_value_four],
                entry_validate= [None] * self.fleet_commands_count,
                entry_validatecommand= [None] * self.fleet_commands_count,
                entry_width= [5] * self.fleet_commands_count,
                entry_xscrollcommand= [None] * self.fleet_commands_count,
                
                entry_grid_cnf = [None] * self.fleet_commands_count,
                entry_grid_column = [3,6,9,3],
                entry_grid_columnspan = [None] * self.fleet_commands_count,
                entry_grid_row = [1,1,1,2],
                entry_grid_rowspawn = [None] * self.fleet_commands_count,
                entry_grid_ipadx = [None] * self.fleet_commands_count,
                entry_grid_ipady = [None] * self.fleet_commands_count,
                entry_grid_padx = [5] * self.fleet_commands_count,
                entry_grid_pady = [5] * self.fleet_commands_count,
                entry_grid_sticky = [None] * self.fleet_commands_count,
                entry_grid_in_ = [None] * self.fleet_commands_count)

                self.enable_hotkey_checkbox_variable.set(0)
                self.lock_hotkey_checkbox_variable.set(0)

                (self.hotkey_checkbutton_container,
                self.hotkey_checkbutton_objects)= formwidgets.FormWidgets.create_checkbutton_grid(self,
                
                grid_objects = self.hotkey_checkbutton_count,
                master_container = self.hotkey_checkbutton_container,
                recreate = True,

                container_border=None,
                container_borderwidth=None,
                container_class=None,
                container_cursor=None,
                container_height=None,
                container_name='hotkey_checkbutton_container',
                container_padding=None,
                container_relief=None,
                container_style=None,
                container_takefocus=None,
                container_width=None,

                container_pack_cnf = None,
                container_pack_after = None,
                container_pack_anchor = None,
                container_pack_before = None,
                container_pack_expand = None,
                container_pack_fill= None,
                container_pack_side = None,
                container_pack_ipadx = None,
                container_pack_ipady = None,
                container_pack_padx = None,
                container_pack_pady = None,
                container_pack_in_ = None,
                
                checkbutton_class_ = [None] * self.hotkey_checkbutton_count,
                checkbutton_command = [lambda:self.toggle_hotkeys(self.enable_hotkey_checkbox_variable),
                                    lambda:self.lock_hotkeys(self.lock_hotkey_checkbox_variable, self.fleet_command_entry_objects)],
                checkbutton_compound = [None] * self.hotkey_checkbutton_count ,
                checkbutton_cursor = [None] * self.hotkey_checkbutton_count,
                checkbutton_image = [None] * self.hotkey_checkbutton_count,
                checkbutton_name = ['toggle_hotkeys', 'lock_hotkeys'],
                checkbutton_offvalue = [0] * self.hotkey_checkbutton_count,
                checkbutton_onvalue = [1] * self.hotkey_checkbutton_count,
                checkbutton_padding = [None] * self.hotkey_checkbutton_count,
                checkbutton_state = [None] * self.hotkey_checkbutton_count,
                checkbutton_style = [None] * self.hotkey_checkbutton_count,
                checkbutton_takefocus = [None] * self.hotkey_checkbutton_count,          
                checkbutton_text = ['Toggle Hotkeys', 'Lock Hotkeys'],
                checkbutton_textvariable = [None] * self.hotkey_checkbutton_count,
                checkbutton_underline = [None] * self.hotkey_checkbutton_count,
                checkbutton_variable = [self.enable_hotkey_checkbox_variable,
                                        self.lock_hotkey_checkbox_variable],
                checkbutton_width = [None] * self.hotkey_checkbutton_count,
                checkbutton_bootstyle = ['success-round-toggle'] * self.hotkey_checkbutton_count,
                
                checkbutton_grid_cnf = [None] * self.hotkey_checkbutton_count,
                checkbutton_grid_column = [1, 2],
                checkbutton_grid_columnspan = [None] * self.hotkey_checkbutton_count,
                checkbutton_grid_row = [1, 1],
                checkbutton_grid_rowspawn = [None] * self.hotkey_checkbutton_count,
                checkbutton_grid_ipadx = [None] * self.hotkey_checkbutton_count,
                checkbutton_grid_ipady = [None] * self.hotkey_checkbutton_count,
                checkbutton_grid_padx = [5] * self.hotkey_checkbutton_count,
                checkbutton_grid_pady = [None] * self.hotkey_checkbutton_count,
                checkbutton_grid_sticky = [None] * self.hotkey_checkbutton_count,
                checkbutton_grid_in_ = [None] * self.hotkey_checkbutton_count)

                for n in range(0, len(self.fleet_command_entry_objects)):
                    add_validation(self.fleet_command_entry_objects[n],
                    Validate.hotkey,
                    when = 'all',
                    error_label = self.hotkey_error_label_objects[0])

                self.save_hotkeys_button_container, self.save_hotkeys_button_objects = formwidgets.FormWidgets.create_button_grid(self,
                grid_objects=1,
                master_container=self.save_hotkeys_button_container,
                recreate=True,

                container_border=None,
                container_borderwidth=None,
                container_class=None,
                container_cursor=None,
                container_height=None,
                container_name='save_hotkeys_button_container',
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
                container_pack_ipady=None,
                container_pack_padx=None,
                container_pack_pady=None,
                container_pack_in_=None,

                button_class_=[None],
                button_command=[self.save_hotkeys],
                button_compound=[None],
                button_cursor=[None],
                button_default=[None],
                button_image=[None],
                button_name=['save_hotkeys_button'],
                button_padding=[None],
                button_state=[None],
                button_style=[None],
                button_takefocus=[None],
                button_text=['Save Hotkeys'],
                button_textvariable=[None],
                button_underline=[None],
                button_width=[20],
                button_bootstyle=[SUCCESS],

                button_grid_cnf=[None],
                button_grid_column=[1],
                button_grid_columnspan=[None],
                button_grid_row=[1],
                button_grid_rowspawn=[None],
                button_grid_ipadx=[None],
                button_grid_ipady=[None],
                button_grid_padx=[None],
                button_grid_pady=[5],
                button_grid_sticky=[None],
                button_grid_in_=[None])
                
                (self.player_enhancements_container,
                self.player_enhancements_button_objects,
                self.player_enhancements_combobox_objects,
                self.player_enhancements_progressbar_objects) = self.generate_player_enhancemnts(self.current_selected_fleet, recreate = True, master_container = self.player_enhancements_container)

                (self.equipment_buff_sets_contiainer,
                self.equipment_buff_sets_sub_container_objects,
                self.equipment_buff_sets_label_objects) = self.generate_equipment_buff_sets(fleet_members = self.current_selected_fleet,
                                                                                            recreate=True,
                                                                                            master_container=self.equipment_buff_sets_contiainer)
                (self.individual_equipment_buff_set_containers,
                self.individual_equipment_buff_set_button_objects,
                self.individual_equipment_buff_set_progressbar_objects) = self.create_individual_buffs(fleet_member_sets=None, sub_containers=self.equipment_buff_sets_sub_container_objects)

                # for i in range(len(self.equipment_buff_sets_sub_container_objects)):
                #     test =(self.equipment_buff_sets_sub_container_objects[i].winfo_children())
                #     print(test)

                # print(len(self.individual_equipment_buff_set_containers))
                # for i in range(len(self.individual_equipment_buff_set_containers)):
                #     for j in range(len(self.individual_equipment_buff_set_containers[i])):
                #         print(self.individual_equipment_buff_set_containers[i][j].winfo_children())

                # for j in range(len(self.individual_equipment_buff_set_containers)):
                #     test =(self.individual_equipment_buff_set_containers[j].winfo_children())
                #     print(test)

            else:
                print('Error')

    def generate_client_buttons(self, fleet_members, recreate, master_container):
        n = len(fleet_members) - 1

        match (n):
            case 1:
                bgc = [1]
                bgr = [1]
                test1 = [lambda: killprocess.target_client(fleet_members[1])] 
                test2 = [f'Kill {fleet_members[1]}']
            case 2:
                bgc = [1, 2]
                bgr = [1, 1]
                test1 = [lambda: killprocess.target_client(fleet_members[1]),
                         lambda: killprocess.target_client(fleet_members[2])] 
                test2 = [f'Kill {fleet_members[1]}',
                         f'Kill {fleet_members[2]}']
            case 3:
                bgc = [1, 2, 3]
                bgr = [1, 1, 1]
                test1 = [lambda: killprocess.target_client(fleet_members[1]),
                         lambda: killprocess.target_client(fleet_members[2]),
                         lambda: killprocess.target_client(fleet_members[3])] 
                test2 = [f'Kill {fleet_members[1]}',
                         f'Kill {fleet_members[2]}',
                         f'Kill {fleet_members[3]}']
            case 4:
                bgc = [1, 2, 3, 1]
                bgr = [1, 1, 1, 2]
                test1 = [lambda: killprocess.target_client(fleet_members[1]),
                         lambda: killprocess.target_client(fleet_members[2]),
                         lambda: killprocess.target_client(fleet_members[3]),
                         lambda: killprocess.target_client(fleet_members[4])] 
                test2 = [f'Kill {fleet_members[1]}',
                         f'Kill {fleet_members[2]}',
                         f'Kill {fleet_members[3]}',
                         f'Kill {fleet_members[4]}']
            case 5:
                bgc = [1, 2, 3, 1, 2]
                bgr = [1, 1, 1, 2, 2]
                test1 = [lambda: killprocess.target_client(fleet_members[1]),
                         lambda: killprocess.target_client(fleet_members[2]),
                         lambda: killprocess.target_client(fleet_members[3]),
                         lambda: killprocess.target_client(fleet_members[4]),
                         lambda: killprocess.target_client(fleet_members[5])] 
                test2 = [f'Kill {fleet_members[1]}',
                         f'Kill {fleet_members[2]}',
                         f'Kill {fleet_members[3]}',
                         f'Kill {fleet_members[4]}',
                         f'Kill {fleet_members[5]}']
            case 6:
                bgc = [1, 2, 3, 1, 2, 3]
                bgr = [1, 1, 1, 2, 2, 2]
                test1 = [lambda: killprocess.target_client(fleet_members[1]),
                         lambda: killprocess.target_client(fleet_members[2]),
                         lambda: killprocess.target_client(fleet_members[3]),
                         lambda: killprocess.target_client(fleet_members[4]),
                         lambda: killprocess.target_client(fleet_members[5]),
                         lambda: killprocess.target_client(fleet_members[6])] 
                test2 = [f'Kill {fleet_members[1]}',
                         f'Kill {fleet_members[2]}',
                         f'Kill {fleet_members[3]}',
                         f'Kill {fleet_members[4]}',
                         f'Kill {fleet_members[5]}',
                         f'Kill {fleet_members[6]}']
                
        (self.kill_indvidual_clients_button_container,
        self.kill_indvidual_clients_button_objects) = formwidgets.FormWidgets.create_button_grid(self,
        
        master_container=master_container,       
        grid_objects=n,
        recreate=recreate,

        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='kill_indvidual_clients_button_container',
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
        container_pack_ipady=None,
        container_pack_padx=None,
        container_pack_pady=10,
        container_pack_in_=None,

        button_class_=[None]*n,
        button_command=test1,
        button_compound=[None]*n,
        button_cursor=[None]*n,
        button_default=[None]*n,
        button_image=[None]*n,
        button_name=[None]*n,
        button_padding=[None]*n,
        button_state=[None]*n,
        button_style=[None]*n,
        button_takefocus=[None]*n,
        button_text=test2,
        button_textvariable=[None]*n,
        button_underline=[None]*n,
        button_width=[15]*n,
        button_bootstyle=[DANGER]*n,

        button_grid_cnf=[None]*n,
        button_grid_column=bgc,
        button_grid_columnspan=[None]*n,
        button_grid_row=bgr,
        button_grid_rowspawn=[None]*n,
        button_grid_ipadx=[None]*n,
        button_grid_ipady=[None]*n,
        button_grid_padx=[5]*n,
        button_grid_pady=[5]*n,
        button_grid_sticky=[None]*n,
        button_grid_in_=[None]*n)

        return self.kill_indvidual_clients_button_container, self.kill_indvidual_clients_button_objects    

    def generate_player_enhancemnts(self, fleet_members, recreate, master_container):

        button_commands = []
        n = len(fleet_members) - 1
        
        match (n):
            case 1:
                bgc = [1]
                bgr = [1]
                cbgc = [2]
                cbgr = [1]
                fggc = [3]
                fggr = [1]
                pb_name = ['test1']
                button_text = ['test1']
                button_name = ['test1']
                for a in range(n):
                    button_commands.append(lambda a=a: self.activate_buff(test=(a+1), button_container=self.player_enhancements_button_objects, progressbar_container=self.player_enhancements_progressbar_objects))
                cb_vars = [['1','2','3','4','5','6','alt-1','alt-2','alt-3','alt-4','alt-5','alt-6']]
            case 2:
                bgc = [1, 4]
                bgr = [1, 1]
                cbgc = [2, 5]
                cbgr = [1, 1]
                fggc = [3, 6]
                fggr = [1, 1]
                pb_name = ['test1','test2']
                button_text = ['test1','test2']
                button_name = ['test1','test2']
                for b in range(n):
                    button_commands.append(lambda b=b: self.activate_buff(test=(b+1), button_container=self.player_enhancements_button_objects, progressbar_container=self.player_enhancements_progressbar_objects))
                cb_vars = [['1','2','3','4','5','6','alt-1','alt-2','alt-3','alt-4','alt-5','alt-6'],
                            ['1','2','3','4','5','6','alt-1','alt-2','alt-3','alt-4','alt-5','alt-6']]                
            case 3:
                bgc = [1, 4, 1]
                bgr = [1, 1, 2]
                cbgc = [2, 5, 2]
                cbgr = [1, 1, 2]
                fggc = [3, 6, 3]
                fggr = [1, 1, 2]
                pb_name = ['test1','test2','test3']
                button_text = ['test1','test2','test3']
                button_name = ['test1','test2','test3']
                for c in range(n):
                    button_commands.append(lambda c=c: self.activate_buff(test=(c+1), button_container=self.player_enhancements_button_objects, progressbar_container=self.player_enhancements_progressbar_objects))
                cb_vars = [['1','2','3','4','5','6','alt-1','alt-2','alt-3','alt-4','alt-5','alt-6'],
                            ['1','2','3','4','5','6','alt-1','alt-2','alt-3','alt-4','alt-5','alt-6'],
                            ['1','2','3','4','5','6','alt-1','alt-2','alt-3','alt-4','alt-5','alt-6']]                
            case 4:
                bgc = [1, 4, 1, 4]
                bgr = [1, 1, 2, 2]
                cbgc = [2, 5, 2, 5]
                cbgr = [1, 1, 2, 2]
                fggc = [3, 6, 3, 6]
                fggr = [1, 1, 2, 2]
                pb_name = ['test1','test2','test3','test4']
                button_text = ['test1','test2','test3','test4']
                button_name = ['test1','test2','test3','test4']
                for d in range(n):
                    button_commands.append(lambda d=d: self.activate_buff(test=(d+1), button_container=self.player_enhancements_button_objects, progressbar_container=self.player_enhancements_progressbar_objects))
                cb_vars = [['1','2','3','4','5','6','alt-1','alt-2','alt-3','alt-4','alt-5','alt-6'],
                            ['1','2','3','4','5','6','alt-1','alt-2','alt-3','alt-4','alt-5','alt-6'],
                            ['1','2','3','4','5','6','alt-1','alt-2','alt-3','alt-4','alt-5','alt-6'],
                            ['1','2','3','4','5','6','alt-1','alt-2','alt-3','alt-4','alt-5','alt-6']]                
            case 5:
                bgc = [1, 4, 1, 4, 1]
                bgr = [1, 1, 2, 2, 3]
                cbgc = [2, 5, 2, 5, 2]
                cbgr = [1, 1, 2, 2, 3]
                fggc = [3, 6, 3, 6, 3]
                fggr = [1, 1, 2, 2, 3]
                pb_name = ['test1','test2','test3','test4','test5']
                button_text = ['test1','test2','test3','test4','test5']
                button_name = ['test1','test2','test3','test4','test5']
                for e in range(n):
                    button_commands.append(lambda e=e: self.activate_buff(test=(e+1), button_container=self.player_enhancements_button_objects, progressbar_container=self.player_enhancements_progressbar_objects))
                cb_vars = [['1','2','3','4','5','6','alt-1','alt-2','alt-3','alt-4','alt-5','alt-6'],
                            ['1','2','3','4','5','6','alt-1','alt-2','alt-3','alt-4','alt-5','alt-6'],
                            ['1','2','3','4','5','6','alt-1','alt-2','alt-3','alt-4','alt-5','alt-6'],
                            ['1','2','3','4','5','6','alt-1','alt-2','alt-3','alt-4','alt-5','alt-6'],
                            ['1','2','3','4','5','6','alt-1','alt-2','alt-3','alt-4','alt-5','alt-6']]                
            case 6:
                bgc = [1, 4, 1, 4, 1, 4]
                bgr = [1, 1, 2, 2, 3, 3]
                cbgc = [2, 5, 2, 5, 2, 5]
                cbgr = [1, 1, 2, 2, 3, 3]
                fggc = [3, 6, 3, 6, 3, 6]
                fggr = [1, 1, 2, 2, 3, 3]
                pb_name = ['test1','test2','test3','test4','test5','test6']
                button_text = ['Psionic Shield','Environment Shield','Reactor Optimization','Shield Charging','Rally','AfterBurn']
                button_name = ['psionic_shield_button','environment_shield_button','reactor_optimization_button','shield_charging_button','rally_button','afterburn_button']
                for f in range(n):
                    button_commands.append(lambda f=f: self.activate_buff(test=(f+1), button_container=self.player_enhancements_button_objects, progressbar_container=self.player_enhancements_progressbar_objects))
                cb_vars = [['1','2','3','4','5','6','alt-1','alt-2','alt-3','alt-4','alt-5','alt-6'],
                            ['1','2','3','4','5','6','alt-1','alt-2','alt-3','alt-4','alt-5','alt-6'],
                            ['1','2','3','4','5','6','alt-1','alt-2','alt-3','alt-4','alt-5','alt-6'],
                            ['1','2','3','4','5','6','alt-1','alt-2','alt-3','alt-4','alt-5','alt-6'],
                            ['1','2','3','4','5','6','alt-1','alt-2','alt-3','alt-4','alt-5','alt-6'],
                            ['1','2','3','4','5','6','alt-1','alt-2','alt-3','alt-4','alt-5','alt-6']]                
        
        (self.player_enhancements_container,
        self.player_enhancements_button_objects,
        self.player_enhancements_combobox_objects,
        self.player_enhancements_progressbar_objects) = formwidgets.FormWidgets.create_button_combobox_progressbar_grid(self,
        
        master_container = master_container,        
        recreate = recreate,
        grid_count = n,

        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='player_enhancements_container',
        container_padding=None,
        container_relief=None,
        container_style=None,
        container_takefocus=None,
        container_width=None,

        container_pack_cnf = None,
        container_pack_after = None,
        container_pack_anchor = None,
        container_pack_before = None,
        container_pack_expand = NO,
        container_pack_fill = None,
        container_pack_side = None,
        container_pack_ipadx = None,
        container_pack_ipady = None,
        container_pack_padx = None,
        container_pack_pady = 10,
        container_pack_in_ = None,
        
        button_class_ = [None] * n,
        button_command = button_commands,
        button_compound = [None] * n,
        button_cursor = [None] * n,
        button_default = [None] * n,
        button_image = [None] * n,
        button_name = button_name,
        button_padding= [None] * n,
        button_state = [None] * n,
        button_style = [None] * n,
        button_takefocus = [None] * n,
        button_text = button_text,
        button_textvariable = [None] * n,
        button_underline = [None] * n,
        button_width = [19] * n,
        button_bootstyle = [PRIMARY] * n,
        
        button_grid_cnf = [None] * n,
        button_grid_column = bgc,
        button_grid_columnspan = [None] * n,
        button_grid_row = bgr,
        button_grid_rowspawn = [None] * n,
        button_grid_ipadx = [None] * n,
        button_grid_ipady = [None] * n,
        button_grid_padx = [5] * n,
        button_grid_pady = [5] * n,
        button_grid_sticky = [None] * n,
        button_grid_in_ = [None] * n,
        
        combobox_background = [None] * n,
        combobox_class_ = [None] * n,
        combobox_cursor = [None] * n,
        combobox_exportselection = [None] * n,
        combobox_font = [None] * n,
        combobox_foreground = [None] * n,
        combobox_height = [None] * n,
        combobox_invalidcommand = [None] * n,
        combobox_justify = [None] * n,
        combobox_name = [None] * n,
        combobox_postcommand = [None] * n,
        combobox_show = [None] * n,
        combobox_state = [READONLY] * n,
        combobox_style = [None] * n,
        combobox_takefocus = [None] * n,
        combobox_textvariable= [None] * n,
        combobox_validate = [None] * n,
        combobox_validatecommand = [None] * n,
        combobox_values = cb_vars,
        combobox_width = [4] * n,
        combobox_xscrollcommand = [None] * n,
        
        combobox_grid_cnf = [None] * n,
        combobox_grid_column = cbgc,
        combobox_grid_columnspan = [None] * n,
        combobox_grid_row = cbgr,
        combobox_grid_rowspawn = [None] * n,
        combobox_grid_ipadx = [None] * n,
        combobox_grid_ipady = [None] * n,
        combobox_grid_padx = [5] * n,
        combobox_grid_pady = [5] * n,
        combobox_grid_sticky = [None] * n,
        combobox_grid_in_ = [None] * n,

        progressbar_class_ = [None] * n,
        progressbar_cursor = [None] * n,
        progressbar_length = [200] * n,
        progressbar_maximum = [100] * n,
        progressbar_mode = [None] * n,
        progressbar_name = pb_name,
        progressbar_orient = [HORIZONTAL] * n,
        progressbar_phase = [None] * n,
        progressbar_style = [None] * n,
        progressbar_takefocus = [None] * n,
        progressbar_value = [0] * n,
        progressbar_variable = [None] * n,
        progressbar_bootstyle =['danger-striped'] * n,
        
        progressbar_grid_cnf = [None] * n,
        progressbar_grid_column = fggc,
        progressbar_grid_columnspan = [None] * n,
        progressbar_grid_row = fggr,
        progressbar_grid_rowspawn = [None] * n,
        progressbar_grid_ipadx = [None] * n,
        progressbar_grid_ipady = [None] * n,
        progressbar_grid_padx = [5] * n,
        progressbar_grid_pady = [5] * n,
        progressbar_grid_sticky = [None] * n,
        progressbar_grid_in_ = [None] * n)

        return  (self.player_enhancements_container,
                self.player_enhancements_button_objects,
                self.player_enhancements_combobox_objects,
                self.player_enhancements_progressbar_objects)


    def generate_equipment_buff_sets(self, fleet_members, recreate, master_container):
        
        (self.equipment_buff_sets_contiainer,
        self.equipment_buff_sets_sub_container_objects,
        self.equipment_buff_sets_label_objects) = formwidgets.FormWidgets.create_frame_label_grid(self,
        
        grid_count = len(fleet_members) - 1,
        master_container = master_container,
        recreate = recreate,

        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='equipment_buff_sets_contiainer',
        container_padding=None,
        container_relief=None,
        container_style=None,
        container_takefocus=None,
        container_width=None,

        container_pack_cnf = None,
        container_pack_after = None,
        container_pack_anchor = None,
        container_pack_before = None,
        container_pack_expand = NO,
        container_pack_fill = None,
        container_pack_side = None,
        container_pack_ipadx = None,
        container_pack_ipady = None,
        container_pack_padx = None,
        container_pack_pady = None,
        container_pack_in_ = None,

        sub_container_border=[None]* (len(fleet_members)-1),
        sub_container_borderwidth=[None]* (len(fleet_members)-1),
        sub_container_class=[None]* (len(fleet_members)-1),
        sub_container_cursor=[None]* (len(fleet_members)-1),
        sub_container_height=[None]* (len(fleet_members)-1),
        sub_container_name=['char_one_equipment_buff_set_sub_contiainer',
                            'char_two_equipment_buff_set_sub_contiainer',
                            'char_three_equipment_buff_set_sub_contiainer',
                            'char_four_equipment_buff_set_sub_contiainer',
                            'char_five_equipment_buff_set_sub_contiainer',
                            'char_six_equipment_buff_set_sub_contiainer'],
        sub_container_padding=[None]* (len(fleet_members)-1),
        sub_container_relief=[None]* (len(fleet_members)-1),
        sub_container_style=[None]* (len(fleet_members)-1),
        sub_container_takefocus=[None]* (len(fleet_members)-1),
        sub_container_width=[None]* (len(fleet_members)-1),

        sub_container_grid_cnf=[None] * (len(fleet_members)-1),
        sub_container_grid_column=[1,2,3,4,5,6],
        sub_container_grid_columnspan=[None] * (len(fleet_members)-1),
        sub_container_grid_row=[1,1,1,1,1,1],
        sub_container_grid_rowspawn=[None] * (len(fleet_members)-1),
        sub_container_grid_ipadx=[None] * (len(fleet_members)-1),
        sub_container_grid_ipady=[None] * (len(fleet_members)-1),
        sub_container_grid_padx=[15] * (len(fleet_members)-1),
        sub_container_grid_pady=[None] * (len(fleet_members)-1),
        sub_container_grid_sticky=[N] * (len(fleet_members)-1),
        sub_container_grid_in_=[None] * (len(fleet_members)-1),
        
        label_anchor = [None] * (len(fleet_members)-1),
        label_background = [None] * (len(fleet_members)-1),
        label_border = [None] * (len(fleet_members)-1),
        label_borderwidth = [None] * (len(fleet_members)-1),
        label_class_ = [None] * (len(fleet_members)-1),
        label_compound = [None] * (len(fleet_members)-1),
        label_cursor = [None] * (len(fleet_members)-1),
        label_font = [None] * (len(fleet_members)-1),
        label_foreground = [None] * (len(fleet_members)-1),
        label_image = [None] * (len(fleet_members)-1),
        label_justify = [None] * (len(fleet_members)-1),
        label_name = ['char_one_equipment_buff_set_label',
                      'char_two_equipment_buff_set_label',
                      'char_three_equipment_buff_set_label',
                      'char_four_equipment_buff_set_label',
                      'char_five_equipment_buff_set_label',
                      'char_six_equipment_buff_set_label'],
        label_padding = [None] * (len(fleet_members)-1),
        label_relief = [None] * (len(fleet_members)-1),
        label_state = [None] * (len(fleet_members)-1),
        label_style = [None] * (len(fleet_members)-1),
        label_takefocus = [None] * (len(fleet_members)-1),
        label_text = ['Char1', 'Char2', 'Char3', 'Char4', 'Char5', 'Char6'],
        label_textvariable = [None] * (len(fleet_members)-1),
        label_underline= [None] * (len(fleet_members)-1),
        label_width = [None] * (len(fleet_members)-1),
        label_wraplength = [None] * (len(fleet_members)-1),

        label_grid_cnf = [None] * (len(fleet_members)-1),
        label_grid_column = [1,2,3,4,5,6],
        label_grid_columnspan = [None] * (len(fleet_members)-1),
        label_grid_row = [1,1,1,1,1,1],
        label_grid_rowspawn = [None] * (len(fleet_members)-1),
        label_grid_ipadx = [None] * (len(fleet_members)-1),
        label_grid_ipady = [None] * (len(fleet_members)-1),
        label_grid_padx = [None] * (len(fleet_members)-1),
        label_grid_pady = [None] * (len(fleet_members)-1),
        label_grid_sticky = [None] * (len(fleet_members)-1),
        label_grid_in_ = [None] * (len(fleet_members)-1))
        
        return (self.equipment_buff_sets_contiainer, 
                self.equipment_buff_sets_sub_container_objects, 
                self.equipment_buff_sets_label_objects)
    

    def create_individual_buffs(self, fleet_member_sets, sub_containers):
        
        fleet_member_sets=[['char1_set1'],
                           ['char2_set1','char2_set2'],
                           ['char3_set1','char3_set2','char3_set3'],
                           ['char4_set1'],
                           ['char5_set1','char5_set2','char5_set3','char5_set4','char5_set5'],
                           ['char6_set1','char6_set2','char6_set3','char6_set4','char6_set5','char6_set6']]
        
        containers = []
        buttons = []
        progressbars = []
        container_name_objects =[]
        container_row_objects =[]
        button_name_objects =[]
        button_text_objects =[]
        progressbar_name_objects =[]
        
        for i in range(len(fleet_member_sets)):
            button_commands = []

            match(i):
                case 0:
                    for a in range(len(fleet_member_sets[i])):
                        button_commands.append(lambda a=a: self.activate_set(character_sub_container=sub_containers[0], button_progressbar_container=(a+1)))
                case 1:
                    for b in range(len(fleet_member_sets[i])):
                        button_commands.append(lambda b=b: self.activate_set(character_sub_container=sub_containers[1], button_progressbar_container=(b+1)))
                case 2:
                    for c in range(len(fleet_member_sets[i])):
                        button_commands.append(lambda c=c: self.activate_set(character_sub_container=sub_containers[2], button_progressbar_container=(c+1)))
                case 3:
                    for d in range(len(fleet_member_sets[i])):
                        button_commands.append(lambda d=d: self.activate_set(character_sub_container=sub_containers[3], button_progressbar_container=(d+1)))
                case 4:
                    for e in range(len(fleet_member_sets[i])):
                        button_commands.append(lambda e=e: self.activate_set(character_sub_container=sub_containers[4], button_progressbar_container=(e+1)))
                case 5:
                    for f in range(len(fleet_member_sets[i])):
                        button_commands.append(lambda f=f: self.activate_set(character_sub_container=sub_containers[5], button_progressbar_container=(f+1)))

            if fleet_member_sets[i] != None:

                for j in range(len(fleet_member_sets[i])):
                    container_name_objects.append(f'{fleet_member_sets[i][j]}_container')
                    button_name_objects.append(f'{fleet_member_sets[i][j]}_button')
                    button_text_objects.append(f'{fleet_member_sets[i][j]}')
                    progressbar_name_objects.append(f'{fleet_member_sets[i][j]}_progressbar')

                for k in range(len(fleet_member_sets[i])):
                    container_row_objects.append(k+2)
            
                (self.individual_equipment_buff_set_containers,
                self.individual_equipment_buff_set_button_objects,
                self.individual_equipment_buff_set_progressbar_objects) = formwidgets.FormWidgets.create_button_progressbar_grid(self,
                
                master_container = sub_containers[i],
                grid_count = len(fleet_member_sets[i]),

                container_border=[None] *len(fleet_member_sets[i]),
                container_borderwidth=[None] * len(fleet_member_sets[i]),
                container_class=[None] * len(fleet_member_sets[i]),
                container_cursor=[None] * len(fleet_member_sets[i]),
                container_height=[None] * len(fleet_member_sets[i]),
                container_name=container_name_objects,
                container_padding=[None] * len(fleet_member_sets[i]),
                container_relief=[None] * len(fleet_member_sets[i]),
                container_style=[None] * len(fleet_member_sets[i]),
                container_takefocus=[None] * len(fleet_member_sets[i]),
                container_width=[None] * len(fleet_member_sets[i]),
                
                container_grid_cnf=[None] * len(fleet_member_sets[i]),
                container_grid_column=[1+i] * len(fleet_member_sets[i]),
                container_grid_columnspan=[None] * len(fleet_member_sets[i]),
                container_grid_row=container_row_objects,
                container_grid_rowspawn=[None] * len(fleet_member_sets[i]),
                container_grid_ipadx=[None] * len(fleet_member_sets[i]),
                container_grid_ipady=[None] * len(fleet_member_sets[i]),
                container_grid_padx=[None] * len(fleet_member_sets[i]),
                container_grid_pady=[5] * len(fleet_member_sets[i]),
                container_grid_sticky=[None] * len(fleet_member_sets[i]),
                container_grid_in_=[None] * len(fleet_member_sets[i]),

                button_class_=[None] * len(fleet_member_sets[i]),
                button_command=button_commands,
                button_compound=[None] * len(fleet_member_sets[i]),
                button_cursor=[None] * len(fleet_member_sets[i]),
                button_default=[None] * len(fleet_member_sets[i]),
                button_image=[None] * len(fleet_member_sets[i]),
                button_name=button_name_objects,
                button_padding=[None] * len(fleet_member_sets[i]),
                button_state=[None] * len(fleet_member_sets[i]),
                button_style=[None] * len(fleet_member_sets[i]),
                button_takefocus=[None] * len(fleet_member_sets[i]),
                button_text=button_text_objects,
                button_textvariable=[None] * len(fleet_member_sets[i]),
                button_underline=[None] * len(fleet_member_sets[i]),
                button_width=[15] * len(fleet_member_sets[i]),
                button_bootstyle=[PRIMARY] * len(fleet_member_sets[i]),
                
                button_grid_cnf=[None] * len(fleet_member_sets[i]),
                button_grid_column=[1] * len(fleet_member_sets[i]),
                button_grid_columnspan=[None] * len(fleet_member_sets[i]),
                button_grid_row=[1] * len(fleet_member_sets[i]),
                button_grid_rowspawn=[None] * len(fleet_member_sets[i]),
                button_grid_ipadx=[None] * len(fleet_member_sets[i]),
                button_grid_ipady=[None] * len(fleet_member_sets[i]), 
                button_grid_padx=[None] * len(fleet_member_sets[i]),
                button_grid_pady=[5] * len(fleet_member_sets[i]),
                button_grid_sticky=[None] * len(fleet_member_sets[i]),
                button_grid_in_=[None] * len(fleet_member_sets[i]),

                progressbar_class_=[None] * len(fleet_member_sets[i]),
                progressbar_cursor=[None] * len(fleet_member_sets[i]),
                progressbar_length=[100] * len(fleet_member_sets[i]),
                progressbar_maximum=[100] * len(fleet_member_sets[i]),
                progressbar_mode =[None] * len(fleet_member_sets[i]),
                progressbar_name=progressbar_name_objects,
                progressbar_orient=[HORIZONTAL] * len(fleet_member_sets[i]),
                progressbar_phase=[None] * len(fleet_member_sets[i]),
                progressbar_style=[None] * len(fleet_member_sets[i]),
                progressbar_takefocus=[None] * len(fleet_member_sets[i]),
                progressbar_value=[0] * len(fleet_member_sets[i]),
                progressbar_variable=[None] * len(fleet_member_sets[i]),
                progressbar_bootstyle=['danger-striped'] * len(fleet_member_sets[i]),
                
                progressbar_grid_cnf=[None] * len(fleet_member_sets[i]),
                progressbar_grid_column=[1] * len(fleet_member_sets[i]),
                progressbar_grid_columnspan=[None] * len(fleet_member_sets[i]),
                progressbar_grid_row=[2] * len(fleet_member_sets[i]),
                progressbar_grid_rowspawn=[None] * len(fleet_member_sets[i]),
                progressbar_grid_ipadx=[None] * len(fleet_member_sets[i]),
                progressbar_grid_ipady=[None] * len(fleet_member_sets[i]),
                progressbar_grid_padx=[None] * len(fleet_member_sets[i]),
                progressbar_grid_pady=[5] * len(fleet_member_sets[i]),
                progressbar_grid_sticky=[None] * len(fleet_member_sets[i]),
                progressbar_grid_in_=[None] * len(fleet_member_sets[i]))

                container_name_objects =[]
                container_row_objects =[]
                button_name_objects =[]
                button_text_objects =[]
                progressbar_name_objects =[]

                containers.append(self.individual_equipment_buff_set_containers)
                buttons.append(self.individual_equipment_buff_set_button_objects)
                progressbars.append(self.individual_equipment_buff_set_progressbar_objects)

        return  (containers,buttons,progressbars)
    

    def activate_set(self, character_sub_container, button_progressbar_container):

        character_sub_container.winfo_children()[button_progressbar_container].winfo_children()[0].config(bootstyle = INFO)
        character_sub_container.winfo_children()[button_progressbar_container].winfo_children()[1].config(bootstyle = 'success-striped', value = 100)
    

    def activate_buff(self, test, button_container, progressbar_container):

        button_container[test - 1].config(bootstyle = INFO)
        progressbar_container[test - 1].config(bootstyle = 'success-striped', value = 100)

        
    

    # def create_new_saved_set_individual_buffs(self, fleet_member_sets, sub_containers):
        
    #     fleet_member_sets=[['char1_set1'],
    #                        ['char2_set1','char2_set2'],
    #                        ['char3_set1','char3_set2','char3_set3'],
    #                        ['char4_set1'],
    #                        ['char5_set1','char5_set2','char5_set3','char5_set4','char5_set5'],
    #                        ['char6_set1','char6_set2','char6_set3','char6_set4','char6_set5','char6_set6']]
        
    #     containers = []
    #     buttons = []
    #     progressbars = []
    #     container_name_objects =[]
    #     container_row_objects =[]
    #     button_name_objects =[]
    #     button_text_objects =[]
    #     progressbar_name_objects =[]

    #     for i in range(len(fleet_member_sets)):

    #         if fleet_member_sets[i] != None:

    #             for j in range(len(fleet_member_sets[i])):
    #                 container_name_objects.append(f'{fleet_member_sets[i][j]}_container')
    #                 button_name_objects.append(f'{fleet_member_sets[i][j]}_button')
    #                 button_text_objects.append(f'{fleet_member_sets[i][j]}')
    #                 progressbar_name_objects.append(f'{fleet_member_sets[i][j]}_progressbar')

    #             for k in range(len(fleet_member_sets[i])):
    #                 container_row_objects.append(k+2)
            
    #             (self.individual_equipment_buff_set_containers,
    #             self.individual_equipment_buff_set_button_objects,
    #             self.individual_equipment_buff_set_progressbar_objects) = formwidgets.FormWidgets.create_button_progressbar_grid(self,
                
    #             master_container = sub_containers[i],
    #             grid_count = len(fleet_member_sets[i]),

    #             container_border=[None] *len(fleet_member_sets[i]),
    #             container_borderwidth=[None] * len(fleet_member_sets[i]),
    #             container_class=[None] * len(fleet_member_sets[i]),
    #             container_cursor=[None] * len(fleet_member_sets[i]),
    #             container_height=[None] * len(fleet_member_sets[i]),
    #             container_name=container_name_objects,
    #             container_padding=[None] * len(fleet_member_sets[i]),
    #             container_relief=[None] * len(fleet_member_sets[i]),
    #             container_style=[None] * len(fleet_member_sets[i]),
    #             container_takefocus=[None] * len(fleet_member_sets[i]),
    #             container_width=[None] * len(fleet_member_sets[i]),
                
    #             container_grid_cnf=[None] * len(fleet_member_sets[i]),
    #             container_grid_column=[1+i] * len(fleet_member_sets[i]),
    #             container_grid_columnspan=[None] * len(fleet_member_sets[i]),
    #             container_grid_row=container_row_objects,
    #             container_grid_rowspawn=[None] * len(fleet_member_sets[i]),
    #             container_grid_ipadx=[None] * len(fleet_member_sets[i]),
    #             container_grid_ipady=[None] * len(fleet_member_sets[i]),
    #             container_grid_padx=[None] * len(fleet_member_sets[i]),
    #             container_grid_pady=[5] * len(fleet_member_sets[i]),
    #             container_grid_sticky=[None] * len(fleet_member_sets[i]),
    #             container_grid_in_=[None] * len(fleet_member_sets[i]),

    #             button_class_=[None] * len(fleet_member_sets[i]),
    #             button_command=[lambda : self.activate_set(sub_containers[i])] * len(fleet_member_sets[i]),
    #             button_compound=[None] * len(fleet_member_sets[i]),
    #             button_cursor=[None] * len(fleet_member_sets[i]),
    #             button_default=[None] * len(fleet_member_sets[i]),
    #             button_image=[None] * len(fleet_member_sets[i]),
    #             button_name=button_name_objects,
    #             button_padding=[None] * len(fleet_member_sets[i]),
    #             button_state=[None] * len(fleet_member_sets[i]),
    #             button_style=[None] * len(fleet_member_sets[i]),
    #             button_takefocus=[None] * len(fleet_member_sets[i]),
    #             button_text=button_text_objects,
    #             button_textvariable=[None] * len(fleet_member_sets[i]),
    #             button_underline=[None] * len(fleet_member_sets[i]),
    #             button_width=[15] * len(fleet_member_sets[i]),
    #             button_bootstyle=[PRIMARY] * len(fleet_member_sets[i]),
                
    #             button_grid_cnf=[None] * len(fleet_member_sets[i]),
    #             button_grid_column=[1] * len(fleet_member_sets[i]),
    #             button_grid_columnspan=[None] * len(fleet_member_sets[i]),
    #             button_grid_row=[1] * len(fleet_member_sets[i]),
    #             button_grid_rowspawn=[None] * len(fleet_member_sets[i]),
    #             button_grid_ipadx=[None] * len(fleet_member_sets[i]),
    #             button_grid_ipady=[None] * len(fleet_member_sets[i]), 
    #             button_grid_padx=[None] * len(fleet_member_sets[i]),
    #             button_grid_pady=[5] * len(fleet_member_sets[i]),
    #             button_grid_sticky=[None] * len(fleet_member_sets[i]),
    #             button_grid_in_=[None] * len(fleet_member_sets[i]),

    #             progressbar_class_=[None] * len(fleet_member_sets[i]),
    #             progressbar_cursor=[None] * len(fleet_member_sets[i]),
    #             progressbar_length=[100] * len(fleet_member_sets[i]),
    #             progressbar_maximum=[100] * len(fleet_member_sets[i]),
    #             progressbar_mode =[None] * len(fleet_member_sets[i]),
    #             progressbar_name=progressbar_name_objects,
    #             progressbar_orient=[HORIZONTAL] * len(fleet_member_sets[i]),
    #             progressbar_phase=[None] * len(fleet_member_sets[i]),
    #             progressbar_style=[None] * len(fleet_member_sets[i]),
    #             progressbar_takefocus=[None] * len(fleet_member_sets[i]),
    #             progressbar_value=[5] * len(fleet_member_sets[i]),
    #             progressbar_variable=[None] * len(fleet_member_sets[i]),
    #             progressbar_bootstyle=[DANGER] * len(fleet_member_sets[i]),
                
    #             progressbar_grid_cnf=[None] * len(fleet_member_sets[i]),
    #             progressbar_grid_column=[1] * len(fleet_member_sets[i]),
    #             progressbar_grid_columnspan=[None] * len(fleet_member_sets[i]),
    #             progressbar_grid_row=[2] * len(fleet_member_sets[i]),
    #             progressbar_grid_rowspawn=[None] * len(fleet_member_sets[i]),
    #             progressbar_grid_ipadx=[None] * len(fleet_member_sets[i]),
    #             progressbar_grid_ipady=[None] * len(fleet_member_sets[i]),
    #             progressbar_grid_padx=[None] * len(fleet_member_sets[i]),
    #             progressbar_grid_pady=[5] * len(fleet_member_sets[i]),
    #             progressbar_grid_sticky=[None] * len(fleet_member_sets[i]),
    #             progressbar_grid_in_=[None] * len(fleet_member_sets[i]))

    #             container_name_objects =[]
    #             container_row_objects =[]
    #             button_name_objects =[]
    #             button_text_objects =[]
    #             progressbar_name_objects =[]

    #             containers.append(self.individual_equipment_buff_set_containers)
    #             buttons.append(self.individual_equipment_buff_set_button_objects)
    #             progressbars.append(self.individual_equipment_buff_set_progressbar_objects)

    #     return  (containers,buttons,progressbars)

            
    