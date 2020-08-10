IsThemeInstalled=/storage/emulated/0/theme_installed
switchstate=`cat /sys/devices/virtual/switch/tri-state-key/state` || switchstate=5
Is3TON=/sys/devices/virtual/switch/tri-state-key/state

read -p "Enter 1 for OnePlus Eon, or enter 2 for LeEco Eon:"  eonval
read -p "Enter the theme number"  themeval

if [ $eonval == 1 ] 
    then
    if [ $themeval == 1 ] 
        then
    elif [ $eonval == 2 ]
    elif [ $eonval == 2 ]
    elif [ $eonval == 2 ]
    elif [ $eonval == 2 ]
    elif [ $eonval == 2 ]
    elif [ $eonval == 2 ]
    elif [ $eonval == 2 ]
    elif [ $eonval == 2 ]
elif [ $eonval == 2 ] 
    then
    echo "2" 
elif [ $eonval > 2 ] 
    then
    echo "I said 1 or 2 you silly goof!" 
fi

#cd /data/hooeypilot
#exec ./installtheme.sh
#cd /storage/emulated/0
#if [ -f "$IsThemeInstalled" ]; then #Is Installed
#    echo "Theme Is Installed"
##else                                #Is Not Installed
#    echo "Theme Is Not Installed"
#    if [ -f "$Is3TON" ]
#    then                              #If 3T EON
#        echo "$Is3TON"
#        echo "3TON Install"
#        #cd /data/hooeypilot/selfdrive/ui/spinner
#        #rm -f spinner
#        #cp /data/hooeypilot/Theme/spinner /data/hooeypilot/selfdrive/ui/spinner
#    
#    else                              #If Leon
#     echo "Leon Install"
#    fi
#fi

#export PASSIVE="0"
#exec ./launch_chffrplus.sh