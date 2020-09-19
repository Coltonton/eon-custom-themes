#!/usr/bin/python
import os 
from os import path
import time
from datetime import datetime
from support.support_variables import BACKUPS_DIR
from support.support_functions import get_user_backups, is_affirmative

os.chdir(os.path.dirname(os.path.realpath(__file__)))  # __file__ is safer since it doesn't change based on where this file is called from

backup_options = []

# Crude device detection, *shrug* it works! LeEco does not have tristate!
if path.exists('/sys/devices/virtual/switch/tri-state-key'): #If 3T-ON
  print('\n*** OG OnePlus EON Device Detected ***')
  BOOT_LOGO_THEME_PATH = 'OP3T-Logo/LOGO'                      # Set the boot logo theme path for 3T
  BOOT_LOGO_PATH = '/dev/block/sde17'                          # Set the boot logo directory for 3T
else:                                                        #If LeON/Two
  print('\n*** LeEco EON (Gold/Comma 2) Device Detected ***\n')
  BOOT_LOGO_THEME_PATH = 'LeEco-Logo/SPLASH'                   # Set the boot logo theme path for Leo
  BOOT_LOGO_PATH = '/dev/block/bootdevice/by-name/splash'      # Set the boot logo directory for Leo

class BackupInstaller:
    def __init__(self):
        if not os.path.exists(BACKUPS_DIR): # Check if theme backup folder doesnt exist
            os.mkdirs('/storage/emulated/0/theme-backups')              #Create theme backup folder

        self.backup_dir = datetime.now().strftime('/storage/emulated/0/theme-backups/backup.%m-%d-%y--%I.%M.%S-%p')  # Get current datetime and store
        os.mkdir(self.backup_dir)  # Create the session backup folder

        self.start_loop()

    def start_loop(self):
        while 1:
            self.selected_backup = get_user_backups()
            if self.selected_backup is None:
                print('Didn\'t select a backup, exiting.')
                return
            self.get_available_options()
            if self.install_function() == 'exit':
                return

    def get_available_options(self):  # Check what assets are available for the selected backup
        
        # Check if the selected backup has a 3T boot logo asset
        if os.path.exists('{}/{}/sde17'.format(BACKUPS_DIR, self.selected_backup)):
            backup_options.append('3T Boot Logo')

        # Check if the selected backup has a 3T boot logo asset
        if os.path.exists('{}/{}/splash'.format(BACKUPS_DIR, self.selected_backup)):
            backup_options.append('LeEco/Gold/Two Boot Logo')

        # Check if the selected theme has a boot annimation asset
        if os.path.exists('{}/{}/bootanimation.zip'.format(BACKUPS_DIR, self.selected_backup)):
            backup_options.append('Boot Animation')

        # Check if the selected theme has a OpenPilot Spinner asset
        if os.path.exists('{}/{}/spinner'.format(BACKUPS_DIR, self.selected_backup)):
            backup_options.append('OpenPilot Spinner')

        # if os.path.exists('{}/{}/additional'.format(BACKUPS_DIR, self.selected_backup)):  # todo disabled for now
        #   self.backup_options.append('4. Additional Resources')

        backup_options.append('-Main Menu-')
        backup_options.append('-Reboot-')

    def install_function(self):       # Self installer program, prompts user on what they want to do
        while 1:
            options = list(backup_options)  # this only contains available options from self.get_available_options
            if not len(options):
                print('The selected backup has no resources available for your device! Try another.')
                time.sleep(2)
                return
        
            print('What resources do you want to install for the {} backup?'.format(self.selected_backup))
            for idx, theme in enumerate(options):
                print('{}. {}'.format(idx + 1, theme))
            indexChoice = int(input("Enter Index Value: "))
            indexChoice -= 1 

            selected_option = backup_options[indexChoice]
            print(selected_option)

            if selected_option == '3T Boot Logo':
                print('Selected to install the Boot Logo backup. Continue?')
                if not is_affirmative():
                    print('Not installing...')
                    time.sleep(1.5)
                    continue
                os.system('cp {} {}'.format(BOOT_LOGO_PATH, self.backup_dir))  # Make Backup
                os.system('dd if={}/{}/sde17 of={}'.format(BACKUPS_DIR, self.selected_backup, BOOT_LOGO_PATH))  # Replace
                print('\nBoot Logo installed successfully! Original backed up to {}'.format(self.backup_dir))
                print('Press enter to continue!')
                input()
            elif selected_option == 'LeEco/Gold/Two Boot Logo':
                print('Selected to install the Boot Logo backup. Continue?')
                if not is_affirmative():
                    print('Not installing...')
                    time.sleep(1.5)
                    continue
                os.system('cp {} {}'.format(BOOT_LOGO_PATH, self.backup_dir))  # Make Backup
                os.system('dd if={}/{}/splash of={}'.format(BACKUPS_DIR, self.selected_backup, BOOT_LOGO_PATH))  # Replace
                print('\nBoot Logo installed successfully! Original backed up to {}'.format(self.backup_dir))
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
                print('\nBoot Animation installed successfully! Original backed up to {}'.format(self.backup_dir))
                print('Press enter to continue!')
                input()
            elif selected_option == 'OpenPilot Spinner':
                print('Selected to install the OP Spinner backup. Continue?')
                if not is_affirmative():
                    print('Not installing...')
                    time.sleep(1.5)
                    continue
                print('Do you have an OP fork with a custom directory name? (ex. arnepilot, dragonpilot)')  # Ask the user if their OP fork used a diffrent directory.
                if is_affirmative():  # Yes there is a custom OP dir
                    print('What is the OP directory name? (case matters, not including /data/)')
                    op_dir = '/data/{}'.format(input('> ').strip('/'))  # get custom dir name, strip slashes for safety
                    print('Your openpilot directory is {}'.format(op_dir))
                    input('*** Please enter to continue, or Ctrl+C to abort if this is incorrect! ***')

                    os.system('mv {}/selfdrive/ui/spinner/spinner {}'.format(op_dir, self.backup_dir))
                    os.system('cp {}/{}/spinner {}/selfdrive/ui/spinner'.format(BACKUPS_DIR, self.selected_backup, op_dir))
                    print('\n{} spinner installed successfully! Original backed up to {}'.format(op_dir.split('/')[2], self.backup_dir))
                else:  # there is not custom OP dir
                    os.system('mv /data/openpilot/selfdrive/ui/spinner/spinner {}'.format(self.backup_dir))
                    os.system('cp {}/{}/spinner /data/openpilot/selfdrive/ui/spinner'.format(BACKUPS_DIR, self.selected_backup))
                    print('\nopenpilot spinner installed successfully! Original backed up to {}'.format(self.backup_dir))
                    print('Press enter to continue!')
                    input()
            elif selected_option == 'Additional Resources':  # additional features
                print('Additional Resources are not an active feature')
                time.sleep(5)
            elif selected_option == '-Main Menu-' or selected_option is None:
                return
            elif selected_option == '-Reboot-':
                print('Rebooting.... Enjoy your new theme!!!')
                os.system('am start -a android.intent.action.REBOOT')  # reboot intent is safer (reboot sometimes causes corruption)
                return 'exit'

    # Created by @ShaneSmiskol
    def is_affirmative(self):           # Ask user for confirmation
        u = input('[Yes/No]: ').lower().strip()
        return u in ['yes', 'ye', 'y', '1']

if __name__ == '__main__':
    ti = BackupInstaller()

