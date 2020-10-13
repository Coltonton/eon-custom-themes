import os
import sys
import time
import difflib
from os import path
from datetime import datetime
from support.support_variables import AUTO_WELCOME_TEXT, BACKUPS_DIR, CONTRIB_THEMES, DESIRED_AUTO_VER, EXCLUDED_THEMES, IS_AUTO_INSTALL
from support.support_variables import MIN_SIM_THRESHOLD, RESTORE_WELCOME_TEXT, WELCOME_TEXT

os.chdir(os.path.dirname(os.path.realpath(__file__)))  # __file__ is safer since it doesn't change based on where this file is called from

## ================= Shared ================= ##
def get_device_theme_data():
  # Crude device detection, *shrug* it works! LeEco does not have tristate!
  if path.exists('/sys/devices/virtual/switch/tri-state-key'): #If 3T-ON
    print('\n*** OG OnePlus EON Device Detected ***')
    BOOT_LOGO_THEME_PATH = 'OP3T-Logo/LOGO'                      # Set the boot logo theme path for 3T
    BOOT_LOGO_PATH = '/dev/block/sde17'                          # Set the boot logo directory for 3T
    BOOT_LOGO_NAME = 'sde17'                                     # Set the boot logo name for 3T
  else:                                                        #If LEON/Two
    print('\n*** LeEco EON (Gold/Comma 2) Device Detected ***\n')
    BOOT_LOGO_THEME_PATH = 'LeEco-Logo/SPLASH'                   # Set the boot logo theme path for Leo
    BOOT_LOGO_PATH = '/dev/block/bootdevice/by-name/splash'      # Set the boot logo directory for Leo
    BOOT_LOGO_NAME = 'splash'                                    # Set the boot logo name for Leo
  print('IMPORTANT: Soft-bricking is likely if this detection is incorrect!')
  return BOOT_LOGO_THEME_PATH, BOOT_LOGO_PATH, BOOT_LOGO_NAME

def is_affirmative():           # Ask user for confirmation
  u = input('[1.Yes / 2.No]: ').lower().strip()
  return u in ['yes', 'ye', 'y', '1']

def make_backup_folder():
  # Check if theme backup folder doesnt exist then create
  if not os.path.exists('/storage/emulated/0/theme-backups'):
    os.mkdir('/storage/emulated/0/theme-backups')
  # Create session backup folder named with date & time 
  backup_dir = datetime.now().strftime('/storage/emulated/0/theme-backups/backup.%m-%d-%y--%I.%M.%S-%p')
  os.mkdir(backup_dir)  # Create the session backup folder
  return backup_dir


## =============== Installer ================ ##.
# Created by @ShaneSmiskol some modifications by coltonton
def get_user_theme():           # Auto discover themes and let user choose!
  available_themes = [t for t in os.listdir(CONTRIB_THEMES)]
  available_themes = [t for t in available_themes if os.path.isdir(os.path.join(CONTRIB_THEMES, t))]
  available_themes = [t for t in available_themes if t not in EXCLUDED_THEMES]
  lower_available_themes = [t.lower() for t in available_themes]
  print('\nAvailable themes:')
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
      #if theme == 69:
      #  print('\nnice\n')
      #  return 'restore'
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

def installer_chooser():
  #Get DO_NOT_AUTO_INSTALL var from its file
  file = open('./support/do_not_auto.txt', 'r')       # Open do_not_auto flag file
  DO_NOT_AUTO_INSTALL = file.read()                     # Store flag
  file.close

  # See if user has a self installed theme. If not auto install permited!
  if path.exists('/storage/emulated/0/eon_custom_themes_self_installed.txt'):
    IS_SELF_INSTALLED = True
  else:
    IS_SELF_INSTALLED = False

  # Check if auto install and do_not_auto is false
  if IS_AUTO_INSTALL == True and DO_NOT_AUTO_INSTALL is '0' and IS_SELF_INSTALLED == False:  
    #Open auto installed version file & store as CURRENT_AUTO_VER - the currently installed version
    file2 = open('./support/auto_install_ver.txt', 'r')
    CURRENT_AUTO_VER = file2.read()
    file2.close

    # Detrtmine if installed version is desired version and act
    if CURRENT_AUTO_VER is not DESIRED_AUTO_VER:         # If current installed version != desired version
      print('First install or new version detected, installing.....')
      return 'Do_Auto'                                       # Do Auto install theme
    else:                                                # If current installed version == desired version 
      print('Most current version installed, canceling.....')
      return None
    
  # If is auto install but do_not_install flag set, if so cancel and exi
  elif IS_AUTO_INSTALL == True and DO_NOT_AUTO_INSTALL is '1':
    print('Do Not install flag set!! Canceling....') 
    return None
    
  # Check if user has a self installed theme, if so cancel and exit
  elif IS_AUTO_INSTALL == True and IS_SELF_INSTALLED == True:
    print('A self installed theme exists!! Canceling....') 
    return None

  # Else return self installer
  else:                                                  
      return 'Do_Self' 

def mark_self_installed():      # Creates a file letting the auto installer know if a self theme installed
  if not path.exists('/storage/emulated/0/eon_custom_themes_self_installed'):
    f = open("/storage/emulated/0/eon_custom_themes_self_installed.txt", "w")
    f.close

# Created by @ShaneSmiskol some modifications by coltonton
def print_welcome_text(text):   # This center formats text automatically
  if text == 's':        # If self text
    showText = WELCOME_TEXT
  elif text == 'a':      # If auto text
    showText = AUTO_WELCOME_TEXT
  elif text == 'r':      # If restore text
    showText = RESTORE_WELCOME_TEXT

  max_line_length = max([len(line) for line in showText]) + 4
  print(''.join(['+' for _ in range(max_line_length)]))
  for line in showText:
    padding = max_line_length - len(line) - 2
    padding_left = padding // 2
    print('+{}+'.format(' ' * padding_left + line + ' ' * (padding - padding_left)))
  print(''.join(['+' for _ in range(max_line_length)]))
  time.sleep(2)  # Pause for suspense, and so can be read


## ================ Restorer ================ ##
# Created by @ShaneSmiskol modified version of get_user_theme() to get all backups by Coltonton
def get_user_backups(exclude):
  available_backups = [t for t in os.listdir(BACKUPS_DIR)]
  available_backups = [t for t in available_backups if os.path.isdir(os.path.join(BACKUPS_DIR, t))]
  available_backups = [t for t in available_backups if t not in exclude]
  lower_available_backups = [t.lower() for t in available_backups]
  print('\nAvailable backups:')
  for idx, backup in enumerate(available_backups):
    print('{}. {}'.format(idx + 1, backup))
  print('Type `exit` or enter 0 to exit.')
  while 1:
    backup = input('\nChoose a backup to install (by index value): ').strip().lower()
    print()
    if backup in ['exit', 'Exit', 'E', 'e', '0']:
      exit()
    if backup.isdigit():
      backup = int(backup)
      if backup > len(available_backups):
        print('Index out of range, try again!')
        continue
      return available_backups[int(backup) - 1]
    else:
      print('Please enter only Index number value!!')
      continue


## ================== Misc ================== ##
# Created by @ShaneSmiskol
def str_sim(a, b):              # Part of Shane's get_user_theme code
  return difflib.SequenceMatcher(a=a, b=b).ratio()