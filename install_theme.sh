um #!/usr/bin/bash
#################################################################################
#           Copyright (c) 2020 Brandon (Colton) S. EndLine \n                   #
#                         http://EndLineTech.com                                #
#                                                                               #
# this software is provided 'as-is', without any express or implied             #
# warranty. In no event will the authors be held liable for any damages         #
# arising from the use of this software.                                        #
#                                                                               #
# Permission is granted to anyone to use /edit this software for any purpose,   #
# and must not be redistributed without written permission. You may fork/modify #
# freely, but must not redistribute in other packages without permission,       #
# subject to the following restrictions:                                        #
#                                                                               #
# 1. The origin of this software must not be misrepresented; you must not       #
#    claim that you wrote the original software.                                #
#                                                                               #
# 2. Altered source versions must be plainly marked as such, and must not be    #
#    misrepresented as being the original software.                             #
#                                                                               #
# 3. This notice may not be removed or altered from any source                  #
#    distribution.                                                              #
#                                                                               # 
#################################################################################
#
#
# View Themes at http://endoflinetech.com/eon-custom-themes
#
# ===============HOW TO USE=========================================
# SSH into your EON and cd /data
# git clone https://github.com/Coltonton/eon-custom-themes.git
# Once downloaded exec /data/eon-custom-themes/install_theme.sh
# Follow all the prompts to install your desired theme elements
#
# All changes here are persistant, OP Spinenr/Additional components
# Will reset if you re-clone openpilot. It should stick through 
# OpenPilot Git Pull updates
#     
# You can leave this repo on your device or remove it with
# cd /data && rm -f eon-custom-themes
#
# ==============DEV NOTES===========================================
# Making your own theme? Wonderful! You dont need to make changes
# to this file! (Unless you have additional content for your theme
# See README_DEV) Its designed to just work! (as long as you follow
# the guidlines in the README_DEV) You WILL have to add your theme 
# name and code to the install_theme.sh (see README_DEV)
#  
# On top of my exellent commenting I have left [DEVNOTE]'s in this file
# with more info or a identifier that can be traced back into the
# README_DEV file for this project under the DevNote, section


############################################################################################################
#======================================= Code Start! ======================================================#
############################################################################################################
echo 'Created By: Brandon (Colton) S. EndLine \n'
echo 'Special Thanks to @ShaneSmiskol for all the help!!!'
echo 'Free to use! Free to Edit! Free to Contribute'
echo "It's your EON, do what you want!"

datetimevar=$(date +%m%d%y_%T)                  #Take current date/time for creating& adding to backup folder 
mkdir /storage/emulated/0/backup.$datetimevar   #Create backup folder

###################################### Get User Device #####################################################
if [ -d "/sys/devices/virtual/switch/tri-state-key" ] #Crude device detection, it works tho *shrug* 
then 
    echo 'OnePlus EON Device Detected'
    bootlogothemepath='OP3T-Logo'
    bootlogodir='/dev/block/bootdevice/by-name/boot'
else
    echo 'LeEco EON Device Detected'
    bootlogothemepath='LeEco-Logo'
    bootlogodir='/dev/block/bootdevice/by-name/splash'
fi

# get theme picked by user with python helper file
selectedtheme="$(python theme_picker.py 2>&1 > /dev/tty)"  # tty is so it redirects python CLI to screen
if [ "$selectedtheme" == "none" ]; then
    echo "User didn't provide a theme, exiting!"
    exit
fi


############################ Determine The Availible Theme Resources ####################################### 
if [ -f "if=./contributed-themes/$selectedtheme/$bootlogothemepath/LOGO" ]; then 
    bootLogoAvailable="Boot_Logo"
else
    bootLogoAvailable="N/A"
fi
if [ -f "./contributed-themes/$selectedtheme/bootanimation.zip" ]; then
    bootAnimationAvailable="Boot-Animation"
else
    bootLogoAvailable="N/A"
fi
if [ -f "./contributed-themes/$selectedtheme/spinner" ]; then
    spinnerAvailable="OP-Spinner"
else
    bootLogoAvailable="N/A"
fi
if [ -d "./contributed-themes/$selectedtheme/additional" ]; then
    additionalAvailable="Additional-resources"
else
    bootLogoAvailable="N/A"
fi

############################################################################################################
############################################# Installation Code ############################################
############################################################################################################
cd /data/EON-Custom-Themes/Contributed-Themes/$selectedtheme          
echo '-----------------------------------------'
PS3="What Would you like to install? "
select asset in Boot-Logo Boot-Animation OP-Spinner Additional Reboot Quit; #Create a selection menu for user 
do                                                                        
    case $asset in            # 
        Boot-Logo)             #Install Boot Logo Code
            if [ $bootLogoAvailable != 'N/A' ]; then 
                cp $bootlogodir /storage/emulated/0/backup.$datetimevar #TEMP DEV EDIT SHOULD BE MV
                dd if=./contributed-themes/$selectedtheme/OP3T-Logo/LOGO of=$bootlogodir
                echo "Boot Logo installed successfully! Original backuped to /sdcard/backup.$datetimevar"
                ;;
            else
                echo "Boot logo is not available for $selectedtheme"
            fi
        Boot-Animation)        #Install Boot Annimation Code
            if [ $bootAnimationAvailable != 'N/A' ]; then 
                mount -o remount,rw /system
                mv /system/media/bootanimation.zip /storage/emulated/0/backup.$datetimevar
                cp ./contributed-themes/$selectedtheme/bootanimation.zip /system/media
                chmod 666 /system/media/bootanimation.zip
                echo "Boot Animation Installed Successfully! Original backuped to /sdcard/backup.$datetimevar"
            else
                echo "Boot Animation is not available for $selectedtheme"
            fi
            ;;
        OP-Spinner)            #Install OP Spinner Code
            if [ $spinenrAvailable != 'N/A' ]; then
                PS3="Does your openpilot directory have a custom name? (ex. arnepilot, dragonpilot) "
                select iscustomop in Yes No; #Create a selection menu for user  
                do 
                    case $iscustomop in
                        Yes)
                            read -p 'What is the OP directory name? (case matters)' opdir 
                            if [ -d  "/data/$opdir" ]
                            then
                                cp /data/$opdir/selfdrive/ui/spinner/spinner /storage/emulated/0/backup.$datetimevar #TEMP DEV EDIT SHOULD BE MV
                                cp ./contributed-themes/$selectedtheme/spinner /data/$opdir/selfdrive/ui/spinner
                                echo "$opdir Spinner installed successfully! Original backuped to /sdcard/backup.$datetimevar"
                            else
                                echo "$opdir does not exist, please check case"
                            fi
                            ;;
                        No)
                            cp /data/openpilot/selfdrive/ui/spinner/spinner /storage/emulated/0/backup.$datetimevar #TEMP DEV EDIT SHOULD BE MV
                            cp ./contributed-themes/$selectedtheme/spinner /data/openpilot/selfdrive/ui/spinner
                            echo "OP Spinner Installed Successfully! Original backuped to /sdcard/backup.$datetimevar"
                            ;;
                        *)
                            echo "Invalid selection"
                            ;;
            else
                echo "OP Spinner not available for $selectedtheme"
            fi
            ;;
        Additional)            #Up To You To Code!!! 
            if [ $bootLogoAvailable != 'N/A' ]; then 
                echo "Additional resources uncoded!"
                ;;
            else
                echo "Additional resources are not available for $selectedtheme"
            fi
            ;;
        Reboot)                #Exit and reboot
            echo "Now Rebooting! Enjoy your new themes!"
            reboot
            ;;
        Quit)                  #Quit Program
            echo "Goodbye!!!"
            break
            ;;
        *)                     #Invalid Selection 
            echo "Invalid selection"
            ;;
    esac
done
