import formwidgets
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
import databasemanager as dbm

class EarthAndBeyondMultiBox(ttkb.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.selected_theme = ttkb.StringVar(self)
        self.selected_theme.set('cyborg')
        ttkb.Style(theme = self.selected_theme.get()).theme_use(self.selected_theme.get())

        self.theme_combobox_values = [
        'cerculean',
        'cosmo',
        'cyborg',
        'darkly',
        'flatly',
        'journal',
        'litera',
        'lumen', 
        'minty',
        'morph',
        'pulse',
        'sandstone',
        'simplex',
        'solar',
        'superhero',
        'united',
        'vapor',
        'yeti']

        (self.theme_selection_container,
        self.theme_selection_label_objects,
        self.theme_selection_combobox_objects) = formwidgets.FormWidgets.create_label_combobox_grid(self,
        
        grid_objects=1,
        master_container=None,
        recreate=False,

        container_border=None,
        container_borderwidth=None,
        container_class=None,
        container_cursor=None,
        container_height=None,
        container_name='theme_selection_container',
        container_padding=None,
        container_relief=None,
        container_style=None,
        container_takefocus=None,
        container_width=None,

        container_pack_cnf=None,
        container_pack_after=None,
        container_pack_anchor=NE,
        container_pack_before=None,
        container_pack_expand=NO,
        container_pack_fill=None,
        container_pack_side=None,
        container_pack_ipadx=None,
        container_pack_ipady=None,
        container_pack_padx=10,
        container_pack_pady=10,
        container_pack_in_=None,

        label_anchor=[None],
        label_background=[None],
        label_border=[None],
        label_borderwidth=[None],
        label_class_=[None],
        label_compound=[None],
        label_cursor=[None],
        label_font=[None],
        label_foreground=[None],
        label_image=[None],
        label_justify=[None],
        label_name=['theme_selection_label'],
        label_padding=[None],
        label_relief=[None],
        label_state=[None],
        label_style=[None],
        label_takefocus=[None],
        label_text=['Theme Selection:'],
        label_textvariable=[None],
        label_underline=[None],
        label_width=[15],
        label_wraplength=[None],

        label_grid_cnf=[None],
        label_grid_column=[1],
        label_grid_columnspan=[None],
        label_grid_row=[1],
        label_grid_rowspawn=[None],
        label_grid_ipadx=[None],
        label_grid_ipady=[None],
        label_grid_padx=[10],
        label_grid_pady=[None],
        label_grid_sticky=[None],
        label_grid_in_=[None],

        combobox_bind_action=[True],
        combobox_action=['<<ComboboxSelected>>'],
        combobox_command=[self.change_style],

        combobox_background=[None],
        combobox_class_=[None],
        combobox_cursor=[None],
        combobox_exportselection=[None],
        combobox_font=[None],
        combobox_foreground=[None],
        combobox_height=[None],
        combobox_invalidcommand=[None],
        combobox_justify=[None],
        combobox_name=['theme_selection_combobox'],
        combobox_postcommand=[None],
        combobox_show=[None],
        combobox_state=[READONLY],
        combobox_style=[None],
        combobox_takefocus=[None],
        combobox_textvariable=[self.selected_theme],
        combobox_validate=[None],
        combobox_validatecommand=[None],
        combobox_values=[self.theme_combobox_values],
        combobox_width=[15],
        combobox_xscrollcommand=[None],
        
        combobox_grid_cnf=[None],
        combobox_grid_column=[2],
        combobox_grid_columnspan=[None],
        combobox_grid_row=[1],
        combobox_grid_rowspawn=[None],
        combobox_grid_ipadx=[None],
        combobox_grid_ipady=[None],
        combobox_grid_padx=[None],
        combobox_grid_pady=[None],
        combobox_grid_sticky=[None],
        combobox_grid_in_=[None])
        
        self.earth_and_beyond_multibox_notebook = formwidgets.FormWidgets.create_notebook(self,
        notebook_class=None,
        notebook_cursor=None,
        notebook_height=None,
        notebook_name='earth_and_beyond_multibox_notebook',
        notebook_padding=None,
        notebook_style=None,
        notebook_takefocus=None,
        notebook_width=None,
        
        notebook_place_cnf=None,
        notebook_place_anchor=None,
        notebook_place_bordermode=None,
        notebook_place_width=None,
        notebook_place_height=None,
        notebook_place_x=0,
        notebook_place_y=40,
        notebook_place_relheight=1,
        notebook_place_relwidth=1,
        notebook_place_relx=None,
        notebook_place_rely=None)

        self.mainloop()
    
    def change_style(self, value):
        selected_theme = self.selected_theme.get()
        ttkb.Style(theme = selected_theme).theme_use(selected_theme)

if __name__ == '__main__':
    EarthAndBeyondMultiBox(title = 'Earth & Beyond Multi-Box', iconphoto = 'C:/Src/pub-multi-box/EB.png', size = (1100, 1100))