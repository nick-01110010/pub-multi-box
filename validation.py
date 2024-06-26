from ttkbootstrap.constants import*
from ttkbootstrap.validation import *

@validator
def character_name(event, error_label = None):
    if int(event.actioncode) == -1 and len(event.prechangetext) == 0:
        error_label['text'] = 'Character Name cannot be empty'
        error_label.config(style = 'danger.TLabel')

        return False
    else:
        error_label['text'] = ''
        error_label.config(style = 'TLabel')
    
    if len(event.prechangetext) == 0 and len(event.insertdeletetext) >= 1 and str(event.postchangetext[0]).islower():
        error_label['text'] = 'The first letter of Character Name must be capitalized'
        error_label.config(style = 'danger.TLabel')

        return False
    
    elif len(event.prechangetext) >= 0 and len(event.insertdeletetext) >= 1:
        upper_count = 0
        
        for i in range(len(event.insertdeletetext)):
            if str(event.insertdeletetext[i]).isupper():
                upper_count = upper_count + 1
        
        if upper_count > 1:
            error_label['text'] = 'Only the first letter in Character Name can be capitalized'
            error_label.config(style = 'danger.TLabel')

            return False
        
        else:
            error_label['text'] = ''
            error_label.config(style = 'TLabel')
    
    if len(event.insertdeletetext) >= 1:
        if str(event.insertdeletetext).isalpha():
            error_label['text'] = ''
            error_label.config(style = 'TLabel')

        else:
            error_label['text'] = 'Character Name can only contain letters a-z'
            error_label.config(style = 'danger.TLabel')

            return False

    if len(event.prechangetext) >= 1 and str(event.insertdeletetext).islower():
        error_label['text'] = ''
        error_label.config(style = 'TLabel')
    elif str(event.insertdeletetext).isupper() and len(event.prechangetext) == 0:
        error_label['text'] = ''
        error_label.config(style = 'TLabel')
    elif str(event.insertdeletetext).isupper() and len(event.postchangetext) == 0:
        error_label['text'] = ''
        error_label.config(style = 'TLabel')
    elif len(event.prechangetext) >= 1 and str(event.insertdeletetext).isupper():
        error_label['text'] = 'Only the first letter in Character Name can be capitalized'
        error_label.config(style = 'danger.TLabel')

        return False
        
    if len(event.prechangetext) <= 2 and int(event.actioncode) == -1:
        error_label['text'] = 'Character Name length must be 3 or more'
        error_label.config(style = 'danger.TLabel')

        return False
    else:
        error_label['text'] = ''
        error_label.config(style = 'TLabel')

    if len(event.postchangetext) < 20:
        error_label['text'] = ''
        error_label.config(style = 'TLabel')
    else:
        error_label['text'] = 'Character Name length must be 20 or less'
        error_label.config(style = 'danger.TLabel')

        return False

    error_label['text'] = ''
    error_label.config(style = 'TLabel')

    return True

@validator
def character_password(event, error_label = None):
    if int(event.actioncode) == -1 and len(event.prechangetext) == 0:
        error_label['text'] = 'Password cannot be empty'
        error_label.config(style = 'danger.TLabel')

        return False
    else:
        error_label['text'] = ''
        error_label.config(style = 'TLabel')
    
    if len(event.prechangetext) <= 4 and int(event.actioncode) == -1:
        error_label['text'] = 'Password length must be 5 or more'
        error_label.config(style = 'danger.TLabel')

        return False
    else:
        error_label['text'] = ''
        error_label.config(style = 'TLabel')

    if len(event.postchangetext) <= 20:
        error_label['text'] = ''
        error_label.config(style = 'TLabel')
    else:
        error_label['text'] = 'Password length must be 20 or less'
        error_label.config(style = 'danger.TLabel')

        return False

    error_label['text'] = ''
    error_label.config(style = 'TLabel')

    return True

@validator
def character_level(event, error_label = None):
    if int(event.actioncode) == -1 and len(event.prechangetext) == 0:
        error_label['text'] = 'Character Level cannot be empty'
        error_label.config(style = 'danger.TLabel')

        return False
    else:
        error_label['text'] = ''
        error_label.config(style = 'TLabel')
    
    if len(event.insertdeletetext) >= 1:
        if str(event.insertdeletetext).isnumeric():
            error_label['text'] = ''
            error_label.config(style = 'TLabel')

        else:
            error_label['text'] = 'Character Level can only contain numbers 0-9'
            error_label.config(style = 'danger.TLabel')

            return False
    
    if len(event.postchangetext) == 2 and int(event.postchangetext) <= 9:
        error_label['text'] = 'Character Level cannot contain leading 0s'
        error_label.config(style = 'danger.TLabel')

        return False
        
    if len(event.postchangetext) > 2 and int(event.postchangetext) < 100:    
        error_label['text'] = 'Character Level cannot contain leading 0s'
        error_label.config(style = 'danger.TLabel')

        return False
        
    if len(event.postchangetext) > 3 and int(event.actioncode) != 0:
            error_label['text'] = 'Character Level must be between 0-150'
            error_label.config(style = 'danger.TLabel')

            return False
    
    if len(event.postchangetext) >= 1:
        level = float(event.postchangetext)
        result = level >= 0 and level <= 150

        if result == True:
            error_label['text'] = ''
            error_label.config(style = 'TLabel')
        else:
            error_label['text'] = 'Character Level must be between 0-150'
            error_label.config(style = 'danger.TLabel')
            
            return False

    error_label['text'] = ''
    error_label.config(style = 'TLabel')

    return True     

@validator
def character_class(event, current_class, weapon_entry_field = None, device_entry_field = None, error_label = None):
    three_slot_configuration = [1, 2, 3]
    four_slot_configuration = [1, 2, 3, 4]
    five_slot_configuration = [1, 2, 3, 4, 5]
    six_slot_configuration = [1, 2, 3, 4, 5, 6]

    if int(event.actioncode) == -1 and len(event.prechangetext) == 0:
        error_label['text'] = 'Character Class cannot be empty'
        error_label.config(style = 'danger.TLabel')
        weapon_entry_field.config(state = DISABLED, values = [])
        device_entry_field.config(state = DISABLED, values = [])
        
        return False
    else:
        error_label['text'] = ''
        error_label.config(style = 'TLabel')
        weapon_entry_field.config(state = READONLY)
        device_entry_field.config(state = READONLY)
        selected_class = event.postchangetext
          
        match selected_class:
            case 'JD':
                weapon_entry_field.config(state = READONLY, values = five_slot_configuration)
                device_entry_field.config(state = READONLY, values =  four_slot_configuration)

                if current_class.get() != 'JD':
                    weapon_entry_field.set('')
                    device_entry_field.set('')

                current_class.set('JD')
            case 'JE':
                weapon_entry_field.config(state = READONLY, values = three_slot_configuration)
                device_entry_field.config(state = READONLY, values =  six_slot_configuration)

                if current_class.get() != 'JE':
                    weapon_entry_field.set('')
                    device_entry_field.set('')
                    
                current_class.set('JE')
            case 'JS':
                weapon_entry_field.config(state = READONLY, values = four_slot_configuration)
                device_entry_field.config(state = READONLY, values =  five_slot_configuration)

                if current_class.get() != 'JS':
                    weapon_entry_field.set('')
                    device_entry_field.set('')

                current_class.set('JS')
            case 'PP':
                weapon_entry_field.config(state = READONLY, values = five_slot_configuration)
                device_entry_field.config(state = READONLY, values =  four_slot_configuration)

                if current_class.get() != 'PP':
                    weapon_entry_field.set('')
                    device_entry_field.set('')

                current_class.set('PP')
            case 'PS':
                weapon_entry_field.config(state = READONLY, values = four_slot_configuration)
                device_entry_field.config(state = READONLY, values =  five_slot_configuration)

                if current_class.get() != 'PS':
                    weapon_entry_field.set('')
                    device_entry_field.set('')

                current_class.set('PS')
            case 'PW':
                weapon_entry_field.config(state = READONLY, values = six_slot_configuration)
                device_entry_field.config(state = READONLY, values =  three_slot_configuration)

                if current_class.get() != 'PW':
                    weapon_entry_field.set('')
                    device_entry_field.set('')

                current_class.set('PW')
            case 'TE':
                weapon_entry_field.config(state = READONLY, values = five_slot_configuration)
                device_entry_field.config(state = READONLY, values =  four_slot_configuration)

                if current_class.get() != 'TE':
                    weapon_entry_field.set('')
                    device_entry_field.set('')

                current_class.set('TE')
            case 'TS':
                weapon_entry_field.config(state = READONLY, values = four_slot_configuration)
                device_entry_field.config(state = READONLY, values =  five_slot_configuration)
                
                if current_class.get() != 'TS':
                    weapon_entry_field.set('')
                    device_entry_field.set('')

                current_class.set('TS')
            case 'TT':
                weapon_entry_field.config(state = READONLY, values = four_slot_configuration)
                device_entry_field.config(state = READONLY, values =  five_slot_configuration)

                if current_class.get() != 'TT':
                    weapon_entry_field.set('')
                    device_entry_field.set('')

                current_class.set('TT')

        return True

@validator
def character_weapon_slots(event, error_label = None):
    if int(event.actioncode) == -1 and len(event.prechangetext) == 0:
        error_label['text'] = 'Character Weapon Slots cannot be empty'
        error_label.config(style = 'danger.TLabel')
        
        return False
    else:
        error_label['text'] = ''
        error_label.config(style = 'TLabel')
        
        return True
    
@validator
def character_device_slots(event, error_label = None):
    if int(event.actioncode) == -1 and len(event.prechangetext) == 0:
        error_label['text'] = 'Character Device Slots cannot be empty'
        error_label.config(style = 'danger.TLabel')
        
        return False
    else:
        error_label['text'] = ''
        error_label.config(style = 'TLabel')
        
        return True

@validator
def character_fleet_position(event, error_label = None):
    if int(event.actioncode) == -1 and len(event.prechangetext) == 0:
        error_label['text'] = 'Character Fleet Position cannot be empty'
        error_label.config(style = 'danger.TLabel')

        return False
    else:
        error_label['text'] = ''
        error_label.config(style = 'TLabel')

        return True
    
@validator
def fleet_name(event, error_label = None):
    if int(event.actioncode) == -1 and len(event.prechangetext) == 0:
        error_label['text'] = 'Fleet Name cannot be empty'
        error_label.config(style = 'danger.TLabel')

        return False
    else:
        error_label['text'] = ''
        error_label.config(style = 'TLabel')

    if len(event.postchangetext) <= 30:
        error_label['text'] = ''
        error_label.config(style = 'TLabel')
    else:
        error_label['text'] = 'Fleet Name length must be 30 or less'
        error_label.config(style = 'danger.TLabel')

        return False

    error_label['text'] = ''
    error_label.config(style = 'TLabel')

    return True


@validator
def hotkey(event, error_label = None):
    if int(event.actioncode) == -1 and len(event.prechangetext) == 0:
        error_label['text'] = 'Fleet Name cannot be empty'
        error_label.config(style = 'danger.TLabel')

        return False
    else:
        error_label['text'] = ''
        error_label.config(style = 'TLabel')

    if len(event.postchangetext) <= 5:
        error_label['text'] = ''
        error_label.config(style = 'TLabel')
    else:
        error_label['text'] = 'Hotkey length must be 5 or less'
        error_label.config(style = 'danger.TLabel')

        return False

    error_label['text'] = ''
    error_label.config(style = 'TLabel')

    return True