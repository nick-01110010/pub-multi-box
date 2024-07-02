# enb-multi-box

This project is for controlling multiple clients of an old space sim game called “Earth and beyond”. Currently the project is set up to control multiple clients on a single machine, but it can use a remote desktop application such as Microsoft RDP or Parsec if you wanted to run a 1:1 client/machine ratio.

This project spawned from an earlier iteration that I first wrote a few years ago using Auto Hotkey. I decided to rewrite everything in Python to gain access to the amazing modules which the Python language has in abundance. When I started to port the functionality from AHK to Python everything went very smoothly, but I soon started to add more features and ran into quite a bit of scope creep because I wasn’t particularly planning what I wanted to accomplish. I just worked on whatever I was interested in on a given day, so this project is not as tidy as I would like it to be. I am in the process of organizing everything and plan to start working on sections in a more agile-centric manner.

The functionality of the program is set up like tabs in a notebook. The tabs are as follows: **add characters**, **create fleet**, **fleet commands**, **fleet equipment**, **trade items**, and **cv2 images references**.

## Add Characters Tab:

The add characters tab allows for the user to create, edit, and delete characters for a given client and the character account which that client is controlling. It has various inputs such as character name, password, level, etc. The user adds all the characters they want and then moves to the next tab to create a fleet of characters.

## Create Fleet Tab:

The create fleet tab allows for the user to create a fleet of characters that were added to the database via the add characters tab and permits the user to control all the characters as a group on the subsequent fleet commands tab. A fleet must have a name and contain at least two characters with a maximum of six characters, a given fleet also cannot contain multiples of the same character.
  

## Fleet Commands Tab:

The fleet commands tab is the meat and potatoes of this project as it allows the user full control over all of characters in a fleet and the ability control them as a single entity. This tab allows for the user to start all the clients, shutdown and restart individual clients in case one crashes or freezes. There are also hotkeys that can be assigned to group functions, or the user can interact with those functions via a mouse click. This tab also displays all the buffs each character can utilize via an ability or item and provides a time indication for how long a given buff or item duration persists.
  

## Fleet Equipment Tab:

The fleet equipment tab is for creating and changing item sets on the fly for each character in a fleet. I haven’t really worked on this much and still have some planning to do for what this tab will include.
  

## Trade Items Tab:

The trade items tab is for trading items between characters utilizing automation via pyautogui.
  

## CV2 Image References Tab:

The cv2 image references tab allows the user to upload images that will be used as locators at various resolutions so the opencv-python module can identify and interact with elements in the client. I’m currently only going to include the resolutions at which I control the clients 3440x1440 and 800x600, but as some individuals may not have monitors that can operate clients at these resolutions, I opted to allow the user to customize the window geometry for their own clients and system.
