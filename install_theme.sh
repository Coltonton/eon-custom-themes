#!/usr/bin/bash
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


datetimevar=$(date +%m%d%y_%T)                  #Take current date/time for creating& adding to backup folder 

echo 'Copyright (c) 2020 Brandon (Colton) S. EndLine \n'
echo 'Free to use! Free to Edit!'
echo "It's your EON, do what you want!"
mkdir /storage/emulated/0/backup.$datetimevar   #Create backup folder

###################################### Get User Device #####################################################
if [ -d "/sys/devices/virtual/switch/tri-state-key" ]; then #Crude device detection, it works tho *shrug*
    echo 'OnePlus EON Device Detected'
    EON_TYPE=1 ## 1 = OnePlus 3T 2 = LeEco
else
    echo 'LeEco EON Device Detected'
    EON_TYPE=2 ## 1 = OnePlus 3T : 2 = LeEco
fi

python theme_picker.py 2> $theme

echo "Selected theme (in bash): ${theme}"
#echo "Available Themes:"
#THEMES=()
#for d in "$CONTRIB_THEMES"/*; do
#    if [ -d "$d" ]; then
#        echo "$d"
#        THEMES+=("$d")
#    fi
#done
#echo "${THEMES[*]}"

####################################### SHANE HALPPPPPPP #####################################################
#PS3="Select The Theme: "
#select theme in Acura Android Apple Arne Chevy Colton CommunityPilot ODragonPilot General Honda Hyundai Kia Lexus OnePlus Subaru Toyota quit;
#
#selectedtheme=$theme #SHANE- this is the new way to do things ignore the case, unless that works better
#echo "Test"
#
#do
#case $theme in
#    Acura)
#        selectedtheme=$theme #SHANE- this is the new way to do things
#        ;;
#    Android)
#        selectedtheme=$theme
#        ;;
#    Apple)
#        selectedtheme=$theme
#        ;;
#    Arne)
#        selectedtheme=$theme
#        ;;
#    Chevy)
#        selectedtheme=$theme
#        ;;
#    Colton)
#        cd /data/EON-Custom-Themes/Contributed-Themes/Colton
#        exec ./OP3T-Install.sh
#        ;;
#    CommunityPilot)
#        cd /data/EON-Custom-Themes/Contributed-Themes/CommunityPilot
#        exec ./OP3T-Install.sh
#        ;;
#    DragonPilot)
#        cd /data/EON-Custom-Themes/Contributed-Themes/DragonPilot
#        exec ./OP3T-Install.sh
#        ;;
#    General)
#        cd /data/EON-Custom-Themes/Contributed-Themes/General
#        exec ./OP3T-Install.sh
#        ;;
#    Honda)
#        cd /data/EON-Custom-Themes/Contributed-Themes/Honda
#        exec ./OP3T-Install.sh
#        ;;
#    Hyundai)
#        cd /data/EON-Custom-Themes/Contributed-Themes/Hyundai
#        exec ./OP3T-Install.sh
#        ;;
#    Kia)
#        cd /data/EON-Custom-Themes/Contributed-Themes/Kia
#        exec ./OP3T-Install.sh
#        ;;
#    Lexus)
#        cd /data/EON-Custom-Themes/Contributed-Themes/Lexus
#        exec ./OP3T-Install.sh
#        ;;
#    OnePlus)
#        cd /data/EON-Custom-Themes/Contributed-Themes/OnePlus
#        exec ./OP3T-Install.sh
#        ;;
#    Subaru)
#        cd /data/EON-Custom-Themes/Contributed-Themes/Subaru
#        exec ./OP3T-Install.sh
#        ;;
#    Toyota)
#        cd /data/EON-Custom-Themes/Contributed-Themes/Toyota
#        exec ./OP3T-Install.sh
#        ;;
#    quit)
#        break
#        ;;
#    *)
#        echo "Invalid option"
#        ;;
#    esac
#done
#
#
############################# Determine The Availible Theme Resources #######################################
##if [ -f "$FILE" ]; then        #(ignore shane, function not active)
##    echo "$FILE exists."
##fi
##if [ -f "/data/EON-Custom-Themes/Contributed-Themes/$theme" ]; then
##    echo "$FILE exists."
##fi
##if [ -f "$FILE" ]; then
##    echo "$FILE exists."
##fi
##if [ -f "$FILE" ]; then
##    echo "$FILE exists."
##fi
#
#############################################################################################################
############################################## Installation Code ############################################
#############################################################################################################
#cd /data/EON-Custom-Themes/Contributed-Themes/$selectedtheme
#if [ $eontype == 1 ]               ##OnePlus EON Installation
#then
#    echo '-----------------------------------------'
#    PS3="What Would you like to install? "
#    select choice in Boot-Logo Boot-Animation OP-Spinner Additional Reboot Quit; #Create a selection menu for user
#    do                                                                           #[DEVNOTE] remove the choices you dont have!
#        case $choice in            #
#            Boot-Logo)             #Install Boot Logo Code
#                cp /dev/block/platform/soc/624000.ufshc/by-name/LOGO /storage/emulated/0/backup.$datetimevar #TEMP DEV EDIT SHOULD BE MV
#                dd if=./OP3T-Logo/LOGO of=/dev/block/platform/soc/624000.ufshc/by-name/LOGO
#                echo "Boot Logo Installed Successfully! Original backuped to /sdcard/backup.$datetimevar"
#                ;;
#            Boot-Animation)        #Install Boot Annimation Code
#                mount -o remount,rw /system
#                mv /system/media/bootanimation.zip /storage/emulated/0/backup.$datetimevar
#                cp bootanimation.zip /system/media
#                chmod 666 /system/media/bootanimation.zip
#                echo "Boot Animation Installed Successfully! Original backuped to /sdcard/backup.$datetimevar"
#                ;;
#            OP-Spinner)            #Install OP Spinner Code
#                echo 'If you are using a OP fork with a custom directory name: '
#                read -p '(ex. like ArnePilot/DragonPilot) enter 1, else enter 0: ' iscustomop
#                if [ $iscustomop = 1 ]
#                then
#                    read -p 'What is the OP directory name? (case matters)' opdir
#                    if [ -d  "/data/$opdir" ]
#                    then
#                        cp /data/$opdir/selfdrive/ui/spinner/spinner /storage/emulated/0/backup.$datetimevar #TEMP DEV EDIT SHOULD BE MV
#                        cp spinner /data/$opdir/selfdrive/ui/spinner
#                        echo "$opdir Spinner installed successfully! Original backuped to /sdcard/backup.$datetimevar"
#                    else
#                        echo "$opdir does not exist, please check case"
#                    fi
#                elif [ $iscustomop == 0 ]
#                then
#                    cp /data/openpilot/selfdrive/ui/spinner/spinner /storage/emulated/0/backup.$datetimevar #TEMP DEV EDIT SHOULD BE MV
#                    cp spinner /data/openpilot/selfdrive/ui/spinner
#                    echo "OP Spinner Installed Successfully! Original backuped to /sdcard/backup.$datetimevar"
#                else
#                    echo "Incorrect responce given Type 1 or 0"
#                fi
#
#                ;;
#            Additional)            #Up To You To Code!!!
#                echo "addit Done!"
#                ;;
#            Reboot)                #Exit and reboot
#                echo "Now Rebooting! Enjoy your new themes!"
#                reboot
#                ;;
#            Quit)                  #Quit Program
#                echo "Goodbye!!!"
#                break
#                ;;
#            *)                     #Invalid Selection
#                echo "Invalid selection"
#                ;;
#        esac
#    done
#elif [ $eontype == 2 ]             ## LeEco Installation
#    rm -d /storage/emulated/0/backup.$datetimevar
#    echo 'Your Device does not appear to be a OnePlus 3T EON.'
#    echo 'Please select the correct device in the main program!'
#    echo 'Aborting to prevent hard bricking!!!'
#fi
#
#
##cd /data/EON-Custom-Themes/Contributed-Themes/Subaru
##exec ./OP3T-Install.sh