#!/usr/bin/python
###################################################################################
#                                  VER dev                                        #
 #                                                                                #
 #      Permission is granted to anyone to use this software for any purpose,     #
 #     excluding commercial applications, and to alter it and redistribute it     #
 #               freely, subject to the following restrictions:                   #
 #                                                                                #
 #    1. The origin of this software must not be misrepresented; you must not     #
 #    claim that you wrote the original software. If you use this software        #
 #    in a product, an acknowledgment in the product documentation is required.   #
 #                                                                                #
 #    2. Altered source versions must be plainly marked as such, and must not be  #
 #    misrepresented as being the original software.                              #
 #                                                                                #
 #    3. This notice may not be removed or altered from any source                #
 #    distribution.                                                               #
 #                                                                                #
 #                                                                                #
 #  ==Created by Colton (Brandon) S. (@Coltonton) for the OpenPilot Community===  #
 #              === http://endoflinetech.com/eon-custom-themes ===                #
 #                                                                                #
 #              With a mission to rid all EONS of Comma.ai branding               #
 #             And give the people the freedom, knowlage, and power!              #
 #                         & to make their EONS purdy!                            #
 #                                                                                #
 #                         Grab life by the horns                                 #
 #                                                                                 #
 #   A very special thank you to @ShaneSmiskol for creating the theme picker      #
 #      for his tireless help, and donating the life of his LeEco EON             #
 #           to get the LeEco based EONs supported by this project                #
 #                   Although revived least we forget.....                        #
 ##################################################################################
 #                                                                                #
 #                     To Get Started Making Your EON Purdy:                      #
 #                                                                                #
 #                              SSH into your EON:                                #
 #https://github.com/commaai/openpilot/wiki/SSH#option-3---githubs-official-instructions#                               #
 #                                                                                #
 #              Type the following command if using the main project              #
 #                  exec /data/eon-custom-themes/theme_install.py                 #

 #                                                                                #
 #               Now follow the prompts and make your selections!                 #
 #                  Everything will be done automagically!!!!!                    #
 #                                                                                #
 #                      Don't forget to tell your friends!!                       #
 #                           Love, Cole (@Coltonton)                              #
 #                                                                                #
 #    Did you know that soontm if you have a custom OP fork you can use this      #
 #      program to auto install your custom theme for your users automagiclly?    #
 #                    And incorparate it into your OP Fork?                       #
 #                                                                                #
##################################################################################
import time, os
from os import path
from support.support_functions import * 
from support.support_variables import *

######################################################################################################
##======================= CODE START ================================================================#
######################################################################################################
os.chdir(os.path.dirname(os.path.realpath(__file__)))  # __file__ is safer since it doesn't change based on where this file is called from

print_text(WELCOME_TEXT)                  # Print welcome text with the flag for self welcome text
DebugPrint("VERBOSE MODE ON")             # Notify if Verbosity Mode is on, DebugPrints only run in dev or verbose mode
DEV_CHECK()                               # Check if running on unsupported PC/MAC
OpInfo = dict                             # Init OPInfo Dict
DeviceData = get_device_theme_data()      # Init Device Data dict with device info

class ThemeInstaller:
    def __init__(self):                   # Init code runs once. sets up & determines if to run auto or self
        #get_running()                     # Get Running Process
        self.start_loop()                 # Do self install theme git                                             # Terminate program

    def start_loop(self):                 # Self Installer loop
        # Create Backup folder(if nonexistant) and Create session backup and get location
        self.backup_dir = make_backup_folder()

        #Main Program (loop)
        while 1:
            # Auto discover themes and let user choose!
            self.selected_theme = get_aval_themes()  
            if self.selected_theme == 'debug' and VERBOSE == False:
                VERBOSE == True
                DebugPrint("Debug Level Verbose On!")
            elif self.selected_theme == 'debug' and VERBOSE == True:
                VERBOSE = False 
                DebugPrint("Debug Level Verbose Off!", 1) 
            if self.selected_theme is None:
                print('Didn\'t select a valid theme, exiting.')
                return
            
            # Check what assets are available for the selected theme
            self.get_available_options()

            #Goto Installer
            if self.install_function() == 'exit':
                return

    def get_available_options(self):      # Check what assets are available for the selected theme
        self.theme_options = []
        # Check if the selected theme has a boot logo asset
        if os.path.exists('{}/{}/{}'.format(CONTRIB_THEMES, self.selected_theme, DeviceData["BOOT_LOGO_THEME_PATH"])):
            self.theme_options.append('Boot Logo')
        # Check if the selected theme has a boot annimation asset
        if os.path.exists('{}/{}/bootanimation.zip'.format(CONTRIB_THEMES, self.selected_theme)):
            self.theme_options.append('Boot Animation')
        # Check if the selected theme has a color boot annimation asset
        if os.path.exists('{}/{}/color_bootanimation.zip'.format(CONTRIB_THEMES, self.selected_theme)):
            self.theme_options.append('Color Boot Animation')
        # Check if the selected theme has a white boot annimation asset
        if os.path.exists('{}/{}/white_bootanimation.zip'.format(CONTRIB_THEMES, self.selected_theme)):
            self.theme_options.append('White Boot Animation')
        # Check if the selected theme has a OpenPilot Spinner asset
        if os.path.exists('{}/{}/spinner'.format(CONTRIB_THEMES, self.selected_theme)) :
            self.theme_options.append('OpenPilot Spinner')

        self.theme_options.append('-Main Menu-')
        self.theme_options.append('-Reboot-')
        self.theme_options.append('-Quit-')

    def install_function(self):           # Self installer program, prompts user on what they want to do
        while 1:
            theme_types = list(self.theme_options)  # this only contains available options from self.get_available_options
            if not len(theme_types):
                print('\n*\nThe selected theme has no resources available for your device! Try another.')
                time.sleep(2)
                return
        
            #Ask users what resources to install
            print('\n*\nWhat resources do you want to install for the {} theme?'.format(self.selected_theme))
            print("NEW! Use commas to seperate multiple selections ex '1,2' for option 1 & 2")
            for idx, theme in enumerate(theme_types):
                print('{}. {}'.format(idx + 1, theme))
            indexChoice = input("Enter Index Value: ")
            indexChoice.replace(" ", "")
            indexChoiceList = indexChoice.split(",")

            selected_option_list= []
            for x in range(len(indexChoiceList)):
                runOne = int(indexChoiceList[x])
                selected_option_list.append(self.theme_options[runOne-1])

            # Some logic that only allows one boot animation to be installed 
            onlyOneBootAnimation = []
            for y in range(len(selected_option_list)):                     # Enumerate through list
                if selected_option_list[y] in VALID_BOOT_ANIMATIONS:       # If current item is a Valid Boot Animation selection
                    onlyOneBootAnimation.append(selected_option_list[y])   # Add to a new list to keep track
            if len(onlyOneBootAnimation) > 1:                              # If there was more then one selection
                for z in range(len(onlyOneBootAnimation)):                   # Enumerate through said new list and 
                    selected_option_list.remove(onlyOneBootAnimation[z])     # remove all boot animation selelctions
                while True:
                    print("\n*\nOnly one boot animation is permitted to install, please select for {} theme.".format(self.selected_theme))
                    for idx, theme in enumerate(onlyOneBootAnimation):       # Enumerate multiple boot animation list
                        print('{}. {}'.format(idx + 1, theme))               # Print to screen
                    realAnimationChoice = int(input("Enter Index Value: "))  # Ask user to select one
                    if realAnimationChoice <= len(onlyOneBootAnimation):     # User input was valid
                        selected_option_list.append(onlyOneBootAnimation[realAnimationChoice-1]) # Add their selection to the stack!! 
                        break
                    else:                                                        # User input was not valid
                        print("Invalid Index... Try Again...")

            # Some logic to not give stupid results to stupid people i.e. reboot should come after all installs and we really dont need to go to the main menu too...
            if "-Reboot-" in selected_option_list:                         #If Reeboot is selected remove Main Menu, Quit, and ensure its at the end
                if "-Main Menu-" in selected_option_list: selected_option_list.remove("-Main Menu-") #Remove Main Menu as we dont need it...
                if "-Quit-" in selected_option_list:selected_option_list.remove("-Quit-")  #Remove Quit as we dont need it...
                selected_option_list.remove("-Reboot-")                                    #Pop Reboot out so we can
                selected_option_list.append("-Reboot-")                                    #Put it on the end!
            if "-Quit-" in selected_option_list:                           #If Quit is selected remove Main Menu, and ensure its at the end            
                if "-Main Menu-" in selected_option_list: selected_option_list.remove("-Main Menu-") #Remove Main Menu as we dont need it...
                selected_option_list.remove("-Quit-")                                      #Pop Quit out so we can
                selected_option_list.append("-Quit-")                                      #Put it on the end!
            if "-Main Menu-" in selected_option_list:                      #If Main Menu is Selected ensure its at the end
                selected_option_list.remove("-Main Menu-")                                 #Pop Quit out so we can
                selected_option_list.append("-Main Menu-")                                 #Put it on the end!

            DebugPrint("Selected Options: ", multi=selected_option_list)

            for z in range(len(selected_option_list)):
                #Main logic
                if selected_option_list[z]   == 'Boot Logo':
                    #Confirm user wants to install bootlogo
                    print('\n*\nSelected to install the {} Boot Logo. Continue?'.format(self.selected_theme))
                    if not is_affirmative():
                        print('Not installing...')
                        time.sleep(1.5)
                        continue

                    print('\nPlease wait....')

                    #Check if there was an Boot logo backup already this session to prevent accidental overwrites
                    #Returns true if okay to proceed. Gets self.backup_dir & asset type name
                    if backup_overide_check(self.backup_dir, DeviceData["BOOT_LOGO_NAME"]) == True:
                        break

                    #Backup & install new
                    install_from_path = ('{}/{}/{}'.format(CONTRIB_THEMES, self.selected_theme, DeviceData["BOOT_LOGO_THEME_PATH"]))
                    if Dev_DoInstall():
                        INSTALL_BOOT_LOGO(DeviceData, self.backup_dir, install_from_path)
                        mark_self_installed()       # Create flag in /sdcard so auto installer knows there is a self installation
                        print('Press enter to continue!')
                        input()
                elif selected_option_list[z] == 'OpenPilot Spinner':
                    ##Confirm user wants to install Spinner
                    print('\n*\nSelected to install the {} OP Spinner. Continue?'.format(self.selected_theme))
                    if not is_affirmative():
                        continue

                    ##Check if there was a spinner backup already this session to prevent accidental overwrites
                    #Returns false if okay to proceed. Gets self.backup_dir & asset type name
                    if backup_overide_check(self.backup_dir, 'spinner') == True:
                        break

                    #Gets OpenPilot Location and Version
                    OP_INFO = get_OP_Ver_Loc()
                    DebugPrint("Got OP Location: {} and Version 0.{}".format(OP_INFO["OP_Location"], OP_INFO["OP_Version"]))

                    #Backup & Install
                    install_from_path = ("{}/{}/spinner".format(CONTRIB_THEMES, self.selected_theme))
                    #Function to ask before installing for use in dev to not screw up my computer, and test logic
                    if Dev_DoInstall():
                        INSTALL_QT_SPINNER(self.backup_dir, OP_INFO, install_from_path)
                        mark_self_installed()        # Create flag in /sdcard so auto installer knows there is a self installation
                        print('Press enter to continue!')
                        input()
                elif selected_option_list[z] == '-Main Menu-' or selected_option_list[z] is None:
                    return
                elif selected_option_list[z] == '-Reboot-':
                    REBOOT()
                    exit()
                elif selected_option_list[z] == '-Quit-':
                    QUIT_PROG()
                elif selected_option_list[z] in VALID_BOOT_ANIMATIONS:
                    #Confirm user wants to install bootlogo
                    print('\n*\nSelected to install the {} {}. Continue?'.format(self.selected_theme, selected_option_list[z]))
                    if not is_affirmative():
                        continue
                
                    #Check if there was a boot ani backup already this session to prevent accidental overwrites
                    #Returns true if okay to proceed. Gets self.backup_dir & asset type name
                    if backup_overide_check(self.backup_dir, 'bootanimation.zip') == True:
                        break

                    #Set bootAniColor based off the selected option - if 'white_', 'color_', or standard bootanimation 
                    if selected_option_list[z] == 'Boot Animation':
                        bootAniColor = ''
                    elif selected_option_list[z] == 'Color Boot Animation':
                        bootAniColor = 'color_'
                    elif selected_option_list[z] == 'White Boot Animation':
                        bootAniColor = 'white_'

                    #Backup And install new bootanimation
                    install_from_path = ('{}/{}'.format(CONTRIB_THEMES, self.selected_theme))
                    if Dev_DoInstall():
                        INSTALL_BOOTANIMATION(self.backup_dir, install_from_path, bootAniColor)
                        mark_self_installed()        # Create flag in /sdcard so auto installer knows there is a self installation
                        print('Press enter to continue!')
                        input()      

if __name__ == '__main__':
    ti = ThemeInstaller()
