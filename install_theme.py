#!/usr/bin/python
##################################################################################
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
#                === http://endoflinetech.com/eon-themes ===                     #
#                                                                                #
#              With a mission to rid all EONS of Comma.ai branding               #
#             And give the people the freedom, knowlage, and power               #
#                         to make their EONS purdy!                              #
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
#                        Type the following commands:                            #
#                                cd /data                                        #
#       git clone https://github.com/Coltonton/eon-custom-themes.git             #
#                      cd /data/eon-custom-themes                                #
#                        python install_theme.py                                 #
#                                                                                #
#            Now follow the prompts and make your selections!                    #
#               Everything will be done automagically!!!!!                       #
#                                                                                #
#                   Don't forget to tell your friends!!                          #
#                            Love Cole (@C-ton)                                  #
#                                                                                #
#        Did you know that if you have a custom OP fork you can use this         #
#      program to auto install your custom boot logo & boot annimation for       #
#                    your users? See ./developer/DEVREADME                       #
#                                                                                #
##################################################################################
import os
import time
from os import path

from support.support_functions import create_backup_folder, create_backup_folder, print_welcome_text, print_auto_welcome_text, get_user_theme, is_affirmative, go_back
from support.support_functions import backup_dir
from support.support_variables import AUTO_INSTALL_CONF, CONTRIB_THEMES, CURRENT_AUTO_VER, IS_AUTO_INSTALL

os.chdir(os.path.dirname(os.path.realpath(__file__)))  # __file__ is safer since it doesn't change based on where this file is called from

if IS_AUTO_INSTALL:
  print_auto_welcome_text()   #Print welcome text with true flag for auto welcome text
else:
  print_welcome_text()  #Print welcome text with false flag for normal welcome text  

# Crude device detection, *shrug* it works! LeEco does not have tristate!
if path.exists('/sys/devices/virtual/switch/tri-state-key'):
  print('\n*** OG OnePlus EON Device Detected ***')
  BOOT_LOGO_THEME_PATH = 'OP3T-Logo/LOGO'  # Set the boot logo theme path for 3T
  BOOT_LOGO_PATH = '/dev/block/sde17'  # Set the boot logo directory for 3T
else:
  print('\n*** LeEco EON (Gold/Comma 2) Device Detected ***\n')
  BOOT_LOGO_THEME_PATH = 'LeEco-Logo/SPLASH'  # Set the boot logo theme path for Leo
  BOOT_LOGO_PATH = '/dev/block/bootdevice/by-name/splash'  # Set the boot logo directory for Leo

if IS_AUTO_INSTALL == False:
  print('IMPORTANT: Soft-bricking is likely if this detection is incorrect. Is this correct?')
  if not is_affirmative():
    exit()

class ThemeInstaller:
  def __init__(self):
    file = open('./support/do_not_auto.txt', 'r')  # check auto installed version
    DO_NOT_AUTO_INSTALL = file.read()
    file.close
    print(DO_NOT_AUTO_INSTALL)

    if IS_AUTO_INSTALL == True and DO_NOT_AUTO_INSTALL == '0':
      file = open('./support/auto_install_ver.txt', 'r')  # check auto installed version
      AUTO_VER = file.read()

      if DO_NOT_AUTO_INSTALL == 0 and AUTO_VER != CURRENT_AUTO_VER:
        create_backup_folder()
        self.auto_installer()  # Do Auto install theme
    
    else:
      if DO_NOT_AUTO_INSTALL is '1':
        exit()
      else:
        create_backup_folder()
        self.start_loop()   

  def start_loop(self):
    while 1:
      self.selected_theme = get_user_theme()
      if self.selected_theme is None:
        print('Didn\'t select a theme, exiting.')
        return
      self.get_available_options()
      if self.install_function() == 'exit':
        return

  def get_available_options(self):  # Check what assets are available for the selected theme
    # Check if the selected theme has a boot logo asset
    self.theme_options = []
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
      self.theme_options.append('OP Spinner')

    # if os.path.exists('{}/{}/additional'.format(CONTRIB_THEMES, self.selected_theme)):  # todo disabled for now
    #   self.theme_options.append('4. Additional Resources')

    self.theme_options.append('-Main Menu-')
    self.theme_options.append('-Reboot-')

  def install_function(self):       # Self installer program, prompts user on what they want to do
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
      print(selected_option)

      if selected_option == 'Boot Logo':
        print('Selected to install the {} Boot Logo. Continue?'.format(self.selected_theme))
        if not is_affirmative():
          print('Not installing...')
          time.sleep(1.5)
          continue
        os.system('cp {} {}'.format(BOOT_LOGO_PATH, backup_dir))  # Make Backup
        os.system('dd if={}/{}/{} of={}'.format(CONTRIB_THEMES, self.selected_theme, BOOT_LOGO_THEME_PATH, BOOT_LOGO_PATH))  # Replace
        print('\nBoot Logo installed successfully! Original backed up to {}'.format(backup_dir))
        print('Press enter to continue!')
        input()

      elif selected_option == 'OP Spinner':
        print('Selected to install the {} OP Spinner. Continue?'.format(self.selected_theme))
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

          os.system('mv {}/selfdrive/ui/spinner/spinner {}'.format(op_dir, backup_dir))
          os.system('cp {}/{}/spinner {}/selfdrive/ui/spinner'.format(CONTRIB_THEMES, self.selected_theme, op_dir))
          print('\n{} spinner installed successfully! Original backed up to {}'.format(op_dir.split('/')[2], backup_dir))
        else:  # there is not custom OP dir
          os.system('mv /data/openpilot/selfdrive/ui/spinner/spinner {}'.format(backup_dir))
          os.system('cp {}/{}/spinner /data/openpilot/selfdrive/ui/spinner'.format(CONTRIB_THEMES, self.selected_theme))
          print('\nopenpilot spinner installed successfully! Original backed up to {}'.format(backup_dir))
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

      elif selected_option == 'Boot Animation' or 'Color Boot Animation' or 'White Boot Animation':
        print('Selected to install the {} Boot Animation. Continue?'.format(self.selected_theme))
        if not is_affirmative():
          print('Not installing...')
          time.sleep(1.5)
          continue

        if selected_option == 'Boot Animation':
          bootAniColor = ""
        elif selected_option == 'Color Boot Animation':
          bootAniColor = "color_"
        elif selected_option == 'White Boot Animation':
          bootAniColor = "white_"
        
        os.system('mount -o remount,rw /system')  # /system read only, must mount as r/w
        os.system('mv /system/media/bootanimation.zip {}'.format(backup_dir))  # backup
        os.system('cp {}/{}/{}bootanimation.zip /system/media/bootanimation.zip'.format(CONTRIB_THEMES, self.selected_theme, bootAniColor))  # replace
        os.system('chmod 666 /system/media/bootanimation.zip')
        print('\nBoot Animation installed successfully! Original backed up to {}'.format(backup_dir))
        print('Press enter to continue!')
        input()
   
  def auto_installer(self):         # Auto Installer program for incorperating into OP forks SEE DEVREADME
    self.selected_theme = AUTO_INSTALL_CONF['auto_selected_theme']
    #selected_ani_color = AUTO_INSTALL_CONF['install_color']

    if AUTO_INSTALL_CONF['install_logo']:  # Auto BootLogo Install Code
      os.system('cp {} {}'.format(BOOT_LOGO_PATH, backup_dir))  # Make Backup
      os.system('dd if={}/{}/{} of={}'.format(CONTRIB_THEMES, self.selected_theme, BOOT_LOGO_THEME_PATH, BOOT_LOGO_PATH))  # Replace
      print('\nBoot Logo installed successfully! Original backed up to {}'.format(backup_dir))

    if AUTO_INSTALL_CONF['install_anim'] == True:  # Auto BootAni Install Code
      os.system('mount -o remount,rw /system')
      os.system('mv /system/media/bootanimation.zip {}'.format(backup_dir))
      os.system('cp {}/{}/{}bootanimation.zip /system/media/bootanimation.zip'.format(CONTRIB_THEMES, self.selected_theme, AUTO_INSTALL_CONF['ani_color']))
      os.system('chmod 666 /system/media/bootanimation.zip')
      print('Boot Animation installed successfully! Original backuped to {}'.format(backup_dir))

    if AUTO_INSTALL_CONF['install_spinner']:  # Auto OP Spinner Code
      os.system('cp /data/{}/selfdrive/ui/spinner/spinner {}'.format(AUTO_INSTALL_CONF['openpilot_dir_name'], backup_dir))  # TEMP DEV EDIT SHOULD BE MV
      os.system('cp {}/{}/spinner /data/{}/selfdrive/ui/spinner'.format(CONTRIB_THEMES, self.selected_theme, AUTO_INSTALL_CONF['openpilot_dir_name']))
      print('OP Spinner installed successfully! Original backed up to {}'.format(backup_dir))

    # if (autoInstallAdditional != 'no'):             #Auto additional features Code (Not An Active feature)
    #  print('Additional Resources are not an active feature')  # todo: refactor this

    fi = open("./support/auto_install_ver.txt", "w")
    fi.write(str(CURRENT_AUTO_VER))


if __name__ == '__main__':
  ti = ThemeInstaller()
