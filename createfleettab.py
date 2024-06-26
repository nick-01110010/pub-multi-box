import formwidgets
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from ttkbootstrap.validation import *
import validation as Validate

class CreateFleetTab(ttkb.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.test_data = [
        ['test1','test1','test1','test1'], ['test2','test2','test2','test2'], ['test3','test3','test3','test3'], ['test4','test4','test4','test4'],
        ['test5','test5','test5','test5'], ['test6','test6','test6','test6'], ['test7','test7','test7','test7'], ['test8','test8','test8','test8'],
        ['test9','test9','test9','test9'], ['test10','test10','test10','test10'], ['test11','test11','test11','test11'], ['test12','test12','test12','test12']]
        self.column_names = [
        {'text': 'Character Name', 'stretch': True},
        {'text': 'Character Class', 'stretch': True},
        {'text': 'Character Level', 'stretch': True},
        {'text': 'Character Fleet Position', 'stretch': True}]
        self.fleet_members = []
        self.fleet_name = ttkb.StringVar(value = "")

        (self.select_fleet_members_table_container,
        self.select_fleet_members_table_objects) = formwidgets.FormWidgets.create_table_grid(self,
                                                                                  
        grid_objects=1,
        master_container=None,
        recreate=False,
        
        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='select_fleet_members_table_container',
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
        table_coldata=[self.column_names,],
        table_rowdata=[self.test_data],
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

        (self.add_fleet_member_button_grid_container,
        self.add_fleet_member_button_grid_container_objects) = formwidgets.FormWidgets.create_button_grid(self,
        grid_objects=1,
        master_container=None,
        recreate=False,

        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='add_fleet_member_button_grid_container',
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
        button_command=[lambda: self.get_selected_row(self.select_fleet_members_table_objects[0])],
        button_compound=[None],
        button_cursor=[None],
        button_default=[None],
        button_image=[None],
        button_name=['add_fleet_member_button'],
        button_padding=[None],
        button_state=[None],
        button_style=[None],
        button_takefocus=[None],
        button_text=['Add Fleet Member'],
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


        (self.selected_fleet_members_table_container,
        self.selected_fleet_members_table_objects) = formwidgets.FormWidgets.create_table_grid(self,
                                                                                  
        grid_objects=1,
        master_container=None,
        recreate=False,
        
        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='selected_fleet_members_table_container',
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
        table_coldata=[self.column_names,],
        table_rowdata=[self.fleet_members],
        table_paginated=[False],
        table_searchable=[False],
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

        (self.remove_fleet_member_button_grid_container,
        self.remove_fleet_member_button_grid_container_objects)=formwidgets.FormWidgets.create_button_grid(self,
        grid_objects=1,
        master_container=None,
        recreate=False,

        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='remove_fleet_member_button_grid_container',
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
        button_command=[lambda: self.remove_selected_row(self.selected_fleet_members_table_objects[0])],
        button_compound=[None],
        button_cursor=[None],
        button_default=[None],
        button_image=[None],
        button_name=['remove_fleet_member_button'],
        button_padding=[None],
        button_state=[None],
        button_style=[None],
        button_takefocus=[None],
        button_text=['Remove Fleet Member'],
        button_textvariable=[None],
        button_underline=[None],
        button_width=[20],
        button_bootstyle=[DANGER],

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

        (self.create_fleet_entry_grid_container,
        self.create_fleet_entry_grid_labels,
        self.create_fleet_entry_grid_entries,
        self.create_fleet_entry_grid_error_labels) = formwidgets.FormWidgets.create_label_entry_label_grid(self,
        
        grid_objects=1,
        master_container=None,
        recreate=False,

        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='create_fleet_entry_container',
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

        label1_anchor=[CENTER],
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
        label1_name=['create_fleet_label'],
        label1_padding=[None],
        label1_relief=[None],
        label1_state=[None],
        label1_style=[None],
        label1_takefocus=[None],
        label1_text=['Fleet Name:'],
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
        label1_grid_padx=[None],
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
        entry_name=['create_fleet_entry'],
        entry_show=[None],
        entry_state=[None],
        entry_style=[None],
        entry_takefocus=[None],
        entry_textvariable=[self.fleet_name],
        entry_validate=[None],
        entry_validatecommand=[None],
        entry_width=[20],
        entry_xscrollcommand=[None],

        entry_grid_cnf=[None],
        entry_grid_column=[1],
        entry_grid_columnspan=[None],
        entry_grid_row=[2],
        entry_grid_rowspawn=[None],
        entry_grid_ipadx=[None],
        entry_grid_ipady=[None],
        entry_grid_padx=[None],
        entry_grid_pady=[5],
        entry_grid_sticky=[None],
        entry_grid_in_=[None],

        label2_anchor=[CENTER],
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
        label2_name=['create_fleet_error_label'],
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
        label2_grid_column=[1],
        label2_grid_columnspan=[None],
        label2_grid_row=[3],
        label2_grid_rowspawn=[None],
        label2_grid_ipadx=[None],
        label2_grid_ipady=[None],
        label2_grid_padx=[None],
        label2_grid_pady=[None],
        label2_grid_sticky=[None],
        label2_grid_in_=[None])

        self.create_fleet_button_grid_container, self.create_fleet_button_grid_objects = formwidgets.FormWidgets.create_button_grid(self,
        grid_objects=1,
        master_container=None,
        recreate=False,

        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='create_fleet_button_grid_container',
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
        button_command=[lambda: self.create_fleet()],
        button_compound=[None],
        button_cursor=[None],
        button_default=[None],
        button_image=[None],
        button_name=['create_fleet_button'],
        button_padding=[None],
        button_state=[None],
        button_style=[None],
        button_takefocus=[None],
        button_text=['Create Fleet'],
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


        #Form validation
        add_validation(self.create_fleet_entry_grid_entries[0],
        Validate.fleet_name,
        when = 'all',
        error_label = self.create_fleet_entry_grid_error_labels[0])
    
    #Button commands
    def get_selected_row(self, table_object):
        row_data = []
        selected_row= table_object.get_rows(selected = True)

        for item in selected_row:
            row_data = item.values

        if (row_data not in self.fleet_members) and (len(self.fleet_members) < 6): 
            self.fleet_members.append(row_data)
        
        elif len(self.fleet_members) == 6:
            formwidgets.FormWidgets.create_warning_messagebox(self,
            message = 'The Fleet is full, please remove a member to add another.',
            title = 'Fleet Full Warning',
            alert = True)
        
        elif row_data in self.fleet_members:
            formwidgets.FormWidgets.create_warning_messagebox(self,
            message = 'This character is already in the fleet.',
            title = 'Duplicate Character Warning',
            alert = True)

        formwidgets.FormWidgets.destroy_children_widgets(self, self.selected_fleet_members_table_container)

        (self.selected_fleet_members_table_container,
        self.selected_fleet_members_table_objects) = formwidgets.FormWidgets.create_table_grid(self,
                                                                                  
        grid_objects=1,
        master_container=self.selected_fleet_members_table_container,
        recreate=True,
        
        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='selected_fleet_members_table_container',
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
        table_coldata=[self.column_names,],
        table_rowdata=[self.fleet_members],
        table_paginated=[False],
        table_searchable=[False],
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
                
    def remove_selected_row(self, table_object):
        row_data = []
        selected_row = table_object.get_rows(selected = True)

        for item in selected_row:
            row_data = item.values

        if row_data in self.fleet_members: 
            self.fleet_members.remove(row_data)

        formwidgets.FormWidgets.destroy_children_widgets(self,self.selected_fleet_members_table_container)

        (self.selected_fleet_members_table_container,
        self.selected_fleet_members_table_objects) = formwidgets.FormWidgets.create_table_grid(self,
                                                                                  
        grid_objects=1,
        master_container=self.selected_fleet_members_table_container,
        recreate=True,
        
        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='selected_fleet_members_table_container',
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
        table_coldata=[self.column_names,],
        table_rowdata=[self.fleet_members],
        table_paginated=[False],
        table_searchable=[False],
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

    def create_fleet(self):
        validate_fleet_name = self.create_fleet_entry_grid_entries[0].validate()

        if validate_fleet_name == True:

            if len(self.fleet_members) <= 1:
                formwidgets.FormWidgets.create_warning_messagebox(self,
                message =  'A fleet must have least two characters.',
                title = 'Not Enough Members Warning',
                alert = True)
            else:
                self.fleet_name.set('')
                self.fleet_members = []

                formwidgets.FormWidgets.destroy_children_widgets(self, self.selected_fleet_members_table_container)

        (self.selected_fleet_members_table_container,
        self.selected_fleet_members_table_objects) = formwidgets.FormWidgets.create_table_grid(self,
                                                                                  
        grid_objects=1,
        master_container=self.selected_fleet_members_table_container,
        recreate=True,
        
        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='selected_fleet_members_table_container',
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
        table_coldata=[self.column_names,],
        table_rowdata=[self.fleet_members],
        table_paginated=[False],
        table_searchable=[False],
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