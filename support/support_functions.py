#!/usr/bin/python
import os
import sys
import time
import difflib
from os import path
from datetime import datetime
from support.support_variables import AUTO_WELCOME_TEXT, BACKUPS_DIR, CONTRIB_THEMES, EXCLUDED_THEMES, MIN_SIM_THRESHOLD, RESTORE_WELCOME_TEXT, WELCOME_TEXT, UTIL_WELCOME_TEXT
from support.auto_config import IS_AUTO_INSTALL, DESIRED_AUTO_VER

os.chdir(os.path.dirname(os.path.realpath(__file__)))  # __file__ is safer since it doesn't change based on where this file is called from

## ================= Shared ================= ##
def get_device_theme_data():
    # Crude device detection, *shrug* it works! LeEco does not have tristate!
    if path.exists('/sys/devices/virtual/switch/tri-state-key'): #If 3T-ON
        print('\n*** OG OnePlus EON Device Detected! OooOoOooo we got a rebel! :O ***')
        print('PLEASE NOTE! Comma wrongfully deprecated the 3T-EON, this program')
        print('will still work for as long as feasable but may not be as maintaind as the')
        print('Eon-Gold and possibly with less features.. I do this for free and fun')
        print('making money by force upgrading is the least of my concern...')
        EON_TYPE             = 'OP3T'                                # EON type is OP3T
        BOOT_LOGO_THEME_NAME = 'LOGO'                                # Set the theme name for the logo for 3T
        BOOT_LOGO_THEME_PATH = 'OP3T-Logo/LOGO'                      # Set the theme boot logo path for 3T
        BOOT_LOGO_NAME       = 'sde17'                               # Set the device boot logo name for 3T
        BOOT_LOGO_PATH       = '/dev/block/sde17'                    # Set the device boot logo directory for 3T
    else:                                                        #If LEON/Two
        print('\n*** LeEco EON (LeON/Gold/Comma 2) Device Detected ***')
        EON_TYPE             = 'LeEco'                               # EON type is LeEco
        BOOT_LOGO_THEME_NAME = 'SPLASH'                              # Set the theme name for the logo for Leo
        BOOT_LOGO_THEME_PATH = 'LeEco-Logo/SPLASH'                   # Set the theme boot logo path for  Leo
        BOOT_LOGO_NAME       = 'splash'                              # Set the device boot logo name for Leo
        BOOT_LOGO_PATH       = '/dev/block/bootdevice/by-name/splash'# Set the device boot logo directory for Leo
    print('IMPORTANT: Soft-bricking is likely if this detection is incorrect!')

    time.sleep(4)  # Pause for suspense, and so can be read
    return EON_TYPE, BOOT_LOGO_THEME_NAME, BOOT_LOGO_THEME_PATH, BOOT_LOGO_NAME, BOOT_LOGO_PATH

def is_affirmative():           # Ask user for confirmation
    u = input('[1.Yes / 2.No]: ').lower().strip()
    if u not in ['yes', 'ye', 'y', '1']:
        print('Not Installing....')
    return u in ['yes', 'ye', 'y', '1']

def make_backup_folder():
    # Check if theme backup folder doesnt exist then create
    if not os.path.exists('/storage/emulated/0/theme-backups'):
        os.mkdir('/storage/emulated/0/theme-backups')
    # Create session backup folder named with date & time 
    backup_dir = datetime.now().strftime('/storage/emulated/0/theme-backups/backup.%m-%d-%y--%I:%M.%S-%p')
    os.mkdir(backup_dir)  # Create the session backup folder
    return backup_dir

def print_text(showText):   # This center formats text automatically
    max_line_length = max([len(line) for line in showText]) + 4
    print(''.join(['+' for _ in range(max_line_length)]))
    for line in showText:
        padding = max_line_length - len(line) - 2
        padding_left = padding // 2
        print('+{}+'.format(' ' * padding_left + line + ' ' * (padding - padding_left)))
    print(''.join(['+' for _ in range(max_line_length)]))

def selector_picker(listvar, printtext):
    options = list(listvar)      # this only contains available options from self.get_available_options
    if not len(options):
        print('No options were given')
        time.sleep(2)
        return
        
    print('\n{}'.format(printtext))
    for idx, select in enumerate(options):
        print('{}. {}'.format(idx + 1, select))
    indexChoice = int(input("Enter Index Value: "))
    indexChoice -= 1 

    selected_option = listvar[indexChoice]
    return selected_option


## ============= Installer Support Funcs ============= ##
# Created by @ShaneSmiskol some modifications by coltonton
def installer_chooser():
    # Do self install checks
    if IS_AUTO_INSTALL == True:
        #Get DO_NOT_AUTO_INSTALL var from its file
        file = open('./support/do_not_auto.txt', 'r')       # Open do_not_auto flag file
        DO_NOT_AUTO_INSTALL = file.read()                     # Store flag
        file.close
        print('Debug: The value as read from do_not_auto.txt is {}'.format(DO_NOT_AUTO_INSTALL))

        # See if user has a self installed theme. If not - auto install is permited!
        if path.exists('/storage/emulated/0/eon_custom_themes_self_installed.txt'):
            IS_SELF_INSTALLED = True
        else:
            IS_SELF_INSTALLED = False
        print('DEBUG: IS_SELF_INSTALLED is {}'.format(IS_SELF_INSTALLED))

        # Check if is auto install and do_not_auto is false and IS_SELF_INSTALLED is false
        if DO_NOT_AUTO_INSTALL == '0' and IS_SELF_INSTALLED == False:  
            #Open auto installed version file & store as CURRENT_AUTO_VER - the currently installed version
            file2 = open('./support/auto_install_ver.txt', 'r')
            CURRENT_AUTO_VER = file2.read()
            file2.close
            print('DEBUG: The Value of the read auto_install_ver.txt is {}'.format(CURRENT_AUTO_VER))

            # Detrtmine if installed version is desired version and act
            if CURRENT_AUTO_VER is not DESIRED_AUTO_VER:         # If current installed version != desired version
                print('First install or new version detected, installing.....')
                return 'Do_Auto'                                       # Do Auto install theme
            else:                                                # If current installed version == desired version 
                print('Most current version installed, Terminating.....')
                return None
        
        # Check If both the do_not_install flag is set and user has a self installed theme, return none to cancel and exit
        elif DO_NOT_AUTO_INSTALL == '1' and IS_SELF_INSTALLED is True:
            print('Do Not install flag set by user & a self installed theme exists terminating....') 
            return None
        
        # Check If do_not_install flag set,return none to cancel and exit
        elif DO_NOT_AUTO_INSTALL == '1':
            print('Do Not install flag set by user!! Terminating....') 
            return None
        
        # Check if user has a self installed theme, return none to cancel and exit
        elif IS_SELF_INSTALLED == True:
            print('A self installed theme exists!! Terminating....') 
            return None


    # Else return self installer
    elif IS_AUTO_INSTALL == False:                                                  
        return 'Do_Self' 

def get_user_theme():           # Auto discover themes and let user choose!
    try:
        available_themes = [t for t in os.listdir(CONTRIB_THEMES)]
    except FileNotFoundError:
        print("\nCRITICAL ERROR: Run this program using 'exec ./theme_install.py' ++++++\n")

    available_themes = [t for t in os.listdir(CONTRIB_THEMES)]
    available_themes = [t for t in available_themes if os.path.isdir(os.path.join(CONTRIB_THEMES, t))]
    available_themes = [t for t in available_themes if t not in EXCLUDED_THEMES]
    lower_available_themes = [t.lower() for t in available_themes]
    print('\n*\nAvailable themes:')

    for idx, theme in enumerate(available_themes):
        print('{}. {}'.format(idx + 1, theme))
    #print('\nType `restore` or enter 69 to restore a backup')
    print('Type `exit` or enter 0 to exit.')
    while 1:
        theme = input('\nChoose a theme to install (by name or index): ').strip().lower()
        print()
        #if theme in ['restore', 'r']:
        #  return 'restore'
        if theme in ['exit', 'e', '0']:
            exit()
        if theme.isdigit():
            theme = int(theme)
            if theme == 69:
                print('nice\n')
            if theme > len(available_themes):
                print('Index out of range, try again!')
                continue
            return available_themes[int(theme) - 1]
        else:
            if theme in lower_available_themes:
                return available_themes[lower_available_themes.index(theme)]
            sims = [str_sim(theme, t.lower()) for t in available_themes]
            most_sim_idx = max(range(len(sims)), key=sims.__getitem__)
            theme = available_themes[most_sim_idx]
            if sims[most_sim_idx] >= MIN_SIM_THRESHOLD:
                print('Selected theme: {}'.format(theme))
                print('Is this correct?')
                print('[Y/n]: ', end='')
                if input().lower().strip() in ['yes', 'y', 1, 'ye']:
                    return theme
            else:
                print('Unknown theme, try again!')
    
def mark_self_installed():      # Creates a file letting the auto installer know if a self theme installed
    if not path.exists('/storage/emulated/0/eon_custom_themes_self_installed'):
        f = open("/storage/emulated/0/eon_custom_themes_self_installed.txt", "w")
        f.close

def get_OP_Ver_Loc():           # Get OpenPilot Version & Location
    global OP_VER
    global OP_LOC
    while True:
        if path.exists('/data/openpilot'):
            print("\n*\nOpenPilot Location Auto-Detected as /data/openpilot")
            print('Is This The Correct OpenPilot Directory?')
            response = input('[1.Yes / 2.No]: ').lower().strip()
        else:
            print("\n*\nOpenPilot Location Not Auto-Detected")     
            response = '2'
        if response == '1' or response == '2':
            break

    if response == "2":
        print('What Is The Correct OpenPilot directory?')
        OP_LOC = input('/data/').lower().strip()
    else:
        OP_LOC = 'openpilot'

    OPVER = ''
    file = open(('/data/{}/RELEASES.md'.format(OP_LOC)), 'r')
    file.seek(10)
    while True:
        temp = file.read(1)
        if(temp != " "):
            OPVER = OPVER + temp
        else:
            OP_VER = float(OPVER)
            break

    print("\n*\nOpenPilot Version Auto-Detected as {} from /data/{}".format(OP_VER, OP_LOC))
    return OP_VER, OP_LOC


##================= Installer Code =================== ##
def INSTALL_BOOT_LOGO(eon_type, backup_dir, install_from_path):
    if eon_type == 'OP3T':
        boot_logo_device_path = '/dev/block/sde17'
        boot_lego_name = 'LOGO'
    elif eon_type == 'LeEco':
        boot_logo_device_path = '/dev/block/bootdevice/by-name/splash'
        boot_lego_name = 'SPLASH'
    os.system('cp {} {}/{}'.format(boot_logo_device_path, backup_dir, boot_lego_name))    # Make Backup
    os.system('dd if={} of={}'.format(install_from_path, boot_logo_device_path))           # Replace
    print('Boot Logo installed! Original file(s) backed up to {}'.format(backup_dir, boot_lego_name))

def INSTALL_BOOTANIMATION(backup_dir, install_from_path, color=''):
    os.system('mount -o remount,rw /system')                                                       # /system read only, must mount as rw
    os.system('mv /system/media/bootanimation.zip {}'.format(backup_dir))       # Backup
    os.system('cp {}/{}bootanimation.zip /system/media/bootanimation.zip'.format(install_from_path, color))  # Replace
    os.system('chmod 666 /system/media/bootanimation.zip')                                         # Need to chmod to edet permissions to 666
    print('\nBoot Animation installed! Original file(s) backed up to {}'.format(backup_dir))

def INSTALL_SPINNER(backup_dir, opver, opdir, install_from_path, con_output):
    # Check if theme contributer provided a spinner logo
    if path.exists('{}/img_spinner_comma.png'.format(install_from_path)):                               #Contibuter Did Provide
        os.system('mv /data/{}/selfdrive/assets/img_spinner_comma.png {}/spinner'.format(opdir, backup_dir))                        #Backup spinner logo
        os.system('cp {}/img_spinner_comma.png /data/{}/selfdrive/assets'.format(install_from_path, opdir)) #Replace spinner logo supplied custom
        custom_logo = True                                                                                                               #Add custom_logo flag
    # Check if theme contributer provided a spinner track
    if path.exists('{}/img_spinner_track.png'.format(install_from_path)):                               #Contibuter Did Provide
        os.system('mv /data/{}/selfdrive/assets/img_spinner_track.png {}/spinner'.format(opdir, backup_dir))                        #Backup spinner track
        os.system('cp {}/img_spinner_track.png /data/{}/selfdrive/assets'.format(CONTRIB_THEMES, self.selected_theme, opdir)) #Replace spinner track supplied custom
        custom_track = True                                                                                                              #Add custom_track flag
    # Check if theme contributer provided a spinner.c
    #if raveRainbow == True:                                                                                                          #User wants rave rainbow
        #os.system('mv /data/{}/selfdrive/common/spinner.c {}/spinner'.format(opdir, backup_dir))                                    #Backup spinner.c
        #os.system('cp ./support/spinner/rainbow_spinner.c /data/{}/selfdrive/common/spinner.c'.format(opdir))                            #Replace spinner.c with rave rainbow spinner.c
        #custom_c = True                                                                                                                  #Add custom_C flag                                                                                                                  #Add custom_C flag
    if path.exists('{}/spinner.c'.format(install_from_path)) and opver == OP_VER <= 7.8:                #Contibuter Did Provide      
        os.system('mv /data/{}/selfdrive/common/spinner.c {}/spinner'.format(opdir, backup_dir))                                    #Backup spinner.c                
        os.system('cp {}/spinner.c /data/{}/selfdrive/common'.format(CONTRIB_THEMES, self.selected_theme, opdir))             #Replace spinner.c with supplied custom 
        custom_c = True                                                                                                                  #Add custom_C flag

    #Final make new spinner & finish if non QT
    if OP_VER <= 7.8:
        print('\nBuilding new spinner files, please wait..... This should take under a minute....')
        os.system('cd /data/openpilot/selfdrive/ui/spinner && make{}'.format(self.con_output))
    print('\n{} spinner installed successfully! Original file(s) backed up to {}'.format(opdir, self.backup_dir))


## ================= Restor-er Code ================= ##
# Created by @ShaneSmiskol modified version of get_user_theme() to get all backups by Coltonton
def get_user_backups(exclude):
    available_backups = [t for t in os.listdir(BACKUPS_DIR)]
    available_backups = [t for t in available_backups if os.path.isdir(os.path.join(BACKUPS_DIR, t))]
    available_backups = [t for t in available_backups if t not in exclude]
    lower_available_backups = [t.lower() for t in available_backups]
  
    print('\nAvailable backups:')
    for idx, backup in enumerate(available_backups):
        print('{}. {}'.format(idx + 1, backup))
    if os.path.exists('/data/eon-custom-themes/{}/Comma-Default'.format(CONTRIB_THEMES)):
        default_restore_exists = 1
        print("\nEnter 'r' to restore the Comma-Default theme")
    else:
        default_restore_exists = 0
    print('\nType `exit` or enter 0 to exit.')
  
    while 1:
        backup = input('\nChoose a backup to install (by index value): ').strip().lower()
        print()
        if backup in ['exit', 'Exit', 'E', 'e', '0']:
            exit()
        if backup in ['r', 'R' and default_restore_exists == 1]:
            return 'Comma-Default'
        if backup.isdigit():
            backup = int(backup)
            if backup > len(available_backups):
                print('Index out of range, try again!')
                continue
            return available_backups[int(backup) - 1]
        else:
            print('Please enter only Index number value!!')
            continue


## ====================== Misc ====================== ##
def backup_overide_check(backup_dir, theme_type):
    #Check if there was a backup already this session to prevent accidental overwrites
    if path.exists('{}/{}'.format(backup_dir, theme_type)):
        print('\nIt appears you already made a(n) {} install this session'.format(theme_type)) 
        print('continuing will overwrite the last {} backup'.format(theme_type))
        print('the program made this session already!!!')
        print('Would you like to continue and overwrite previous?')
        if not is_affirmative():
            print('Not installed.......')
            return True
    else:
        os.mkdir('{}/{}'.format(backup_dir, theme_type))
        return False

def REBOOT():
    print('\nRebooting.... Thank You, Come Again!!!')
    os.system('am start -a android.intent.action.REBOOT')  # reboot intent is safer (reboot sometimes causes corruption)
    return 'exit'

def QUIT_PROG():
    print('\nThank you come again! You will see your changes next reboot!\n')
    exit()  

# Created by @ShaneSmiskol
def str_sim(a, b):              # Part of Shane's get_user_theme code
    return difflib.SequenceMatcher(a=a, b=b).ratio()