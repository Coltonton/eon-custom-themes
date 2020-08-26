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
from os import path
import sys
import time
from datetime import datetime
# import curses
# from support.pick.pick import Picker
from support.support_functions import str_sim, print_welcome_text

os.chdir(os.path.dirname(os.path.realpath(__file__)))  # __file__ is safer since it doesn't change based on where this file is called from

# selected_theme = ""
# bootlogothemepath = ""
# bootlogodir = ""
#
# bootLogoAvailable = "N/A"
# bootAnimationAvailable = "N/A"
# spinnerAvailable = "N/A"
# additionalAvailable = "N/A"
#
# running = 1

#Crude device detection, *shrug* it works! LeEco does not have tristate!
if(path.exists('/sys/devices/virtual/switch/tri-state-key') == True):
  print('\n*** OnePlus EON Device Detected ***\n')
  bootlogothemepath = "OP3T-Logo/LOGO"      #Set the boot logo theme path for 3T
  bootlogodir = "/dev/block/sde17"          #Set the boot logo directory for 3T
else:
  print ('\n*** LeEco EON Device Detected ***\n')
  bootlogothemepath = "LeEco-Logo/SPLASH"   #Set the boot logo theme path for Leo
  bootlogodir = "/dev/block/bootdevice/by-name/splash" #Set the boot logo directory for Leo

#Auto Install variables - see DEVREADME
isAutoInstall          = 0            #
selectedAutoTheme      = "arne"       #
autoInstallLogo        = "no"         #
autoInstallAnim        = "no"         #
autoInstallSpinner     = "no"         #
autoOpenPilotDirName   = "arnepilot"  #
autoInstallAdditional  = "no"         #
#=====================================#

#=================== Functions =================================

def MainLoop():
  global selected_theme
  while (running == 1):
    if (isAutoInstall == 1):                #If auto install set run auto installer
      if( CheckAutoInstalability() == True):
        selected_theme = selectedAutoTheme  #Make the selected_theme the provided auto theme
        Auto_Installer()
      else:
        sys.exit()
    elif (isAutoInstall == 0):              #else use self installer
      selected_theme = ThemePicker()        #Make selected_theme chosen theme from prompt
      setup()
      Self_Installer()

def CheckAutoInstalability():
  doInstall = False
  if(os.path.exists("./auto_theme_installed.txt") == True): #if auto installed before
    isOveride  = open("override_auto_install.txt", "r")         #check if override set
    if isOveride.mode == 'r':                               
      contents = isOveride.read()
      if (contents == 1):                                   #if overide == 1
        doInstall = True                                    #overide and Do Auto install theme
      else:
        doInstall = False                                   #do not override reinstall, do not pass go do not collect $200
  else:                                      #If auto_theme_installed.txt does not exist
    doInstall = True                         #Do Auto install theme
    f= open("auto_theme_installed.txt","w+") #Create auto_theme_installed.txt to prevent more installs
    f.write("1")
    f.close()         

  return doInstall

#Created by @ShaneSmiskol
def ThemePicker():                   #Auto discover themes and let user choose!
  available_themes = [t for t in os.listdir(CONTRIB_THEMES)]
  available_themes = [t for t in available_themes if os.path.isdir(os.path.join(CONTRIB_THEMES, t))]
  available_themes = [t for t in available_themes if t not in EXCLUDED_THEMES]
  lower_available_themes = [t.lower() for t in available_themes]
  print('\nAvailable themes:')
  for idx, theme in enumerate(available_themes):
    print('{}. {}'.format(idx + 1, theme))
  print('\nChoose a theme to install (by name or index)')
  while 1:
    print('Select a theme: ', end='')
    theme = input().strip().lower()
    print()
    if theme in ['exit', '']:
      return 'none'

    if theme.isdigit():
      theme = int(theme)
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
        if input().lower().strip() in ['yes', 'y']:
          return theme
      else:
        print('Unknown theme, try again!')

def setup():                         #Check what assets are available for the selected theme
  global bootLogoAvailable
  global bootAnimationAvailable
  global spinnerAvailable
  global additionalAvailable

  #Check if the selected theme has a boot logo  asset
  if(os.path.exists("./contributed-themes/"+str(selected_theme)+"/"+str(bootlogothemepath)) == True):
    bootLogoAvailable = "Boot_Logo"
  else:
    bootLogoAvailable = "N/A"

  #Check if the selected theme has a boot annimation asset
  if(os.path.exists('./contributed-themes/'+str(selected_theme)+'/bootanimation.zip') == True):
    bootAnimationAvailable="Boot_Animation"
  else:
    bootAnimationAvailable = "N/A"

  #Check if the selected theme has a OpenPilot Spinner asset
  if(os.path.exists('./contributed-themes/'+str(selected_theme)+'/spinner') == True):
    spinnerAvailable="OP_Spinner"
  else:
    spinnerAvailable = "N/A"

  #Check if the selected theme has a additional assets (feature not active)
  #if(os.path.exists('./contributed-themes/'+str(selected_theme)+'/additional') == True):
  #  additionalAvailable="Additional-resources"
  #else:
  #  additionalAvailable = "N/A"

def Auto_Installer():                #Auto Installer program for incorperating into OP forks SEE DEVREADME
    if (autoInstallLogo != 'no'):                   #Auto BootLogo Install Code
      os.system("cp "+str(bootlogodir)+" backups/backup."+str(dateTimeVar)) #DEV EDIT SHOULD BE MV
      os.system("dd if=./contributed-themes/"+str(selected_theme)+"/OP3T-Logo/LOGO of="+str(bootlogodir))
      print("Boot Logo installed successfully! Original backuped to ./backups/backup."+str(dateTimeVar))

    if (autoInstallAnim != 'no'):                   #Auto BootAni Install Code
      os.system("mount -o remount,rw /system")
      os.system("mv /system/media/bootanimation.zip backups/backup."+str(dateTimeVar))
      os.system("cp ./contributed-themes/"+str(selected_theme)+"/bootanimation.zip /system/media")
      os.system("chmod 666 /system/media/bootanimation.zip")
      print("Boot Logo installed successfully! Original backuped to ./backups/backup."+str(dateTimeVar))

    if (autoInstallSpinner != 'no'):                #Auto OP Spinner Code
      os.system("cp /data/"+str(autoOpenPilotDirName)+"/selfdrive/ui/spinner/spinner backups/backup."+str(dateTimeVar)) #TEMP DEV EDIT SHOULD BE MV
      os.system("cp ./contributed-themes/"+str(selected_theme)+"/spinner /data/"+str(autoOpenPilotDirName)+"/selfdrive/ui/spinner")
      print("OP Spinner Installed Successfully! Original backuped to ./backups/backup."+str(dateTimeVar))

    #if (autoInstallAdditional != 'no'):             #Auto additional features Code (Not An Active feature)
    #  print("Additional Resources are not an active feature")

def Self_Installer():                #Self installer program, prompts user on what they want to do
  while 1:
    title = 'What resources do you want to install for the '+str(selected_theme)+' theme?: '
    options = [bootLogoAvailable, bootAnimationAvailable, spinnerAvailable, additionalAvailable, 'Main Menu', 'Reboot']

    picker = Picker(options, title)
    picker.register_custom_handler(curses.KEY_LEFT, go_back)
    option, index = picker.start()
    print(option, index)

    if (index == 0):                   #BootLogo Install Code
      if (bootLogoAvailable != 'N/A'):       
        os.system("cp "+str(bootlogodir)+" backups/backup."+str(dateTimeVar)) #Make Backup
        os.system("dd if=./contributed-themes/"+str(selected_theme)+"/"+str(bootlogothemepath)+" of="+str(bootlogodir)) #Replace
        print("Boot Logo installed successfully! Original backuped to ./backups/backup."+str(dateTimeVar))
      else:
        print("Boot logo is not available for "+str(selected_theme))
        time.sleep(5)

    if (index == 1):                   #BootAni Install Code
      if (bootAnimationAvailable != 'N/A'):
        os.system("mount -o remount,rw /system")           #/system read only, must mount as r/w
        os.system("mv /system/media/bootanimation.zip backups/backup."+str(dateTimeVar))             #backup 
        os.system("cp ./contributed-themes/"+str(selected_theme)+"/bootanimation.zip /system/media") #replace
        os.system("chmod 666 /system/media/bootanimation.zip")
        print("Boot Logo installed successfully! Original backuped to ./backups/backup."+str(dateTimeVar))
      else:
        print("Boot Annimation is not available for "+str(selected_theme))
        time.sleep(5)

    if (index == 2):                   #OP Spinner Code
      if (spinnerAvailable == 'N/A'):
        print("Do you have an OP fork with a custom directory name? (ex. arnepilot, dragonpilot)")
        print("Choose an option (by name or index) (case matters)")
        print("1. Yes")                #Ask the user if their OP fork used a diffrent directory.
        print("2. No")
        isCustOP = input("")

        if (isCustOP == 'y','Y','yes','Yes',1):  #Yes there is a custom OP dir
          opdir = input("What is the OP directory name? (case matters)") #get custom dir name
          print("Your OpenPilot directory is /data/"+str(opdir))
          os.system("mv /data/"+str(opdir)+"/selfdrive/ui/spinner/spinner backups/backup."+str(dateTimeVar))
          os.system("cp ./contributed-themes/"+str(selected_theme)+"/spinner /data/"+str(opdir)+"/selfdrive/ui/spinner")
          print(str(opdir)+" Spinner installed Successfully! Original backuped to ./backups/backup."+str(dateTimeVar))
        elif (isCustOP == 'n','N','no','No',2):  #No there is not custom OP dir
          os.system("mv /data/openpilot/selfdrive/ui/spinner/spinner backups/backup."+str(dateTimeVar))
          os.system("cp ./contributed-themes/"+str(selected_theme)+"/spinner /data/openpilot/selfdrive/ui/spinner")
          print("OpenPIlot Spinner installed Successfully! Original backuped to ./backups/backup."+str(dateTimeVar))
        else:
          print("Invalid selection")

      else:
        print("OP Spinner is not available for "+str(selected_theme))
        time.sleep(5)

    if (index == 3):                          #additional features
      print("Additional Resources are not an active feature")
      time.sleep(5)
      #if (additionalAvailable != 'N/A'):
      #  print("Additional Resources are not an active feature")
      #  time.sleep(5)
      #else:
      #  print("Additional Resources are not an active feature")
      #  time.sleep(5)

    if (index == 4):                          #main menu
      break

    if (index == 5):                          #reboot
      print('Rebooting.... Enjoy your new theme!!!')
      os.system('reboot')


def go_back(picker): #part of the picker code
  return (None, -1)


CONTRIB_THEMES = "contributed-themes"
EXCLUDED_THEMES = ["Comma-Default", "Example", "ignoreme"]
MIN_SIM_THRESHOLD = 0.25  # user's input needs to be this percent or higher similar to a theme to select it



class ThemeInstaller:
  def __init__(self):
    print_welcome_text()
    self.backup_dir = datetime.now().strftime('backups/backup.%m-%d-%y--%I.%M.%S-%p')  # Get current datetime and store
    os.mkdir(self.backup_dir)  # Create the session backup folder


  def start(self):
    pass



if __name__ == "__main__":
  ti = ThemeInstaller()
  ti.start()
  # MainLoop()
