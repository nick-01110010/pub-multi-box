import json
import ctypes

block_input = ctypes.windll.user32.BlockInput

currentWindow = 'Character1'
file_location = 'C:/Program Files (x86)/Net-7/bin/LaunchNet7.exe'
launcher_hwnd_title ='LaunchNet7 v2.2.0'
config_hwnd_title = '    Earth & Beyond Config Version 1.11'
main_window_length = 3440
main_window_height = 1440
side_window_length = 800 
side_window_height = 600
ability_shields_wait = 7
shields_duration = 645

Character1_lo1 = ['good_fortune', 'advanced_weapon_control_system', 'intolerance_mk_viii', 'seal_of_the_dragon', 'dv_ws_x4_roadrunner_mk_viii']
Character2_lo1 = ['good_fortune', 'advanced_weapon_control_system', 'intolerance_mk_viii', 'seal_of_the_dragon', 'chimeras_dread_scourge', 'deadly_focus']
Character3_lo1 = ['good_fortune', 'advanced_weapon_control_system', 'intolerance_mk_viii', 'seal_of_the_dragon']
Character4_lo1 = ['good_fortune', 'advanced_weapon_control_system', 'intolerance_mk_viii', 'seal_of_the_dragon']
Character5_lo1 = ['good_fortune', 'advanced_weapon_control_system', 'intolerance_mk_viii']
Character6_lo1 = ['good_fortune', 'advanced_weapon_control_system', 'intolerance_mk_viii', 'seal_of_the_dragon', 'golden_tooth']


character_data = '''
{
    "character" : 
    {    
        "0" : [
            {
                "name" : "Character1",
                "password" : "password1!",
                "position" : 0,
                "class" : "TT",
                "win_x_pos" : 0,
                "win_y_pos" : 0,
                "win_x_len" : 3440,
                "win_y_len" : 1440
            }
        ],
        "1" : [
            {
                "name" : "Character2",
                "password" : "password1!",
                "position" : 1,
                "class" : "JE",
                "win_x_pos" : 3440,
                "win_y_pos" : 0,
                "win_x_len" : 800,
                "win_y_len" : 600
            }
        ],
        "2" : [
            {
                "name" : "Character3",
                "password" : "password1!",
                "position" : 2,
                "class" : "JD",
                "win_x_pos" : 3440,
                "win_y_pos" : 0,
                "win_x_len" : 800,
                "win_y_len" : 600
            }
        ],
        "3" : [
            {
                "name" : "Character4",
                "password" : "password1!",
                "position" : 3,
                "class" : "TE",
                "win_x_pos" : 3440,
                "win_y_pos" : 0,
                "win_x_len" : 800,
                "win_y_len" : 600
            }
        ],
        "4" : [
            {
                "name" : "Character5",
                "password" : "password1!",
                "position" : 4,
                "class" : "PW",
                "win_x_pos" : 3440,
                "win_y_pos" : 0,
                "win_x_len" : 800,
                "win_y_len" : 600
            }
        ],
        "5" : [
            {
                "name" : "Character6",
                "password" : "password1!",
                "position" : 5,
                "class" : "TS",
                "win_x_pos" : 3440,
                "win_y_pos" : 0,
                "win_x_len" : 800,
                "win_y_len" : 600
            }
        ]
    }
}
'''

main_window_positions = '''
{
    "main_window" : 
    {   "gate_dock" : [
            {
                "x": 3320,
                "y": 965
            }
        ], 
        "login_input" : [
            {
                "x": 820,
                "y": 350
            }
        ],
        "password_input" : [
            {
                "x" : 820,
                "y" : 450
            }
        ],
        "character_slot_one" : [
            {
                "x" : 820,
                "y" : 100
            }
        ],
        "character_slot_two" : [
            {
                "x" : 675,
                "y" : 170
            }
        ],
        "character_slot_three" : [
            {
                "x" : 675,
                "y" : 240
            }
        ],
        "character_slot_four" : [
            {
                "x" : 675,
                "y" : 320
            }
        ],
        "character_slot_five" : [
            {
                "x" : 675,
                "y" : 390
            }
        ],
        "inventory_slot1" : [
            {
                "x" : 165,
                "y" : 630
            }
        ],
        "inventory_slot2" : [
            {
                "x" : 365,
                "y" : 630
            }
        ],
        "inventory_slot3" : [
            {
                "x" : 565,
                "y" : 630
            }
        ],
        "inventory_slot4" : [
            {
                "x" : 165,
                "y" : 740
            }
        ],
        "inventory_slot5" : [
            {
                "x" : 365,
                "y" : 740
            }
        ],
        "inventory_slot6" : [
            {
                "x" : 565,
                "y" : 740
            }
        ],
        "inventory_slot7" : [
            {
                "x" : 165,
                "y" : 850
            }
        ],
        "inventory_slot8" : [
            {
                "x" : 365,
                "y" : 850
            }
        ],
        "inventory_slot9" : [
            {
                "x" : 565,
                "y" : 850
            }
        ],
        "inventory_slot10" : [
            {
                "x" : 165,
                "y" : 960
            }
        ],
        "inventory_slot11" : [
            {
                "x" : 365,
                "y" : 960
            }
        ],
        "inventory_slot12" : [
            {
                "x" : 565,
                "y" : 960
            }
        ],
        "filter_button" : [
            {
                "x" : 230,
                "y" : 530
            }
        ],
        "sort_button" : [
            {
                "x" : 540,
                "y" : 530
            }
        ],
        "inventory_left" : [
            {
                "x" : 95,
                "y" : 1040
            }
        ],
        "inventory_right" : [
            {
                "x" : 635,
                "y" : 1040
            }
        ],
        "weapon_slot1" : [
            {
                "x" : 900,
                "y" : 500
            }
        ],
        "weapon_slot2" : [
            {
                "x" : 900,
                "y" : 615
            }
        ],
        "weapon_slot3" : [
            {
                "x" : 900,
                "y" : 730
            }
        ],
        "weapon_slot4" : [
            {
                "x" : 900,
                "y" : 845
            }
        ],
        "weapon_slot5" : [
            {
                "x" : 900,
                "y" : 960
            }
        ],
        "weapon_slot6" : [
            {
                "x" : 900,
                "y" : 1075
            }
        ],
        "device_slot1" : [
            {
                "x" : 2530,
                "y" : 500
            }
        ],
        "device_slot2" : [
            {
                "x" : 2530,
                "y" : 615
            }
        ],
        "device_slot3" : [
            {
                "x" : 2530,
                "y" : 730
            }
        ],
        "device_slot4" : [
            {
                "x" : 2530,
                "y" : 845
            }
        ],
        "device_slot5" : [
            {
                "x" : 2530,
                "y" : 960
            }
        ],
        "device_slot6" : [
            {
                "x" : 2530,
                "y" : 1075
            }
        ],
        "shield_slot" : [
            {
                "x" : 1290,
                "y" : 1115
            }
        ],
        "reactor_slot" : [
            {
                "x" : 1720,
                "y" : 1115
            }
        ],
        "engine_slot" : [
            {
                "x" : 2150,
                "y" : 1115
            }
        ]
    }
}
'''

side_window_offsets = '''
{
    "side_window" : 
    {
        "login_input" : [
            {
                "x": -610,
                "y": -455
            }
        ],
        "password_input" : [
            {
                "x" : -610,
                "y" : -420
            }
        ],
        "character_slot_one" : [
            {
                "x" : -650,
                "y" : -565
            }
        ],
        "character_slot_two" : [
            {
                "x" : -650,
                "y" : -530
            }
        ],
        "character_slot_three" : [
            {
                "x" : -650,
                "y" : -495
            }
        ],
        "character_slot_four" : [
            {
                "x" : -650,
                "y" : -465
            }
        ],
        "character_slot_five" : [
            {
                "x" : -650,
                "y" : -435
            }
        ],    
        "assist_leader" : [
            {
                "x": -40,
                "y": -240
            }
        ],
        "gate_dock" : [
            {
                "x" : -25,
                "y" : -200
            }
        ],
        "accept_invite" : [
            {
                "x" : -490,
                "y" : -270
            }
        ],
        "reject_invite" : [
            {
                "x" : -310,
                "y" : -270
            }
        ],
        "inventory_slot1" : [
            {
                "x" : -765,
                "y" : -345
            }
        ],
        "inventory_slot2" : [
            {
                "x" : -715,
                "y" : -345
            }
        ],
        "inventory_slot3" : [
            {
                "x" : -665,
                "y" : -345
            }
        ],
        "inventory_slot4" : [
            {
                "x" : -765,
                "y" : -300
            }
        ],
        "inventory_slot5" : [
            {
                "x" : -715,
                "y" : -300
            }
        ],
        "inventory_slot6" : [
            {
                "x" : -665,
                "y" : -300
            }
        ],
        "inventory_slot7" : [
            {
                "x" : -765,
                "y" : -255
            }
        ],
        "inventory_slot8" : [
            {
                "x" : -715,
                "y" : -255
            }
        ],
        "inventory_slot9" : [
            {
                "x" : -665,
                "y" : -255
            }
        ],
        "inventory_slot10" : [
            {
                "x" : -765,
                "y" : -210
            }
        ],
        "inventory_slot11" : [
            {
                "x" : -715,
                "y" : -210
            }
        ],
        "inventory_slot12" : [
            {
                "x" : -665,
                "y" : -210
            }
        ],
        "filter_button" : [
            {
                "x" : -750,
                "y" : -380
            }
        ],
        "sort_button" : [
            {
                "x" : -675,
                "y" : -380
            }
        ],
        "inventory_left" : [
            {
                "x" : -780,
                "y" : -170
            }
        ],
        "inventory_right" : [
            {
                "x" : -650,
                "y" : -170
            }
        ],
        "weapon_slot1" : [
            {
                "x" : -590,
                "y" : -390
            }
        ],
        "weapon_slot2" : [
            {
                "x" : -590,
                "y" : -345
            }
        ],
        "weapon_slot3" : [
            {
                "x" : -590,
                "y" : -300
            }
        ],
        "weapon_slot4" : [
            {
                "x" : -590,
                "y" : -255
            }
        ],
        "weapon_slot5" : [
            {
                "x" : -590,
                "y" : -210
            }
        ],
        "weapon_slot6" : [
            {
                "x" : -590,
                "y" : -165
            }
        ],
        "device_slot1" : [
            {
                "x" : -210,
                "y" : -390
            }
        ],
        "device_slot2" : [
            {
                "x" : -210,
                "y" : -345
            }
        ],
        "device_slot3" : [
            {
                "x" : -210,
                "y" : -300
            }
        ],
        "device_slot4" : [
            {
                "x" : -210,
                "y" : -255
            }
        ],
        "device_slot5" : [
            {
                "x" : -210,
                "y" : -210
            }
        ],
        "device_slot6" : [
            {
                "x" : -210,
                "y" : -165
            }
        ],
        "shield_slot" : [
            {
                "x" : -500,
                "y" : -135
            }
        ],
        "reactor_slot" : [
            {
                "x" : -400,
                "y" : -135
            }
        ],
        "engine_slot" : [
            {
                "x" : -300,
                "y" : -135
            }
        ]
    }
}
'''
character_data_json = json.loads(character_data)
main_window_positions_json = json.loads(main_window_positions)
side_window_offsets_json = json.loads(side_window_offsets)