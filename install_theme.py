import os
from os import path
import sys
import difflib
import time
import datetime
import curses
from misc.pick.pick import Picker


os.chdir(os.getcwd())

CONTRIB_THEMES         = "contributed-themes"
EXCLUDED_THEMES        = ["Comma-Default", "Example", "ignoreme"]
MIN_SIM_THRESHOLD      = 0.25  # user's input needs to be this percent or higher similar to a theme to select it

selected_theme         = ""
bootlogothemepath      = ""
bootlogodir            = ""

bootLogoAvailable      = "N/A"
bootAnimationAvailable = "N/A"
spinnerAvailable       = "N/A"
additionalAvailable    = "N/A"

running                = 1

dt = datetime.datetime.now()
dateTimeVar = dt.strftime("%m%d%y_%T")

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
def Main():
  print ('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
  print ("+     Created By: Brandon (Colton) S. EndLine \ n      +")
  print ('+  Special Thanks to @ShaneSmiskol for all the help!!! +')
  print ('+     Free to use! Free to Edit! Free to Contribute!   +')
  print ("+           It's your EON, do what you want!           +")
  print ('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

  os.mkdir('backups/backup.'+str(dateTimeVar))

  if(path.exists('/sys/devices/virtual/switch/tri-state-key') == True):
    print('\nOnePlus EON Device Detected')
    bootlogothemepath = "OP3T-Logo/LOGO"
    bootlogodir = "/dev/block/bootdevice/by-name/logo"
  else:
    print ('LeEco EON Device Detected')
    bootlogothemepath = "LeEco-Logo/SPLASH"
    bootlogodir = "/dev/block/bootdevice/by-name/splash"

  time.sleep(3)

def MainLoop():
  global selected_theme
  while (running == 1):
    if (isAutoInstall == 1):
      selected_theme = selectedAutoTheme
      Auto_Installer()
    else:
      selected_theme = ThemePicker()
      setup()
      Self_Installer()

def ThemePicker():
  available_themes = [t for t in os.listdir(CONTRIB_THEMES)]
  available_themes = [t for t in available_themes if os.path.isdir(os.path.join(CONTRIB_THEMES, t))]
  available_themes = [t for t in available_themes if t not in EXCLUDED_THEMES]
  lower_available_themes = [t.lower() for t in available_themes]
  print('\nAvailable themes:')
  for idx, theme in enumerate(available_themes):
    print('{}. {}'.format(idx + 1, theme))
  print('\nChoose a theme to install (by name or index)')
  print("Enter Q to quit and reboot.")
  while 1:
    print('Select a theme: ', end='')
    theme = input().strip().lower()
    if (theme == 'q', 'Q', 'r', 'R' ):
      print("Rebooting...")
      #Sos.system("reboot")
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

def setup():
  if(path.exists('./contributed-themes/'+str(selected_theme)+'/'+str(bootlogothemepath)) == True):
    bootLogoAvailable = "Boot_Logo"
  if(path.exists('./contributed-themes/'+str(selected_theme)+'/bootanimation.zip') == True):
    bootAnimationAvailable="Boot_Animation"
  if(path.exists('./contributed-themes/'+str(selected_theme)+'/spinner') == True):
    spinnerAvailable="OP_Spinner"
  if(path.exists('./contributed-themes/'+str(selected_theme)+'/additional') == True):
    additionalAvailable="Additional-resources"

def Auto_Installer():
    if (autoInstallLogo != 'no'):                   #BootLogo Install Code
      os.system("cp "+str(bootlogodir)+" backups/backup."+str(dateTimeVar)) #DEV EDIT SHOULD BE MV
      os.system("dd if=./contributed-themes/"+str(selected_theme)+"/OP3T-Logo/LOGO of="+str(bootlogodir))
      print("Boot Logo installed successfully! Original backuped to ./backups/backup."+str(dateTimeVar))

    if (autoInstallAnim != 'no'):                   #BootAni Install Code
      os.system("mount -o remount,rw /system")
      os.system("mv /system/media/bootanimation.zip backups/backup."+str(dateTimeVar))
      os.system("cp ./contributed-themes/"+str(selected_theme)+"/bootanimation.zip /system/media")
      os.system("chmod 666 /system/media/bootanimation.zip")
      print("Boot Logo installed successfully! Original backuped to ./backups/backup."+str(dateTimeVar))

    if (autoInstallSpinner != 'no'):                #OP Spinner Code
      os.system("cp /data/"+str(autoOpenPilotDirName)+"/selfdrive/ui/spinner/spinner backups/backup."+str(dateTimeVar)) #TEMP DEV EDIT SHOULD BE MV
      os.system("cp ./contributed-themes/"+str(selected_theme)+"/spinner /data/"+str(autoOpenPilotDirName)+"/selfdrive/ui/spinner")
      print("OP Spinner Installed Successfully! Original backuped to ./backups/backup."+str(dateTimeVar))

    if (autoInstallAdditional != 'no'):             #additional features
      print("Additional Resources are not an active feature")

def Self_Installer():
  r=1
  while (r == 1):
    title = 'What resources do you want to install for the '+str(selected_theme)+' theme?: '
    options = [bootLogoAvailable, bootAnimationAvailable, spinnerAvailable, additionalAvailable, 'Main Menu', 'Reboot']

    picker = Picker(options, title)
    picker.register_custom_handler(curses.KEY_LEFT, go_back)
    option, index = picker.start()
    print(option, index)

    if (index == 0):                   #BootLogo Install Code
      if (bootLogoAvailable != 'N/A'):
        os.system("cp "+str(bootlogodir)+" backups/backup."+str(dateTimeVar)) #DEV EDIT SHOULD BE MV
        os.system("dd if=./contributed-themes/"+str(selected_theme)+'/'+str(bootlogothemepath)+" of="+str(bootlogodir))
        print("Boot Logo installed successfully! Original backuped to ./backups/backup."+str(dateTimeVar))
      else:
        print("Boot logo is not available for "+str(selected_theme))

    if (index == 1):                   #BootAni Install Code
      if (bootAnimationAvailable != 'N/A'):
        os.system("mount -o remount,rw /system")
        os.system("mv /system/media/bootanimation.zip backups/backup."+str(dateTimeVar))
        os.system("cp ./contributed-themes/"+str(selected_theme)+"/bootanimation.zip /system/media")
        os.system("chmod 666 /system/media/bootanimation.zip")
        print("Boot Logo installed successfully! Original backuped to ./backups/backup."+str(dateTimeVar))
      else:
        print("Boot Annimation is not available for "+str(selected_theme))

    if (index == 2):                   #OP Spinner Code
      if (spinnerAvailable == 'N/A'):
        print("Does your OpenPilot directory have a custom name? (ex. arnepilot, dragonpilot)")
        print("Choose an option (by name or index) (case matters)")
        print("1. Yes")
        print("2. No")
        isCustOP = input("")

        if (isCustOP == 'y','Y','yes','Yes',1):  #Yes custom OP dir
          opdir = input("What is the OP directory name? (case matters)")
          os.system("cp /data/"+str(opdir)+"/selfdrive/ui/spinner/spinner backups/backup."+str(dateTimeVar)) #TEMP DEV EDIT SHOULD BE MV
          os.system("cp ./contributed-themes/"+str(selected_theme)+"/spinner /data/"+str(opdir)+"/selfdrive/ui/spinner")
          print("OP Spinner Installed Successfully! Original backuped to ./backups/backup."+str(dateTimeVar))
        elif (isCustOP == 'n','N','no','No',2):#No custom OP dir
          os.system("cp /data/openpilot/selfdrive/ui/spinner/spinner backups/backup."+str(dateTimeVar)) #TEMP DEV EDIT SHOULD BE MV
          os.system("cp ./contributed-themes/"+str(selected_theme)+"/spinner /data/openpilot/selfdrive/ui/spinner")
          print("OP Spinner Installed Successfully! Original backuped to ./backups/backup."+str(dateTimeVar))
        else:
          print("Invalid selection")

      else:
        print("OP Spinner is not available for "+str(selected_theme))

    if (index == 3):                          #additional features
      if (additionalAvailable != 'N/A'):
        print("Additional Resources are not an active feature")
      else:
        print("Additional Resources are not an active feature")

    if (index == 4):                          #main menu
      break

    if (index == 5):                          #reboot
      print('Rebooting.... Enjoy!!!!')
      os.system('reboot')
  

def str_sim(a, b):
  return difflib.SequenceMatcher(a=a, b=b).ratio()

def go_back(picker):
  return (None, -1)




if __name__ == "__main__":
  Main()
  MainLoop()
