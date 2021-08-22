#!/usr/bin/python
###################################################################################
#                                  VER 2.0 PR                                    #
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
 #                                  [REDACTED]                                    #
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
from support.support_variables import BACKUPS_DIR, BACKUP_OPTIONS, CONTRIB_THEMES, OP_VER, OP_LOC, SHOW_CONSOLE_OUTPUT
from support.auto_config       import AUTO_INSTALL_CONF, IS_AUTO_INSTALL, DESIRED_AUTO_VER

##======================= CODE START ================================================================
os.chdir(os.path.dirname(os.path.realpath(__file__)))  # __file__ is safer since it doesn't change based on where this file is called from
if IS_AUTO_INSTALL:
    print_text(AUTO_WELCOME_TEXT)         #Print welcome text with the flag for auto welcome text
else:
    print_text(WELCOME_TEXT)              #Print welcome text with the flag for self welcome text
  
EON_TYPE, BOOT_LOGO_THEME_NAME, BOOT_LOGO_THEME_PATH, BOOT_LOGO_DEVICE_NAME, BOOT_LOGO_DEVICE_PATH = get_device_theme_data() # Get Perams based off detected device

class ThemeInstaller:
    def __init__(self):                   # Init code runs once. sets up & determines if to run auto or self
        # Create and get backup folder
        self.backup_dir = make_backup_folder()

        # Dev function to show console output when this program calls make for example....
        if SHOW_CONSOLE_OUTPUT == False:
            self.con_output = ' >/dev/null 2>&1'  # string to surpress output
        else:
            self.con_output = ''

        # Detrimine if should self install, auto install, or exit
        auto_found_installer = installer_chooser()  
        if auto_found_installer == 'Do_Self':
            self.start_loop()                                      # Do self install theme git
        elif auto_found_installer == 'Do_Auto':
            self.auto_installer()                                  # Do auto install theme
        else:
            os.rmdir(self.backup_dir)                              # Remove session backup folder as we are doing nada
            exit()                                                 # Terminate program

    def start_loop(self):                 # Self Installer loop
        while 1:
            self.selected_theme = get_user_theme()
            if self.selected_theme is None:
                print('Didn\'t select a theme, exiting.')
                return
            OP_VER, OP_LOC = get_OP_Ver_Loc()
            print("OpenLocation{}".format(OP_LOC))
            self.get_available_options()
            if self.install_function(OP_LOC) == 'exit':
                return

    def get_available_options(self):      # Check what assets are available for the selected theme
        self.theme_options = []
        # Check if the selected theme has a boot logo asset
        if os.path.exists('{}/{}/{}'.format(CONTRIB_THEMES, self.selected_theme, BOOT_LOGO_THEME_PATH)):
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
        if os.path.exists('{}/{}/spinner'.format(CONTRIB_THEMES, self.selected_theme)):
            self.theme_options.append('OpenPilot Spinner')

        self.theme_options.append('-Main Menu-')
        self.theme_options.append('-Reboot-')
        self.theme_options.append('-Quit-')

    def install_function(self, OPLOC):           # Self installer program, prompts user on what they want to do
        while 1:
            theme_types = list(self.theme_options)  # this only contains available options from self.get_available_options
            if not len(theme_types):
                print('\n*\nThe selected theme has no resources available for your device! Try another.')
                time.sleep(2)
                return
        
            #Ask users what resources to install
            print('\n*\nWhat resources do you want to install for the {} theme?'.format(self.selected_theme))
            for idx, theme in enumerate(theme_types):
                print('{}. {}'.format(idx + 1, theme))
            indexChoice = int(input("Enter Index Value: "))
            indexChoice -= 1 

            selected_option = self.theme_options[indexChoice]

            #Main logic
            if selected_option   == 'Boot Logo':
                #Confirm user wants to install bootlogo
                print('\nSelected to install the {} Boot Logo. Continue?'.format(self.selected_theme))
                if not is_affirmative():
                    print('Not installing...')
                    time.sleep(1.5)
                    continue

                print('\nPlease wait....')

                #Check if there was an Boot logo backup already this session to prevent accidental overwrites
                #Returns true if okay to proceed. Gets self.backup_dir & asset type name
                if backup_overide_check(self.backup_dir, 'spinner') == True:
                    break

                #Backup & install new
                install_from_path = ('{}/{}/{}'.format(CONTRIB_THEMES, self.selected_theme, BOOT_LOGO_THEME_PATH))
                INSTALL_BOOT_LOGO(EON_TYPE, self.backup_dir, install_from_path)
                mark_self_installed()       # Create flag in /sdcard so auto installer knows there is a self installation
                print('Press enter to continue!')
                input()
            elif selected_option == 'OpenPilot Spinner':
                ##Confirm user wants to install Spinner
                print('\nSelected to install the {} OP Spinner. Continue?'.format(self.selected_theme))
                if not is_affirmative():
                    print('Not installing...')
                    time.sleep(1.5)
                    continue

                ##Check if there was a spinner backup already this session to prevent accidental overwrites
                #Returns false if okay to proceed. Gets self.backup_dir & asset type name
                if backup_overide_check(self.backup_dir, 'spinner') == True:
                    break

                print("Location {}".format(OP_LOC))
                install_from_path = ("{}/{}/spinner".format(CONTRIB_THEMES, self.selected_theme))
                INSTALL_QT_SPINNER(self.backup_dir, OP_VER, OP_LOC, install_from_path, SHOW_CONSOLE_OUTPUT)
                mark_self_installed()        # Create flag in /sdcard so auto installer knows there is a self installation
                print('Press enter to continue!')
                input()
            elif selected_option == '-Main Menu-' or selected_option is None:
                return
            elif selected_option == '-Reboot-':
                REBOOT()
                exit()
            elif selected_option == '-Quit-' or selected_option is None:
                QUIT_PROG()
            elif selected_option == 'Boot Animation' or 'Color Boot Animation' or 'White Boot Animation':
                #Confirm user wants to install bootlogo
                print('\nSelected to install the {} {}. Continue?'.format(self.selected_theme, selected_option))
                if not is_affirmative():
                    print('Not installing...')
                    time.sleep(1.5)
                    continue
            
                #Check if there was an APK backup already this session to prevent accidental overwrites
                #Returns true if okay to proceed. Gets self.backup_dir & asset type name
                if backup_overide_check(self.backup_dir, 'spinner') == True:
                    break

                #Set bootAniColor based off the selected option - if 'white_', 'color_', or standard bootanimation 
                if selected_option == 'Boot Animation':
                    bootAniColor = ''
                elif selected_option == 'Color Boot Animation':
                    bootAniColor = 'color_'
                elif selected_option == 'White Boot Animation':
                    bootAniColor = 'white_'

                #Backup And install new bootanimation
                install_from_path = ('./{}/{}/{}'.format(CONTRIB_THEMES, self.selected_theme, bootAniColor))
                INSTALL_BOOTANIMATION(self.backup_dir, install_from_path)
                mark_self_installed()        # Create flag in /sdcard so auto installer knows there is a self installation
                print('Press enter to continue!')
                input()
   
    def auto_installer(self):             # Auto Installer program for incorperating into OP forks SEE DEVREADME
        self.selected_theme = AUTO_INSTALL_CONF['auto_selected_theme']
        opdir               = AUTO_INSTALL_CONF['op_dir_name']
        install_3t_logo     = AUTO_INSTALL_CONF['install_3T_logo']
        install_leo_logo    = AUTO_INSTALL_CONF['install_Leo_logo']
        install_bootani     = AUTO_INSTALL_CONF['install_bootanim']
        selected_ani_color  = AUTO_INSTALL_CONF['ani_color']
    

        if (EON_TYPE == 'OP3T' and install_3t_logo == True) or (EON_TYPE == 'LeEco' and install_leo_logo == True): # Auto BootLogo Install Code
            os.system('cp {} {}'.format(BOOT_LOGO_PATH, self.backup_dir))                                                        # Make Backup
            os.system('dd if={}/{}/{} of={}'.format(CONTRIB_THEMES, self.selected_theme, BOOT_LOGO_THEME_PATH, BOOT_LOGO_PATH))  # Replace
            print('\nBoot Logo installed successfully! Original file(s) backed up to {}'.format(self.backup_dir))
        else:
            print('Debug: No Boot Logo to install for device: {} EON'.format(EON_TYPE))

        if install_bootani == True:  # Auto BootAni Install Code
            os.system('mount -o remount,rw /system')
            os.system('mv /system/media/bootanimation.zip {}'.format(self.backup_dir))
            os.system('cp {}/{}/{}bootanimation.zip /system/media/bootanimation.zip'.format(CONTRIB_THEMES, self.selected_theme, selected_ani_color))
            os.system('chmod 666 /system/media/bootanimation.zip')
            print('Boot Animation installed successfully! Original file(s) backuped to {}'.format(self.backup_dir))
        else:
            print('Debug: No Boot Animation to install for device: {} EON'.format(EON_TYPE))

        fi = open("./support/auto_install_ver.txt", "w")
        fi.write(str(DESIRED_AUTO_VER))
        print('Have a wonderful day, program run complete, terminating!')
        exit()


if __name__ == '__main__':
    ti = ThemeInstaller()
