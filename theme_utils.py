#!/usr/bin/python
import os
import time
from support.support_functions import op_dir_finder, is_affirmative, print_text, mark_self_installed, selector_picker, get_device_theme_data, make_backup_folder

#=====================Vars====================================


#===================CODE START================================
print_text('util')

class ThemeUtil:
    def __init__(self):
        while 1:
            util_options = ['Install from custom location', 'Remove git --skip-worktree flag(s)', 'Restore Comma-default', 'Restore backup', 'Cleanup for uninstall', '-Reboot-', '-Quit-']
            selected_util = selector_picker(util_options, 'This Is a Test')

            if selected_util == 'Install from custom location':
                self.Install_from_loc('I')
            elif selected_util == 'Remove git --skip-worktree flag(s)':
                self.Fix_git()
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
 
        
        print('\nWhat is the full path to your folder? ex. /sdcard/mythemefolder')
        install_from_path = input('?: ')


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

            if selected_option == 'Boot Animation':
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
                ##Ask user if they want to --skip-worktree
                print_text('spin warn')
                print('\nHave you read the statment above, understand, and wish to use it? (its optional)')
                print('Please look at the main README at the `Spinner OP Hack` section for more info....')
                if is_affirmative():
                    skip_worktree = True
                else:
                    skip_worktree = False

                ##Ask user if their OP directory is custom (like arnepilot / dragonpilot)
                opdir = op_dir_finder()

                ##Backup & Copy in relevant files
                # Check if theme contributer provided a spinner logo
                if path.exists('{}/img_spinner_comma.png'.format(install_path)):                                             #Contibuter Did Provide
                    os.system('mv /data/{}/selfdrive/assets/img_spinner_comma.png {}/spinner'.format(opdir, self.backup_dir)) #Backup logo
                    os.system('cp {}/img_spinner_comma.png /data/{}/selfdrive/assets'.format(install_path, opdir))            #Replace spinner logo supplied custom
                    custom_logo == True
                # Check if theme contributer provided a spinner track
                if path.exists('{}/img_spinner_track.png'.format(install_path)):                                             #Contibuter Did Provide
                    os.system('mv /data/{}/selfdrive/assets/img_spinner_track.png {}/spinner'.format(opdir, self.backup_dir)) #backup spinner track
                    os.system('cp {}/img_spinner_track.png /data/{}/selfdrive/assets'.format(install_path, opdir))            #replace spinner track supplied custom
                    custom_track = True
                # Check  if theme contributer provided a spinner.c
                if path.exists('{}/spinner.c'.format(install_path)):                                                         #Contibuter Did Provide
                    os.system('mv /data/{}/selfdrive/common/spinner.c {}/spinner'.format(opdir, self.backup_dir))             #backup spinner.c     
                    os.system('cp {}/spinner.c /data/{}/selfdrive/common'.format(install_path, opdir))                        #replace spinner.c with supplied custom 
                    custom_c = True

                #Hack to keep OpenPilot from overriding
                if skip_worktree == True:
                    if custom_logo == True:
                        os.system('cd /data/{} && git update-index --skip-worktree ./selfdrive/assets/img_spinner_comma.png'.format(opdir))
                    if custom_track == True:    
                        os.system('cd /data/{} && git update-index --skip-worktree ./selfdrive/assets/img_spinner_track.png'.format(opdir))
                    if custom_c == True:
                        os.system('cd /data/{} && git update-index --skip-worktree ./selfdrive/common/spinner.c'.format(opdir))
                    print('--skip-worktree flag(s) set for custom files')

                #Final make new spinner & finish
                print('\nBuilding new spinner files, please wait..... This should take under a minute....')
                os.system('cd /data/openpilot/selfdrive/ui/spinner && make')
                print('\n{} spinner installed successfully! Original file(s) backed up to {}'.format(opdir, self.backup_dir))
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

    def Fix_git(self):
        print('This program removes the --skip-worktree flag for the OpenPilot spinner')
        print('Continue?')
        if is_affirmative():
            u = True

        ##Ask user if their OP directory is custom
        opdir = op_dir_finder()

        if u == True:
            print('\nStarting.....')
            os.system('git update-index --no-skip-worktree /data/{}/selfdrive/assets/img_spinner_comma.png'.format(opdir))
            print('- Removed flag from img_spinner_comma.png')
            os.system('git update-index --no-skip-worktree /data/{}/selfdrive/assets/img_spinner_track.png'.format(opdir))
            print('- Removed flag from img_spinner_track.png')
            os.system('git update-index --no-skip-worktree /data/{}/selfdrive/common/spinner.c'.format(opdir))
            print('- Removed flag from spinner.c')
            print('Completed! Goodbye....')
            exit()
        else:
            print('Program terminating...')
            exit()

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