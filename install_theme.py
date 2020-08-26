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
import curses
from os import path
from datetime import datetime
from support.pick.pick import Picker
from support.support_functions import print_welcome_text, check_auto_installability, get_user_theme, is_affirmative, go_back
from support.support_variables import CONTRIB_THEMES, IS_AUTO_INSTALL, AUTO_INSTALL_CONF

os.chdir(os.path.dirname(os.path.realpath(__file__)))  # __file__ is safer since it doesn't change based on where this file is called from
print_welcome_text()

# Crude device detection, *shrug* it works! LeEco does not have tristate!
if path.exists('/sys/devices/virtual/switch/tri-state-key'):
  print('\n*** OnePlus EON Device Detected ***')
  BOOT_LOGO_THEME_PATH = 'OP3T-Logo/LOGO'  # Set the boot logo theme path for 3T
  BOOT_LOGO_PATH = '/dev/block/sde17'  # Set the boot logo directory for 3T
else:
  print('\n*** LeEco EON Device Detected ***\n')
  BOOT_LOGO_THEME_PATH = 'LeEco-Logo/SPLASH'  # Set the boot logo theme path for Leo
  BOOT_LOGO_PATH = '/dev/block/bootdevice/by-name/splash'  # Set the boot logo directory for Leo

print('IMPORTANT: Soft-bricking is likely if this detection is incorrect. Is this correct?')
if not is_affirmative():
  exit()


class ThemeInstaller:
  def __init__(self):
    self.backup_dir = datetime.now().strftime('backups/backup.%m-%d-%y--%I.%M.%S-%p')  # Get current datetime and store
    os.mkdir(self.backup_dir)  # Create the session backup folder

    if IS_AUTO_INSTALL:
      assert check_auto_installability(), 'Error when checking if auto install available'
      self.auto_installer()
    else:
      self.start()

  def start(self):
    while 1:
      self.selected_theme = get_user_theme()
      if self.selected_theme is None:
        print('Didn\'t select a theme, exiting.')
        return
      self.get_available_options()
      self.install_function()

  def get_available_options(self):  # Check what assets are available for the selected theme
    # Check if the selected theme has a boot logo asset
    self.theme_options = []
    if os.path.exists('{}/{}/{}'.format(CONTRIB_THEMES, self.selected_theme, BOOT_LOGO_THEME_PATH)):
      self.theme_options.append('Boot Logo')

    # Check if the selected theme has a boot annimation asset
    if os.path.exists('{}/{}/bootanimation.zip'.format(CONTRIB_THEMES, self.selected_theme)):
      self.theme_options.append('Boot Animation')

    # Check if the selected theme has a OpenPilot Spinner asset
    if os.path.exists('{}/{}/spinner'.format(CONTRIB_THEMES, self.selected_theme)):
      self.theme_options.append('OP Spinner')

    # if os.path.exists('{}/{}/additional'.format(CONTRIB_THEMES, self.selected_theme)):  # todo disabled for now
    #   self.theme_options.append('Additional Resources')

  def install_function(self):  # Self installer program, prompts user on what they want to do
    while 1:
      options = list(self.theme_options)  # this only contains available options from self.get_available_options
      if not len(options):
        print('The selected theme has no resources available for your device! Try another.')
        time.sleep(2)
        return

      options += ['-Main Menu-', '-Reboot-']

      picker = Picker(options, 'What resources do you want to install for the {} theme?'.format(self.selected_theme))
      picker.register_custom_handler(curses.KEY_LEFT, go_back)
      selected_option, index = picker.start()
      # print(selected_option, index)

      if selected_option == 'Boot Logo':
        print('Selected to install the {} Boot Logo. Continue?'.format(self.selected_theme))
        if not is_affirmative():
          print('Not installing...')
          time.sleep(1.5)
          break
        os.system('cp {} {}'.format(BOOT_LOGO_PATH, self.backup_dir))  # Make Backup
        os.system('dd if={}/{}/{} of={}'.format(CONTRIB_THEMES, self.selected_theme, BOOT_LOGO_THEME_PATH, BOOT_LOGO_PATH))  # Replace
        print('Boot Logo installed successfully! Original backed up to {}'.format(self.backup_dir))
        input('Press enter to continue!')

      elif selected_option == 'Boot Animation':
        print('Selected to install the {} Boot Animation. Continue?'.format(self.selected_theme))
        if not is_affirmative():
          print('Not installing...')
          time.sleep(1.5)
          break
        os.system('mount -o remount,rw /system')  # /system read only, must mount as r/w
        os.system('mv /system/media/bootanimation.zip {}'.format(self.backup_dir))  # backup
        os.system('cp {}/{}/bootanimation.zip /system/media'.format(CONTRIB_THEMES, self.selected_theme))  # replace
        os.system('chmod 666 /system/media/bootanimation.zip')
        print('Boot Logo installed successfully! Original backed up to {}'.format(self.backup_dir))
        input('Press enter to continue!')

      elif selected_option == 'OP Spinner':
        print('Selected to install the {} OP Spinner. Continue?'.format(self.selected_theme))
        if not is_affirmative():
          print('Not installing...')
          time.sleep(1.5)
          break
        print('Do you have an OP fork with a custom directory name? (ex. arnepilot, dragonpilot)')  # Ask the user if their OP fork used a diffrent directory.
        if is_affirmative():  # Yes there is a custom OP dir
          print('What is the OP directory name? (case matters, not including /data/)')
          op_dir = '/data/{}'.format(input('> ').strip('/'))  # get custom dir name, strip slashes for safety
          print('Your openpilot directory is {}'.format(op_dir))
          input('*** Please enter to continue, or Ctrl+C to abort if this is incorrect! ***')

          os.system('mv {}/selfdrive/ui/spinner/spinner {}'.format(op_dir, self.backup_dir))
          os.system('cp {}/{}/spinner {}/selfdrive/ui/spinner'.format(CONTRIB_THEMES, self.selected_theme, op_dir))
          print('{} spinner installed successfully! Original backed up to {}'.format(op_dir.split('/')[2], self.backup_dir))
        else:  # there is not custom OP dir
          os.system('mv /data/openpilot/selfdrive/ui/spinner/spinner {}'.format(self.backup_dir))
          os.system('cp {}/{}/spinner /data/openpilot/selfdrive/ui/spinner'.format(CONTRIB_THEMES, self.selected_theme))
          print('openpilot spinner installed successfully! Original backed up to {}'.format(self.backup_dir))
        input('Press enter to continue!')

      elif selected_option == 'Additional Resources':  # additional features
        print('Additional Resources are not an active feature')
        time.sleep(5)

      elif selected_option == '-Main Menu-' or selected_option is None:
        return

      elif selected_option == '-Reboot-':
        print('Rebooting.... Enjoy your new theme!!!')
        os.system('am start -a android.intent.action.REBOOT')  # reboot intent is safer (reboot sometimes causes corruption)
        return

  def auto_installer(self):  # Auto Installer program for incorperating into OP forks SEE DEVREADME
    if AUTO_INSTALL_CONF['install_logo']:  # Auto BootLogo Install Code
      os.system('cp {} {}'.format(BOOT_LOGO_PATH, self.backup_dir))  # DEV EDIT SHOULD BE MV
      os.system('dd if={}/{}/OP3T-Logo/LOGO of={}'.format(CONTRIB_THEMES, self.selected_theme, BOOT_LOGO_PATH))
      print('Boot Logo installed successfully! Original backuped to ' + self.backup_dir)

    if AUTO_INSTALL_CONF['install_anim']:  # Auto BootAni Install Code
      os.system('mount -o remount,rw /system')
      os.system('mv /system/media/bootanimation.zip {}'.format(self.backup_dir))
      os.system('cp {}/{}/bootanimation.zip /system/media'.format(CONTRIB_THEMES, self.selected_theme))
      os.system('chmod 666 /system/media/bootanimation.zip')
      print('Boot Logo installed successfully! Original backuped to {}'.format(self.backup_dir))

    if AUTO_INSTALL_CONF['install_spinner']:  # Auto OP Spinner Code
      os.system('cp /data/{}/selfdrive/ui/spinner/spinner {}'.format(AUTO_INSTALL_CONF['openpilot_dir_name'], self.backup_dir))  # TEMP DEV EDIT SHOULD BE MV
      os.system('cp {}/{}/spinner /data/{}/selfdrive/ui/spinner'.format(CONTRIB_THEMES, self.selected_theme, AUTO_INSTALL_CONF['openpilot_dir_name']))
      print('OP Spinner installed successfully! Original backed up to {}'.format(self.backup_dir))

    # if (autoInstallAdditional != 'no'):             #Auto additional features Code (Not An Active feature)
    #  print('Additional Resources are not an active feature')  # todo: refactor this


if __name__ == '__main__':
  ti = ThemeInstaller()
