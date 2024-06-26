import formwidgets
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from ttkbootstrap.validation import *
import validation as Validate

class CreateCharacterTab(ttkb.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.data = []
        self.data2 = []
        self.character_name = ttkb.StringVar(value = '')
        self.update_character_name = ttkb.StringVar(value = '')
        self.character_password = ttkb.StringVar(value = '')
        self.update_character_password = ttkb.StringVar(value = '')
        self.pw_checkbutton_variable = ttkb.IntVar(value = 0)
        self.update_pw_checkbutton_variable = ttkb.IntVar(value = 0)
        self.character_class = ttkb.StringVar( value = '')
        self.update_character_class = ttkb.StringVar( value = '')
        self.character_level = ttkb.IntVar(value = 0)
        self.update_character_level = ttkb.IntVar(value = 0)
        self.character_weapon_slots = ttkb.IntVar(value = '')
        self.update_character_weapon_slots = ttkb.IntVar(value = '')
        self.character_device_slots = ttkb.IntVar(value = '')
        self.update_character_device_slots = ttkb.IntVar(value = '')
        self.character_fleet_position = ttkb.IntVar(value = '')
        self.update_character_fleet_position = ttkb.IntVar(value = '')
        self.character_class_selection = ['JD', 'JE', 'JS', 'PP', 'PS', 'PW', 'TE', 'TS', 'TT']
        self.character_fleet_position_values = [1, 2, 3, 4, 5, 6]
        self.add_character_table_columns = [
        {'text': 'Character Name', 'stretch': True},
        {'text': 'Character Password', 'stretch': True},
        {'text': 'Character Class', 'stretch': True},
        {'text': 'Character Level', 'stretch': True},
        {'text': 'Character Weapon Slots', 'stretch': True},
        {'text': 'Character Device Slots', 'stretch': True},
        {'text': 'Character Fleet Position', 'stretch': True}]
        self.current_class = ttkb.StringVar(value = '')
        self.update_current_class = ttkb.StringVar(value = '')

        npw_entry_field_count=2

        (self.npw_entry_field_container,
        self.npw_entry_field_label_objects,
        self.npw_entry_field_entry_objects,
        self.npw_entry_field_error_label_objects)=formwidgets.FormWidgets.create_label_entry_label_grid(self,
        
        grid_objects=npw_entry_field_count,
        master_container=None,
        recreate=False,

        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='npw_entry_field_container',
        container_padding=None,
        container_relief=None,
        container_style=None,
        container_takefocus=None,
        container_width=None,

        container_pack_cnf=None,
        container_pack_after=None,
        container_pack_anchor=None,
        container_pack_before=None,
        container_pack_expand=None,
        container_pack_fill=None,
        container_pack_side=None,
        container_pack_ipadx=None,
        container_pack_ipady=None,
        container_pack_padx=None,
        container_pack_pady=None,
        container_pack_in_=None,

        label1_anchor=[None]*npw_entry_field_count,
        label1_background=[None]*npw_entry_field_count,
        label1_border=[None]*npw_entry_field_count,
        label1_borderwidth=[None]*npw_entry_field_count,
        label1_class_=[None]*npw_entry_field_count,
        label1_compound=[None]*npw_entry_field_count,
        label1_cursor=[None]*npw_entry_field_count,
        label1_font=[None]*npw_entry_field_count,
        label1_foreground=[None]*npw_entry_field_count,
        label1_image=[None]*npw_entry_field_count,
        label1_justify=[None]*npw_entry_field_count,
        label1_name=['npw_entry_field_name_label','npw_entry_field_password_label'],
        label1_padding=[None]*npw_entry_field_count,
        label1_relief=[None]*npw_entry_field_count,
        label1_state=[None]*npw_entry_field_count,
        label1_style=[None]*npw_entry_field_count,
        label1_takefocus=[None]*npw_entry_field_count,
        label1_text=['Character Name:','Character Password'],
        label1_textvariable=[None]*npw_entry_field_count,
        label1_underline=[None]*npw_entry_field_count,
        label1_width=[23]*npw_entry_field_count,
        label1_wraplength=[None]*npw_entry_field_count,

        label1_grid_cnf=[None]*npw_entry_field_count,
        label1_grid_column=[1,1],
        label1_grid_columnspan=[None]*npw_entry_field_count,
        label1_grid_row=[1,2],
        label1_grid_rowspawn=[None]*npw_entry_field_count,
        label1_grid_ipadx=[None]*npw_entry_field_count,
        label1_grid_ipady=[5]*npw_entry_field_count,
        label1_grid_padx=[(360,0)]*npw_entry_field_count,
        label1_grid_pady=[None]*npw_entry_field_count,
        label1_grid_sticky=[None]*npw_entry_field_count,
        label1_grid_in_=[None]*npw_entry_field_count,

        entry_background=[None]*npw_entry_field_count,
        entry_class_=[None]*npw_entry_field_count,
        entry_cursor=[None]*npw_entry_field_count,
        entry_exportselection=[None]*npw_entry_field_count,
        entry_font=[None]*npw_entry_field_count,
        entry_foreground=[None]*npw_entry_field_count,
        entry_invalidcommand=[None]*npw_entry_field_count,
        entry_justify=[None]*npw_entry_field_count,
        entry_name=['npw_entry_field_name_entry', 'npw_entry_field_password_entry'],
        entry_show=[None,'*'],
        entry_state=[None]*npw_entry_field_count,
        entry_style=[None]*npw_entry_field_count,
        entry_takefocus=[None]*npw_entry_field_count,
        entry_textvariable=[self.character_name, self.character_password],
        entry_validate=[None]*npw_entry_field_count,
        entry_validatecommand=[None]*npw_entry_field_count,
        entry_width=[20]*npw_entry_field_count,
        entry_xscrollcommand=[None]*npw_entry_field_count,

        entry_grid_cnf=[None]*npw_entry_field_count,
        entry_grid_column=[2,2],
        entry_grid_columnspan=[None]*npw_entry_field_count,
        entry_grid_row=[1,2],
        entry_grid_rowspawn=[None]*npw_entry_field_count,
        entry_grid_ipadx=[None]*npw_entry_field_count,
        entry_grid_ipady=[None]*npw_entry_field_count,
        entry_grid_padx=[None]*npw_entry_field_count,
        entry_grid_pady=[5]*npw_entry_field_count,
        entry_grid_sticky=[None]*npw_entry_field_count,
        entry_grid_in_=[None]*npw_entry_field_count,

        label2_anchor=[None]*npw_entry_field_count,
        label2_background=[None]*npw_entry_field_count,
        label2_border=[None]*npw_entry_field_count,
        label2_borderwidth=[None]*npw_entry_field_count,
        label2_class_=[None]*npw_entry_field_count,
        label2_compound=[None]*npw_entry_field_count,
        label2_cursor=[None]*npw_entry_field_count,
        label2_font=[None]*npw_entry_field_count,
        label2_foreground=[None]*npw_entry_field_count,
        label2_image=[None]*npw_entry_field_count,
        label2_justify=[None]*npw_entry_field_count,
        label2_name=['npw_entry_field_name_error_label', 'npw_entry_field_password_error_label'],
        label2_padding=[None]*npw_entry_field_count,
        label2_relief=[None]*npw_entry_field_count,
        label2_state=[None]*npw_entry_field_count,
        label2_style=[None]*npw_entry_field_count,
        label2_takefocus=[None]*npw_entry_field_count,
        label2_text=['']*npw_entry_field_count,
        label2_textvariable=[None]*npw_entry_field_count,
        label2_underline=[None]*npw_entry_field_count,
        label2_width=[60]*npw_entry_field_count,
        label2_wraplength=[None]*npw_entry_field_count,

        label2_grid_cnf=[None]*npw_entry_field_count,
        label2_grid_column=[3,3],
        label2_grid_columnspan=[None]*npw_entry_field_count,
        label2_grid_row=[1,2],
        label2_grid_rowspawn=[None]*npw_entry_field_count,
        label2_grid_ipadx=[None]*npw_entry_field_count,
        label2_grid_ipady=[None]*npw_entry_field_count,
        label2_grid_padx=[5]*npw_entry_field_count,
        label2_grid_pady=[None]*npw_entry_field_count,
        label2_grid_sticky=[None]*npw_entry_field_count,
        label2_grid_in_=[None]*npw_entry_field_count)

        (self.show_pw_checkbutton_container,
        self.show_pw_checkbutton_objects)=formwidgets.FormWidgets.create_checkbutton_grid(self,
        
        grid_objects=1,
        master_container=None,
        recreate=False,

        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='show_pw_checkbutton_container',
        container_padding=None,
        container_relief=None,
        container_style=None,
        container_takefocus=None,
        container_width=None,

        container_pack_cnf=None,
        container_pack_after= None,
        container_pack_anchor=None,
        container_pack_before=None,
        container_pack_expand=None,
        container_pack_fill=None,
        container_pack_side=None,
        container_pack_ipadx=None,
        container_pack_ipady=None,
        container_pack_padx=None,
        container_pack_pady=None,
        container_pack_in_=None,
        
        checkbutton_class_=[None],
        checkbutton_command=[lambda:self.show_password(self.npw_entry_field_entry_objects[1],self.pw_checkbutton_variable)],
        checkbutton_compound=[None],
        checkbutton_cursor=[None],
        checkbutton_image=[None],
        checkbutton_name=['show_pw_checkbutton'],
        checkbutton_offvalue=[0],
        checkbutton_onvalue=[1],
        checkbutton_padding=[None],
        checkbutton_state=[None],
        checkbutton_style=[None],
        checkbutton_takefocus=[None],
        checkbutton_text=['Show Password'],
        checkbutton_textvariable=[None],
        checkbutton_underline=[None],
        checkbutton_variable=[self.pw_checkbutton_variable],
        checkbutton_width=[None],
        checkbutton_bootstyle=['success-round-toggle'],
        
        checkbutton_grid_cnf=[None],
        checkbutton_grid_column=[1],
        checkbutton_grid_columnspan=[None],
        checkbutton_grid_row=[1],
        checkbutton_grid_rowspawn=[None],
        checkbutton_grid_ipadx=[None],
        checkbutton_grid_ipady=[None],
        checkbutton_grid_padx=[(131, 0)],
        checkbutton_grid_pady=[None],
        checkbutton_grid_sticky=[None],
        checkbutton_grid_in_=[None])

        (self.lvl_entry_field_container,
        self.lvl_entry_field_label_objects,
        self.lvl_entry_field_entry_objects,
        self.lvl_entry_field_error_label_objects)=formwidgets.FormWidgets.create_label_entry_label_grid(self,
        
        grid_objects=1,
        master_container=None,
        recreate=False,

        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='lvl_entry_field_container',
        container_padding=None,
        container_relief=None,
        container_style=None,
        container_takefocus=None,
        container_width=None,

        container_pack_cnf=None,
        container_pack_after=None,
        container_pack_anchor=None,
        container_pack_before=None,
        container_pack_expand=None,
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
        label1_name=['lvl_entry_field_label'],
        label1_padding=[None],
        label1_relief=[None],
        label1_state=[None],
        label1_style=[None],
        label1_takefocus=[None],
        label1_text=['Character Level:'],
        label1_textvariable=[None],
        label1_underline=[None],
        label1_width=[23],
        label1_wraplength=[None],

        label1_grid_cnf=[None],
        label1_grid_column=[1],
        label1_grid_columnspan=[None],
        label1_grid_row=[1],
        label1_grid_rowspawn=[None],
        label1_grid_ipadx=[None],
        label1_grid_ipady=[None],
        label1_grid_padx=[(360,0)],
        label1_grid_pady=[None],
        label1_grid_sticky=[None],
        label1_grid_in_=[None],

        entry_background=[None],
        entry_class_=[None],
        entry_cursor=[None],
        entry_exportselection=[None],
        entry_font=[None],
        entry_foreground=[None],
        entry_invalidcommand=[None],
        entry_justify=[None],
        entry_name=['lvl_entry_field_entry'],
        entry_show=[None],
        entry_state=[None],
        entry_style=[None],
        entry_takefocus=[None],
        entry_textvariable=[self.character_level],
        entry_validate=[None],
        entry_validatecommand=[None],
        entry_width=[20],
        entry_xscrollcommand=[None],

        entry_grid_cnf=[None],
        entry_grid_column=[2],
        entry_grid_columnspan=[None],
        entry_grid_row=[1],
        entry_grid_rowspawn=[None],
        entry_grid_ipadx=[None],
        entry_grid_ipady=[None],
        entry_grid_padx=[None],
        entry_grid_pady=[5],
        entry_grid_sticky=[None],
        entry_grid_in_=[None],

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
        label2_name=['lvl_entry_field_error_label'],
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
        label2_grid_pady=[None],
        label2_grid_sticky=[None],
        label2_grid_in_=[None])

        cwdp_count=4

        (self.cwdp_entry_field_container,
        self.cwdp_entry_field_label_objects,
        self.cwdp_entry_field_combobox_objects,
        self.cwdp_entry_field_error_label_objects)=formwidgets.FormWidgets.create_label_combobox_label_grid(self,
        
        grid_objects=cwdp_count,
        master_container=None,
        recreate=False,

        bind_combobox_action=[False]*cwdp_count,
        combobox_action=[None]*cwdp_count,
        combobox_command=[None]*cwdp_count,

        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='cwdp_entry_field_container',
        container_padding=None,
        container_relief=None,
        container_style=None,
        container_takefocus=None,
        container_width=None,

        container_pack_cnf=None,
        container_pack_after=None,
        container_pack_anchor=None,
        container_pack_before=None,
        container_pack_expand=None,
        container_pack_fill=None,
        container_pack_side=None,
        container_pack_ipadx=None,
        container_pack_ipady=None,
        container_pack_padx=None,
        container_pack_pady=None,
        container_pack_in_=None,

        label1_anchor=[None]*cwdp_count,
        label1_background=[None]*cwdp_count,
        label1_border=[None]*cwdp_count,
        label1_borderwidth=[None]*cwdp_count,
        label1_class_=[None]*cwdp_count,
        label1_compound=[None]*cwdp_count,
        label1_cursor=[None]*cwdp_count,
        label1_font=[None]*cwdp_count,
        label1_foreground=[None]*cwdp_count,
        label1_image=[None]*cwdp_count,
        label1_justify=[None]*cwdp_count,
        label1_name=['class_entry_field_label','weapon_entry_field_label','device_entry_field_label','position_entry_field_label'],
        label1_padding=[None]*cwdp_count,
        label1_relief=[None]*cwdp_count,
        label1_state=[None]*cwdp_count,
        label1_style=[None]*cwdp_count,
        label1_takefocus=[None]*cwdp_count,
        label1_text=['Character Class:','Character Weapons Slots:','Character Device Slots:','Character Fleet Position:'],
        label1_textvariable=[None]*cwdp_count,
        label1_underline=[None]*cwdp_count,
        label1_width=[23]*cwdp_count,
        label1_wraplength=[None]*cwdp_count,

        label1_grid_cnf=[None]*cwdp_count,
        label1_grid_column=[1,1,1,1],
        label1_grid_columnspan=[None]*cwdp_count,
        label1_grid_row=[1,2,3,4],
        label1_grid_rowspawn=[None]*cwdp_count,
        label1_grid_ipadx=[None]*cwdp_count,
        label1_grid_ipady=[None]*cwdp_count,
        label1_grid_padx=[(360,0)]*cwdp_count,
        label1_grid_pady=[None]*cwdp_count,
        label1_grid_sticky=[None]*cwdp_count,
        label1_grid_in_=[None]*cwdp_count,

        combobox_background=[None]*cwdp_count,
        combobox_class_=[None]*cwdp_count,
        combobox_cursor=[None]*cwdp_count,
        combobox_exportselection=[None]*cwdp_count,
        combobox_font=[None]*cwdp_count,
        combobox_foreground=[None]*cwdp_count,
        combobox_height=[None]*cwdp_count,
        combobox_invalidcommand=[None]*cwdp_count,
        combobox_justify=[None]*cwdp_count,
        combobox_name=['class_entry_field_combobox','weapon_entry_field_combobox','device_entry_field_combobox','position_entry_field_combobox'],
        combobox_postcommand=[None]*cwdp_count,
        combobox_show=[None]*cwdp_count,
        combobox_state=[READONLY, DISABLED, DISABLED, READONLY],
        combobox_style=[None]*cwdp_count,
        combobox_takefocus=[None]*cwdp_count,
        combobox_textvariable=[self.character_class,self.character_weapon_slots,self.character_device_slots,self.character_fleet_position],
        combobox_validate=[None]*cwdp_count,
        combobox_validatecommand=[None]*cwdp_count,
        combobox_values=[self.character_class_selection,None,None,self.character_fleet_position_values],
        combobox_width=[18]*cwdp_count,
        combobox_xscrollcommand=[None]*cwdp_count,
        
        combobox_grid_cnf=[None]*cwdp_count,
        combobox_grid_column=[2,2,2,2],
        combobox_grid_columnspan=[None]*cwdp_count,
        combobox_grid_row=[1,2,3,4],
        combobox_grid_rowspawn=[None]*cwdp_count,
        combobox_grid_ipadx=[None]*cwdp_count,
        combobox_grid_ipady=[None]*cwdp_count,
        combobox_grid_padx=[None]*cwdp_count,
        combobox_grid_pady=[5]*cwdp_count,
        combobox_grid_sticky=[None]*cwdp_count,
        combobox_grid_in_=[None]*cwdp_count,
        
        label2_anchor=[None]*cwdp_count,
        label2_background=[None]*cwdp_count,
        label2_border=[None]*cwdp_count,
        label2_borderwidth=[None]*cwdp_count,
        label2_class_=[None]*cwdp_count,
        label2_compound=[None]*cwdp_count,
        label2_cursor=[None]*cwdp_count,
        label2_font=[None]*cwdp_count,
        label2_foreground=[None]*cwdp_count,
        label2_image=[None]*cwdp_count,
        label2_justify=[None]*cwdp_count,
        label2_name=['class_entry_field_error_label','weapon_entry_field_error_label','device_entry_field_error_label','position_entry_field_error_label'],
        label2_padding=[None]*cwdp_count,
        label2_relief=[None]*cwdp_count,
        label2_state=[None]*cwdp_count,
        label2_style=[None]*cwdp_count,
        label2_takefocus=[None]*cwdp_count,
        label2_text=['']*cwdp_count,
        label2_textvariable=[None]*cwdp_count,
        label2_underline=[None]*cwdp_count,
        label2_width=[60]*cwdp_count,
        label2_wraplength=[None]*cwdp_count,

        label2_grid_cnf=[None]*cwdp_count,
        label2_grid_column=[3,3,3,3],
        label2_grid_columnspan=[None]*cwdp_count,
        label2_grid_row=[1,2,3,4],
        label2_grid_rowspawn=[None]*cwdp_count,
        label2_grid_ipadx=[None]*cwdp_count,
        label2_grid_ipady=[None]*cwdp_count,
        label2_grid_padx=[5]*cwdp_count,
        label2_grid_pady=[None]*cwdp_count,
        label2_grid_sticky=[None]*cwdp_count,
        label2_grid_in_=[None]*cwdp_count)

        add_clear_button_count = 2

        (self.add_clear_button_container,
        self.add_clear_button_objects)=formwidgets.FormWidgets.create_button_grid(self,
        
        grid_objects=add_clear_button_count,
        master_container=None,
        recreate=False,

        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='add_clear_button_container',
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

        button_class_=[None]*add_clear_button_count,
        button_command=[self.submit_character_entry_fields,self.clear_character_entry_fields],
        button_compound=[None]*add_clear_button_count,
        button_cursor=[None]*add_clear_button_count,
        button_default=[None]*add_clear_button_count,
        button_image=[None]*add_clear_button_count,
        button_name=['add_character_button','clear_character_button'],
        button_padding=[None]*add_clear_button_count,
        button_state=[None]*add_clear_button_count,
        button_style=[None]*add_clear_button_count,
        button_takefocus=[None]*add_clear_button_count,
        button_text=['Add Character','Clear'],
        button_textvariable=[None]*add_clear_button_count,
        button_underline=[None]*add_clear_button_count,
        button_width=[15]*add_clear_button_count,
        button_bootstyle=[SUCCESS,PRIMARY],

        button_grid_cnf=[None]*add_clear_button_count,
        button_grid_column=[1,2],
        button_grid_columnspan=[None]*add_clear_button_count,
        button_grid_row=[1,1],
        button_grid_rowspawn=[None]*add_clear_button_count,
        button_grid_ipadx=[None]*add_clear_button_count,
        button_grid_ipady=[None]*add_clear_button_count,
        button_grid_padx=[5]*add_clear_button_count,
        button_grid_pady=[5]*add_clear_button_count,
        button_grid_sticky=[None]*add_clear_button_count,
        button_grid_in_=[None]*add_clear_button_count)

        (self.character_table_container,
        self.character_table_objects) = formwidgets.FormWidgets.create_table_grid(self,
                                                                                  
        grid_objects=1,
        master_container=None,
        recreate=False,
        
        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='character_table_container',
        container_padding=None,
        container_relief=None,
        container_style=None,
        container_takefocus=None,
        container_width=None,
        
        container_pack_cnf=None,
        container_pack_after=None,
        container_pack_anchor=None,
        container_pack_before=None,
        container_pack_expand=None,
        container_pack_fill= None,
        container_pack_side=None,
        container_pack_ipadx=None,
        container_pack_ipady=5,
        container_pack_padx=None,
        container_pack_pady=None,
        container_pack_in_=None,

        table_bootstyle=[PRIMARY],
        table_coldata=[self.add_character_table_columns],
        table_rowdata=[self.data],
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

        (self.select_character_button_container,
        self.select_character_button_objects)=formwidgets.FormWidgets.create_button_grid(self,
        grid_objects=1,
        master_container=None,
        recreate=False,

        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='select_character_button_container',
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
        button_command=[lambda: self.get_selected_row(self.character_table_objects[0])],
        button_compound=[None],
        button_cursor=[None],
        button_default=[None],
        button_image=[None],
        button_name=['select_character_button'],
        button_padding=[None],
        button_state=[None],
        button_style=[None],
        button_takefocus=[None],
        button_text=['Select Character'],
        button_textvariable=[None],
        button_underline=[None],
        button_width=[15],
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

        update_npw_entry_field_count = 2

        (self.update_npw_entry_field_container,
        self._update_npw_entry_field_label_objects,
        self.update_npw_entry_field_entry_objects,
        self.update_npw_entry_field_error_label_objects)=formwidgets.FormWidgets.create_label_entry_label_grid(self,
        
        grid_objects=update_npw_entry_field_count,
        master_container=None,
        recreate=False,

        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='update_npw_entry_field_container',
        container_padding=None,
        container_relief=None,
        container_style=None,
        container_takefocus=None,
        container_width=None,

        container_pack_cnf=None,
        container_pack_after=None,
        container_pack_anchor=None,
        container_pack_before=None,
        container_pack_expand=None,
        container_pack_fill=None,
        container_pack_side=None,
        container_pack_ipadx=None,
        container_pack_ipady=None,
        container_pack_padx=None,
        container_pack_pady=None,
        container_pack_in_=None,

        label1_anchor=[None]*update_npw_entry_field_count,
        label1_background=[None]*update_npw_entry_field_count,
        label1_border=[None]*update_npw_entry_field_count,
        label1_borderwidth=[None]*update_npw_entry_field_count,
        label1_class_=[None]*update_npw_entry_field_count,
        label1_compound=[None]*update_npw_entry_field_count,
        label1_cursor=[None]*update_npw_entry_field_count,
        label1_font=[None]*update_npw_entry_field_count,
        label1_foreground=[None]*update_npw_entry_field_count,
        label1_image=[None]*update_npw_entry_field_count,
        label1_justify=[None]*update_npw_entry_field_count,
        label1_name=['update_npw_entry_field_name_label', 'update_npw_entry_field_password_label'],
        label1_padding=[None]*update_npw_entry_field_count,
        label1_relief=[None]*update_npw_entry_field_count,
        label1_state=[None]*update_npw_entry_field_count,
        label1_style=[None]*update_npw_entry_field_count,
        label1_takefocus=[None]*update_npw_entry_field_count,
        label1_text=['Update Character Name:', 'Update Character Password'],
        label1_textvariable=[None]*update_npw_entry_field_count,
        label1_underline=[None]*update_npw_entry_field_count,
        label1_width=[30]*update_npw_entry_field_count,
        label1_wraplength=[None]*update_npw_entry_field_count,

        label1_grid_cnf=[None]*update_npw_entry_field_count,
        label1_grid_column=[1,1],
        label1_grid_columnspan=[None]*update_npw_entry_field_count,
        label1_grid_row=[1,2],
        label1_grid_rowspawn=[None]*update_npw_entry_field_count,
        label1_grid_ipadx=[None]*update_npw_entry_field_count,
        label1_grid_ipady=[5]*update_npw_entry_field_count,
        label1_grid_padx=[(360,0)]*update_npw_entry_field_count,
        label1_grid_pady=[None]*update_npw_entry_field_count,
        label1_grid_sticky=[None]*update_npw_entry_field_count,
        label1_grid_in_=[None]*update_npw_entry_field_count,

        entry_background=[None]*update_npw_entry_field_count,
        entry_class_=[None]*update_npw_entry_field_count,
        entry_cursor=[None]*update_npw_entry_field_count,
        entry_exportselection=[None]*update_npw_entry_field_count,
        entry_font=[None]*update_npw_entry_field_count,
        entry_foreground=[None]*update_npw_entry_field_count,
        entry_invalidcommand=[None]*update_npw_entry_field_count,
        entry_justify=[None]*update_npw_entry_field_count,
        entry_name=['update_npw_entry_field_name_entry', 'update_npw_entry_field_password_entry'],
        entry_show=[None,'*'],
        entry_state=[None]*update_npw_entry_field_count,
        entry_style=[None]*npw_entry_field_count,
        entry_takefocus=[None]*update_npw_entry_field_count,
        entry_textvariable=[self.update_character_name, self.update_character_password],
        entry_validate=[None]*update_npw_entry_field_count,
        entry_validatecommand=[None]*update_npw_entry_field_count,
        entry_width=[20]*update_npw_entry_field_count,
        entry_xscrollcommand=[None]*update_npw_entry_field_count,

        entry_grid_cnf=[None]*update_npw_entry_field_count,
        entry_grid_column=[2,2],
        entry_grid_columnspan=[None]*update_npw_entry_field_count,
        entry_grid_row=[1,2],
        entry_grid_rowspawn=[None]*update_npw_entry_field_count,
        entry_grid_ipadx=[None]*update_npw_entry_field_count,
        entry_grid_ipady=[None]*update_npw_entry_field_count,
        entry_grid_padx=[None]*update_npw_entry_field_count,
        entry_grid_pady=[5]*update_npw_entry_field_count,
        entry_grid_sticky=[None]*update_npw_entry_field_count,
        entry_grid_in_=[None]*update_npw_entry_field_count,

        label2_anchor=[None]*update_npw_entry_field_count,
        label2_background=[None]*update_npw_entry_field_count,
        label2_border=[None]*update_npw_entry_field_count,
        label2_borderwidth=[None]*update_npw_entry_field_count,
        label2_class_=[None]*update_npw_entry_field_count,
        label2_compound=[None]*update_npw_entry_field_count,
        label2_cursor=[None]*update_npw_entry_field_count,
        label2_font=[None]*update_npw_entry_field_count,
        label2_foreground=[None]*update_npw_entry_field_count,
        label2_image=[None]*update_npw_entry_field_count,
        label2_justify=[None]*update_npw_entry_field_count,
        label2_name=['update_npw_entry_field_name_error_label', 'update_npw_entry_field_password_error_label'],
        label2_padding=[None]*update_npw_entry_field_count,
        label2_relief=[None]*update_npw_entry_field_count,
        label2_state=[None]*update_npw_entry_field_count,
        label2_style=[None]*update_npw_entry_field_count,
        label2_takefocus=[None]*update_npw_entry_field_count,
        label2_text=['']*update_npw_entry_field_count,
        label2_textvariable=[None]*update_npw_entry_field_count,
        label2_underline=[None]*update_npw_entry_field_count,
        label2_width=[60]*update_npw_entry_field_count,
        label2_wraplength=[None]*update_npw_entry_field_count,

        label2_grid_cnf=[None]*update_npw_entry_field_count,
        label2_grid_column=[3,3],
        label2_grid_columnspan=[None]*update_npw_entry_field_count,
        label2_grid_row=[1,2],
        label2_grid_rowspawn=[None]*update_npw_entry_field_count,
        label2_grid_ipadx=[None]*update_npw_entry_field_count,
        label2_grid_ipady=[None]*update_npw_entry_field_count,
        label2_grid_padx=[5]*update_npw_entry_field_count,
        label2_grid_pady=[None]*update_npw_entry_field_count,
        label2_grid_sticky=[None]*update_npw_entry_field_count,
        label2_grid_in_=[None]*update_npw_entry_field_count)

        (self.update_show_pw_checkbutton_container,
        self.update_show_pw_checkbutton_objects)=formwidgets.FormWidgets.create_checkbutton_grid(self,
        
        grid_objects=1,
        master_container=None,
        recreate=False,

        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='update_show_pw_checkbutton_container',
        container_padding=None,
        container_relief=None,
        container_style=None,
        container_takefocus=None,
        container_width=None,

        container_pack_cnf=None,
        container_pack_after= None,
        container_pack_anchor=None,
        container_pack_before=None,
        container_pack_expand=None,
        container_pack_fill=None,
        container_pack_side=None,
        container_pack_ipadx=None,
        container_pack_ipady=None,
        container_pack_padx=None,
        container_pack_pady=None,
        container_pack_in_=None,
        
        checkbutton_class_=[None],
        checkbutton_command=[lambda:self.show_password(self.update_npw_entry_field_entry_objects[1],self.update_pw_checkbutton_variable)],
        checkbutton_compound=[None],
        checkbutton_cursor=[None],
        checkbutton_image=[None],
        checkbutton_name=['update_show_pw_checkbutton'],
        checkbutton_offvalue=[0],
        checkbutton_onvalue=[1],
        checkbutton_padding=[None],
        checkbutton_state=[None],
        checkbutton_style=[None],
        checkbutton_takefocus=[None],
        checkbutton_text=['Show Password'],
        checkbutton_textvariable=[None],
        checkbutton_underline=[None],
        checkbutton_variable=[self.update_pw_checkbutton_variable],
        checkbutton_width=[None],
        checkbutton_bootstyle=['success-round-toggle'],
        
        checkbutton_grid_cnf=[None],
        checkbutton_grid_column=[1],
        checkbutton_grid_columnspan=[None],
        checkbutton_grid_row=[1],
        checkbutton_grid_rowspawn=[None],
        checkbutton_grid_ipadx=[None],
        checkbutton_grid_ipady=[None],
        checkbutton_grid_padx=[(172, 0)],
        checkbutton_grid_pady=[None],
        checkbutton_grid_sticky=[None],
        checkbutton_grid_in_=[None])

        (self.update_lvl_entry_field_container,
        self.update_lvl_entry_field_label_objects,
        self.update_lvl_entry_field_entry_objects,
        self.update_lvl_entry_field_error_label_objects)=formwidgets.FormWidgets.create_label_entry_label_grid(self,
        
        grid_objects=1,
        master_container=None,
        recreate=False,

        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='update_lvl_entry_field_container',
        container_padding=None,
        container_relief=None,
        container_style=None,
        container_takefocus=None,
        container_width=None,

        container_pack_cnf=None,
        container_pack_after=None,
        container_pack_anchor=None,
        container_pack_before=None,
        container_pack_expand=None,
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
        label1_name=['update_lvl_entry_field_label'],
        label1_padding=[None],
        label1_relief=[None],
        label1_state=[None],
        label1_style=[None],
        label1_takefocus=[None],
        label1_text=['Update Character Level:'],
        label1_textvariable=[None],
        label1_underline=[None],
        label1_width=[30],
        label1_wraplength=[None],

        label1_grid_cnf=[None],
        label1_grid_column=[1],
        label1_grid_columnspan=[None],
        label1_grid_row=[1],
        label1_grid_rowspawn=[None],
        label1_grid_ipadx=[None],
        label1_grid_ipady=[None],
        label1_grid_padx=[(360,0)],
        label1_grid_pady=[None],
        label1_grid_sticky=[None],
        label1_grid_in_=[None],

        entry_background=[None],
        entry_class_=[None],
        entry_cursor=[None],
        entry_exportselection=[None],
        entry_font=[None],
        entry_foreground=[None],
        entry_invalidcommand=[None],
        entry_justify=[None],
        entry_name=['update_lvl_entry_field_entry'],
        entry_show=[None],
        entry_state=[None],
        entry_style=[None],
        entry_takefocus=[None],
        entry_textvariable=[self.update_character_level],
        entry_validate=[None],
        entry_validatecommand=[None],
        entry_width=[20],
        entry_xscrollcommand=[None],

        entry_grid_cnf=[None],
        entry_grid_column=[2],
        entry_grid_columnspan=[None],
        entry_grid_row=[1],
        entry_grid_rowspawn=[None],
        entry_grid_ipadx=[None],
        entry_grid_ipady=[None],
        entry_grid_padx=[None],
        entry_grid_pady=[5],
        entry_grid_sticky=[None],
        entry_grid_in_=[None],

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
        label2_name=['update_lvl_entry_field_error_label'],
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
        label2_grid_pady=[None],
        label2_grid_sticky=[None],
        label2_grid_in_=[None])

        update_cwdp_count = 4

        (self.update_cwdp_entry_field_container,
        self.update_cwdp_entry_field_label_objects,
        self.update_cwdp_entry_field_combobox_objects,
        self.update_cwdp_entry_field_error_label_objects)=formwidgets.FormWidgets.create_label_combobox_label_grid(self,
        
        grid_objects=update_cwdp_count,
        master_container=None,
        recreate=False,

        bind_combobox_action=[False]*update_cwdp_count,
        combobox_action=[None]*update_cwdp_count,
        combobox_command=[None]*update_cwdp_count,

        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='update_cwdp_entry_field_container',
        container_padding=None,
        container_relief=None,
        container_style=None,
        container_takefocus=None,
        container_width=None,

        container_pack_cnf=None,
        container_pack_after=None,
        container_pack_anchor=None,
        container_pack_before=None,
        container_pack_expand=None,
        container_pack_fill=None,
        container_pack_side=None,
        container_pack_ipadx=None,
        container_pack_ipady=None,
        container_pack_padx=None,
        container_pack_pady=None,
        container_pack_in_=None,

        label1_anchor=[None]*update_cwdp_count,
        label1_background=[None]*update_cwdp_count,
        label1_border=[None]*update_cwdp_count,
        label1_borderwidth=[None]*update_cwdp_count,
        label1_class_=[None]*update_cwdp_count,
        label1_compound=[None]*update_cwdp_count,
        label1_cursor=[None]*update_cwdp_count,
        label1_font=[None]*update_cwdp_count,
        label1_foreground=[None]*update_cwdp_count,
        label1_image=[None]*update_cwdp_count,
        label1_justify=[None]*update_cwdp_count,
        label1_name=['update_class_entry_field_label','update_weapon_entry_field_label','update_device_entry_field_label','update_position_entry_field_label'],
        label1_padding=[None]*update_cwdp_count,
        label1_relief=[None]*update_cwdp_count,
        label1_state=[None]*update_cwdp_count,
        label1_style=[None]*update_cwdp_count,
        label1_takefocus=[None]*update_cwdp_count,
        label1_text=['Update Character Class:','Update Character Weapons Slots:','Update Character Device Slots:','Update Character Fleet Position:'],
        label1_textvariable=[None]*update_cwdp_count,
        label1_underline=[None]*update_cwdp_count,
        label1_width=[30]*update_cwdp_count,
        label1_wraplength=[None]*update_cwdp_count,

        label1_grid_cnf=[None]*update_cwdp_count,
        label1_grid_column=[1,1,1,1],
        label1_grid_columnspan=[None]*update_cwdp_count,
        label1_grid_row=[1,2,3,4],
        label1_grid_rowspawn=[None]*update_cwdp_count,
        label1_grid_ipadx=[None]*update_cwdp_count,
        label1_grid_ipady=[None]*update_cwdp_count,
        label1_grid_padx=[(360,0)]*update_cwdp_count,
        label1_grid_pady=[None]*update_cwdp_count,
        label1_grid_sticky=[None]*update_cwdp_count,
        label1_grid_in_=[None]*update_cwdp_count,

        combobox_background=[None]*update_cwdp_count,
        combobox_class_=[None]*update_cwdp_count,
        combobox_cursor=[None]*update_cwdp_count,
        combobox_exportselection=[None]*update_cwdp_count,
        combobox_font=[None]*update_cwdp_count,
        combobox_foreground=[None]*update_cwdp_count,
        combobox_height=[None]*update_cwdp_count,
        combobox_invalidcommand=[None]*update_cwdp_count,
        combobox_justify=[None]*update_cwdp_count,
        combobox_name=['update_class_entry_field_combobox','update_weapon_entry_field_combobox','update_device_entry_field_combobox','update_position_entry_field_combobox'],
        combobox_postcommand=[None]*update_cwdp_count,
        combobox_show=[None]*update_cwdp_count,
        combobox_state=[READONLY, DISABLED, DISABLED, READONLY],
        combobox_style=[None]*update_cwdp_count,
        combobox_takefocus=[None]*update_cwdp_count,
        combobox_textvariable=[self.update_character_class,self.update_character_weapon_slots,self.update_character_device_slots,self.update_character_fleet_position],
        combobox_validate=[None]*update_cwdp_count,
        combobox_validatecommand=[None]*update_cwdp_count,
        combobox_values=[self.character_class_selection,None,None,self.character_fleet_position_values],
        combobox_width=[18]*update_cwdp_count,
        combobox_xscrollcommand=[None]*update_cwdp_count,
        
        combobox_grid_cnf=[None]*update_cwdp_count,
        combobox_grid_column=[2,2,2,2],
        combobox_grid_columnspan=[None]*update_cwdp_count,
        combobox_grid_row=[1,2,3,4],
        combobox_grid_rowspawn=[None]*update_cwdp_count,
        combobox_grid_ipadx=[None]*update_cwdp_count,
        combobox_grid_ipady=[None]*update_cwdp_count,
        combobox_grid_padx=[None]*update_cwdp_count,
        combobox_grid_pady=[5]*update_cwdp_count,
        combobox_grid_sticky=[None]*update_cwdp_count,
        combobox_grid_in_=[None]*update_cwdp_count,
        
        label2_anchor=[None]*update_cwdp_count,
        label2_background=[None]*update_cwdp_count,
        label2_border=[None]*update_cwdp_count,
        label2_borderwidth=[None]*update_cwdp_count,
        label2_class_=[None]*update_cwdp_count,
        label2_compound=[None]*update_cwdp_count,
        label2_cursor=[None]*update_cwdp_count,
        label2_font=[None]*update_cwdp_count,
        label2_foreground=[None]*update_cwdp_count,
        label2_image=[None]*update_cwdp_count,
        label2_justify=[None]*update_cwdp_count,
        label2_name=['update_class_entry_field_error_label','update_weapon_entry_field_error_label','update_device_entry_field_error_label','update_position_entry_field_error_label'],
        label2_padding=[None]*update_cwdp_count,
        label2_relief=[None]*update_cwdp_count,
        label2_state=[None]*update_cwdp_count,
        label2_style=[None]*update_cwdp_count,
        label2_takefocus=[None]*update_cwdp_count,
        label2_text=['']*update_cwdp_count,
        label2_textvariable=[None]*update_cwdp_count,
        label2_underline=[None]*update_cwdp_count,
        label2_width=[60]*update_cwdp_count,
        label2_wraplength=[None]*update_cwdp_count,

        label2_grid_cnf=[None]*update_cwdp_count,
        label2_grid_column=[3,3,3,3],
        label2_grid_columnspan=[None]*update_cwdp_count,
        label2_grid_row=[1,2,3,4],
        label2_grid_rowspawn=[None]*update_cwdp_count,
        label2_grid_ipadx=[None]*update_cwdp_count,
        label2_grid_ipady=[None]*update_cwdp_count,
        label2_grid_padx=[5]*update_cwdp_count,
        label2_grid_pady=[None]*update_cwdp_count,
        label2_grid_sticky=[None]*update_cwdp_count,
        label2_grid_in_=[None]*update_cwdp_count)

        udc_button_count = 3

        (self.udc_button_container,
        self.udc_button_objects)=formwidgets.FormWidgets.create_button_grid(self,
        grid_objects=udc_button_count,
        master_container=None,
        recreate=False,

        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='udc_button_container',
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

        button_class_=[None]*udc_button_count,
        button_command=[self.update_character,self.delete_character,self.clear_update_character_entry_fields],
        button_compound=[None]*udc_button_count,
        button_cursor=[None]*udc_button_count,
        button_default=[None]*udc_button_count,
        button_image=[None]*udc_button_count,
        button_name=['update_character_button','delete_character_button','clear_character_button'],
        button_padding=[None]*udc_button_count,
        button_state=[None]*udc_button_count,
        button_style=[None]*udc_button_count,
        button_takefocus=[None]*udc_button_count,
        button_text=['Update Character','Delete Character','Clear'],
        button_textvariable=[None]*udc_button_count,
        button_underline=[None]*udc_button_count,
        button_width=[16]*udc_button_count,
        button_bootstyle=[WARNING,DANGER,PRIMARY],

        button_grid_cnf=[None]*udc_button_count,
        button_grid_column=[1,2,3],
        button_grid_columnspan=[None]*udc_button_count,
        button_grid_row=[1,1,1],
        button_grid_rowspawn=[None]*udc_button_count,
        button_grid_ipadx=[None]*udc_button_count,
        button_grid_ipady=[None]*udc_button_count,
        button_grid_padx=[5]*udc_button_count,
        button_grid_pady=[5]*udc_button_count,
        button_grid_sticky=[None]*udc_button_count,
        button_grid_in_=[None]*udc_button_count)    

        #Form validation
        add_validation(self.npw_entry_field_entry_objects[0],
        Validate.character_name,
        when = 'all',
        error_label = self.npw_entry_field_error_label_objects[0])

        add_validation(self.update_npw_entry_field_entry_objects[0],
        Validate.character_name,
        when = 'all',
        error_label = self.update_npw_entry_field_error_label_objects[0])

        add_validation(self.npw_entry_field_entry_objects[1],
        Validate.character_password,
        when = 'all',
        error_label = self.npw_entry_field_error_label_objects[1])

        add_validation(self.update_npw_entry_field_entry_objects[1],
        Validate.character_password,
        when = 'all',
        error_label = self.update_npw_entry_field_error_label_objects[1])

        add_validation(self.lvl_entry_field_entry_objects[0],
        Validate.character_level,
        when = 'all',
        error_label = self.lvl_entry_field_error_label_objects[0])

        add_validation(self.update_lvl_entry_field_entry_objects[0],
        Validate.character_level,
        when = 'all',
        error_label = self.update_lvl_entry_field_error_label_objects[0])

        add_validation(self.cwdp_entry_field_combobox_objects[0],
        Validate.character_class,
        when = 'focusin',
        current_class = self.current_class,
        weapon_entry_field = self.cwdp_entry_field_combobox_objects[1],
        device_entry_field = self.cwdp_entry_field_combobox_objects[2],
        error_label = self.cwdp_entry_field_error_label_objects[0])

        add_validation(self.update_cwdp_entry_field_combobox_objects[0],
        Validate.character_class,
        when = 'focusin',
        current_class = self.update_current_class,
        weapon_entry_field = self.update_cwdp_entry_field_combobox_objects[1],
        device_entry_field = self.update_cwdp_entry_field_combobox_objects[2],
        error_label = self.update_cwdp_entry_field_error_label_objects[0])

        add_validation(self.cwdp_entry_field_combobox_objects[1],
        Validate.character_weapon_slots,
        when = 'all',
        error_label = self.cwdp_entry_field_error_label_objects[1])

        add_validation(self.update_cwdp_entry_field_combobox_objects[1],
        Validate.character_weapon_slots,
        when = 'all',
        error_label = self.update_cwdp_entry_field_error_label_objects[1])
        
        add_validation(self.cwdp_entry_field_combobox_objects[2],
        Validate.character_device_slots,
        when = 'all',
        error_label = self.cwdp_entry_field_error_label_objects[2])

        add_validation(self.update_cwdp_entry_field_combobox_objects[2],
        Validate.character_device_slots,
        when = 'all',
        error_label = self.update_cwdp_entry_field_error_label_objects[2])
        
        add_validation(self.cwdp_entry_field_combobox_objects[3],
        Validate.character_fleet_position,
        when = 'all',
        error_label = self.cwdp_entry_field_error_label_objects[3])

        add_validation(self.update_cwdp_entry_field_combobox_objects[3],
        Validate.character_fleet_position,
        when = 'all',
        error_label = self.update_cwdp_entry_field_error_label_objects[3])

    #Button commands
    def submit_character_entry_fields(self):
        validate_name = self.npw_entry_field_entry_objects[0].validate()
        validate_password = self.npw_entry_field_entry_objects[1].validate()
        validate_level = self.lvl_entry_field_entry_objects[0].validate()
        validate_class = self.cwdp_entry_field_combobox_objects[0].validate()
        validate_weapons = self.cwdp_entry_field_combobox_objects[1].validate()
        validate_devices = self.cwdp_entry_field_combobox_objects[2].validate()
        validate_position = self.cwdp_entry_field_combobox_objects[3].validate()

        if validate_name == True and validate_password == True and validate_level == True and validate_class == True and validate_weapons == True and validate_devices == True and validate_position == True :
            character_name = self.character_name.get()
            character_password = self.character_password.get()
            character_level = self.character_level.get()
            character_class = self.character_class.get()
            character_weapon_slots = self.character_weapon_slots.get()
            character_device_slots = self.character_device_slots.get()
            character_fleet_position = self.character_fleet_position.get()

            self.clear_character_entry_fields()

            self.data.append((
            character_name,
            character_password,
            character_class,
            character_level,
            character_weapon_slots,
            character_device_slots,
            character_fleet_position))

            formwidgets.FormWidgets.create_toastnotification(self, 
            title = 'Submission Successful!',
            message = 'Your character has been saved to the database.',
            duration = 3000)
            
            formwidgets.FormWidgets.destroy_children_widgets(self, self.character_table_container)
            
        (self.character_table_container,
        self.character_table_objects) = formwidgets.FormWidgets.create_table_grid(self,
                                                                                  
        grid_objects=1,
        master_container=self.character_table_container,
        recreate=True,
        
        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='character_table_container',
        container_padding=None,
        container_relief=None,
        container_style=None,
        container_takefocus=None,
        container_width=None,
        
        container_pack_cnf=None,
        container_pack_after=None,
        container_pack_anchor=None,
        container_pack_before=None,
        container_pack_expand=None,
        container_pack_fill= None,
        container_pack_side=None,
        container_pack_ipadx=None,
        container_pack_ipady=5,
        container_pack_padx=None,
        container_pack_pady=None,
        container_pack_in_=None,

        table_bootstyle=[PRIMARY],
        table_coldata=[self.add_character_table_columns],
        table_rowdata=[self.data],
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
                            
    def clear_character_entry_fields(self):
        self.character_name.set('')
        self.character_password.set('')
        self.pw_checkbutton_variable.set(0)
        self.npw_entry_field_entry_objects[1].config(show = '*')
        self.character_level.set(0)
        self.character_class.set('')
        self.character_weapon_slots.set('')
        self.character_device_slots.set('')
        self.character_fleet_position.set('')
        self.cwdp_entry_field_combobox_objects[1].config(state = DISABLED)
        self.cwdp_entry_field_combobox_objects[2].config(state = DISABLED)

    def get_selected_row(self, table_object):
        self.clear_update_character_entry_fields()

        row_data = []
        selected_row = table_object.get_rows(selected = True)

        if selected_row != []:
            for item in selected_row:
                row_data = item.values
            
            self.update_character_name.set(row_data[0])
            self.update_character_password.set(row_data[1])
            self.update_character_class.set(row_data[2])
            self.update_current_class.set(row_data[2])
            self.update_character_level.set(row_data[3])
            self.update_character_weapon_slots.set(row_data[4])
            self.update_character_device_slots.set(row_data[5])
            self.update_character_fleet_position.set(row_data[6])
            self.update_cwdp_entry_field_combobox_objects[1].config(state = 'readonly')
            self.update_cwdp_entry_field_combobox_objects[2].config(state = 'readonly')
            
        else:
            formwidgets.FormWidgets.create_warning_messagebox(self,
            message =  'There are no characters to select. Please add a character.',
            title = 'No characters warning',
            alert = True)
  
    def update_character(self):
        validate_name = self.update_npw_entry_field_entry_objects[0].validate()
        validate_password = self.update_npw_entry_field_entry_objects[1].validate()
        validate_level = self.update_lvl_entry_field_entry_objects[0].validate()
        validate_class = self.update_cwdp_entry_field_combobox_objects[0].validate()
        validate_weapons = self.update_cwdp_entry_field_combobox_objects[1].validate()
        validate_devices = self.update_cwdp_entry_field_combobox_objects[2].validate()
        validate_position = self.update_cwdp_entry_field_combobox_objects[3].validate()

        if validate_name == True and validate_password == True and validate_level == True and validate_class == True and validate_weapons == True and validate_devices == True and validate_position == True :
            confirm_update = formwidgets.FormWidgets.create_warning_messagebox_yesno(self,
            message = f'You are about to update the character {self.update_npw_entry_field_entry_objects[0].get()}.\nAre you sure you want to do this?',
            title = 'Update Character Warning',
            alert = True)

            print(confirm_update)
            self.clear_update_character_entry_fields()
        else:
            print('Not Valid')

    def delete_character(self):
        validate_name = self.update_npw_entry_field_entry_objects[0].validate()

        if validate_name == True:
            confirm_delete = formwidgets.FormWidgets.create_warning_messagebox_yesno(self,
            message = f'You are about to delete the character {self.update_npw_entry_field_entry_objects[0].get()}. \nThis will also delete all of this characters equipment sets. \nAre you sure you want to do this?',
            title = 'Delete Character Warning',
            alert = True)

            print(confirm_delete)
            self.clear_update_character_entry_fields()
        else:
            print('Not Valid')

    def clear_update_character_entry_fields(self):
        self.update_character_name.set('')
        self.update_character_password.set('')
        self.update_pw_checkbutton_variable.set(0)
        self.update_npw_entry_field_entry_objects[1].config(show = '*')
        self.update_character_level.set(0)
        self.update_character_class.set('')
        self.update_character_weapon_slots.set('')
        self.update_character_device_slots.set('')
        self.update_character_fleet_position.set('')
        self.update_cwdp_entry_field_combobox_objects[1].config(state = DISABLED)
        self.update_cwdp_entry_field_combobox_objects[2].config(state = DISABLED)
    
    def show_password(self, password_entry, checkbox_variable):
        if checkbox_variable.get() == 1:
            password_entry.config(show = '')
        else:
            password_entry.config(show = '*')