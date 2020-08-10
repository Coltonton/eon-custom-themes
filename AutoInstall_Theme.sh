IsThemeInstalled=/storage/emulated/0/theme_installed
switchstate=`cat /sys/devices/virtual/switch/tri-state-key/state` || switchstate=5
Is3TON=/sys/devices/virtual/switch/tri-state-key/state

PS3="Select The Theme: "
select theme in OP3T-Acura OP3T-Android OP3T-Apple OP3T-Arne OP3T-Chevy OP3T-Colton quit; 

do
    case $theme in
        OP3T-Acura)
            echo "oof"
            ;;
        OP3T-Android)
            read -p "Enter the first number: " n1
            read -p "Enter the second number: " n2
            echo "$n1 - $n2 = $(($n1-$n2))"
            ;;
        OP3T-Apple)
            read -p "Enter the first number: " n1
            read -p "Enter the second number: " n2
            echo "$n1 * $n2 = $(($n1*$n2))"
            ;;
        OP3T-Arne)
            read -p "Enter the first number: " n1
            read -p "Enter the second number: " n2
            echo "$n1 / $n2 = $(($n1/$n2))"
            ;;
        OP3T-Chevy)
            read -p "Enter the first number: " n1
            read -p "Enter the second number: " n2
            echo "$n1 / $n2 = $(($n1/$n2))"
            ;;
        OP3T-Colton)
            read -p "Enter the first number: " n1
            read -p "Enter the second number: " n2
            echo "$n1 / $n2 = $(($n1/$n2))"
            ;;
        quit)
            break
            ;;
    *) 
      echo "Invalid option $REPLY"
      ;;
  esac
done

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