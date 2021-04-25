#!/usr/bin/python
import os
import time
from support.support_functions import *
#====================== Vars ===================================


#=================== CODE START ================================
print_text('util')

class ThemeUtil:
    def __init__(self):
        while 1:
            util_options = ['Install from custom location', 'Remove git --skip-worktree flag(s)', 'Restore Comma-default', 'Restore backup', 'Cleanup for uninstall', '-Reboot-', '-Quit-']
            selected_util = selector_picker(util_options, 'This Is a Test')

            if selected_util   == 'Install from custom location':
                self.Install_from_loc('I')
            elif selected_util == 'Restore Comma-default':
                self.Restore_comma_default()
            elif selected_util == 'Restore backup':
                self.backup_dir = make_backup_folder()  # Create and get backup folder
                self.Restore_backup()
            elif selected_util == 'Cleanup for uninstall':
                self.Cleanup_files()
            elif selected_util == '-Reboot-':
                print('Rebooting.... Enjoy your old theme!!!')
                os.system('am start -a android.intent.action.REBOOT') #create an android action to reboot
                exit()
            elif selected_util == '-Quit-':
                print('Thank you come again! You will see your changes next reboot!')
                exit()


    def Install_from_loc(self):
        EON_TYPE, BOOT_LOGO_THEME_NAME, BOOT_LOGO_THEME_PATH, BOOT_LOGO_NAME, BOOT_LOGO_PATH = get_device_theme_data() # Get Perams based off detected device
        backup_dir = make_backup_folder()
        theme_options = []
        custom_logo = False 
        custom_track = False 
        custom_c = False
 
        print('\nWhat is the full path to your custom theme folder? ')
        print('ex. /sdcard/mythemefolder')
        install_from_path = input('?: ')

        OP_VER, OP_LOC = get_OP_Ver_Loc()

        if path.exists('{}/LOGO'.format(install_path)):
            self.theme_options.append('OP3T Boot Logo')
            boot_name = 'LOGO'
            if EON_TYPE == 'OP3T':
                op3_compat = 'Compatable'
                leo_compat = 'Not compatable'
                boot_name = 'LOGO'
        if path.exists('{}/SPLASH'.format(install_path)):
            self.theme_options.append('LeEco Boot Logo')
            if EON_TYPE == 'LeEco':
                op3_compat = 'Not compatable'
                leo_compat = 'Compatable'
                boot_name = 'SPLASH'
        if path.exists('{}/bootanimation.zip'.format(install_path)):
            self.theme_options.append('Boot Animation')
        if path.exists('{}/img_spinner_comma.png'.format(install_path)) or path.exists('{}/img_spinner_track.png'.format(install_path)) or path.exists('{}/spinner.c'.format(install_path)):
            self.theme_options.append('OP Spinner')
        self.theme_options.append('-Reboot-')
        self.theme_options.append('-Quit-')
    
        while 1:
            options = list(self.theme_options)  # this only contains available options from self.get_available_options
            if not len(options):
                print('The selected theme has no resources available for your device! Try another.')
                time.sleep(2)
                return

            print('What resources do you want to install?')
            for idx, theme in enumerate(options):
                print('{}. {}'.format(idx + 1, theme))
                indexChoice = int(input("Enter Index Value: "))
                indexChoice -= 1 

            selected_option = self.theme_options[indexChoice]

            if selected_option   == 'Boot Animation':
                #Backup And install new bootanimation
                os.system('mount -o remount,rw /system')                                    # /system read only, must mount as r/w
                os.system('mv /system/media/bootanimation.zip {}/bootanimation'.format(self.backup_dir))  # backup
                os.system('cp {}/bootanimation.zip /system/media/bootanimation.zip'.format(install_path, self.selected_theme))  # replace
                os.system('chmod 666 /system/media/bootanimation.zip')                      #Need to chmod and edet permissions to 666
                print('\nBoot Animation installed successfully! Original file(s) backed up to {}'.format(self.backup_dir))
                mark_self_installed()        # Create flag in /sdcard so auto installer knows there is a self installation
                print('Press enter to continue!')
                input()
            elif selected_option == 'OP Spinner':
                ##Confirm user wants to install Spinner
                print('\nSelected to install the Custom OP Spinner. Continue?')
                if not is_affirmative():
                    print('Not installing...')
                    time.sleep(1.5)
                    continue

                ##Check if there was a spinner backup already this session to prevent accidental overwrites
                #Returns false if okay to proceed. Gets self.backup_dir & asset type name
                if backup_overide_check(self.backup_dir, 'spinner') == True:
                    break

                install_from_path = ("{}/{}/spinner".format(CONTRIB_THEMES, self.selected_theme))
                INSTALL_QT_SPINNER(self.backup_dir, OP_VER, OP_LOC, install_from_path, SHOW_CONSOLE_OUTPUT)
                mark_self_installed()        # Create flag in /sdcard so auto installer knows there is a self installation
                print('Press enter to continue!')
                input()    
            elif selected_option == '-Reboot-':
                print('\nRebooting.... Thank You, Come Again!!!')
                os.system('am start -a android.intent.action.REBOOT')  # reboot intent is safer (reboot sometimes causes corruption)
                return 'exit'
            elif selected_option == '-Quit-' or selected_option is None:
                print('\nThank you come again! You will see your changes next reboot!\n')
                exit()          
            elif selected_option == 'OP3T Boot Logo' or selected_option == 'LeEco Boot Logo':
                #Backup & install new
                os.system('cp {} {}/logo'.format(BOOT_LOGO_PATH, self.backup_dir))  # Make Backup
                os.system('dd if={}/{} of={}'.format(install_path, boot_name, BOOT_LOGO_PATH))  # Replace
                print('\nBoot Logo installed successfully! Original file(s) backed up to {}/logo'.format(self.backup_dir))
                mark_self_installed()        # Create flag in /sdcard so auto installer knows there is a self installation
                print('Press enter to continue!')
                input()   

    def Restore_comma_default(self):
        print('Selected to restore Comma-Default theme. Continue?')
        print('Process is fully automagic!')
        if not is_affirmative():
            print('Not restoring...')
            time.sleep(1.5)
            self.backup_reinstaller_loop()

        os.system('cp {} {}'.format(BOOT_LOGO_PATH, self.backup_dir))      # Make Backup
        os.system('dd if=./{}/{}/{} of={}'.format(CONTRIB_THEMES, self.selected_backup, BOOT_LOGO_THEME_PATH, BOOT_LOGO_PATH))  # Replace
        print('Factory Boot Logo restored successfully! Custom file(s) backed up to {}\n'.format(self.backup_dir))

        os.system('mount -o remount,rw /system')  # /system read only, must mount as r/w
        os.system('mv /system/media/bootanimation.zip {}'.format(self.backup_dir))  # backup
        os.system('cp ./{}/{}/bootanimation.zip /system/media/bootanimation.zip'.format(CONTRIB_THEMES, self.selected_backup,))  # replace
        os.system('chmod 666 /system/media/bootanimation.zip')
        print('Factory Boot Animation restored successfully! Custom file(s) backed up to {}\n'.format(self.backup_dir))
        print('Thank you come again!')
        exit()

    def Restore_backup(self):
        BACKUP_OPTIONS = []

    def Cleanup_files(self):
        print('\n\nWelcome to the uninstall - cleanup utility')
        print("I'm sad to see you go... :(")
        print('\nThis program removes the following files not stored in the main directory:')
        print('- WARNING!!!! ALL BACKUPS!!! Stored in /sdcard/theme-backups')
        print('- eon_custom_themes_self_installed.txt in /sdcard used as a marker to the auto installer')
        print('\nIt does not remove:')
        print('- The main project directory')
        print('- Any installed themes, please run restore_theme.py and choose')
        print('  option r to restore the comma-default boot logo and boot animation')
        print('  BEFORE running this utility')

        print('Have you read and understand the warning above and wish to proceed?')
        if is_affirmative():
            u = True

        if u == True:
            print('\nStarting.....')
            os.system('cd /storage/emulated/0 && rm -rf theme-backups')
            print('Removed the theme-backups directory')
            os.system('cd /storage/emulated/0 && rm -r eon_custom_themes_self_installed.txt')
            print('Removed eon_custom_themes_self_installed.txt')
            print('\nPlease take a look and make sure the file and directory is removed....')
            os.system('cd /storage/emulated/0 && ls')
            print('\n\nThank you! You will be missed dont forget to run')
            print('cd /data && rm -rf eon-custom-themes')
            print('to finish your complete un-installation')
            print('Goodbye....')
            exit()
        else:
            print('Program terminating...')
            exit()


if __name__ == '__main__':
    tu = ThemeUtil()