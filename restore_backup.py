import os
import time
from os import path
from support.support_variables import BACKUPS_DIR, BACKUP_OPTIONS
from support.support_functions import get_device_theme_data, get_user_backups, is_affirmative, make_backup_folder, print_welcome_text


##======================= CODE START ================================================================
os.chdir(os.path.dirname(os.path.realpath(__file__)))  # __file__ is safer since it doesn't change based on where this file is called from
print_welcome_text('r')                                #Print welcome text with the flag for restore welcome text
BOOT_LOGO_THEME_PATH, BOOT_LOGO_PATH, BOOT_LOGO_NAME = get_device_theme_data() # Get Perams based off detected device

class BackupReinstaller:
    def __init__(self):                       # Init code runs once. sets up.
        self.backup_dir = make_backup_folder()  # Create and get backup folder
        self.backup_reinstaller_loop()          # Start main loop

    def backup_reinstaller_loop(self):        # Backup Reinstaller!
        # Backup_restore Loop
        while 1:
            self.selected_backup = get_user_backups(self.backup_dir)
            if self.selected_backup is None:
                print('Didn\'t select a backup, exiting.')
                return
            self.backup_get_available_options()
            if self.backup_reinstall_function() == 'exit':
                return
  
    def backup_get_available_options(self):   # Check what assets are available for the selected backup
        
        # Check if the selected backup has a boot logo asset
        if os.path.exists('{}/{}/{}'.format(BACKUPS_DIR, self.selected_backup, BOOT_LOGO_NAME)):
            BACKUP_OPTIONS.append('Boot Logo')

        # Check if the selected backup has a boot annimation asset
        if os.path.exists('{}/{}/bootanimation.zip'.format(BACKUPS_DIR, self.selected_backup)):
            BACKUP_OPTIONS.append('Boot Animation')

        # Check if the selected backup has a OpenPilot Spinner asset
        if os.path.exists('{}/{}/spinner'.format(BACKUPS_DIR, self.selected_backup)):
            BACKUP_OPTIONS.append('OpenPilot Spinner')

        # if os.path.exists('{}/{}/additional'.format(BACKUPS_DIR, self.selected_backup)):  # todo disabled for now
        #   self.BACKUP_OPTIONS.append('4. Additional Resources')

        BACKUP_OPTIONS.append('-Main Menu-')
        BACKUP_OPTIONS.append('-Reboot-')
        BACKUP_OPTIONS.append('-Quit-')

    def backup_reinstall_function(self):      # Backuo re-installer program, prompts user on what they want to do
        while 1:
            options = list(BACKUP_OPTIONS)  # this only contains available options from self.get_available_options
            if not len(options):
                print('The selected backup has no resources available for your device! Try another.')
                time.sleep(2)
                return
        
            print('What resources do you want to install for the {} backup?'.format(self.selected_backup))
            for idx, theme in enumerate(options):
                print('{}. {}'.format(idx + 1, theme))
            indexChoice = int(input("Enter Index Value: "))
            indexChoice -= 1 

            selected_option = BACKUP_OPTIONS[indexChoice]

            if selected_option == 'Boot Logo':
                print('Selected to install the Boot Logo backup. Continue?')
                if not is_affirmative():
                    print('Not installing...')
                    time.sleep(1.5)
                    continue
                os.system('cp {} {}'.format(BOOT_LOGO_PATH, self.backup_dir))  # Make Backup
                os.system('dd if={}/{}/{} of={}'.format(BACKUPS_DIR, self.selected_backup, BOOT_LOGO_NAME, BOOT_LOGO_PATH))  # Replace
                print('\nBoot Logo re-installed successfully! Original backed up to {}'.format(self.backup_dir))
                print('Press enter to continue!')
                input()
            elif selected_option == 'Boot Animation':
                print('Selected to install the Boot Animation backup. Continue?')
                if not is_affirmative():
                    print('Not installing...')
                    time.sleep(1.5)
                    continue
              
                os.system('mount -o remount,rw /system')  # /system read only, must mount as r/w
                os.system('mv /system/media/bootanimation.zip {}'.format(self.backup_dir))  # backup
                os.system('cp {}/{}/bootanimation.zip /system/media/bootanimation.zip'.format(BACKUPS_DIR, self.selected_backup))  # replace
                os.system('chmod 666 /system/media/bootanimation.zip')
                print('\nBoot Animation re-installed successfully! Original backed up to {}'.format(self.backup_dir))
                print('Press enter to continue!')
                input()
            elif selected_option == 'OpenPilot Spinner':
                #Confirm user wants to install Spinner
                print('Selected to install the {} OP Spinner backup. Continue?'.format(self.selected_theme))
                if not is_affirmative():
                    print('Not installing...')
                    time.sleep(1.5)
                    continue
        
                #Check if there was a backup already this session to prevent accidental overwrites
                if path.exists('{}/spinner'.format(self.backup_dir)):                  
                    print('It appears you already made a spinner backup this session') 
                    print('continuing will overwrite last spinner backup!')
                    print('Would you like to continue and overwrite previous?')
                    if not is_affirmative():
                        print('Not installed, exiting session..... Please re-run program')
                        exit()      #Exit program if user does not want to overwrite, so they can start a new session
                else:
                    os.mkdir('{}/spinner'.format(self.backup_dir))

                #Ask user if their OP directory is custom (like arnepilot / dragonpilot)
                print('Do you have an OP fork with a custom directory name? (ex. arnepilot, dragonpilot)')  # Ask the user if their OP fork used a diffrent directory.
                if is_affirmative():  # Yes there is a custom OP dir
                    print('What is the OP directory name? (case matters, not including /data/)')
                    opdir = '/data/{}'.format(input('> ').strip('/'))  # get custom dir name, strip slashes for safety
                    print('Your openpilot directory is {}'.format(opdir))
                    input('*** Please enter to continue, or Ctrl+C to abort if this is incorrect! ***')
                else:
                    opdir = 'openpilot'                                #op directory is not custom so openpilot

                #Backup files
                os.system('mv /data/{}/selfdrive/assets/img_spinner_comma.png {}/spinner'.format(opdir, self.backup_dir)) #Backup logo
                os.system('mv /data/{}/selfdrive/assets/img_spinner_track.png {}/spinner'.format(opdir, self.backup_dir)) #backup sprinner track
                os.system('mv /data/{}/selfdrive/common/spinner.c {}/spinner'.format(opdir, self.backup_dir))             #backup spinner.c

                #Copy in new files
                os.system('cp {}/{}/spinner/img_spinner_comma.png /data/{}/selfdrive/assets'.format(BACKUPS_DIR, self.selected_backup, opdir)) #Replace logo
                os.system('cp {}/{}/spinner/img_spinner_track.png /data/{}/selfdrive/assets'.format(BACKUPS_DIR, self.selected_backup, opdir)) #Replace sprinner
                os.system('cp {}/{}/spinner/spinner.c /data/{}/selfdrive/common'.format(BACKUPS_DIR, self.selected_backup, opdir))             #Replace spinner.c

                #Final make new spinner & finish
                os.system('cd /data/{}/selfdrive/ui/spinner && make'.format(opdir))
                print('\n{} spinner re-installed successfully! Original backed up to {}'.format(opdir, self.backup_dir))
                print('Press enter to continue!')
                input()
            elif selected_option == 'Additional Resources':  # additional features
                print('Additional Resources are not an active feature')
                time.sleep(5)
            elif selected_option == '-Main Menu-' or selected_option is None:
                return
            elif selected_option == '-Reboot-':
                print('Rebooting.... Enjoy your old theme!!!')
                os.system('am start -a android.intent.action.REBOOT')  # reboot intent is safer (reboot sometimes causes corruption)
                exit()
            elif selected_option == '-Quit-':
                print('Thank you come again! You will see your changes next reboot!')
                exit()

if __name__ == '__main__':
  bi = BackupReinstaller()
