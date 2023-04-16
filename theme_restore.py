#!/usr/bin/python
###################################################################################
#                                  VER 1.2                                        #
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
import os
import time
from os import path
from support.support_variables import BACKUPS_DIR, BACKUP_OPTIONS
from support.support_functions import *

######################################################################################################
##======================= CODE START ================================================================#
######################################################################################################
os.chdir(os.path.dirname(os.path.realpath(__file__)))  # __file__ is safer since it doesn't change based on where this file is called from
print_text(RESTORE_WELCOME_TEXT)                  # Print welcome text with the flag for self welcome text
DebugPrint("VERBOSE MODE ON")             # Notify if Verbosity Mode is on, DebugPrints only run in dev or verbose mode
DEV_CHECK()                               # Check if running on unsupported PC/MAC
OpInfo = dict                             # Init OPInfo Dict
DeviceData = get_device_theme_data()      # Init Device Data dict with device info

class ThemeRestorer:
    def __init__(self):                       # Init code runs once. sets up.
        self.backup_dir = make_backup_folder()  # Create and get backup folder
        self.theme_restore_loop()          # Start main loop

    def theme_restore_loop(self):             # Theme_restorer!
        # Backup_restore Loop
        while 1:
            self.selected_backup = get_user_backups(self.backup_dir)
            if self.selected_backup is None:
                print('Didn\'t select a backup, exiting.')
                return
            if self.selected_backup == 'Comma-Default':
                self.restore_default_comma()
            self.backup_get_available_options()
            if self.backup_reinstall_function() == 'exit':
                return
  
    def backup_get_available_options(self):   # Check what assets are available for the selected backup
        # Check if the selected backup has a boot logo asset
        if os.path.exists('{}/{}/{}'.format(BACKUPS_DIR, self.selected_backup, DeviceData["BOOT_LOGO_NAME"])):
            BACKUP_OPTIONS.append('Boot Logo')

        # Check if the selected backup has a boot annimation asset
        if os.path.exists('{}/{}/bootanimation.zip'.format(BACKUPS_DIR, self.selected_backup)):
            BACKUP_OPTIONS.append('Boot Animation')

        # Check if the selected backup has a OpenPilot Spinner asset
        if os.path.exists('{}/{}/spinner'.format(BACKUPS_DIR, self.selected_backup)):
            BACKUP_OPTIONS.append('OpenPilot Spinner') 

        BACKUP_OPTIONS.append('-Main Menu-')
        BACKUP_OPTIONS.append('-Reboot-')
        BACKUP_OPTIONS.append('-Quit-')

    def backup_reinstall_function(self):      # Backuo re-installer program, prompts user on what they want to do
        while 1:
            options = list(BACKUP_OPTIONS)      # this only contains available options from self.get_available_options
            if not len(options):
                print('The selected backup has no resources available for your device! Try another.')
                time.sleep(2)
                return
        
            print('What resources do you want to install for the {} backup?'.format(self.selected_backup))
            for idx, theme in enumerate(options):
                print('{}. {}'.format(idx + 1, theme))
            indexChoice = int(input("Enter Index Value: "))

            selected_option = BACKUP_OPTIONS[indexChoice-1]
            
            if   selected_option == 'Boot Logo':
                print('Selected to install the Boot Logo backup. Continue?')
                if not is_affirmative():
                    continue

                #Backup & install new
                install_from_path = ('{}/{}/{}'.format(BACKUPS_DIR, self.selected_backup, DeviceData["BOOT_LOGO_THEME_PATH"], re=True))
                if Dev_DoInstall():
                    INSTALL_BOOT_LOGO(DeviceData, self.backup_dir, install_from_path)
                    mark_self_installed()       # Create flag in /sdcard so auto installer knows there is a self installation
                    print('Press enter to continue!')
                    input()
            elif selected_option == 'Boot Animation':
                print('Selected to install the Boot Animation backup. Continue?')
                if not is_affirmative():
                    continue

                #Backup And install new bootanimation
                install_from_path = ('{}/{}'.format(BACKUPS_DIR, self.selected_backup))
                if Dev_DoInstall():
                    INSTALL_BOOTANIMATION(self.backup_dir, install_from_path, re=True)
                    mark_self_installed()        # Create flag in /sdcard so auto installer knows there is a self installation
                    print('Press enter to continue!')
                    input()      
            elif selected_option == 'OpenPilot Spinner':
                ##Confirm user wants to install Spinner
                print('\nSelected to install the {} OP Spinner. Continue?'.format(self.selected_theme))
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
                install_from_path = ("{}/{}/spinner".format(BACKUPS_DIR, self.selected_backup))
                #Function to ask before installing for use in dev to not screw up my computer, and test logic
                if Dev_DoInstall():
                    INSTALL_QT_SPINNER(self.backup_dir, OP_INFO, install_from_path, re=True)
                    mark_self_installed()        # Create flag in /sdcard so auto installer knows there is a self installation
                    print('Press enter to continue!')
                    input()
            elif selected_option == '-Main Menu-' or selected_option is None:
                return
            elif selected_option == '-Reboot-':
                REBOOT()
            elif selected_option == '-Quit-':
                QUIT_PROG()

    def restore_default_comma(self):           # Restore the devices default theme
        restore_comma_default(DeviceData, self.backup_dir)

if __name__ == '__main__':
  bi = ThemeRestorer()
