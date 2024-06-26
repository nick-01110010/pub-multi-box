import ttkbootstrap as ttkb
import createcharactertab
import createcv2imagetab
import createfleetequipmenttab
import createfleetcommands
import createfleettab
import tradeitems
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.toast import ToastNotification

class FormWidgets(ttkb.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
    
    def destroy_children_widgets(self, child_widgets):
        for child in child_widgets.winfo_children():
            child.destroy()

    def create_notebook(self,
        notebook_class=None,notebook_cursor=None,notebook_height=None,notebook_name=None,
        notebook_padding=None,notebook_style=None,notebook_takefocus=None,notebook_width=None,
        
        notebook_place_cnf=None,notebook_place_anchor=None,notebook_place_bordermode=None,notebook_place_width=None,
        notebook_place_height=None,notebook_place_x=None,notebook_place_y=None,notebook_place_relheight=None,
        notebook_place_relwidth=None,notebook_place_relx=None,notebook_place_rely=None):
        
        notebook = ttkb.Notebook(
        master=self,class_=notebook_class,cursor=notebook_cursor,height=notebook_height,
        name=notebook_name,padding=notebook_padding,style=notebook_style,takefocus=notebook_takefocus,
        width=notebook_width)
        
        notebook.place(
        cnf=notebook_place_cnf,anchor=notebook_place_anchor,bordermode=notebook_place_bordermode,width=notebook_place_width,
        height=notebook_place_height,x=notebook_place_x,y=notebook_place_y,relheight=notebook_place_relheight,
        relwidth=notebook_place_relwidth,relx=notebook_place_relx,rely=notebook_place_rely)

        character_tab=createcharactertab.CreateCharacterTab(notebook)
        fleet_creation_tab=createfleettab.CreateFleetTab(notebook)
        fleet_commands_tab=createfleetcommands.CreateFleetCommandsTab(notebook)
        fleet_equipment_tab=createfleetequipmenttab.CreateFleetEquipmentTab(notebook)
        trade_items_tab=tradeitems.TradeItemsTab(notebook)
        cv_image_tab=createcv2imagetab.CreateCV2ImageTab(notebook)

        notebook.add(character_tab, text='Add Characters')
        notebook.add(fleet_creation_tab, text='Create Fleet')
        notebook.add(fleet_commands_tab, text='Fleet Commands')
        notebook.add(fleet_equipment_tab, text='Fleet Equipment')
        notebook.add(trade_items_tab, text='Trade Items')
        notebook.add(cv_image_tab, text='CV2 Image Refrences')

    def create_label_combobox_grid(self,
        
        grid_objects=None,master_container=None,recreate=False,

        container_border=None,container_borderwidth=None,container_class=None,container_cursor=None,
        container_height=None,container_name=None,container_padding=None,container_relief=None,
        container_style=None,container_takefocus=None,container_width=None,

        container_pack_cnf=None,container_pack_after=None,container_pack_anchor=None,container_pack_before=None,
        container_pack_expand=None,container_pack_fill=None,container_pack_side=None,container_pack_ipadx=None,
        container_pack_ipady=None,container_pack_padx=None,container_pack_pady=None,container_pack_in_=None,

        label_anchor=[None],label_background=[None],label_border=[None],label_borderwidth=[None],
        label_class_=[None],label_compound=[None],label_cursor=[None],label_font=[None],label_foreground=[None],
        label_image=[None],label_justify=[None],label_name=[None],label_padding=[None],label_relief=[None],
        label_state=[None],label_style=[None], label_takefocus=[None],label_text=[None],label_textvariable=[None],
        label_underline=[None],label_width=[None],label_wraplength=[None],

        label_grid_cnf=[None],label_grid_column=[None],label_grid_columnspan=[None],label_grid_row=[None],
        label_grid_rowspawn=[None],label_grid_ipadx=[None],label_grid_ipady=[None],label_grid_padx=[None],
        label_grid_pady=[None],label_grid_sticky=[None],label_grid_in_=[None],

        combobox_bind_action=[False],combobox_action=[None],combobox_command=[None],

        combobox_background=[None],combobox_class_=[None],combobox_cursor=[None],combobox_exportselection=[None],
        combobox_font=[None],combobox_foreground=[None],combobox_height=[None],combobox_invalidcommand=[None],
        combobox_justify=[None],combobox_name=[None],combobox_postcommand=[None],combobox_show=[None],
        combobox_state=[None],combobox_style=[None],combobox_takefocus=[None],combobox_textvariable=[None],
        combobox_validate=[None],combobox_validatecommand=[None],combobox_values=[None],combobox_width=[None],
        combobox_xscrollcommand=[None],
        
        combobox_grid_cnf=[None],combobox_grid_column=[None],combobox_grid_columnspan=[None],combobox_grid_row=[None],
        combobox_grid_rowspawn=[None],combobox_grid_ipadx=[None],combobox_grid_ipady=[None],combobox_grid_padx=[None],
        combobox_grid_pady=[None],combobox_grid_sticky=[None],combobox_grid_in_=[None]):

        label_objects=[]
        combobox_objects=[]

        if recreate==False:

            container=ttkb.Frame(
            master=self,border=container_border,borderwidth=container_borderwidth,class_=container_class,
            cursor=container_cursor,height=container_height,name=container_name,padding=container_padding,
            relief=container_relief,style=container_style,takefocus=container_takefocus,width=container_width)
            
            container.pack(
            cnf=container_pack_cnf,after=container_pack_after,anchor=container_pack_anchor,before=container_pack_before,
            expand=container_pack_expand,fill=container_pack_fill,side=container_pack_side,ipadx=container_pack_ipadx,
            ipady=container_pack_ipady,padx=container_pack_padx,pady=container_pack_pady,in_=container_pack_in_)

            for object in range(grid_objects):

                label = ttkb.Label(
                master=container,anchor=label_anchor[object],background=label_background[object],border=label_border[object],
                borderwidth=label_borderwidth[object],class_=label_class_[object],compound=label_compound[object],cursor=label_cursor[object],
                font=label_font[object],foreground=label_foreground[object],image=label_image[object],justify=label_justify[object],
                name=label_name[object],padding=label_padding[object],relief=label_relief[object],state=label_state[object],
                style=label_style[object],takefocus=label_takefocus[object],text=label_text[object],textvariable=label_textvariable[object],
                underline=label_underline[object],width=label_width[object],wraplength=label_wraplength[object])

                label.grid(
                cnf=label_grid_cnf[object],column=label_grid_column[object],columnspan=label_grid_columnspan[object],row=label_grid_row[object],
                rowspan=label_grid_rowspawn[object],ipadx=label_grid_ipadx[object],ipady=label_grid_ipady[object],padx=label_grid_padx[object],
                pady=label_grid_pady[object],sticky=label_grid_sticky[object],in_= label_grid_in_[object])

                label_objects.append(label)

                combobox = ttkb.Combobox(
                master=container,background=combobox_background[object],class_=combobox_class_[object],cursor=combobox_cursor[object],
                exportselection=combobox_exportselection[object],font=combobox_font[object],foreground=combobox_foreground[object],height=combobox_height[object],
                invalidcommand=combobox_invalidcommand[object],justify=combobox_justify[object],name=combobox_name[object],postcommand=combobox_postcommand[object],
                show=combobox_show[object],state=combobox_state[object],style=combobox_style[object],takefocus=combobox_takefocus[object],
                textvariable=combobox_textvariable[object],validate=combobox_validate[object],validatecommand=combobox_validatecommand[object],values=combobox_values[object],
                width=combobox_width[object],xscrollcommand=combobox_xscrollcommand[object])
                
                combobox.grid(
                cnf=combobox_grid_cnf[object],column=combobox_grid_column[object],columnspan=combobox_grid_columnspan[object],row=combobox_grid_row[object],
                rowspan=combobox_grid_rowspawn[object],ipadx=combobox_grid_ipadx[object],ipady=combobox_grid_ipady[object],padx=combobox_grid_padx[object],
                pady=combobox_grid_pady[object],sticky=combobox_grid_sticky[object],in_=combobox_grid_in_[object])

                if combobox_bind_action[object]==True:
                    combobox.bind(combobox_action[object],combobox_command[object])
                
                combobox_objects.append(combobox)
        
            return container,label_objects,combobox_objects 
        
        else:
            
            if recreate==True:
                for object in range(grid_objects):

                    label=ttkb.Label(
                    master=master_container,anchor=label_anchor[object],background=label_background[object],border=label_border[object],
                    borderwidth=label_borderwidth[object],class_=label_class_[object],compound=label_compound[object],cursor=label_cursor[object],
                    font=label_font[object],foreground=label_foreground[object],image=label_image[object],justify=label_justify[object],
                    name=label_name[object],padding=label_padding[object],relief=label_relief[object],state=label_state[object],
                    style=label_style[object],takefocus=label_takefocus[object],text=label_text[object],textvariable=label_textvariable[object],
                    underline=label_underline[object],width=label_width[object],wraplength=label_wraplength[object])

                    label.grid(
                    cnf=label_grid_cnf[object],column=label_grid_column[object],columnspan=label_grid_columnspan[object],row=label_grid_row[object],
                    rowspan=label_grid_rowspawn[object],ipadx=label_grid_ipadx[object],ipady=label_grid_ipady[object],padx=label_grid_padx[object],
                    pady=label_grid_pady[object],sticky=label_grid_sticky[object],in_= label_grid_in_[object])

                    label_objects.append(label)

                    combobox=ttkb.Combobox(
                    master=master_container,background=combobox_background[object],class_=combobox_class_[object],cursor=combobox_cursor[object],
                    exportselection=combobox_exportselection[object],font=combobox_font[object],foreground=combobox_foreground[object],height=combobox_height[object],
                    invalidcommand=combobox_invalidcommand[object],justify=combobox_justify[object],name=combobox_name[object],postcommand=combobox_postcommand[object],
                    show=combobox_show[object],state=combobox_state[object],style=combobox_style[object],takefocus=combobox_takefocus[object],
                    textvariable=combobox_textvariable[object],validate=combobox_validate[object],validatecommand=combobox_validatecommand[object],values=combobox_values[object],
                    width=combobox_width[object],xscrollcommand=combobox_xscrollcommand[object])
                    
                    combobox.grid(
                    cnf=combobox_grid_cnf[object],column=combobox_grid_column[object],columnspan=combobox_grid_columnspan[object],row=combobox_grid_row[object],
                    rowspan=combobox_grid_rowspawn[object],ipadx=combobox_grid_ipadx[object],ipady=combobox_grid_ipady[object],padx=combobox_grid_padx[object],
                    pady=combobox_grid_pady[object],sticky=combobox_grid_sticky[object],in_=combobox_grid_in_[object])

                    if combobox_bind_action[object]==True:
                        combobox.bind(combobox_action[object],combobox_command[object])
                    
                    combobox_objects.append(combobox)

            return master_container,label_objects,combobox_objects
    
    def create_label_entry_label_grid(self,
        grid_objects=None,
        master_container=None,
        recreate=False,

        container_border=None,container_borderwidth=None,container_class=None,container_cursor=None,
        container_height=None,container_name=None,container_padding=None,container_relief=None,
        container_style=None,container_takefocus=None,container_width=None,

        container_pack_cnf=None,container_pack_after=None,container_pack_anchor=None,container_pack_before=None,
        container_pack_expand=None,container_pack_fill=None,container_pack_side=None,container_pack_ipadx=None,
        container_pack_ipady=None,container_pack_padx=None,container_pack_pady=None,container_pack_in_=None,

        label1_anchor=[None],label1_background=[None],label1_border=[None],label1_borderwidth=[None],
        label1_class_=[None],label1_compound=[None],label1_cursor=[None],label1_font=[None],label1_foreground=[None],
        label1_image=[None],label1_justify=[None],label1_name=[None],label1_padding=[None],label1_relief=[None],
        label1_state=[None],label1_style=[None], label1_takefocus=[None],label1_text=[None],label1_textvariable=[None],
        label1_underline=[None],label1_width=[None],label1_wraplength=[None],

        label1_grid_cnf=[None],label1_grid_column=[None],label1_grid_columnspan=[None],label1_grid_row=[None],
        label1_grid_rowspawn=[None],label1_grid_ipadx=[None],label1_grid_ipady=[None],label1_grid_padx=[None],
        label1_grid_pady=[None],label1_grid_sticky=[None],label1_grid_in_=[None],

        entry_background=[None],entry_class_=[None],entry_cursor=[None],entry_exportselection=[None],
        entry_font=[None],entry_foreground=[None],entry_invalidcommand=[None],entry_justify=[None],
        entry_name=[None],entry_show=[None],entry_state=[None],entry_style=[None],
        entry_takefocus=[None],entry_textvariable=[None],entry_validate=[None],entry_validatecommand=[None],
        entry_width=[None],entry_xscrollcommand=[None],

        entry_grid_cnf=[None],entry_grid_column=[None],entry_grid_columnspan=[None],entry_grid_row=[None],
        entry_grid_rowspawn=[None],entry_grid_ipadx=[None],entry_grid_ipady=[None],entry_grid_padx=[None],
        entry_grid_pady=[None],entry_grid_sticky=[None],entry_grid_in_=[None],

        label2_anchor=[None],label2_background=[None],label2_border=[None],label2_borderwidth=[None],
        label2_class_=[None],label2_compound=[None],label2_cursor=[None],label2_font=[None],label2_foreground=[None],
        label2_image=[None],label2_justify=[None],label2_name=[None],label2_padding=[None],label2_relief=[None],
        label2_state=[None],label2_style=[None], label2_takefocus=[None],label2_text=[None],label2_textvariable=[None],
        label2_underline=[None],label2_width=[None],label2_wraplength=[None],

        label2_grid_cnf=[None],label2_grid_column=[None],label2_grid_columnspan=[None],label2_grid_row=[None],
        label2_grid_rowspawn=[None],label2_grid_ipadx=[None],label2_grid_ipady=[None],label2_grid_padx=[None],
        label2_grid_pady=[None],label2_grid_sticky=[None],label2_grid_in_=[None]):
        
        label1_objects=[]
        entry_objects=[]
        label2_objects=[]

        if recreate==False:

            container=ttkb.Frame(
            master=self,border=container_border,borderwidth=container_borderwidth,class_=container_class,
            cursor=container_cursor,height=container_height,name=container_name,padding=container_padding,
            relief=container_relief,style=container_style,takefocus=container_takefocus,width=container_width)
            
            container.pack(
            cnf=container_pack_cnf,after=container_pack_after,anchor=container_pack_anchor,before=container_pack_before,
            expand=container_pack_expand,fill=container_pack_fill,side=container_pack_side,ipadx=container_pack_ipadx,
            ipady=container_pack_ipady,padx=container_pack_padx,pady=container_pack_pady,in_=container_pack_in_)

            for object in range(grid_objects):

                label1 = ttkb.Label(
                master=container,anchor=label1_anchor[object],background=label1_background[object],border=label1_border[object],
                borderwidth=label1_borderwidth[object],class_=label1_class_[object],compound=label1_compound[object],cursor=label1_cursor[object],
                font=label1_font[object],foreground=label1_foreground[object],image=label1_image[object],justify=label1_justify[object],
                name=label1_name[object],padding=label1_padding[object],relief=label1_relief[object],state=label1_state[object],
                style=label1_style[object],takefocus=label1_takefocus[object],text=label1_text[object],textvariable=label1_textvariable[object],
                underline=label1_underline[object],width=label1_width[object],wraplength=label1_wraplength[object])

                label1.grid(
                cnf=label1_grid_cnf[object],column=label1_grid_column[object],columnspan=label1_grid_columnspan[object],row=label1_grid_row[object],
                rowspan=label1_grid_rowspawn[object],ipadx=label1_grid_ipadx[object],ipady=label1_grid_ipady[object],padx=label1_grid_padx[object],
                pady=label1_grid_pady[object],sticky=label1_grid_sticky[object],in_= label1_grid_in_[object])

                label1_objects.append(label1)

                entry = ttkb.Entry(
                master=container,background=entry_background[object],class_=entry_class_[object],cursor=entry_cursor[object],
                exportselection=entry_exportselection[object],font=entry_font[object],foreground=entry_foreground[object],invalidcommand=entry_invalidcommand[object],
                justify=entry_justify[object],name=entry_name[object],show=entry_show[object],state=entry_state[object],
                style=entry_style[object],takefocus=entry_takefocus[object],textvariable=entry_textvariable[object],validate=entry_validate[object],
                validatecommand=entry_validatecommand[object],width=entry_width[object],xscrollcommand=entry_xscrollcommand[object])

                entry.grid(
                cnf=entry_grid_cnf[object],column=entry_grid_column[object],columnspan=entry_grid_columnspan[object],row=entry_grid_row[object],
                rowspan=entry_grid_rowspawn[object],ipadx=entry_grid_ipadx[object],ipady=entry_grid_ipady[object],padx=entry_grid_padx[object],
                pady=entry_grid_pady[object],sticky=entry_grid_sticky[object],in_=entry_grid_in_[object])

                entry_objects.append(entry)

                label2 = ttkb.Label(
                master=container,anchor=label2_anchor[object],background=label2_background[object],border=label2_border[object],
                borderwidth=label2_borderwidth[object],class_=label2_class_[object],compound=label2_compound[object],cursor=label2_cursor[object],
                font=label2_font[object],foreground=label2_foreground[object],image=label2_image[object],justify=label2_justify[object],
                name=label2_name[object],padding=label2_padding[object],relief=label2_relief[object],state=label2_state[object],
                style=label2_style[object],takefocus=label2_takefocus[object],text=label2_text[object],textvariable=label2_textvariable[object],
                underline=label2_underline[object],width=label2_width[object],wraplength=label2_wraplength[object])

                label2.grid(
                cnf=label2_grid_cnf[object],column=label2_grid_column[object],columnspan=label2_grid_columnspan[object],row=label2_grid_row[object],
                rowspan=label2_grid_rowspawn[object],ipadx=label2_grid_ipadx[object],ipady=label2_grid_ipady[object],padx=label2_grid_padx[object],
                pady=label2_grid_pady[object],sticky=label2_grid_sticky[object],in_= label2_grid_in_[object])

                label2_objects.append(label2)

            return container,label1_objects,entry_objects,label2_objects 
        
        else:
            
            if recreate==True:
                for object in range(grid_objects):

                    label1 = ttkb.Label(
                    master=master_container,anchor=label1_anchor[object],background=label1_background[object],border=label1_border[object],
                    borderwidth=label1_borderwidth[object],class_=label1_class_[object],compound=label1_compound[object],cursor=label1_cursor[object],
                    font=label1_font[object],foreground=label1_foreground[object],image=label1_image[object],justify=label1_justify[object],
                    name=label1_name[object],padding=label1_padding[object],relief=label1_relief[object],state=label1_state[object],
                    style=label1_style[object],takefocus=label1_takefocus[object],text=label1_text[object],textvariable=label1_textvariable[object],
                    underline=label1_underline[object],width=label1_width[object],wraplength=label1_wraplength[object])

                    label1.grid(
                    cnf=label1_grid_cnf[object],column=label1_grid_column[object],columnspan=label1_grid_columnspan[object],row=label1_grid_row[object],
                    rowspan=label1_grid_rowspawn[object],ipadx=label1_grid_ipadx[object],ipady=label1_grid_ipady[object],padx=label1_grid_padx[object],
                    pady=label1_grid_pady[object],sticky=label1_grid_sticky[object],in_= label1_grid_in_[object])

                    label1_objects.append(label1)

                    entry = ttkb.Entry(
                    master=master_container,background=entry_background[object],class_=entry_class_[object],cursor=entry_cursor[object],
                    exportselection=entry_exportselection[object],font=entry_font[object],foreground=entry_foreground[object],invalidcommand=entry_invalidcommand[object],
                    justify=entry_justify[object],name=entry_name[object],show=entry_show[object],state=entry_state[object],
                    style=entry_style[object],takefocus=entry_takefocus[object],textvariable=entry_textvariable[object],validate=entry_validate[object],
                    validatecommand=entry_validatecommand[object],width=entry_width[object],xscrollcommand=entry_xscrollcommand[object])

                    entry.grid(
                    cnf=entry_grid_cnf[object],column=entry_grid_column[object],columnspan=entry_grid_columnspan[object],row=entry_grid_row[object],
                    rowspan=entry_grid_rowspawn[object],ipadx=entry_grid_ipadx[object],ipady=entry_grid_ipady[object],padx=entry_grid_padx[object],
                    pady=entry_grid_pady[object],sticky=entry_grid_sticky[object],in_=entry_grid_in_[object])

                    entry_objects.append(entry)

                    label2 = ttkb.Label(
                    master=master_container,anchor=label2_anchor[object],background=label2_background[object],border=label2_border[object],
                    borderwidth=label2_borderwidth[object],class_=label2_class_[object],compound=label2_compound[object],cursor=label2_cursor[object],
                    font=label2_font[object],foreground=label2_foreground[object],image=label2_image[object],justify=label2_justify[object],
                    name=label2_name[object],padding=label2_padding[object],relief=label2_relief[object],state=label2_state[object],
                    style=label2_style[object],takefocus=label2_takefocus[object],text=label2_text[object],textvariable=label2_textvariable[object],
                    underline=label2_underline[object],width=label2_width[object],wraplength=label2_wraplength[object])

                    label2.grid(
                    cnf=label2_grid_cnf[object],column=label2_grid_column[object],columnspan=label2_grid_columnspan[object],row=label2_grid_row[object],
                    rowspan=label2_grid_rowspawn[object],ipadx=label2_grid_ipadx[object],ipady=label2_grid_ipady[object],padx=label2_grid_padx[object],
                    pady=label2_grid_pady[object],sticky=label2_grid_sticky[object],in_= label2_grid_in_[object])

                    label2_objects.append(label2)

            return master_container,label1_objects,entry_objects,label2_objects 

    def create_label_combobox_label_grid(self,
        grid_objects=None,
        master_container=None,
        recreate=False,

        bind_combobox_action=[False],
        combobox_action=[None],
        combobox_command=[None],

        container_border=None,container_borderwidth=None,container_class=None,container_cursor=None,
        container_height=None,container_name=None,container_padding=None,container_relief=None,
        container_style=None,container_takefocus=None,container_width=None,

        container_pack_cnf=None,container_pack_after=None,container_pack_anchor=None,container_pack_before=None,
        container_pack_expand=None,container_pack_fill=None,container_pack_side=None,container_pack_ipadx=None,
        container_pack_ipady=None,container_pack_padx=None,container_pack_pady=None,container_pack_in_=None,

        label1_anchor=[None],label1_background=[None],label1_border=[None],label1_borderwidth=[None],
        label1_class_=[None],label1_compound=[None],label1_cursor=[None],label1_font=[None],label1_foreground=[None],
        label1_image=[None],label1_justify=[None],label1_name=[None],label1_padding=[None],label1_relief=[None],
        label1_state=[None],label1_style=[None], label1_takefocus=[None],label1_text=[None],label1_textvariable=[None],
        label1_underline=[None],label1_width=[None],label1_wraplength=[None],

        label1_grid_cnf=[None],label1_grid_column=[None],label1_grid_columnspan=[None],label1_grid_row=[None],
        label1_grid_rowspawn=[None],label1_grid_ipadx=[None],label1_grid_ipady=[None],label1_grid_padx=[None],
        label1_grid_pady=[None],label1_grid_sticky=[None],label1_grid_in_=[None],

        combobox_background=[None],combobox_class_=[None],combobox_cursor=[None],combobox_exportselection=[None],
        combobox_font=[None],combobox_foreground=[None],combobox_height=[None],combobox_invalidcommand=[None],
        combobox_justify=[None],combobox_name=[None],combobox_postcommand=[None],combobox_show=[None],
        combobox_state=[None],combobox_style=[None],combobox_takefocus=[None],combobox_textvariable=[None],
        combobox_validate=[None],combobox_validatecommand=[None],combobox_values=[None],combobox_width=[None],
        combobox_xscrollcommand=[None],
        
        combobox_grid_cnf=[None],combobox_grid_column=[None],combobox_grid_columnspan=[None],combobox_grid_row=[None],
        combobox_grid_rowspawn=[None],combobox_grid_ipadx=[None],combobox_grid_ipady=[None],combobox_grid_padx=[None],
        combobox_grid_pady=[None],combobox_grid_sticky=[None],combobox_grid_in_=[None],

        label2_anchor=[None],label2_background=[None],label2_border=[None],label2_borderwidth=[None],
        label2_class_=[None],label2_compound=[None],label2_cursor=[None],label2_font=[None],label2_foreground=[None],
        label2_image=[None],label2_justify=[None],label2_name=[None],label2_padding=[None],label2_relief=[None],
        label2_state=[None],label2_style=[None], label2_takefocus=[None],label2_text=[None],label2_textvariable=[None],
        label2_underline=[None],label2_width=[None],label2_wraplength=[None],

        label2_grid_cnf=[None],label2_grid_column=[None],label2_grid_columnspan=[None],label2_grid_row=[None],
        label2_grid_rowspawn=[None],label2_grid_ipadx=[None],label2_grid_ipady=[None],label2_grid_padx=[None],
        label2_grid_pady=[None],label2_grid_sticky=[None],label2_grid_in_=[None]):

        label1_objects=[]
        combobox_objects=[]
        label2_objects=[]

        if recreate==False:

            container=ttkb.Frame(
            master=self,border=container_border,borderwidth=container_borderwidth,class_=container_class,
            cursor=container_cursor,height=container_height,name=container_name,padding=container_padding,
            relief=container_relief,style=container_style,takefocus=container_takefocus,width=container_width)
            
            container.pack(
            cnf=container_pack_cnf,after=container_pack_after,anchor=container_pack_anchor,before=container_pack_before,
            expand=container_pack_expand,fill=container_pack_fill,side=container_pack_side,ipadx=container_pack_ipadx,
            ipady=container_pack_ipady,padx=container_pack_padx,pady=container_pack_pady,in_=container_pack_in_)

            for object in range(grid_objects):

                label1 = ttkb.Label(
                master=container,anchor=label1_anchor[object],background=label1_background[object],border=label1_border[object],
                borderwidth=label1_borderwidth[object],class_=label1_class_[object],compound=label1_compound[object],cursor=label1_cursor[object],
                font=label1_font[object],foreground=label1_foreground[object],image=label1_image[object],justify=label1_justify[object],
                name=label1_name[object],padding=label1_padding[object],relief=label1_relief[object],state=label1_state[object],
                style=label1_style[object],takefocus=label1_takefocus[object],text=label1_text[object],textvariable=label1_textvariable[object],
                underline=label1_underline[object],width=label1_width[object],wraplength=label1_wraplength[object])

                label1.grid(
                cnf=label1_grid_cnf[object],column=label1_grid_column[object],columnspan=label1_grid_columnspan[object],row=label1_grid_row[object],
                rowspan=label1_grid_rowspawn[object],ipadx=label1_grid_ipadx[object],ipady=label1_grid_ipady[object],padx=label1_grid_padx[object],
                pady=label1_grid_pady[object],sticky=label1_grid_sticky[object],in_= label1_grid_in_[object])

                label1_objects.append(label1)

                combobox = ttkb.Combobox(
                master=container,background=combobox_background[object],class_=combobox_class_[object],cursor=combobox_cursor[object],
                exportselection=combobox_exportselection[object],font=combobox_font[object],foreground=combobox_foreground[object],height=combobox_height[object],
                invalidcommand=combobox_invalidcommand[object],justify=combobox_justify[object],name=combobox_name[object],postcommand=combobox_postcommand[object],
                show=combobox_show[object],state=combobox_state[object],style=combobox_style[object],takefocus=combobox_takefocus[object],
                textvariable=combobox_textvariable[object],validate=combobox_validate[object],validatecommand=combobox_validatecommand[object],values=combobox_values[object],
                width=combobox_width[object],xscrollcommand=combobox_xscrollcommand[object])

                combobox.grid(
                cnf=combobox_grid_cnf[object],column=combobox_grid_column[object],columnspan=combobox_grid_columnspan[object],row=combobox_grid_row[object],
                rowspan=combobox_grid_rowspawn[object],ipadx=combobox_grid_ipadx[object],ipady=combobox_grid_ipady[object],padx=combobox_grid_padx[object],
                pady=combobox_grid_pady[object],sticky=combobox_grid_sticky[object],in_=combobox_grid_in_[object])

                if bind_combobox_action[object]==True:
                    combobox.bind(combobox_action[object],combobox_command[object])

                combobox_objects.append(combobox)

                label2 = ttkb.Label(
                master=container,anchor=label2_anchor[object],background=label2_background[object],border=label2_border[object],
                borderwidth=label2_borderwidth[object],class_=label2_class_[object],compound=label2_compound[object],cursor=label2_cursor[object],
                font=label2_font[object],foreground=label2_foreground[object],image=label2_image[object],justify=label2_justify[object],
                name=label2_name[object],padding=label2_padding[object],relief=label2_relief[object],state=label2_state[object],
                style=label2_style[object],takefocus=label2_takefocus[object],text=label2_text[object],textvariable=label2_textvariable[object],
                underline=label2_underline[object],width=label2_width[object],wraplength=label2_wraplength[object])

                label2.grid(
                cnf=label2_grid_cnf[object],column=label2_grid_column[object],columnspan=label2_grid_columnspan[object],row=label2_grid_row[object],
                rowspan=label2_grid_rowspawn[object],ipadx=label2_grid_ipadx[object],ipady=label2_grid_ipady[object],padx=label2_grid_padx[object],
                pady=label2_grid_pady[object],sticky=label2_grid_sticky[object],in_= label2_grid_in_[object])

                label2_objects.append(label2)

            return container,label1_objects,combobox_objects,label2_objects 
        
        else:
            
            if recreate==True:
                for object in range(grid_objects):

                    label1 = ttkb.Label(
                    master=master_container,anchor=label1_anchor[object],background=label1_background[object],border=label1_border[object],
                    borderwidth=label1_borderwidth[object],class_=label1_class_[object],compound=label1_compound[object],cursor=label1_cursor[object],
                    font=label1_font[object],foreground=label1_foreground[object],image=label1_image[object],justify=label1_justify[object],
                    name=label1_name[object],padding=label1_padding[object],relief=label1_relief[object],state=label1_state[object],
                    style=label1_style[object],takefocus=label1_takefocus[object],text=label1_text[object],textvariable=label1_textvariable[object],
                    underline=label1_underline[object],width=label1_width[object],wraplength=label1_wraplength[object])

                    label1.grid(
                    cnf=label1_grid_cnf[object],column=label1_grid_column[object],columnspan=label1_grid_columnspan[object],row=label1_grid_row[object],
                    rowspan=label1_grid_rowspawn[object],ipadx=label1_grid_ipadx[object],ipady=label1_grid_ipady[object],padx=label1_grid_padx[object],
                    pady=label1_grid_pady[object],sticky=label1_grid_sticky[object],in_= label1_grid_in_[object])

                    label1_objects.append(label1)

                    combobox = ttkb.Combobox(
                    master=master_container,background=combobox_background[object],class_=combobox_class_[object],cursor=combobox_cursor[object],
                    exportselection=combobox_exportselection[object],font=combobox_font[object],foreground=combobox_foreground[object],height=combobox_height[object],
                    invalidcommand=combobox_invalidcommand[object],justify=combobox_justify[object],name=combobox_name[object],postcommand=combobox_postcommand[object],
                    show=combobox_show[object],state=combobox_state[object],style=combobox_style[object],takefocus=combobox_takefocus[object],
                    textvariable=combobox_textvariable[object],validate=combobox_validate[object],validatecommand=combobox_validatecommand[object],values=combobox_values[object],
                    width=combobox_width[object],xscrollcommand=combobox_xscrollcommand[object])

                    combobox.grid(
                    cnf=combobox_grid_cnf[object],column=combobox_grid_column[object],columnspan=combobox_grid_columnspan[object],row=combobox_grid_row[object],
                    rowspan=combobox_grid_rowspawn[object],ipadx=combobox_grid_ipadx[object],ipady=combobox_grid_ipady[object],padx=combobox_grid_padx[object],
                    pady=combobox_grid_pady[object],sticky=combobox_grid_sticky[object],in_=combobox_grid_in_[object])
                    
                    if bind_combobox_action[object]==True:
                        combobox.bind(combobox_action[object],combobox_command[object])
                    
                    combobox_objects.append(combobox)

                    label2 = ttkb.Label(
                    master=master_container,anchor=label2_anchor[object],background=label2_background[object],border=label2_border[object],
                    borderwidth=label2_borderwidth[object],class_=label2_class_[object],compound=label2_compound[object],cursor=label2_cursor[object],
                    font=label2_font[object],foreground=label2_foreground[object],image=label2_image[object],justify=label2_justify[object],
                    name=label2_name[object],padding=label2_padding[object],relief=label2_relief[object],state=label2_state[object],
                    style=label2_style[object],takefocus=label2_takefocus[object],text=label2_text[object],textvariable=label2_textvariable[object],
                    underline=label2_underline[object],width=label2_width[object],wraplength=label2_wraplength[object])

                    label2.grid(
                    cnf=label2_grid_cnf[object],column=label2_grid_column[object],columnspan=label2_grid_columnspan[object],row=label2_grid_row[object],
                    rowspan=label2_grid_rowspawn[object],ipadx=label2_grid_ipadx[object],ipady=label2_grid_ipady[object],padx=label2_grid_padx[object],
                    pady=label2_grid_pady[object],sticky=label2_grid_sticky[object],in_= label2_grid_in_[object])

                    label2_objects.append(label2)

            return master_container,label1_objects,combobox_objects,label2_objects 
        
    def create_checkbutton_grid(self,
        grid_objects=None,
        master_container=None,
        recreate=False,

        container_border=None,container_borderwidth=None,container_class=None,container_cursor=None,
        container_height=None,container_name=None,container_padding=None,container_relief=None,
        container_style=None,container_takefocus=None,container_width=None,
        
        container_pack_cnf=None,container_pack_after=None,container_pack_anchor=None,container_pack_before=None,
        container_pack_expand=None,container_pack_fill= None,container_pack_side=None,container_pack_ipadx=None,
        container_pack_ipady=None,container_pack_padx=None,container_pack_pady=None,container_pack_in_=None,
        checkbutton_class_=None,checkbutton_command=None,checkbutton_compound=None,checkbutton_cursor=None,checkbutton_image=None,
        
        checkbutton_name=[None],checkbutton_offvalue=[None],checkbutton_onvalue=[None],checkbutton_padding=[None],
        checkbutton_state=[None],checkbutton_style=[None],checkbutton_takefocus=[None],checkbutton_text=[None],
        checkbutton_textvariable=[None],checkbutton_underline=[None],checkbutton_variable=[None],checkbutton_width=[None],
        checkbutton_bootstyle=[None],
        
        checkbutton_grid_cnf=[None],checkbutton_grid_column=[None],checkbutton_grid_columnspan=[None],checkbutton_grid_row=[None],
        checkbutton_grid_rowspawn=[None],checkbutton_grid_ipadx=[None],checkbutton_grid_ipady=[None],checkbutton_grid_padx=[None],
        checkbutton_grid_pady=[None],checkbutton_grid_sticky=[None],checkbutton_grid_in_=[None]):
        
        checkbutton_objects = []

        if recreate == False:

            container=ttkb.Frame(
            master=self,border=container_border,borderwidth=container_borderwidth,class_=container_class,
            cursor=container_cursor,height=container_height,name=container_name,padding=container_padding,
            relief=container_relief,style=container_style,takefocus=container_takefocus,width=container_width)

            container.pack(
            cnf=container_pack_cnf,after=container_pack_after,anchor=container_pack_anchor,before=container_pack_before,
            expand=container_pack_expand,fill=container_pack_fill,side=container_pack_side,ipadx=container_pack_ipadx,
            ipady=container_pack_ipady,padx=container_pack_padx,pady=container_pack_pady,in_=container_pack_in_)

            for object in range(grid_objects):

                checkbutton = ttkb.Checkbutton(
                master=container,class_=checkbutton_class_[object],command=checkbutton_command[object],compound=checkbutton_compound[object],
                cursor=checkbutton_cursor[object],image=checkbutton_image[object],name=checkbutton_name[object],offvalue=checkbutton_offvalue[object],
                onvalue=checkbutton_onvalue[object],padding=checkbutton_padding[object],state=checkbutton_state[object],style=checkbutton_style[object],
                takefocus=checkbutton_takefocus[object],text=checkbutton_text[object],textvariable=checkbutton_textvariable[object],underline=checkbutton_underline[object],
                variable=checkbutton_variable[object],width=checkbutton_width[object],bootstyle=checkbutton_bootstyle[object])
                
                checkbutton.grid(
                cnf=checkbutton_grid_cnf[object],column=checkbutton_grid_column[object],columnspan=checkbutton_grid_columnspan[object],row=checkbutton_grid_row[object],
                rowspan=checkbutton_grid_rowspawn[object],ipadx=checkbutton_grid_ipadx[object],ipady=checkbutton_grid_ipady[object],padx=checkbutton_grid_padx[object],
                pady=checkbutton_grid_pady[object],sticky=checkbutton_grid_sticky[object],in_=checkbutton_grid_in_[object])

                checkbutton_objects.append(checkbutton)

            return container, checkbutton_objects
        
        else:

            for object in range(grid_objects):

                checkbutton = ttkb.Checkbutton(
                master=master_container,class_=checkbutton_class_[object],command=checkbutton_command[object],compound=checkbutton_compound[object],
                cursor=checkbutton_cursor[object],image=checkbutton_image[object],name=checkbutton_name[object],offvalue=checkbutton_offvalue[object],
                onvalue=checkbutton_onvalue[object],padding=checkbutton_padding[object],state=checkbutton_state[object],style=checkbutton_style[object],
                takefocus=checkbutton_takefocus[object],text=checkbutton_text[object],textvariable=checkbutton_textvariable[object],underline=checkbutton_underline[object],
                variable=checkbutton_variable[object],width=checkbutton_width[object],bootstyle=checkbutton_bootstyle[object])
                
                checkbutton.grid(
                cnf=checkbutton_grid_cnf[object],column=checkbutton_grid_column[object],columnspan=checkbutton_grid_columnspan[object],row=checkbutton_grid_row[object],
                rowspan=checkbutton_grid_rowspawn[object],ipadx=checkbutton_grid_ipadx[object],ipady=checkbutton_grid_ipady[object],padx=checkbutton_grid_padx[object],
                pady=checkbutton_grid_pady[object],sticky=checkbutton_grid_sticky[object],in_=checkbutton_grid_in_[object])

                checkbutton_objects.append(checkbutton)

            return master_container, checkbutton_objects
                
    def create_button_grid(self,
        grid_objects=None,
        master_container=None,
        recreate=False,

        container_border=None,container_borderwidth=None,container_class=None,container_cursor=None,
        container_height=None,container_name=None,container_padding=None,container_relief=None,
        container_style=None,container_takefocus=None,container_width=None,
        
        container_pack_cnf=None,container_pack_after=None,container_pack_anchor=None,container_pack_before=None,
        container_pack_expand=None,container_pack_fill= None,container_pack_side=None,container_pack_ipadx=None,
        container_pack_ipady=None,container_pack_padx=None,container_pack_pady=None,container_pack_in_=None,

        button_class_=[None],button_command=[None],button_compound=[None],button_cursor=[None],
        button_default=[None],button_image=[None],button_name=[None],button_padding=[None],
        button_state=[None],button_style=[None],button_takefocus=[None],button_text=[None],
        button_textvariable=[None],button_underline=[None],button_width=[None],button_bootstyle=[None],
        
        button_grid_cnf=[None],button_grid_column=[None],button_grid_columnspan=[None],button_grid_row=[None],
        button_grid_rowspawn=[None],button_grid_ipadx=[None],button_grid_ipady=[None], button_grid_padx=[None],
        button_grid_pady=[None],button_grid_sticky=[None],button_grid_in_=[None]):

        button_objects = []

        if recreate == False:

            container=ttkb.Frame(
            master=self,border=container_border,borderwidth=container_borderwidth,class_=container_class,
            cursor=container_cursor,height=container_height,name=container_name,padding=container_padding,
            relief=container_relief,style=container_style,takefocus=container_takefocus,width=container_width)

            container.pack(
            cnf=container_pack_cnf,after=container_pack_after,anchor=container_pack_anchor,before=container_pack_before,
            expand=container_pack_expand,fill=container_pack_fill,side=container_pack_side,ipadx=container_pack_ipadx,
            ipady=container_pack_ipady,padx=container_pack_padx,pady=container_pack_pady,in_=container_pack_in_)


            for object in range(grid_objects):

                button=ttkb.Button(
                master=container,class_=button_class_[object],command=button_command[object],compound=button_compound[object],
                cursor=button_cursor[object],default=button_default[object],image=button_image[object],name=button_name[object],
                padding=button_padding[object],state=button_state[object],style=button_style[object],takefocus=button_takefocus[object],
                text=button_text[object],textvariable=button_textvariable[object],underline=button_underline[object],width=button_width[object],
                bootstyle=button_bootstyle[object])
                
                button.grid(
                cnf=button_grid_cnf[object],column=button_grid_column[object],columnspan=button_grid_columnspan[object],row=button_grid_row[object],
                rowspan=button_grid_rowspawn[object],ipadx=button_grid_ipadx[object],ipady=button_grid_ipady[object],padx=button_grid_padx[object],
                pady=button_grid_pady[object],sticky=button_grid_sticky[object],in_=button_grid_in_[object])

                button_objects.append(button)

            return container,button_objects
        
        else:

            for object in range(grid_objects):

                button = ttkb.Button(
                master = master_container,class_=button_class_[object],command=button_command[object],compound=button_compound[object],
                cursor=button_cursor[object],default=button_default[object],image=button_image[object],name=button_name[object],
                padding=button_padding[object],state=button_state[object],style=button_style[object],takefocus=button_takefocus[object],
                text=button_text[object],textvariable=button_textvariable[object],underline=button_underline[object],width=button_width[object],
                bootstyle=button_bootstyle[object])
                
                button.grid(
                cnf=button_grid_cnf[object],column=button_grid_column[object],columnspan=button_grid_columnspan[object],row=button_grid_row[object],
                rowspan=button_grid_rowspawn[object],ipadx=button_grid_ipadx[object],ipady=button_grid_ipady[object],padx=button_grid_padx[object],
                pady=button_grid_pady[object],sticky=button_grid_sticky[object],in_=button_grid_in_[object])

                button_objects.append(button)

            return master_container, button_objects
    
    def create_table_grid(self,
        grid_objects=None,
        master_container=None,
        recreate=False,

        container_border=None,container_borderwidth=None,container_class=None,container_cursor=None,
        container_height=None,container_name=None,container_padding=None,container_relief=None,
        container_style=None,container_takefocus=None,container_width=None,
        
        container_pack_cnf=None,container_pack_after=None,container_pack_anchor=None,container_pack_before=None,
        container_pack_expand=None,container_pack_fill= None,container_pack_side=None,container_pack_ipadx=None,
        container_pack_ipady=None,container_pack_padx=None,container_pack_pady=None,container_pack_in_=None,

        table_bootstyle=[None],table_coldata=[None],table_rowdata=[None],table_paginated=[False],
        table_searchable=[False],table_autofit=[False],table_autoalign=[False],table_stripecolor=[None],
        table_pagesize=[None],table_height=[None],table_delimiter=[None],
        
        table_grid_cnf=[None],table_grid_column=[None],table_grid_columnspan=[None],table_grid_row=[None],
        table_grid_rowspawn=[None],table_grid_ipadx=[None],table_grid_ipady=[None],table_grid_padx=[None],
        table_grid_pady=[None],table_grid_sticky=[None],table_grid_in_=[None]):

        table_objects = []

        if recreate==False:

            container=ttkb.Frame(
            master=self,border=container_border,borderwidth=container_borderwidth,class_=container_class,
            cursor=container_cursor,height=container_height,name=container_name,padding=container_padding,
            relief=container_relief,style=container_style,takefocus=container_takefocus,width=container_width)

            container.pack(
            cnf=container_pack_cnf,after=container_pack_after,anchor=container_pack_anchor,before=container_pack_before,
            expand=container_pack_expand,fill=container_pack_fill,side=container_pack_side,ipadx=container_pack_ipadx,
            ipady=container_pack_ipady,padx=container_pack_padx,pady=container_pack_pady,in_=container_pack_in_)
        
            for object in range(grid_objects):
                
                table=Tableview(
                master=container,bootstyle=table_bootstyle[object],coldata=table_coldata[object],rowdata=table_rowdata[object],
                paginated=table_paginated[object],searchable=table_searchable[object],autofit=table_autofit[object],autoalign=table_autoalign[object],
                stripecolor=table_stripecolor[object],pagesize=table_pagesize[object],height=table_height[object],delimiter=table_delimiter[object])

                table.grid(
                cnf=table_grid_cnf[object],column=table_grid_column[object],columnspan=table_grid_columnspan[object],row=table_grid_row[object],
                rowspan=table_grid_rowspawn[object],ipadx=table_grid_ipadx[object],ipady=table_grid_ipady[object],padx=table_grid_padx[object],
                pady=table_grid_pady[object],sticky=table_grid_sticky[object],in_=table_grid_in_[object])

                table_objects.append(table)

            return container,table_objects
        
        else:
                
                for object in range(grid_objects):
                    table=Tableview(
                    master=master_container,bootstyle=table_bootstyle[object],coldata=table_coldata[object],rowdata=table_rowdata[object],
                    paginated=table_paginated[object],searchable=table_searchable[object],autofit=table_autofit[object],autoalign=table_autoalign[object],
                    stripecolor=table_stripecolor[object],pagesize=table_pagesize[object],height=table_height[object],delimiter=table_delimiter[object])

                    table.grid(
                    cnf=table_grid_cnf[object],column=table_grid_column[object],columnspan=table_grid_columnspan[object],row=table_grid_row[object],
                    rowspan=table_grid_rowspawn[object],ipadx=table_grid_ipadx[object],ipady=table_grid_ipady[object],padx=table_grid_padx[object],
                    pady=table_grid_pady[object],sticky=table_grid_sticky[object],in_=table_grid_in_[object])

                    table_objects.append(table)
                
                return master_container,table_objects
        
    def create_label_grid(self,
        master_container = None,
        recreate = False,
        grid_count = None,

        container_border=None,container_borderwidth=None,container_class=None,container_cursor=None,
        container_height=None,container_name=None,container_padding=None,container_relief=None,
        container_style=None,container_takefocus=None,container_width=None,
        
        container_pack_cnf=None,container_pack_after=None,container_pack_anchor=None,container_pack_before=None,
        container_pack_expand=None,container_pack_fill= None,container_pack_side=None,container_pack_ipadx=None,
        container_pack_ipady=None,container_pack_padx=None,container_pack_pady=None,container_pack_in_=None,
        
        label_anchor=[None],label_background=[None],label_border=[None],label_borderwidth=[None],
        label_class_=[None],label_compound=[None],label_cursor=[None],label_font=[None],label_foreground=[None],
        label_image=[None],label_justify=[None],label_name=[None],label_padding=[None],label_relief=[None],
        label_state=[None],label_style=[None], label_takefocus=[None],label_text=[None],label_textvariable=[None],
        label_underline=[None],label_width=[None],label_wraplength=[None],

        label_grid_cnf=[None],label_grid_column=[None],label_grid_columnspan=[None],label_grid_row=[None],
        label_grid_rowspawn=[None],label_grid_ipadx=[None],label_grid_ipady=[None],label_grid_padx=[None],
        label_grid_pady=[None],label_grid_sticky=[None],label_grid_in_=[None]):

        label_objects = []
        
        if recreate == False:

            container=ttkb.Frame(
            master=self,border=container_border,borderwidth=container_borderwidth,class_=container_class,
            cursor=container_cursor,height=container_height,name=container_name,padding=container_padding,
            relief=container_relief,style=container_style,takefocus=container_takefocus,width=container_width)

            container.pack(
            cnf=container_pack_cnf,after=container_pack_after,anchor=container_pack_anchor,before=container_pack_before,
            expand=container_pack_expand,fill=container_pack_fill,side=container_pack_side,ipadx=container_pack_ipadx,
            ipady=container_pack_ipady,padx=container_pack_padx,pady=container_pack_pady,in_=container_pack_in_)

            for object in range(grid_count):

                label = ttkb.Label(
                master=container,anchor=label_anchor[object],background=label_background[object],border=label_border[object],
                borderwidth=label_borderwidth[object],class_=label_class_[object],compound=label_compound[object],cursor=label_cursor[object],
                font=label_font[object],foreground=label_foreground[object],image=label_image[object],justify=label_justify[object],
                name=label_name[object],padding=label_padding[object],relief=label_relief[object],state=label_state[object],
                style=label_style[object],takefocus=label_takefocus[object],text=label_text[object],textvariable=label_textvariable[object],
                underline=label_underline[object],width=label_width[object],wraplength=label_wraplength[object])

                label.grid(
                cnf=label_grid_cnf[object],column=label_grid_column[object],columnspan=label_grid_columnspan[object],row=label_grid_row[object],
                rowspan=label_grid_rowspawn[object],ipadx=label_grid_ipadx[object],ipady=label_grid_ipady[object],padx=label_grid_padx[object],
                pady=label_grid_pady[object],sticky=label_grid_sticky[object],in_= label_grid_in_[object])

                label_objects.append(label)
            
            return container, label_objects
        
        else:
 
            for object in range(grid_count):

                label = ttkb.Label(
                master=master_container,anchor=label_anchor[object],background=label_background[object],border=label_border[object],
                borderwidth=label_borderwidth[object],class_=label_class_[object],compound=label_compound[object],cursor=label_cursor[object],
                font=label_font[object],foreground=label_foreground[object],image=label_image[object],justify=label_justify[object],
                name=label_name[object],padding=label_padding[object],relief=label_relief[object],state=label_state[object],
                style=label_style[object],takefocus=label_takefocus[object],text=label_text[object],textvariable=label_textvariable[object],
                underline=label_underline[object],width=label_width[object],wraplength=label_wraplength[object])

                label.grid(
                cnf=label_grid_cnf[object],column=label_grid_column[object],columnspan=label_grid_columnspan[object],row=label_grid_row[object],
                rowspan=label_grid_rowspawn[object],ipadx=label_grid_ipadx[object],ipady=label_grid_ipady[object],padx=label_grid_padx[object],
                pady=label_grid_pady[object],sticky=label_grid_sticky[object],in_= label_grid_in_[object])

                label_objects.append(label)

        return master_container, label_objects
    
    def create_warning_messagebox(self, message, title, alert):
        Messagebox.show_warning(
        message = message,
        title = title,
        alert = alert)
    
    def create_warning_messagebox_yesno(self, message, title, alert):
        result = Messagebox.yesno(
        message = message,
        title = title,
        alert = alert)

        if result == 'Yes':
            return True
        elif result == 'No':
            return False
        elif result == None:
            return False
        else:
            return 'error'
        
    def create_toastnotification(self, title, message, duration):
        toast = ToastNotification(
        title = title,
        message = message,
        duration = duration)

        toast.show_toast()
        
    def create_button_combobox_progressbar_grid(self,
        grid_count = None,
        master_container = None,
        recreate = False,

        container_border=None,container_borderwidth=None,container_class=None,container_cursor=None,
        container_height=None,container_name=None,container_padding=None,container_relief=None,
        container_style=None,container_takefocus=None,container_width=None,

        container_pack_cnf=None,container_pack_after=None,container_pack_anchor=None,container_pack_before=None,
        container_pack_expand=None,container_pack_fill=None,container_pack_side=None,container_pack_ipadx=None,
        container_pack_ipady=None,container_pack_padx=None,container_pack_pady=None,container_pack_in_=None,

        combobox_background=[None],combobox_class_=[None],combobox_cursor=[None],combobox_exportselection=[None],
        combobox_font=[None],combobox_foreground=[None],combobox_height=[None],combobox_invalidcommand=[None],
        combobox_justify=[None],combobox_name=[None],combobox_postcommand=[None],combobox_show=[None],
        combobox_state=[None],combobox_style=[None],combobox_takefocus=[None],combobox_textvariable=[None],
        combobox_validate=[None],combobox_validatecommand=[None],combobox_values=[None],combobox_width=[None],
        combobox_xscrollcommand=[None],
        
        combobox_grid_cnf=[None],combobox_grid_column=[None],combobox_grid_columnspan=[None],combobox_grid_row=[None],
        combobox_grid_rowspawn=[None],combobox_grid_ipadx=[None],combobox_grid_ipady=[None],combobox_grid_padx=[None],
        combobox_grid_pady=[None],combobox_grid_sticky=[None],combobox_grid_in_=[None],

        button_class_=[None],button_command=[None],button_compound=[None],button_cursor=[None],
        button_default=[None],button_image=[None],button_name=[None],button_padding=[None],
        button_state=[None],button_style=[None],button_takefocus=[None],button_text=[None],
        button_textvariable=[None],button_underline=[None],button_width=[None],button_bootstyle=[None],
        
        button_grid_cnf=[None],button_grid_column=[None],button_grid_columnspan=[None],button_grid_row=[None],
        button_grid_rowspawn=[None],button_grid_ipadx=[None],button_grid_ipady=[None], button_grid_padx=[None],
        button_grid_pady=[None],button_grid_sticky=[None],button_grid_in_=[None],

        progressbar_class_=[None],progressbar_cursor=[None],progressbar_length=[None],progressbar_maximum=[None],
        progressbar_mode =[None],progressbar_name=[None],progressbar_orient=[None],progressbar_phase=[None],
        progressbar_style=[None],progressbar_takefocus=[None],progressbar_value=[None],progressbar_variable=[None],
        progressbar_bootstyle=[None],
        
        progressbar_grid_cnf=[None],progressbar_grid_column=[None],progressbar_grid_columnspan=[None],progressbar_grid_row=[None],
        progressbar_grid_rowspawn=[None],progressbar_grid_ipadx=[None],progressbar_grid_ipady=[None],progressbar_grid_padx=[None],
        progressbar_grid_pady=[None],progressbar_grid_sticky=[None],progressbar_grid_in_=[None]):
    
        button_objects = []
        combobox_objects = []
        progressbar_objects = []
        
        if recreate == False:
            
            container=ttkb.Frame(
            master=self,border=container_border,borderwidth=container_borderwidth,class_=container_class,
            cursor=container_cursor,height=container_height,name=container_name,padding=container_padding,
            relief=container_relief,style=container_style,takefocus=container_takefocus,width=container_width)

            container.pack(
            cnf=container_pack_cnf,after=container_pack_after,anchor=container_pack_anchor,before=container_pack_before,
            expand=container_pack_expand,fill=container_pack_fill,side=container_pack_side,ipadx=container_pack_ipadx,
            ipady=container_pack_ipady,padx=container_pack_padx,pady=container_pack_pady,in_=container_pack_in_)

            for object in range(grid_count):

                button=ttkb.Button(
                master=container,class_=button_class_[object],command=button_command[object],compound=button_compound[object],
                cursor=button_cursor[object],default=button_default[object],image=button_image[object],name=button_name[object],
                padding=button_padding[object],state=button_state[object],style=button_style[object],takefocus=button_takefocus[object],
                text=button_text[object],textvariable=button_textvariable[object],underline=button_underline[object],width=button_width[object],
                bootstyle=button_bootstyle[object])
                
                button.grid(
                cnf=button_grid_cnf[object],column=button_grid_column[object],columnspan=button_grid_columnspan[object],row=button_grid_row[object],
                rowspan=button_grid_rowspawn[object],ipadx=button_grid_ipadx[object],ipady=button_grid_ipady[object],padx=button_grid_padx[object],
                pady=button_grid_pady[object],sticky=button_grid_sticky[object],in_=button_grid_in_[object])

                button_objects.append(button)

                combobox = ttkb.Combobox(
                master=container,background=combobox_background[object],class_=combobox_class_[object],cursor=combobox_cursor[object],
                exportselection=combobox_exportselection[object],font=combobox_font[object],foreground=combobox_foreground[object],height=combobox_height[object],
                invalidcommand=combobox_invalidcommand[object],justify=combobox_justify[object],name=combobox_name[object],postcommand=combobox_postcommand[object],
                show=combobox_show[object],state=combobox_state[object],style=combobox_style[object],takefocus=combobox_takefocus[object],
                textvariable=combobox_textvariable[object],validate=combobox_validate[object],validatecommand=combobox_validatecommand[object],values=combobox_values[object],
                width=combobox_width[object],xscrollcommand=combobox_xscrollcommand[object])
                
                combobox.grid(
                cnf=combobox_grid_cnf[object],column=combobox_grid_column[object],columnspan=combobox_grid_columnspan[object],row=combobox_grid_row[object],
                rowspan=combobox_grid_rowspawn[object],ipadx=combobox_grid_ipadx[object],ipady=combobox_grid_ipady[object],padx=combobox_grid_padx[object],
                pady=combobox_grid_pady[object],sticky=combobox_grid_sticky[object],in_=combobox_grid_in_[object])

                combobox_objects.append(combobox)

                progressbar = ttkb.Progressbar(
                master=container,class_=progressbar_class_[object],cursor=progressbar_cursor[object],length=progressbar_length[object],
                maximum=progressbar_maximum[object],mode=progressbar_mode [object],name=progressbar_name[object],orient=progressbar_orient[object],
                phase=progressbar_phase[object],style=progressbar_style[object],takefocus=progressbar_takefocus[object],value=progressbar_value[object],
                variable=progressbar_variable[object],bootstyle=progressbar_bootstyle[object])
                
                progressbar.grid(
                cnf=progressbar_grid_cnf[object],column=progressbar_grid_column[object],columnspan=progressbar_grid_columnspan[object],row=progressbar_grid_row[object],
                rowspan=progressbar_grid_rowspawn[object],ipadx=progressbar_grid_ipadx[object],ipady=progressbar_grid_ipady[object],padx=progressbar_grid_padx[object],
                pady=progressbar_grid_pady[object],sticky=progressbar_grid_sticky[object],in_=progressbar_grid_in_[object])

                progressbar_objects.append(progressbar)

            return container, button_objects, combobox_objects, progressbar_objects
        
        else:

            for object in range(grid_count):

                button=ttkb.Button(
                master=master_container,class_=button_class_[object],command=button_command[object],compound=button_compound[object],
                cursor=button_cursor[object],default=button_default[object],image=button_image[object],name=button_name[object],
                padding=button_padding[object],state=button_state[object],style=button_style[object],takefocus=button_takefocus[object],
                text=button_text[object],textvariable=button_textvariable[object],underline=button_underline[object],width=button_width[object],
                bootstyle=button_bootstyle[object])
                
                button.grid(
                cnf=button_grid_cnf[object],column=button_grid_column[object],columnspan=button_grid_columnspan[object],row=button_grid_row[object],
                rowspan=button_grid_rowspawn[object],ipadx=button_grid_ipadx[object],ipady=button_grid_ipady[object],padx=button_grid_padx[object],
                pady=button_grid_pady[object],sticky=button_grid_sticky[object],in_=button_grid_in_[object])

                button_objects.append(button)

                combobox = ttkb.Combobox(
                master=master_container,background=combobox_background[object],class_=combobox_class_[object],cursor=combobox_cursor[object],
                exportselection=combobox_exportselection[object],font=combobox_font[object],foreground=combobox_foreground[object],height=combobox_height[object],
                invalidcommand=combobox_invalidcommand[object],justify=combobox_justify[object],name=combobox_name[object],postcommand=combobox_postcommand[object],
                show=combobox_show[object],state=combobox_state[object],style=combobox_style[object],takefocus=combobox_takefocus[object],
                textvariable=combobox_textvariable[object],validate=combobox_validate[object],validatecommand=combobox_validatecommand[object],values=combobox_values[object],
                width=combobox_width[object],xscrollcommand=combobox_xscrollcommand[object])
                
                combobox.grid(
                cnf=combobox_grid_cnf[object],column=combobox_grid_column[object],columnspan=combobox_grid_columnspan[object],row=combobox_grid_row[object],
                rowspan=combobox_grid_rowspawn[object],ipadx=combobox_grid_ipadx[object],ipady=combobox_grid_ipady[object],padx=combobox_grid_padx[object],
                pady=combobox_grid_pady[object],sticky=combobox_grid_sticky[object],in_=combobox_grid_in_[object])

                combobox_objects.append(combobox)

                progressbar = ttkb.Progressbar(
                master=master_container,class_=progressbar_class_[object],cursor=progressbar_cursor[object],length=progressbar_length[object],
                maximum=progressbar_maximum[object],mode=progressbar_mode [object],name=progressbar_name[object],orient=progressbar_orient[object],
                phase=progressbar_phase[object],style=progressbar_style[object],takefocus=progressbar_takefocus[object],value=progressbar_value[object],
                variable=progressbar_variable[object],bootstyle=progressbar_bootstyle[object])
                
                progressbar.grid(
                cnf=progressbar_grid_cnf[object],column=progressbar_grid_column[object],columnspan=progressbar_grid_columnspan[object],row=progressbar_grid_row[object],
                rowspan=progressbar_grid_rowspawn[object],ipadx=progressbar_grid_ipadx[object],ipady=progressbar_grid_ipady[object],padx=progressbar_grid_padx[object],
                pady=progressbar_grid_pady[object],sticky=progressbar_grid_sticky[object],in_=progressbar_grid_in_[object])

                progressbar_objects.append(progressbar)

            return master_container, button_objects, combobox_objects, progressbar_objects
        
    def create_button_label_entry_grid(self,
        
        grid_count = None,
        master_container = None,
        recreate = False,
        
        container_border=None,container_borderwidth=None,container_class=None,container_cursor=None,
        container_height=None,container_name=None,container_padding=None,container_relief=None,
        container_style=None,container_takefocus=None,container_width=None,

        container_pack_cnf=None,container_pack_after=None,container_pack_anchor=None,container_pack_before=None,
        container_pack_expand=None,container_pack_fill=None,container_pack_side=None,container_pack_ipadx=None,
        container_pack_ipady=None,container_pack_padx=None,container_pack_pady=None,container_pack_in_=None,
        
        button_class_=[None],button_command=[None],button_compound=[None],button_cursor=[None],
        button_default=[None],button_image=[None],button_name=[None],button_padding=[None],
        button_state=[None],button_style=[None],button_takefocus=[None],button_text=[None],
        button_textvariable=[None],button_underline=[None],button_width=[None],button_bootstyle=[None],
        
        button_grid_cnf=[None],button_grid_column=[None],button_grid_columnspan=[None],button_grid_row=[None],
        button_grid_rowspawn=[None],button_grid_ipadx=[None],button_grid_ipady=[None], button_grid_padx=[None],
        button_grid_pady=[None],button_grid_sticky=[None],button_grid_in_=[None],

        label_anchor=[None],label_background=[None],label_border=[None],label_borderwidth=[None],
        label_class_=[None],label_compound=[None],label_cursor=[None],label_font=[None],label_foreground=[None],
        label_image=[None],label_justify=[None],label_name=[None],label_padding=[None],label_relief=[None],
        label_state=[None],label_style=[None], label_takefocus=[None],label_text=[None],label_textvariable=[None],
        label_underline=[None],label_width=[None],label_wraplength=[None],

        label_grid_cnf=[None],label_grid_column=[None],label_grid_columnspan=[None],label_grid_row=[None],
        label_grid_rowspawn=[None],label_grid_ipadx=[None],label_grid_ipady=[None],label_grid_padx=[None],
        label_grid_pady=[None],label_grid_sticky=[None],label_grid_in_=[None],
        
        entry_background=[None],entry_class_=[None],entry_cursor=[None],entry_exportselection=[None],
        entry_font=[None],entry_foreground=[None],entry_invalidcommand=[None],entry_justify=[None],
        entry_name=[None],entry_show=[None],entry_state=[None],entry_style=[None],
        entry_takefocus=[None],entry_textvariable=[None],entry_validate=[None],entry_validatecommand=[None],
        entry_width=[None],entry_xscrollcommand=[None],

        entry_grid_cnf=[None],entry_grid_column=[None],entry_grid_columnspan=[None],entry_grid_row=[None],
        entry_grid_rowspawn=[None],entry_grid_ipadx=[None],entry_grid_ipady=[None],entry_grid_padx=[None],
        entry_grid_pady=[None],entry_grid_sticky=[None],entry_grid_in_=[None]):
        
        button_objects = []
        label_objects = []
        entry_objects = []
        
        if recreate == False:
            
            container=ttkb.Frame(
            master=self,border=container_border,borderwidth=container_borderwidth,class_=container_class,
            cursor=container_cursor,height=container_height,name=container_name,padding=container_padding,
            relief=container_relief,style=container_style,takefocus=container_takefocus,width=container_width)

            container.pack(
            cnf=container_pack_cnf,after=container_pack_after,anchor=container_pack_anchor,before=container_pack_before,
            expand=container_pack_expand,fill=container_pack_fill,side=container_pack_side,ipadx=container_pack_ipadx,
            ipady=container_pack_ipady,padx=container_pack_padx,pady=container_pack_pady,in_=container_pack_in_)
            
            for object in range(grid_count):
                
                button=ttkb.Button(
                master=container,class_=button_class_[object],command=button_command[object],compound=button_compound[object],
                cursor=button_cursor[object],default=button_default[object],image=button_image[object],name=button_name[object],
                padding=button_padding[object],state=button_state[object],style=button_style[object],takefocus=button_takefocus[object],
                text=button_text[object],textvariable=button_textvariable[object],underline=button_underline[object],width=button_width[object],
                bootstyle=button_bootstyle[object])
                
                button.grid(
                cnf=button_grid_cnf[object],column=button_grid_column[object],columnspan=button_grid_columnspan[object],row=button_grid_row[object],
                rowspan=button_grid_rowspawn[object],ipadx=button_grid_ipadx[object],ipady=button_grid_ipady[object],padx=button_grid_padx[object],
                pady=button_grid_pady[object],sticky=button_grid_sticky[object],in_=button_grid_in_[object])

                button_objects.append(button)

                label = ttkb.Label(
                master=container,anchor=label_anchor[object],background=label_background[object],border=label_border[object],
                borderwidth=label_borderwidth[object],class_=label_class_[object],compound=label_compound[object],cursor=label_cursor[object],
                font=label_font[object],foreground=label_foreground[object],image=label_image[object],justify=label_justify[object],
                name=label_name[object],padding=label_padding[object],relief=label_relief[object],state=label_state[object],
                style=label_style[object],takefocus=label_takefocus[object],text=label_text[object],textvariable=label_textvariable[object],
                underline=label_underline[object],width=label_width[object],wraplength=label_wraplength[object])

                label.grid(
                cnf=label_grid_cnf[object],column=label_grid_column[object],columnspan=label_grid_columnspan[object],row=label_grid_row[object],
                rowspan=label_grid_rowspawn[object],ipadx=label_grid_ipadx[object],ipady=label_grid_ipady[object],padx=label_grid_padx[object],
                pady=label_grid_pady[object],sticky=label_grid_sticky[object],in_= label_grid_in_[object])

                label_objects.append(label)

                entry = ttkb.Entry(
                master=container,background=entry_background[object],class_=entry_class_[object],cursor=entry_cursor[object],
                exportselection=entry_exportselection[object],font=entry_font[object],foreground=entry_foreground[object],invalidcommand=entry_invalidcommand[object],
                justify=entry_justify[object],name=entry_name[object],show=entry_show[object],state=entry_state[object],
                style=entry_style[object],takefocus=entry_takefocus[object],textvariable=entry_textvariable[object],validate=entry_validate[object],
                validatecommand=entry_validatecommand[object],width=entry_width[object],xscrollcommand=entry_xscrollcommand[object])

                entry.grid(
                cnf=entry_grid_cnf[object],column=entry_grid_column[object],columnspan=entry_grid_columnspan[object],row=entry_grid_row[object],
                rowspan=entry_grid_rowspawn[object],ipadx=entry_grid_ipadx[object],ipady=entry_grid_ipady[object],padx=entry_grid_padx[object],
                pady=entry_grid_pady[object],sticky=entry_grid_sticky[object],in_=entry_grid_in_[object])

                entry_objects.append(entry)

            return container, button_objects, label_objects, entry_objects
        
        else:

            for object in range(grid_count):

                button=ttkb.Button(
                master=master_container,class_=button_class_[object],command=button_command[object],compound=button_compound[object],
                cursor=button_cursor[object],default=button_default[object],image=button_image[object],name=button_name[object],
                padding=button_padding[object],state=button_state[object],style=button_style[object],takefocus=button_takefocus[object],
                text=button_text[object],textvariable=button_textvariable[object],underline=button_underline[object],width=button_width[object],
                bootstyle=button_bootstyle[object])
                
                button.grid(
                cnf=button_grid_cnf[object],column=button_grid_column[object],columnspan=button_grid_columnspan[object],row=button_grid_row[object],
                rowspan=button_grid_rowspawn[object],ipadx=button_grid_ipadx[object],ipady=button_grid_ipady[object],padx=button_grid_padx[object],
                pady=button_grid_pady[object],sticky=button_grid_sticky[object],in_=button_grid_in_[object])

                button_objects.append(button)

                label = ttkb.Label(
                master=master_container,anchor=label_anchor[object],background=label_background[object],border=label_border[object],
                borderwidth=label_borderwidth[object],class_=label_class_[object],compound=label_compound[object],cursor=label_cursor[object],
                font=label_font[object],foreground=label_foreground[object],image=label_image[object],justify=label_justify[object],
                name=label_name[object],padding=label_padding[object],relief=label_relief[object],state=label_state[object],
                style=label_style[object],takefocus=label_takefocus[object],text=label_text[object],textvariable=label_textvariable[object],
                underline=label_underline[object],width=label_width[object],wraplength=label_wraplength[object])

                label.grid(
                cnf=label_grid_cnf[object],column=label_grid_column[object],columnspan=label_grid_columnspan[object],row=label_grid_row[object],
                rowspan=label_grid_rowspawn[object],ipadx=label_grid_ipadx[object],ipady=label_grid_ipady[object],padx=label_grid_padx[object],
                pady=label_grid_pady[object],sticky=label_grid_sticky[object],in_= label_grid_in_[object])

                label_objects.append(label)

                entry = ttkb.Entry(
                master=master_container,background=entry_background[object],class_=entry_class_[object],cursor=entry_cursor[object],
                exportselection=entry_exportselection[object],font=entry_font[object],foreground=entry_foreground[object],invalidcommand=entry_invalidcommand[object],
                justify=entry_justify[object],name=entry_name[object],show=entry_show[object],state=entry_state[object],
                style=entry_style[object],takefocus=entry_takefocus[object],textvariable=entry_textvariable[object],validate=entry_validate[object],
                validatecommand=entry_validatecommand[object],width=entry_width[object],xscrollcommand=entry_xscrollcommand[object])

                entry.grid(
                cnf=entry_grid_cnf[object],column=entry_grid_column[object],columnspan=entry_grid_columnspan[object],row=entry_grid_row[object],
                rowspan=entry_grid_rowspawn[object],ipadx=entry_grid_ipadx[object],ipady=entry_grid_ipady[object],padx=entry_grid_padx[object],
                pady=entry_grid_pady[object],sticky=entry_grid_sticky[object],in_=entry_grid_in_[object])

                entry_objects.append(entry)

            return master_container, button_objects, label_objects, entry_objects
                         
    def create_frame_label_grid(self,
        
        master_container = None,
        grid_count = None,
        recreate = False,

        container_border=None,container_borderwidth=None,container_class=None,container_cursor=None,
        container_height=None,container_name=None,container_padding=None,container_relief=None,
        container_style=None,container_takefocus=None,container_width=None,

        container_pack_cnf=None,container_pack_after=None,container_pack_anchor=None,container_pack_before=None,
        container_pack_expand=None,container_pack_fill=None,container_pack_side=None,container_pack_ipadx=None,
        container_pack_ipady=None,container_pack_padx=None,container_pack_pady=None,container_pack_in_=None,

        sub_container_border=[None],sub_container_borderwidth=[None],sub_container_class=[None],sub_container_cursor=[None],
        sub_container_height=[None],sub_container_name=[None],sub_container_padding=[None],sub_container_relief=[None],
        sub_container_style=[None],sub_container_takefocus=[None],sub_container_width=[None],

        sub_container_grid_cnf=[None],sub_container_grid_column=[None],sub_container_grid_columnspan=[None],sub_container_grid_row=[None],
        sub_container_grid_rowspawn=[None],sub_container_grid_ipadx=[None],sub_container_grid_ipady=[None],sub_container_grid_padx=[None],
        sub_container_grid_pady=[None],sub_container_grid_sticky=[None],sub_container_grid_in_=[None],
        
        label_anchor=[None],label_background=[None],label_border=[None],label_borderwidth=[None],
        label_class_=[None],label_compound=[None],label_cursor=[None],label_font=[None],label_foreground=[None],
        label_image=[None],label_justify=[None],label_name=[None],label_padding=[None],label_relief=[None],
        label_state=[None],label_style=[None], label_takefocus=[None],label_text=[None],label_textvariable=[None],
        label_underline=[None],label_width=[None],label_wraplength=[None],

        label_grid_cnf=[None],label_grid_column=[None],label_grid_columnspan=[None],label_grid_row=[None],
        label_grid_rowspawn=[None],label_grid_ipadx=[None],label_grid_ipady=[None],label_grid_padx=[None],
        label_grid_pady=[None],label_grid_sticky=[None],label_grid_in_=[None]):

        sub_container_objects = []
        label_objects = []
        
        if recreate == False:
            
            container=ttkb.Frame(
            master=self,border=container_border,borderwidth=container_borderwidth,class_=container_class,
            cursor=container_cursor,height=container_height,name=container_name,padding=container_padding,
            relief=container_relief,style=container_style,takefocus=container_takefocus,width=container_width)

            container.pack(
            cnf=container_pack_cnf,after=container_pack_after,anchor=container_pack_anchor,before=container_pack_before,
            expand=container_pack_expand,fill=container_pack_fill,side=container_pack_side,ipadx=container_pack_ipadx,
            ipady=container_pack_ipady,padx=container_pack_padx,pady=container_pack_pady,in_=container_pack_in_)

            for object in range(grid_count):

                sub_container=ttkb.Frame(
                master=container,border=sub_container_border[object],borderwidth=sub_container_borderwidth[object],class_=sub_container_class[object],
                cursor=sub_container_cursor[object],height=sub_container_height[object],name=sub_container_name[object],padding=sub_container_padding[object],
                relief=sub_container_relief[object],style=sub_container_style[object],takefocus=sub_container_takefocus[object],width=sub_container_width[object])

                sub_container.grid(
                cnf=sub_container_grid_cnf[object],column=sub_container_grid_column[object],columnspan=sub_container_grid_columnspan[object],row=sub_container_grid_row[object],
                rowspan=sub_container_grid_rowspawn[object],ipadx=sub_container_grid_ipadx[object],ipady=sub_container_grid_ipady[object],padx=sub_container_grid_padx[object],
                pady=sub_container_grid_pady[object],sticky=sub_container_grid_sticky[object],in_= sub_container_grid_in_[object])
                
                sub_container_objects.append(sub_container)

                label = ttkb.Label(
                master=sub_container,anchor=label_anchor[object],background=label_background[object],border=label_border[object],
                borderwidth=label_borderwidth[object],class_=label_class_[object],compound=label_compound[object],cursor=label_cursor[object],
                font=label_font[object],foreground=label_foreground[object],image=label_image[object],justify=label_justify[object],
                name=label_name[object],padding=label_padding[object],relief=label_relief[object],state=label_state[object],
                style=label_style[object],takefocus=label_takefocus[object],text=label_text[object],textvariable=label_textvariable[object],
                underline=label_underline[object],width=label_width[object],wraplength=label_wraplength[object])

                label.grid(
                cnf=label_grid_cnf[object],column=label_grid_column[object],columnspan=label_grid_columnspan[object],row=label_grid_row[object],
                rowspan=label_grid_rowspawn[object],ipadx=label_grid_ipadx[object],ipady=label_grid_ipady[object],padx=label_grid_padx[object],
                pady=label_grid_pady[object],sticky=label_grid_sticky[object],in_= label_grid_in_[object])

            return container, sub_container_objects, label_objects

        else:

            for object in range(grid_count):

                sub_container=ttkb.Frame(
                master=master_container,border=sub_container_border[object],borderwidth=sub_container_borderwidth[object],class_=sub_container_class[object],
                cursor=sub_container_cursor[object],height=sub_container_height[object],name=sub_container_name[object],padding=sub_container_padding[object],
                relief=sub_container_relief[object],style=sub_container_style[object],takefocus=sub_container_takefocus[object],width=sub_container_width[object])

                sub_container.grid(
                cnf=sub_container_grid_cnf[object],column=sub_container_grid_column[object],columnspan=sub_container_grid_columnspan[object],row=sub_container_grid_row[object],
                rowspan=sub_container_grid_rowspawn[object],ipadx=sub_container_grid_ipadx[object],ipady=sub_container_grid_ipady[object],padx=sub_container_grid_padx[object],
                pady=sub_container_grid_pady[object],sticky=sub_container_grid_sticky[object],in_= sub_container_grid_in_[object])
                
                sub_container_objects.append(sub_container)

                label = ttkb.Label(
                master=sub_container,anchor=label_anchor[object],background=label_background[object],border=label_border[object],
                borderwidth=label_borderwidth[object],class_=label_class_[object],compound=label_compound[object],cursor=label_cursor[object],
                font=label_font[object],foreground=label_foreground[object],image=label_image[object],justify=label_justify[object],
                name=label_name[object],padding=label_padding[object],relief=label_relief[object],state=label_state[object],
                style=label_style[object],takefocus=label_takefocus[object],text=label_text[object],textvariable=label_textvariable[object],
                underline=label_underline[object],width=label_width[object],wraplength=label_wraplength[object])

                label.grid(
                cnf=label_grid_cnf[object],column=label_grid_column[object],columnspan=label_grid_columnspan[object],row=label_grid_row[object],
                rowspan=label_grid_rowspawn[object],ipadx=label_grid_ipadx[object],ipady=label_grid_ipady[object],padx=label_grid_padx[object],
                pady=label_grid_pady[object],sticky=label_grid_sticky[object],in_= label_grid_in_[object])

            return master_container,sub_container_objects,label_objects


    def create_button_progressbar_grid(self,
        
        master_container = None,
        grid_count = None,

        container_border=[None],container_borderwidth=[None],container_class=[None],container_cursor=[None],
        container_height=[None],container_name=[None],container_padding=[None],container_relief=[None],
        container_style=[None],container_takefocus=[None],container_width=[None],

        container_grid_cnf=[None],container_grid_column=[None],container_grid_columnspan=[None],container_grid_row=[None],
        container_grid_rowspawn=[None],container_grid_ipadx=[None],container_grid_ipady=[None],container_grid_padx=[None],
        container_grid_pady=[None],container_grid_sticky=[None],container_grid_in_=[None],

        button_class_=[None],button_command=[None],button_compound=[None],button_cursor=[None],
        button_default=[None],button_image=[None],button_name=[None],button_padding=[None],
        button_state=[None],button_style=[None],button_takefocus=[None],button_text=[None],
        button_textvariable=[None],button_underline=[None],button_width=[None],button_bootstyle=[None],
        
        button_grid_cnf=[None],button_grid_column=[None],button_grid_columnspan=[None],button_grid_row=[None],
        button_grid_rowspawn=[None],button_grid_ipadx=[None],button_grid_ipady=[None], button_grid_padx=[None],
        button_grid_pady=[None],button_grid_sticky=[None],button_grid_in_=[None],

        progressbar_class_=[None],progressbar_cursor=[None],progressbar_length=[None],progressbar_maximum=[None],
        progressbar_mode =[None],progressbar_name=[None],progressbar_orient=[None],progressbar_phase=[None],
        progressbar_style=[None],progressbar_takefocus=[None],progressbar_value=[None],progressbar_variable=[None],
        progressbar_bootstyle=[None],
        
        progressbar_grid_cnf=[None],progressbar_grid_column=[None],progressbar_grid_columnspan=[None],progressbar_grid_row=[None],
        progressbar_grid_rowspawn=[None],progressbar_grid_ipadx=[None],progressbar_grid_ipady=[None],progressbar_grid_padx=[None],
        progressbar_grid_pady=[None],progressbar_grid_sticky=[None],progressbar_grid_in_=[None]):

        container_objects = []
        button_objects = []
        progressbar_objects = []

        for object in range(grid_count):

            container=ttkb.Frame(
            master=master_container,border=container_border[object],borderwidth=container_borderwidth[object],class_=container_class[object],
            cursor=container_cursor[object],height=container_height[object],name=container_name[object],padding=container_padding[object],
            relief=container_relief[object],style=container_style[object],takefocus=container_takefocus[object],width=container_width[object])

            container.grid(
            cnf=container_grid_cnf[object],column=container_grid_column[object],columnspan=container_grid_columnspan[object],row=container_grid_row[object],
            rowspan=container_grid_rowspawn[object],ipadx=container_grid_ipadx[object],ipady=container_grid_ipady[object],padx=container_grid_padx[object],
            pady=container_grid_pady[object],sticky=container_grid_sticky[object],in_=container_grid_in_[object])
            
            container_objects.append(container)

            button=ttkb.Button(
            master=container,class_=button_class_[object],command=button_command[object],compound=button_compound[object],
            cursor=button_cursor[object],default=button_default[object],image=button_image[object],name=button_name[object],
            padding=button_padding[object],state=button_state[object],style=button_style[object],takefocus=button_takefocus[object],
            text=button_text[object],textvariable=button_textvariable[object],underline=button_underline[object],width=button_width[object],
            bootstyle=button_bootstyle[object])
            
            button.grid(
            cnf=button_grid_cnf[object],column=button_grid_column[object],columnspan=button_grid_columnspan[object],row=button_grid_row[object],
            rowspan=button_grid_rowspawn[object],ipadx=button_grid_ipadx[object],ipady=button_grid_ipady[object],padx=button_grid_padx[object],
            pady=button_grid_pady[object],sticky=button_grid_sticky[object],in_=button_grid_in_[object])

            button_objects.append(button)

            progressbar=ttkb.Progressbar(
            master=container,class_=progressbar_class_[object],cursor=progressbar_cursor[object],length=progressbar_length[object],
            maximum=progressbar_maximum[object],mode=progressbar_mode [object],name=progressbar_name[object],orient=progressbar_orient[object],
            phase=progressbar_phase[object],style=progressbar_style[object],takefocus=progressbar_takefocus[object],value=progressbar_value[object],
            variable=progressbar_variable[object],bootstyle=progressbar_bootstyle[object])
            
            progressbar.grid(
            cnf=progressbar_grid_cnf[object],column=progressbar_grid_column[object],columnspan=progressbar_grid_columnspan[object],row=progressbar_grid_row[object],
            rowspan=progressbar_grid_rowspawn[object],ipadx=progressbar_grid_ipadx[object],ipady=progressbar_grid_ipady[object],padx=progressbar_grid_padx[object],
            pady=progressbar_grid_pady[object],sticky=progressbar_grid_sticky[object],in_=progressbar_grid_in_[object])

            progressbar_objects.append(progressbar)

        return container_objects, button_objects, progressbar_objects