#!/usr/bin/python
##################################################################################
#                                   VER 2.0                                      #
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
#    ===Created by Colton (Brandon) S. (@C-ton) for the OpenPilot Community===   #
#              === http://endoflinetech.com/eon-custom-themes ===                #
#                                                                                #
#              With a mission to rid all EONS of Comma.ai branding               #
#             And give the people the freedom, knowlage, and power!              #
#                         & to make their EONS purdy!                            #
#                                                                                #
#                         Grab life by the horns                                 #
#                                                                                #
#   A very special thank you to @ShaneSmiskol for creating the theme picker      #
#      for his tireless help, and donating the life of his LeEco EON             #
#           to get the LeEco based EONs supported by this project                #
#                   Although revived least we forget.....                        #
##################################################################################
#                                                                                #
#                     To Get Started Making Your EON Purdy:                      #
#                                                                                #
#                              SSH into your EON:                                #
#  (https://medium.com/@jfrux/comma-eon-getting-connected-with-ssh-3ed6136e4a75) #
#                                                                                #
#              Type the following command if using the main project              #
#                  exec /data/eon-custom-themes/install_theme.py                 #
#                                                                                #
#            Or if trying to use the included package with an OP Fork:           #
#              cd /data/(your openpilot directory)/eon-custom-themes             #
#                          exec ./install_theme.py                               #
#                                                                                #
#               Now follow the prompts and make your selections!                 #
#                  Everything will be done automagically!!!!!                    #
#                                                                                #
#                      Don't forget to tell your friends!!                       #
#                              Love, Cole (@C-ton)                               #
#                                                                                #
#        Did you know that if you have a custom OP fork you can use this         #
#     program to auto install your custom theme for your users automagiclly?     #
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
  print_text('auto')               #Print welcome text with the flag for auto welcome text
else:
  print_text('self')               #Print welcome text with the flag for self welcome text
  
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
      self.get_OP_Ver_Loc()
      self.get_available_options()
      if self.install_function() == 'exit':
        return

  def get_OP_Ver_Loc(self):             # Get OpenPilot Version & Location
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

    print("OpenPilot Version Auto-Detected as {} from /data/{}".format(OP_VER, OP_LOC))

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
    if os.path.exists('{}/{}/spinner'.format(CONTRIB_THEMES, self.selected_theme)) and (OP_VER <= 7.8):
      #self.theme_options.append('Non-QT OpenPilot Spinner')
      pass
    # Check if the selected theme has a QT OpenPilot Spinner asset
    if os.path.exists('{}/{}/spinner'.format(CONTRIB_THEMES, self.selected_theme)) and (OP_VER >= 8.3):
      self.theme_options.append('QT OpenPilot Spinner')

    self.theme_options.append('-Main Menu-')
    self.theme_options.append('-Reboot-')
    self.theme_options.append('-Quit-')

  def install_function(self):           # Self installer program, prompts user on what they want to do
    while 1:
      options = list(self.theme_options)  # this only contains available options from self.get_available_options
      if not len(options):
        print('\n*\nThe selected theme has no resources available for your device! Try another.')
        time.sleep(2)
        return
      
      print('\n*\nWhat resources do you want to install for the {} theme?'.format(self.selected_theme))
      for idx, theme in enumerate(options):
        print('{}. {}'.format(idx + 1, theme))
      indexChoice = int(input("Enter Index Value: "))
      indexChoice -= 1 

      selected_option = self.theme_options[indexChoice]

      if selected_option   == 'Boot Logo':
        #Confirm user wants to install bootlogo
        print('\nSelected to install the {} Boot Logo. Continue?'.format(self.selected_theme))
        if not is_affirmative():
          print('Not installing...')
          time.sleep(1.5)
          continue

        #Check if there was an Boot logo backup already this session to prevent accidental overwrites
        #Returns true if okay to proceed. Gets self.backup_dir & asset type name
        if backup_overide_check(self.backup_dir, 'logo') == True:
          exit()

        #Backup & install new
        install_from_path = ('{}/{}/{}'.format(CONTRIB_THEMES, self.selected_theme, BOOT_LOGO_THEME_PATH))
        INSTALL_BOOT_LOGO(EON_TYPE, self.backup_dir, install_from_path)
        mark_self_installed()       # Create flag in /sdcard so auto installer knows there is a self installation
        print('Press enter to continue!')
        input()

      elif selected_option == 'Non-QT OpenPilot Spinner':
        ##Confirm user wants to install Spinner
        print('\nSelected to install the {} OP Spinner. Continue?'.format(self.selected_theme))
        if not is_affirmative():
          print('Not installing...')
          time.sleep(1.5)
          continue

        ##Ask user if they want to --skip-worktree
          print_text('spin warn')
          print('\nHave you read the statment above, understand, and wish to use it? (its optional)')
          print('Please look at the main README at the `Spinner OP Hack` section for more info....')
          if is_affirmative():
            skip_worktree = True
          else:
            skip_worktree = False

        ##Check if there was a spinner backup already this session to prevent accidental overwrites
        #Returns false if okay to proceed. Gets self.backup_dir & asset type name
        if backup_overide_check(self.backup_dir, 'spinner') == True:
          exit()

        ##Ask user if their OP directory is custom (like arnepilot / dragonpilot)
        opdir = OP_LOC #op_dir_finder()

        ##Ask user if they want @shaneSmiskol rave rainbow spinner
        raveRainbow = ask_rainbow_spinner()

        ##Backup & Copy in relevant files
        install_from_path = ('{}/{}/spinner'.format(CONTRIB_THEMES, self.selected_theme,))
        INSTALL_SPINNER(self.backup_dir, opdir, install_from_path, rave_rainbow, skip_worktree, self.con_output)
        # Check if theme contributer provided a spinner logo
        if path.exists('{}/{}/spinner/img_spinner_comma.png'.format(CONTRIB_THEMES, self.selected_theme)):                               #Contibuter Did Provide
          os.system('mv /data/{}/selfdrive/assets/img_spinner_comma.png {}/spinner'.format(opdir, self.backup_dir))                        #Backup spinner logo
          os.system('cp {}/{}/spinner/img_spinner_comma.png /data/{}/selfdrive/assets'.format(CONTRIB_THEMES, self.selected_theme, opdir)) #Replace spinner logo supplied custom
          custom_logo = True                                                                                                               #Add custom_logo flag
        # Check if theme contributer provided a spinner track
        if path.exists('{}/{}/spinner/img_spinner_track.png'.format(CONTRIB_THEMES, self.selected_theme)):                               #Contibuter Did Provide
          os.system('mv /data/{}/selfdrive/assets/img_spinner_track.png {}/spinner'.format(opdir, self.backup_dir))                        #Backup spinner track
          os.system('cp {}/{}/spinner/img_spinner_track.png /data/{}/selfdrive/assets'.format(CONTRIB_THEMES, self.selected_theme, opdir)) #Replace spinner track supplied custom
          custom_track = True                                                                                                              #Add custom_track flag
        # Check if user wants rave rainbow spinner or if theme contributer provided a spinner.c
        if raveRainbow == True:                                                                                                          #User wants rave rainbow
          os.system('mv /data/{}/selfdrive/common/spinner.c {}/spinner'.format(opdir, self.backup_dir))                                    #Backup spinner.c
          os.system('cp ./support/spinner/rainbow_spinner.c /data/{}/selfdrive/common/spinner.c'.format(opdir))                            #Replace spinner.c with rave rainbow spinner.c
          custom_c = True                                                                                                                  #Add custom_C flag                                                                                                                  #Add custom_C flag
        elif path.exists('{}/{}/spinner/spinner.c'.format(CONTRIB_THEMES, self.selected_theme)) and raveRainbow == False:                #Contibuter Did Provide      
          os.system('mv /data/{}/selfdrive/common/spinner.c {}/spinner'.format(opdir, self.backup_dir))                                    #Backup spinner.c                
          os.system('cp {}/{}/spinner/spinner.c /data/{}/selfdrive/common'.format(CONTRIB_THEMES, self.selected_theme, opdir))             #Replace spinner.c with supplied custom 
          custom_c = True                                                                                                                  #Add custom_C flag

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
        os.system('cd /data/openpilot/selfdrive/ui/spinner && make{}'.format(self.con_output))
        print('\n{} spinner installed successfully! Original file(s) backed up to {}'.format(opdir, self.backup_dir))
        mark_self_installed()        # Create flag in /sdcard so auto installer knows there is a self installation
        print('Press enter to continue!')
        input()
 
      elif selected_option == 'QT OpenPilot Spinner':
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

        install_from_path = ("{}/{}/spinner".format(CONTRIB_THEMES, self.selected_theme))
        INSTALL_QT_SPINNER(self.backup_dir, OP_LOC, install_from_path, SHOW_CONSOLE_OUTPUT)
        mark_self_installed()        # Create flag in /sdcard so auto installer knows there is a self installation
        print('Press enter to continue!')
        input()

      elif selected_option == '-Main Menu-' or selected_option is None:
        return

      elif selected_option == '-Reboot-':
        print('\nRebooting.... Thank You, Come Again!!!')
        os.system('am start -a android.intent.action.REBOOT')  # reboot intent is safer (reboot sometimes causes corruption)
        return 'exit'

      elif selected_option == '-Quit-' or selected_option is None:
        print('\nThank you come again! You will see your changes next reboot!\n')
        exit()

      elif selected_option == 'Boot Animation' or 'Color Boot Animation' or 'White Boot Animation':
        #Confirm user wants to install bootlogo
        print('\nSelected to install the {} {}. Continue?'.format(self.selected_theme, selected_option))
        if not is_affirmative():
          print('Not installing...')
          time.sleep(1.5)
          continue
        
        #Check if there was an APK backup already this session to prevent accidental overwrites
        #Returns true if okay to proceed. Gets self.backup_dir & asset type name
        if backup_overide_check(self.backup_dir, 'bootanimation') == True:
          exit()

        #Set bootAniColor based off the selected option - if 'white_', 'color_', or standard bootanimation 
        if selected_option == 'Boot Animation':
          bootAniColor = ''
        elif selected_option == 'Color Boot Animation':
          bootAniColor = 'color_'
        elif selected_option == 'White Boot Animation':
          bootAniColor = 'white_'

        #Backup And install new bootanimation
        install_from_path = ('{}/{}/{}'.format(CONTRIB_THEMES, self.selected_theme, bootAniColor))
        INSTALL_BOOTANIMATION(self.backup_dir, install_from_path)
        mark_self_installed()        # Create flag in /sdcard so auto installer knows there is a self installation
        print('Press enter to continue!')
        input()
   
  # Auto installer stuff
  def auto_installer(self):               # Auto Installer program for incorperating into OP forks SEE DEVREADME
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
