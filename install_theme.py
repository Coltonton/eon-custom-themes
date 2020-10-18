#!/usr/bin/python
##################################################################################
#                                   VER 1.1                                      #
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
#                  exec /data/eon-custom-themes/restore_backup.py                #
#                                                                                #
#            Or if trying to use the included package with an OP Fork:           #
#              cd /data/(your openpilot directory)/eon-custom-themes             #
#                          exec ./install_theme.py                               #
#                                                                                #
#               Now follow the prompts and make your selections!                 #
#                  Everything will be done automagically!!!!!                    #
#                                                                                #
#                      Don't forget to tell your friends!!                       #
#                               Love Cole (@C-ton)                               #
#                                                                                #
#        Did you know that if you have a custom OP fork you can use this         #
#     program to auto install your custom theme for your users automagiclly?     #
#       And incorparate it into your OP Fork? See ./developer/DEVREADME          #
#                                                                                #
##################################################################################
import os
import time
from os import path
from support.support_functions import get_device_theme_data, get_user_backups, get_user_theme, installer_chooser, is_affirmative
from support.support_functions import make_backup_folder, mark_self_installed, print_welcome_text, backup_overide_check, op_dir_finder
from support.support_variables import AUTO_INSTALL_CONF, BACKUPS_DIR, BACKUP_OPTIONS, CONTRIB_THEMES, DESIRED_AUTO_VER, IS_AUTO_INSTALL


##======================= CODE START ================================================================
os.chdir(os.path.dirname(os.path.realpath(__file__)))  # __file__ is safer since it doesn't change based on where this file is called from
if IS_AUTO_INSTALL:
  print_welcome_text('a')               #Print welcome text with the flag for auto welcome text
else:
  print_welcome_text('s')               #Print welcome text with the flag for normal welcome text
BOOT_LOGO_THEME_PATH, BOOT_LOGO_PATH, BOOT_LOGO_NAME = get_device_theme_data() # Get Perams based off detected device


class ThemeInstaller:
  def __init__(self):                   # Init code runs once. sets up & determines if to run auto or self
    # Create and get backup folder
    self.backup_dir = make_backup_folder()

    # Detrimine if should self install, auto install, or exit
    auto_found_installer = installer_chooser()  
    if auto_found_installer == 'Do_Self':
      self.start_loop()                                      # Do self install theme
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
      if self.selected_theme == 'restore':
        self.backup_reinstaller_loop()
      self.get_available_options()
      if self.install_function() == 'exit':
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

    # if os.path.exists('{}/{}/additional'.format(CONTRIB_THEMES, self.selected_theme)):  # todo disabled for now
    #   self.theme_options.append('4. Additional Resources')

    self.theme_options.append('-Main Menu-')
    self.theme_options.append('-Reboot-')
    self.theme_options.append('-Quit-')

  def install_function(self):           # Self installer program, prompts user on what they want to do
    while 1:
      options = list(self.theme_options)  # this only contains available options from self.get_available_options
      if not len(options):
        print('The selected theme has no resources available for your device! Try another.')
        time.sleep(2)
        return
      
      print('What resources do you want to install for the {} theme?'.format(self.selected_theme))
      for idx, theme in enumerate(options):
        print('{}. {}'.format(idx + 1, theme))
      indexChoice = int(input("Enter Index Value: "))
      indexChoice -= 1 

      selected_option = self.theme_options[indexChoice]

      if selected_option == 'Boot Logo':
        #Confirm user wants to install bootlogo
        print('Selected to install the {} Boot Logo. Continue?'.format(self.selected_theme))
        if not is_affirmative():
          print('Not installing...')
          time.sleep(1.5)
          continue

        #Check if there was a backup already this session to prevent accidental overwrites
        if path.exists('{}/{}'.format(self.backup_dir, BOOT_LOGO_NAME)):                 #Func to see if there was a backup already this session
            print('It appears you already made a boot logo backup this session')         #to prevent accidental overwrites
            print('continuing will overwrite last boot logo backup!')
            print('Would you like to continue and overwrite previous?')
            if not is_affirmative():
              print('Not installed, exiting session..... Please re-run program')
              exit()                  #Exit program if user does not want to overwrite, so they can start a new session

        #Backup & install new
        os.system('cp {} {}'.format(BOOT_LOGO_PATH, self.backup_dir))  # Make Backup
        os.system('dd if={}/{}/{} of={}'.format(CONTRIB_THEMES, self.selected_theme, BOOT_LOGO_THEME_PATH, BOOT_LOGO_PATH))  # Replace
        print('\nBoot Logo installed successfully! Original backed up to {}'.format(self.backup_dir))
        mark_self_installed()       # Create flag in /sdcard so auto installer knows there is a self installation
        print('Press enter to continue!')
        input()

      elif selected_option == 'OpenPilot Spinner':
        #Confirm user wants to install Spinner
        print('Selected to install the {} OP Spinner. Continue?'.format(self.selected_theme))
        if not is_affirmative():
          print('Not installing...')
          time.sleep(1.5)
          continue
        
        #Check if there was a spinner backup already this session to prevent accidental overwrites
        #Returns false if okay to proceed. Gets self.backup_dir & asset type name
        if backup_overide_check(self.backup_dir, 'spinner') is True:
          exit()

        #Ask user if their OP directory is custom (like arnepilot / dragonpilot)
        opdir = op_dir_finder()

        #Backup files
        os.system('mv /data/{}/selfdrive/assets/img_spinner_comma.png {}/spinner'.format(opdir, self.backup_dir)) #Backup logo
        os.system('mv /data/{}/selfdrive/assets/img_spinner_track.png {}/spinner'.format(opdir, self.backup_dir)) #backup spinner track
        os.system('mv /data/{}/selfdrive/common/spinner.c {}/spinner'.format(opdir, self.backup_dir))             #backup spinner.c

        #Copy in new files
        if path.exists('{}/{}/spinner/img_spinner_comma.png'.format(CONTRIB_THEMES, self.selected_theme)):                   # Check if theme contributer provided a spinner track
          os.system('cp {}/{}/spinner/img_spinner_comma.png /data/{}/selfdrive/assets'.format(CONTRIB_THEMES, self.selected_theme, opdir)) #Replace spinner track supplied custom
        else:
          os.system('cp ./support/spinner/img_spinner_comma.png /data/{}/selfdrive/assets'.format(opdir))     #Replace spinner track with standard 
        if path.exists('{}/{}/spinner/img_spinner_track.png'.format(CONTRIB_THEMES, self.selected_theme)):                   # Check if theme contributer provided a spinner track
          os.system('cp {}/{}/spinner/img_spinner_track.png /data/{}/selfdrive/assets'.format(CONTRIB_THEMES, self.selected_theme, opdir)) #Replace spinner track supplied custom
        else:
          os.system('cp ./support/spinner/img_spinner_track.png /data/{}/selfdrive/assets'.format(opdir))     #Replace spinner track with standard 
        if path.exists('{}/{}/spinner/spinner.c'.format(CONTRIB_THEMES, self.selected_theme)):                               # Check if theme contributer provided a spinner.c
          os.system('cp {}/{}/spinner/spinner.c /data/{}/selfdrive/common'.format(CONTRIB_THEMES, self.selected_theme, opdir))             #Replace spinner.c with supplied custom 
        else:
          os.system('cp ./support/spinner/spinner.c /data/{}/selfdrive/common'.format(opdir))             #Replace spinner.c with standard file

        #Final make new spinner & finish
        os.system('cd /data/openpilot/selfdrive/ui/spinner && make')
        print('\n{} spinner installed successfully! Original backed up to {}'.format(opdir, self.backup_dir))
        mark_self_installed()        # Create flag in /sdcard so auto installer knows there is a self installation
        print('Press enter to continue!')
        input()

      elif selected_option == 'APK':
        #Confirm user wants to install Kumar Nightmode APK
        print('**PLEASE NOTE** ')
        print("This is ONLY installable on 'stock' OpenPilot installs")
        print('If you have a fork like ArnePilot, or any other with')
        print('a modified UI DO NOT USE THIS!! OpenPilot will fail to run!! \n')
        print('Instead refer to the DEVREADME located in this project')
        print("at ./developer, in the 'APK' section for more info!!\n")
        print('Selected to install the {} APK. Continue?'.format(self.selected_theme))
        if not is_affirmative():
          print('Not installing...')
          time.sleep(1.5)
          continue

        #Check if there was an APK backup already this session to prevent accidental overwrites
        #Returns false if okay to proceed. Gets self.backup_dir & asset type name
        if backup_overide_check(self.backup_dir, 'apk') is True:
          exit()
    
        #Ask user if their OP directory is custom (like arnepilot / dragonpilot)
        opdir = op_dir_finder()

        #Backup files
        os.system('mv /data/{}/apk/ai.comma.plus.offroad.apk {}/apk'.format(opdir, self.backup_dir)) # Backup apk
        os.system('mv /data/{}/selfdrive/ui/ui.hpp {}/apk'.format(opdir, self.backup_dir))           # backup ui.hpp

        #Copy in new files
        os.system('cp {}/{}/apk/ai.comma.plus.offroad.apk /data/{}/apk'.format(CONTRIB_THEMES, self.selected_theme, opdir)) # Copy APK
        os.system('cp {}/{}/apk/ui.hpp /data/{}/selfdrive/ui'.format(CONTRIB_THEMES, self.selected_theme, opdir))           # Copy ui.hpp

        # Finish
        print('\n{} apk installed successfully! Original backed up to {}'.format(self.selected_theme, self.backup_dir))
        mark_self_installed()        # Create flag in /sdcard so auto installer knows there is a self installation
        print('Press enter to continue!')
        input()

      elif selected_option == 'Kumar-Nightmode-APK':  # Kumar-Nightmode-APK
        #Confirm user wants to install Kumar Nightmode APK
        print('**PLEASE NOTE** ')
        print("This is ONLY installable on 'stock' OpenPilot installs")
        print('If you have a fork like ArnePilot, or any other with')
        print('a modified UI DO NOT USE THIS!! OpenPilot will fail to run!! \n')
        print('Instead refer to the DEVREADME located in this project')
        print("at ./developer, in the 'Kumar-Nightmode-APK' section for more info!!\n")
        print('Selected to install the Kumar Nightmode APK. Continue?')
        if not is_affirmative():
          print('Not installing...')
          time.sleep(1.5)
          continue

        #Check if there was an APK backup already this session to prevent accidental overwrites
        #Returns true if okay to proceed. Gets self.backup_dir & asset type name
        if backup_overide_check(self.backup_dir, 'apk') is False:
          exit()
    
        #Ask user if their OP directory is custom (like arnepilot / dragonpilot)
        opdir = op_dir_finder()

        #Backup files
        os.system('mv /data/{}/apk/ai.comma.plus.offroad.apk {}/apk'.format(opdir, self.backup_dir)) # Backup apk
        os.system('mv /data/{}/selfdrive/ui/ui.hpp {}/apk'.format(opdir, self.backup_dir))           # Backup ui.hpp

        #Copy in new files
        os.system('cp ./support/nightmode-apk/ai.comma.plus.offroad.apk /data/{}/apk'.format(opdir)) # Copy APK
        os.system('cp ./support/nightmode-apk/ui.hpp /data/{}/selfdrive/ui'.format(opdir))           # Copy ui.hpp

        # Finish
        print('\nkumar-nightmode-apk installed successfully! Original backed up to {}'.format(self.backup_dir))
        mark_self_installed()        # Create flag in /sdcard so auto installer knows there is a self installation
        print('Press enter to continue!')
        input()

      elif selected_option == '-Main Menu-' or selected_option is None:
        return

      elif selected_option == '-Reboot-':
        print('Rebooting.... Enjoy your new theme!!!')
        os.system('am start -a android.intent.action.REBOOT')  # reboot intent is safer (reboot sometimes causes corruption)
        return 'exit'

      elif selected_option == '-Quit-' or selected_option is None:
        print('Thank you come again! You will see your changes next reboot!')
        exit()

      elif selected_option == 'Boot Animation' or 'Color Boot Animation' or 'White Boot Animation':
        #Confirm user wants to install bootlogo
        print('Selected to install the {} {}. Continue?'.format(self.selected_theme, selected_option))
        if not is_affirmative():
          print('Not installing...')
          time.sleep(1.5)
          continue
        
        #Check if there was a backup already this session to prevent accidental overwrites
        if path.exists('{}/bootanimation.zip'.format(self.backup_dir)):                 #Func to see if there was a backup already this session
            print('It appears you already made a boot animation backup this session')    #to prevent accidental overwrites
            print('continuing will overwrite last boot animation backup!')
            print('Would you like to continue and overwrite previous?')
            if not is_affirmative():
              print('Not installed, exiting session..... Please re-run program')
              exit()                  #Exit program if user does not want to overwrite, so they can start a new session

        #Set bootAniColor based off the selected option - if white_, color, or standard bootanimation 
        if selected_option == 'Boot Animation':
          bootAniColor = ""
        elif selected_option == 'Color Boot Animation':
          bootAniColor = "color_"
        elif selected_option == 'White Boot Animation':
          bootAniColor = "white_"

        #Backup And install new bootanimation
        os.system('mount -o remount,rw /system')                                    # /system read only, must mount as r/w
        os.system('mv /system/media/bootanimation.zip {}'.format(self.backup_dir))  # backup
        os.system('cp {}/{}/{}bootanimation.zip /system/media/bootanimation.zip'.format(CONTRIB_THEMES, self.selected_theme, bootAniColor))  # replace
        os.system('chmod 666 /system/media/bootanimation.zip')                      #Need to chmod and edet permissions to 666
        print('\nBoot Animation installed successfully! Original backed up to {}'.format(self.backup_dir))
        mark_self_installed()        # Create flag in /sdcard so auto installer knows there is a self installation
        print('Press enter to continue!')
        input()
   
  # Auto installer stuff
  def auto_installer(self):               # Auto Installer program for incorperating into OP forks SEE DEVREADME
    self.selected_theme = AUTO_INSTALL_CONF['auto_selected_theme']
    opdir = AUTO_INSTALL_CONF['openpilot_dir_name']
    selected_ani_color = AUTO_INSTALL_CONF['ani_color']

    if AUTO_INSTALL_CONF['install_logo']:  # Auto BootLogo Install Code
      os.system('cp {} {}'.format(BOOT_LOGO_PATH, self.backup_dir))  # Make Backup
      os.system('dd if={}/{}/{} of={}'.format(CONTRIB_THEMES, self.selected_theme, BOOT_LOGO_THEME_PATH, BOOT_LOGO_PATH))  # Replace
      print('\nBoot Logo installed successfully! Original backed up to {}'.format(self.backup_dir))

    if AUTO_INSTALL_CONF['install_anim'] == True:  # Auto BootAni Install Code
      os.system('mount -o remount,rw /system')
      os.system('mv /system/media/bootanimation.zip {}'.format(self.backup_dir))
      os.system('cp {}/{}/{}bootanimation.zip /system/media/bootanimation.zip'.format(CONTRIB_THEMES, self.selected_theme, selected_ani_color))
      os.system('chmod 666 /system/media/bootanimation.zip')
      print('Boot Animation installed successfully! Original backuped to {}'.format(self.backup_dir))

    if AUTO_INSTALL_CONF['install_spinner']:  # Auto OP Spinner Code
      #Backup files
      os.system('mv /data/{}/selfdrive/assets/img_spinner_comma.png {}/spinner'.format(opdir, self.backup_dir)) #Backup logo
      os.system('mv /data/{}/selfdrive/assets/img_spinner_track.png {}/spinner'.format(opdir, self.backup_dir)) #backup sprinner track
      os.system('mv /data/{}/selfdrive/common/spinner.c {}/spinner'.format(opdir, self.backup_dir))             #backup spinner.c

      #Copy in new files
      os.system('cp {}/{}/spinner/img_spinner_comma.png /data/{}/selfdrive/assets'.format(CONTRIB_THEMES, self.selected_theme, opdir)) #Replace logo
      if path.exists('{}/{}/spinner/img_spinner_track.png'.format(CONTRIB_THEMES, self.selected_theme)):                   # Check if theme contributer provided a spinner track
        os.system('cp {}/{}/spinner/img_spinner_track.png /data/{}/selfdrive/assets'.format(CONTRIB_THEMES, self.selected_theme, opdir)) #Replace sprinner track supplied custom
      else:
        os.system('cp ./support/img_spinner_track.png /data/{}/selfdrive/assets'.format(opdir))     #Replace sprinner track with standard 
      if path.exists('{}/{}/spinner/spinner.c'.format(CONTRIB_THEMES, self.selected_theme)):                               # Check if theme contributer provided a spinner.c
        os.system('cp {}/{}/spinner/spinner.c /data/{}/selfdrive/common'.format(CONTRIB_THEMES, self.selected_theme, opdir))             #Replace spinner.c with supplied custom 
      else:
        os.system('cp ./support/spinner.c /data/{}/selfdrive/common'.format(opdir))             #Replace spinner.c with standard file

      #Final make new spinner & finish
      os.system('cd /data/openpilot/selfdrive/ui/spinner && make')
      print('\n{} spinner installed successfully! Original backed up to {}'.format(opdir, self.backup_dir))

    # if (autoInstallAdditional != 'no'):             #Auto additional features Code (Not An Active feature)
    #  print('Additional Resources are not an active feature')  # todo: this

    fi = open("./support/auto_install_ver.txt", "w")
    fi.write(str(DESIRED_AUTO_VER))

if __name__ == '__main__':
  ti = ThemeInstaller()
