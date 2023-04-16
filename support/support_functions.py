#!/usr/bin/python
import os, sys, time, platform, difflib, json
from os import path
from datetime import datetime
from support.support_variables import *
os.chdir(os.path.dirname(os.path.realpath(__file__)))  # __file__ is safer since it doesn't change based on where this file is called from

## ================= Shared ================= ##
def get_device_theme_data(onprocess='null'):
    DebugPrint('Getting Device Data...', 'sf')
    devicedata = dict
    # Crude device detection, *shrug* it works! LeEco does not have tristate!
    if path.exists('/sys/devices/virtual/switch/tri-state-key'): #If 3T-ON
        print('\n*** OG OnePlus EON Device Detected! OooOoOooo we got a rebel! :O ***')
        print('PLEASE NOTE! Comma wrongfully deprecated the 3T-EON, this program')
        print('will still work for as long as feasable but may not be as maintaind as the')
        print('Eon-Gold and possibly with less features.. I do this for free and fun')
        print('making money by force upgrading is the least of my concern...')
        devicedata = {
            "EON_TYPE"             : 'OP3T',                                # EON type is OP3T
            "BOOT_LOGO_THEME_NAME" : 'LOGO',                                # Set the theme name for the logo for 3T
            "BOOT_LOGO_THEME_PATH" : 'OP3T-Logo/LOGO',                      # Set the theme boot logo path for 3T
            "BOOT_LOGO_NAME"       : 'sde17',                               # Set the device boot logo name for 3T
            "BOOT_LOGO_PATH"      : '/dev/block/sde17'                    # Set the device boot logo directory for 3T
        }
    else:                                                        #If LEON/Two
        print('\n*** {} ***'.format("LeEco EON (LeON/Gold/Comma 2) Device Detected" if not DEVMODE else "[DEVMODE] Device Faked as LeEco based"))
        devicedata = {
            "EON_TYPE"             : 'LeEco',                               # EON type is LeEco
            "BOOT_LOGO_THEME_NAME" : 'SPLASH',                              # Set the theme name for the logo for Leo
            "BOOT_LOGO_THEME_PATH" : 'LeEco-Logo/SPLASH',                   # Set the theme boot logo path for  Leo
            "BOOT_LOGO_NAME"       : 'splash',                              # Set the device boot logo name for Leo
            "BOOT_LOGO_PATH"       : "/dev/block/bootdevice/by-name/splash" # Set the device boot logo directory for Leo
        }
    print('IMPORTANT: {}-bricking is likely if this detection is incorrect!'.format("Soft" if not DEVMODE else "SEVERE"))

    if not DEVMODE:
        time.sleep(4)  # Pause for suspense, and so can be read
  
    cycle = 0
    for x in devicedata.keys():
        DebugPrint('{} = {}'.format(x, devicedata[x]), overide="sf" ,multi=1 if cycle <1 else 2)
        cycle = cycle +1
    return devicedata

def is_affirmative(key1="Yes", key2="No", output="Not installing..."):           # Ask user for confirmation
    #DebugPrint('Asking to confirm', 'sf')
    key1_s = key1.lower().strip()                   # lowercase key1 for compare
    key1_f = key1_s[0] if key1_s[0] != "n" else "y" # Get first letter of lowercase key1 Just in case if is "n" (same as no) just ignore...
    afirm = input('[1.{} / 2.{}]: '.format(key1,key2)).lower().strip()
    DebugPrint('Got {}'.format(afirm), 'sf')
    if ((afirm in IS_AFFIRMATIVE_YES) or (afirm in [key1_s, key1_f])): 
        return True
    if afirm in IS_AFFIRMATIVE_UNSURE:
        print("WTF do you mean {}... I'm going to assume NO so I dont brick ya shi...".format(afirm))
    if afirm in ['i dont talk to cops without my lawyer present']:
        print("Attaboy oat!")
    
    if output != "silent": print('{}'.format(output))
    time.sleep(1.5) 
    return False

def make_backup_folder():
    DebugPrint('Getting backup Folder congig', fromprocess_input="sf")
    # Check if theme backup folder doesnt exist then create
    if not os.path.exists(BACKUPS_DIR): 
        DebugPrint('It doesent exist... Creating at {}'.format(BACKUPS_DIR), fromprocess_input="sf")
        os.mkdir(BACKUPS_DIR)
    # Create session backup folder
    while True:
        print("\n*\nDo You wish to name your backup or use default? ")
        if is_affirmative(key1="Custom", key2="Default", output="silent"):
            usersChoice = input("Enter: backup.")
            backup_dir = '{}/backup.{}'.format(BACKUPS_DIR, usersChoice)
            if path.exists('{}'.format(backup_dir)):
                print("Directory already exists... Overwrite Data?")
                if is_affirmative(key1="Overwrite", key2="Don't Overwrite"):
                    os.removedirs(backup_dir)
                    break
                else:
                    print("Please try again...")
            else:
                break
        else:
            backup_dir = datetime.now().strftime('{}/backup.%m-%d-%y--%I:%M.%S-%p'.format(BACKUPS_DIR))
            break
    os.mkdir(backup_dir)  # Create the session backup folder
    DebugPrint('Created session backup folder at {}'.format(backup_dir), fromprocess_input="sf")
    return backup_dir

def print_text(showText, withver=0):   # This center formats text automatically
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

#########################################################
## ============= Installer Support Funcs ============= ##
#########################################################
# Created by @ShaneSmiskol some modifications by coltonton
'''def installer_chooser():        # Choose what installer to use (DEPRICATED) 
    DebugPrint("installer_chooser() called", fromprocess_input="sf")                                                   
    return 'Do_Self' '''

def get_aval_themes():          # Auto discover themes and let user choose!
    DebugPrint("get_aval_themes() called", fromprocess_input="sf")
    try:
        available_themes = [t for t in os.listdir(CONTRIB_THEMES)]
    except FileNotFoundError:
        print("\nCRITICAL ERROR: Run this program using 'exec ./theme_install.py' ++++++\n")
        DebugPrint("File Not Found or doesnt have access", fromprocess_input="sf")

    available_themes = [t for t in os.listdir(CONTRIB_THEMES)]
    available_themes = [t for t in available_themes if os.path.isdir(os.path.join(CONTRIB_THEMES, t))]
    if DEVMODE:
        DebugPrint("Found all these directorys: ", multi=available_themes, fromprocess_input="sf")
        DebugPrint("Are Excluded in support.support_variables.py: ", multi=EXCLUDED_THEMES, fromprocess_input="sf")
    available_themes = [t for t in available_themes if t not in EXCLUDED_THEMES]
    lower_available_themes = [t.lower() for t in available_themes]
    print('\n*\nAvailable themes:')

    for idx, theme in enumerate(available_themes):
        print('{}. {}'.format(idx + 1, theme))
    #print('\nType `restore` or enter 69 to restore a backup')
    print('Type `exit` or enter 0 to exit.')
    while 1:
        theme = input('\nChoose a theme to install (by name or index): ').strip().lower()
        DebugPrint("User entered: {}".format(theme), fromprocess_input="sf")
        print()
        #if theme in ['restore', 'r']:
        #  return 'restore'
        if theme in ['exit', 'e', '0', 'stop']:
            DebugPrint("Got Exit", fromprocess_input="sf")
            exit()
        if theme in ['devmode']:
            return 'devmode'
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
                if input().lower().strip() in ['yes', 'ye', 'y', '1', "j", "ja", "si"]:
                    DebugPrint("You entered: {}".format(input), fromprocess_input="sf")
                    return theme
            else:
                print('Unknown theme, try again!')
                DebugPrint("Did not match", fromprocess_input="sf")
    
def mark_self_installed():      # Creates a file letting the auto installer know if a self theme installed
    DebugPrint("mark_self_installed() called", fromprocess_input="sf")
    DebugPrint("Marking as self installed to /storage/emulated/0/eon_custom_themes_self_installed'", fromprocess_input="sf")
    if Dev_DoInstall() and not path.exists ('/storage/emulated/0/eon_custom_themes_self_installed'):
        f = open("/storage/emulated/0/eon_custom_themes_self_installed.txt", "w")
        f.close

def get_OP_Ver_Loc():           # Get OpenPilot Version & Location
    DebugPrint("mark_self_installed() called", fromprocess_input="sf")
    #Get Location Information
    while True:
        if path.exists('/data/openpilot'):
            print("\n*\nOpenPilot Location Auto-Detected as /data/openpilot")
            print('Is This The Correct OpenPilot Directory?')
            response = input('[1.Yes / 2.No]: ').lower().strip()
        else:
            print("\n*\nOpenPilot Location Not Auto-Detected")     
            response = '2'
        if response == '1' or response == '2': break

    while True:
        if response == "1":
            OP_Location = '/data/openpilot'
        if response == "2" or DEVMODE is True and response == "2":
            print('What Is The Correct OpenPilot directory?')
            #print("Enter 'overide' to choose a location other then /data/")
            OP_Location = input('/data/')
            if OP_Location in ["override", "o"]: 
                OP_Location = input('Enter Full Path To OpenPilot ex. /data/openpilot: ')
            else: 
                OP_Location = "/data/{}".format(OP_Location)

        print("Looking For {}/releases.md to auto determine version...".format(OP_Location))
        
        if os.path.isfile("{}/RELEASES.md".format(OP_Location)) is True: 
            print("I Found an OpenPilot Software Release!") 
            break
        else: 
            print("You typed {}".format(OP_Location))
            print("Hmm I could not find that or an error occured... Try Again...")

    #Start Getting Version Information
    filesize = os.path.getsize('{}/RELEASES.md'.format(OP_Location))
    DebugPrint("Got {} bytes".format(filesize), fromprocess_input="sf")
    if filesize < 26:
        print("\n*")
        print("Invalid RELEASES.md found in {}. File size invalid.".format(OP_Location))
        print("Please see issue #28 on my repo https://github.com/Coltonton/eon-custom-themes/issues/28")
        print("\n*")
        print("Auto-detection failed please manually enter...")
        OP_Version=input("OpenPilot Version 0.")
    else:
        OP_Version = ''
        file = open(('{}/RELEASES.md'.format(OP_Location)), 'r')
        OP_Version = file.readline(13)
        OP_Version = OP_Version.strip("Version 0.")
        file.close()

        print("OpenPilot Version Auto-Detected as 0.{} from {}".format(OP_Version, OP_Location))
    OP_info_dict = {
        "OP_Version": OP_Version,
        "OP_Location": OP_Location
    }
    return OP_info_dict

#########################################################
##================= Installer Code =================== ##
#########################################################
def INSTALL_BOOT_LOGO(DeviceData, backup_dir, install_from_path, re=False):               #INSTALL_BOOT_LOGO
    DebugPrint("INSTALL_BOOT_LOGO() called", multi=[DeviceData["BOOT_LOGO_PATH"], DeviceData["BOOT_LOGO_THEME_NAME"], backup_dir, install_from_path], fromprocess_input="sf")
    DebugPrint("Installing Boot Logo...", fromprocess_input="sf")
    os.system('cp {} {}/{}'.format(DeviceData["BOOT_LOGO_PATH"], backup_dir, DeviceData["BOOT_LOGO_THEME_NAME"]))    # Make Backup
    os.system('dd if={} of={}'.format(install_from_path, DeviceData["BOOT_LOGO_PATH"]))           # Replace
    if re == False:
        print('#Boot Logo installed! Original file(s) backed up to {}'.format(backup_dir, DeviceData["BOOT_LOGO_THEME_NAME"]))
    elif re == True:
        print('#Boot Logo re-installed from backup! Current file(s) backed up to {}'.format(backup_dir, DeviceData["BOOT_LOGO_THEME_NAME"]))

def INSTALL_BOOTANIMATION(backup_dir, install_from_path, color='', re=False):             #INSTALL_BOOTANIMATION
    DebugPrint("INSTALL_BOOTANIMATION() called".format([backup_dir, install_from_path, color]), fromprocess_input="sf")
    DebugPrint("Installing Boot Animation...", fromprocess_input="sf")
    os.system('mount -o remount,rw /system')                                                       # /system read only, must mount as rw
    os.system('mv /system/media/bootanimation.zip {}/bootanimation.zip'.format(backup_dir))       # Backup
    os.system('cp {}/{}bootanimation.zip /system/media/bootanimation.zip'.format(install_from_path, color))  # Replace
    os.system('chmod 666 /system/media/bootanimation.zip')
    if re == False:                                         # Need to chmod to edet permissions to 666
        print('#Boot Animation installed! Original file(s) backed up to {}'.format(backup_dir))
    elif re == True:
        print('#Boot Animation Re-installed! Current file(s) backed up to {}'.format(backup_dir))

def INSTALL_QT_SPINNER(backup_dir, OP_INFO, install_from_path, con_output='', re=False):  #INSTALL_QT_SPINNER
    DebugPrint("INSTALL_QT_SPINNER() called".format([backup_dir, OP_INFO["OP_Location"], OP_INFO["OP_Version"], install_from_path]), fromprocess_input="sf")
    flags=[]
    # Check if theme contributer provided a spinner logo
    if path.exists('{}/img_spinner_comma.png'.format(install_from_path)):                   #Contibuter Did Provide
        DebugPrint("Installing logo...", fromprocess_input="sf")
        os.system('mv {}/selfdrive/assets/img_spinner_comma.png {}/spinner'.format(OP_INFO["OP_Location"], backup_dir))      #Backup spinner logo
        os.system('cp {}/img_spinner_comma.png {}/selfdrive/assets'.format(install_from_path, OP_INFO["OP_Location"]))       #Replace spinner logo supplied custom
        flags.append("custom_logo")                                                                                                #Add custom_logo flag
    # Check if theme contributer provided a spinner track
    if path.exists('{}/img_spinner_track.png'.format(install_from_path)):                   #Contibuter Did Provide
        DebugPrint("Installing track...", fromprocess_input="sf")
        os.system('mv {}/selfdrive/assets/img_spinner_track.png {}/spinner'.format(OP_INFO["OP_Location"], backup_dir))      #Backup spinner track
        os.system('cp {}/img_spinner_track.png {}/selfdrive/assets'.format(install_from_path, OP_INFO["OP_Location"]))       #Replace spinner track supplied custom
        flags.append("custom_track")                                                                                               #Add custom_trackflag
    # Check if theme contributer provided a spinner.c                                                                                                                                                                                                          #Add custom_C flag                                                                                                                  #Add custom_C flag
    #if path.exists('{}/spinner.c'.format(install_from_path)) and opver == OP_VER <= 7.8:   #Contibuter Did Provide      
        #DebugPrint("Installing spinner.c...", fromprocess_input="sf")
        #os.system('mv {}/selfdrive/common/spinner.c {}/spinner'.format(opdir, backup_dir))                                   #Backup spinner.c                
        #os.system('cp {}/spinner.c {}/selfdrive/common'.format(install_from_path, opdir))                                    #Replace spinner.c with supplied custom 
        #flags.append("custom_c")  
    if re == False:                                         # Need to chmod to edet permissions to 666
        print('#OpenPilot Spinner installed! Original file(s) backed up to {}'.format(backup_dir))
    elif re == True:
        print('#OpenPilot Spinner Re-installed! Current file(s) backed up to {}'.format(backup_dir))                                                                                                 #Add custom_C flag

## ================= Restor-er Code ================= ##
# Created by @ShaneSmiskol modified version of get_aval_themes() to get all backups by Coltonton
def get_user_backups(exclude):  #Gets users backups in /sdcard/theme-backups
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

def restore_comma_default(DeviceData, backup_dir):
    print('\nSelected to restore Comma-Default theme. Continue?')
    print('Process is fully automagic!')
    if not is_affirmative():
        return None

    print('Please wait..... This should only take a few moments!\n')
    
    #Boot-Logo
    install_from_path = '{}/Comma-Default/{}'.format(CONTRIB_THEMES, DeviceData["BOOT_LOGO_THEME_PATH"])
    INSTALL_BOOT_LOGO(DeviceData, backup_dir, install_from_path)

    #Boot-Animation
    install_from_path = '{}/Comma-Default/'.format(CONTRIB_THEMES)
    INSTALL_BOOTANIMATION(backup_dir, install_from_path)

    print('\nThank you come again! - Boot Logo & Boot Animation factory restored!!')
    exit()

#########################################################
## ====================== Misc ======================= ##
#########################################################
'''def set_running(data):
    with open('person.txt', 'w') as json_file:
        json.dump(data, json_file)

def get_running():
    with open('./support/vars.json', 'r') as f:
        datadict = json.load(f)
    x = datadict['Launched Program']
    return x
'''
def REBOOT():                   #Reboot EON Device
    print('\nRebooting.... Thank You, Come Again!!!\n\n########END OF PROGRAM########\n')
    os.system('am start -a android.intent.action.REBOOT')  # reboot intent is safer (reboot sometimes causes corruption)
    sys.exit()

def QUIT_PROG():                # Terminate Program friendly
    print('\nThank you come again! You will see your changes next reboot!\n\n########END OF PROGRAM########\n')
    sys.exit()  

def str_sim(a, b):              # Part of @ShaneSmiskol's get_aval_themes code
    return difflib.SequenceMatcher(a=a, b=b).ratio()

#########################################################
## ==================== DEV/Debug ==================== ##
#########################################################
def setVerbose(a=False):        #Set Verbosity (DEPRICATED)
    if a == True:
        con_output = ' >/dev/null 2>&1'  # string to surpress output
    else:
        con_output = ''  # string to surpress output
    print('[DEBUG MSG]: Verbose ' + a)

def DebugPrint(msg, fromprocess_input="null", overide=0, multi=0):  #My own utility for debug msgs
    if VERBOSE == True or DEVMODE == True or overide == 1:
        now = datetime.now()
        debugtime = now.strftime("%m/%d %I:%M.%S")
        runprocess = "theme_install.py"
        fromprocess_input = runprocess if fromprocess_input == "null" else fromprocess_input
        if fromprocess_input == "sf":
            runprocess = (runprocess.strip(".py")+"/support/support_functions.py")

        if type(multi) == list:
            print("\n##[DEBUG][{} {}] || GOT MULTIPLE DATA".format(debugtime, runprocess))
            print("##[DEBUG] {}".format(msg))
            for x in range(len(multi)):
                print("--> {}".format(multi[x])),
        else:
            print("##[DEBUG][{} {}] || {}".format(debugtime, runprocess, msg))#] #Debug Msg ()s

def DEV_CHECK():                #Hault Program If Ran On PC/Mac
    global DEV_PLATFORM, DEVMODE, VERBOSE
    # Simple if PC check, not needed but nice to have
    DEV_PLATFORM = platform.system()
    if DEV_PLATFORM in ['Windows', 'Darwin']:
        print(DEV_PLATFORM)
        print("This program only works on Comma EONS & Comma Two, sorry...")
        print("Press enter to exit.")
        u = input('')
        if u == "override":
            print('EON DEVMODE enabled, proceed with great caution!')
            VERBOSE = True
            DEVMODE = True
        else:
            sys.exit()

def Dev_DoInstall():            #Function to ask before installing for use in dev to not screw up my computer, and test logic
    if DEVMODE == True:
        DebugPrint("Developer Mode enabled do you actually want to install?", overide="sf")
        DebugPrint("Type 'install' to install or press enter to skip.", overide="sf")
        askinstall = input("## ").lower().strip()
        if askinstall == "install":
            return True
        else:
            DebugPrint("Install Skipped...", overide="sf")
            return False
    else:
        return True