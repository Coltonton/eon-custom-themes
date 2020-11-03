#!/usr/bin/python
import os

print('Welcome to the uninstall - cleanup utility')
print("I'm sad to see you go... :(")
print('\nThis program removes the following files not stored in the main directory:')
print('- WARNING!!!! ALL BACKUPS!!! Stored in /sdcard/theme-backups')
print('- eon_custom_themes_self_installed.txt in /sdcard used as a marker to the auto installer')
print('\nIt does not remove:')
print('- The main project directory')
print('- Any installed themes, please run restore_backup.py and choose')
print('  option r to restore the comma-default boot logo and boot animation')
print('  BEFORE running this utility')

print('Have you read and understand the warning above and wish to proceed?')
u = input('[1.Yes / 2.No]: ').lower().strip()

if u == '1':
    print('\nStarting.....')
    os.system('cd /storage/emulated/0 && rm -rf theme-backups')
    print('Removed the theme-backups directory')
    os.system('cd /storage/emulated/0 && rm -r eon_custom_themes_self_installed.txt')
    print('Removed eon_custom_themes_self_installed.txt')
    print('\nPlease take a look and make sure the file and directory is removed....')
    os.system('cd /storage/emulated/0 && ls')
    print('\n\n Thank you! You will be missed dont forget to run')
    print('cd /data && rm -rf eon-custom-themes')
    print('to finish your complete un-installation')
    print('Goodbye....')
    exit()
    
else:
    print('Program terminating...')
    exit()
