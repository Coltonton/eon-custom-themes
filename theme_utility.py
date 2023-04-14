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
 #https://github.com/commaai/openpilot/wiki/SSH#option-3---githubs-official-instructions#   
 #                                                                                #
 #              Type the following command if using the main project              #
 #                  exec /data/eon-custom-themes/theme_install.py                 #
 #                                                                                #
 #            Or if trying to use the included package with an OP Fork:           #
 #              cd /data/(your openpilot directory)/eon-custom-themes             #
 #                          exec ./theme_install.py                               #
 #                                                                                #
 #               Now follow the prompts and make your selections!                 #
 #                  Everything will be done automagically!!!!!                    #
 #                                                                                #
 #                      Don't forget to tell your friends!!                       #
 #                           Love, Cole (@Coltonton)                              #
 #                                                                                #
 #        Did you know that if you have a custom OP fork you can use this         #
 #      program to auto install your custom theme for your users automagiclly?    #
 #       And incorparate it into your OP Fork? See ./developer/DEVREADME          #
 #                                                                                #
##################################################################################
import os
import time
from os import path
from support.support_functions import *
from support.support_variables import CLEANUP_TEXT, CONTRIB_THEMES, UTIL_WELCOME_TEXT
#====================== Vars ===================================


#=================== CODE START ================================
os.chdir(os.path.dirname(os.path.realpath(__file__)))  # __file__ is safer since it doesn't change based on where this file is called from
print_text(UTIL_WELCOME_TEXT)
DEV_CHECK()                               # Check if running on unsupported PC/MAC
DeviceData = get_device_theme_data()      # Init Device Data dict with device info

class ThemeUtility:
    def __init__(self):
        while True:
            util_options = ['Install from custom location', 'Restore Comma-default', 'Cleanup for uninstall', '-Reboot-', '-Quit-']
            selected_util = selector_picker(util_options, 'This Is a Test')

            if   selected_util == 'Install from custom location':
                self.Install_From_Loc()
            elif selected_util == 'Restore Comma-default':
                self.Restore_Comma_Default()
            elif selected_util == 'Cleanup for uninstall':
                self.Cleanup_Files()
            elif selected_util == '-Reboot-':
                REBOOT()
            elif selected_util == '-Quit-':
                QUIT_PROG()

    def Install_From_Loc(self):      #TEST & Cleanup the spare vars
        backup_dir = make_backup_folder()
        theme_options = []
 
        print('\n*')
        print('What is the full path to your custom theme folder? ')
        print('ex. /sdcard/mythemefolder')
        install_folder = input('?: ')
        
        # cd /data/eon-custom-themes && exec ./theme_utils.py
        # /data/eon-custom-themes/contributed-themes/Subaru
        if path.exists('{}/OP3T-Logo/LOGO'.format(install_folder)):
            theme_options.append('OP3T Boot Logo')
        if path.exists('{}/LeEco-Logo/SPLASH'.format(install_folder)):
            theme_options.append('LeEco Boot Logo')
        if path.exists('{}/bootanimation.zip'.format(install_folder)):
            theme_options.append('Boot Animation')
        if path.exists('{}/spinner/img_spinner_comma.png'.format(install_folder)) or path.exists('{}/img_spinner_track.png'.format(install_folder)) or path.exists('{}/spinner.c'.format(install_folder)):
            self.theme_options.append('OP Spinner')
        theme_options.append('-Reboot-')
        theme_options.append('-Quit-')
    
        while 1:
            options = list(theme_options)  # this only contains available options from self.get_available_options
            if not len(options):
                print('\n*\nThe selected theme has no resources available for your device! Try another.')
                time.sleep(2)
                return
        
            #Ask users what resources to install
            print('\n*\nWhat resources do you want to install for the Custom theme?')
            for idx, theme in enumerate(options):
                print('{}. {}'.format(idx + 1, theme))
            indexChoice = int(input("Enter Index Value: "))
            indexChoice -= 1 

            selected_option = self.theme_options[indexChoice]

            if selected_option  in ['Boot Animation', 'OP3T Boot Logo', 'LeEco Boot Logo', 'OP Spinner']:    
                ##Confirm user wants to install asset
                print('\nSelected to install the Custom {}. Continue?'.format(selected_option))
                if not is_affirmative():
                    continue       
    
            if selected_option   == 'Boot Animation': #Done 23
                ##Check if there was a boot ani backup already this session to prevent accidental overwrites
                #Returns false if okay to proceed. Gets self.backup_dir & asset type name
                if backup_overide_check(self.backup_dir, 'bootanimation.zip') == True:
                    break

                #Backup And install new bootanimation
                install_from_path = ('{}/{}'.format(CONTRIB_THEMES, self.selected_theme))
                if Dev_DoInstall():
                    INSTALL_BOOTANIMATION(self.backup_dir, install_from_path,)
                    mark_self_installed()        # Create flag in /sdcard so auto installer knows there is a self installation
                    print('Press enter to continue!')
                    input()  
            elif selected_option == 'OP Spinner':
                ##Check if there was a spinner backup already this session to prevent accidental overwrites
                #Returns false if okay to proceed. Gets self.backup_dir & asset type name
                if backup_overide_check(self.backup_dir, 'spinner') == True:
                    break

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
            elif selected_option == '-Reboot-':
                REBOOT()
            elif selected_option == '-Quit-' or selected_option is None:
                QUIT_PROG()        
            elif selected_option == 'OP3T Boot Logo' or selected_option == 'LeEco Boot Logo':
                ##Check if there was a Boot Logo backup already this session to prevent accidental overwrites
                #Returns false if okay to proceed. Gets self.backup_dir & asset type name
                if backup_overide_check(self.backup_dir, DeviceData["BOOT_LOGO_NAME"]) == True:
                    break

                #Backup & install new
                install_from_path = ('{}/{}/{}'.format(CONTRIB_THEMES, self.selected_theme, DeviceData["BOOT_LOGO_THEME_PATH"]))
                if Dev_DoInstall():
                    INSTALL_BOOT_LOGO(DeviceData, self.backup_dir, install_from_path)
                    mark_self_installed()       # Create flag in /sdcard so auto installer knows there is a self installation
                    print('Press enter to continue!')
                    input()

    def Restore_Comma_Default(self): #Restore the default theme for EON 
        print('\nSelected to restore Comma-Default theme. Continue?')
        print('Process is fully automagic!')
        if not is_affirmative():
            return None

        print('Please wait..... This should only take a few moments!\n')
        backup_dir = make_backup_folder()

        #Boot-Logo
        install_from_path = '{}/Comma-Default/{}'.format(CONTRIB_THEMES, DeviceData["BOOT_LOGO_THEME_PATH"])
        INSTALL_BOOT_LOGO(DeviceData, backup_dir, install_from_path)

        #Boot-Animation
        install_from_path = '{}/Comma-Default/'.format(CONTRIB_THEMES)
        INSTALL_BOOTANIMATION(backup_dir, install_from_path)

        print('\nThank you come again! - Boot Logo & Boot Animation factory restored!!')
        exit()

    def Cleanup_Files(self):         #Remove all traces of EON Custom Themes
        #Print hAllo message
        print_text(CLEANUP_TEXT)
        #Confirm user wants to install bootlogo
        print('\nHave you read and understand the warning above and wish to proceed?')
        if not is_affirmative():
            print('Canceling...')
            time.sleep(1.5)
            exit()                 #Fix ??

        print('\nStarting.....')
        os.system('cd /storage/emulated/0 && rm -rf theme-backups')
        print('Removed the theme-backups directory')
        os.system('cd /storage/emulated/0 && rm -r eon_custom_themes_self_installed.txt')
        print('Removed eon_custom_themes_self_installed.txt')
        print('\nPlease take a look and make sure the file and directory is removed....')
        os.system('cd /storage/emulated/0 && ls')
        print("\n\nThank you! You will be missed; don't forget to run...")
        print('cd /data && rm -rf eon-custom-themes')
        print('to finish your complete un-installation')
        print('Until we meet again.....')
        exit()



if __name__ == '__main__':
    tu = ThemeUtility()