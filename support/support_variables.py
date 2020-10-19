BACKUPS_DIR = '/storage/emulated/0/theme-backups'
BACKUP_OPTIONS = []

# =============  get_user_theme() vars ============= ##
CONTRIB_THEMES = 'contributed-themes'
ECT_LOCATION = '/data/eon-custom-themes'
EXCLUDED_THEMES = ['Example', 'ignoreme']
MIN_SIM_THRESHOLD = 0.25  # user's input needs to be this percent or higher similar to a theme to select it

# ==============  Auto Installer Vars ============== ## - see DEVREADME
IS_AUTO_INSTALL = False                    # Do Auto Install
DESIRED_AUTO_VER = '1'                     # Desired theme version, add 1 to update users theme.
AUTO_INSTALL_CONF = {'auto_selected_theme': 'Arne',   # Your theme folder, name (case matter)
                     'op_dir_name': 'arnepilot',      # Name of your OpenPilot Directory
                     'install_3T_logo': True,         # Do you have a 3T logo to install?
                     'install_Leo_logo': True,        # Do you have a LeEco logo to install?
                     'install_bootanim': True,        # Do you have a bootanimation.zip to install?
                     'ani_color': ''}                 # 'color_' or 'white_' or no special? 

# =================  Welcome Texts ================= ##
WELCOME_TEXT = ['Created By: Colton (Brandon) S. EndLine \\n',
                'Special Thanks to @ShaneSmiskol for all the help!!!',
                'Free to use! Free to Edit! Free to integrate!',
                'Design and contribute your themes today!',
                '(See the developer folder in this repo)',
                'It\'s your EON, do what you want!']
AUTO_WELCOME_TEXT = ['Created By: Colton (Brandon) S. EndLine \\n',
                'Special Thanks to @ShaneSmiskol for all the help!!!',
                'Free to use! Free to Edit! Free to integrate!',
                'Design and contribute your themes today!',
                '(See the developer folder in this repo)',
                'It\'s your EON, do what you want!',
                '*NOTE* THIS IS AN AUTO INSTALL PROGRAM',
                'This is a minimal installer and only made to',
                'auto install the theme the developer of this fork',
                'has decided on and will not work if you want to',
                'manually install another theme\n',
                "'cd /data && git clone https://github.com/Coltonton/eon-custom-themes.git'",
                "Then cd exec /data/eon-custom-themes/install_theme.py",
                ' to use the full program! Installing a theme manually',
                'blocks this auto installer from overwriting!']
RESTORE_WELCOME_TEXT = ['Created By: Colton (Brandon) S. EndLine \\n',
                'Special Thanks to @ShaneSmiskol for all the help!!!',
                'Free to use! Free to Edit! Free to integrate!',
                'Design and contribute your themes today!',
                '(See the developer folder in this repo)',
                'It\'s your EON, do what you want!',
                ' ',
                '*NOTE* this is the backup restore program']
