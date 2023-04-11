#!/usr/bin/python
# ===================  Misc vars =================== ##
SHOW_CONSOLE_OUTPUT = False                # Show the console output when 'make' is called?
VERBOSE = False
DEVMODE = False
DEV_PLATFORM = ""
EON_CUSTOM_THEMES_VER = "1.2"              # This Softwares Version

# ==============  Backup related vars ============== ##
BACKUPS_DIR = '/storage/emulated/0/theme-backups' if not DEVMODE else './test-theme-backups'
BACKUP_OPTIONS = []

# =============  get_aval_themes() vars ============= ##
CONTRIB_THEMES = '/data/eon-custom-themes/contributed-themes' if not DEVMODE else "./contributed-themes"
EXCLUDED_THEMES = ["Test", 'Example', 'ignoreme', 'Colton'] if not DEVMODE else ['Example', 'ignoreme', 'Colton']
MIN_SIM_THRESHOLD = 0.25      # user's input needs to be this percent or higher similar to a theme to select it

# =========== Get OP Ver & Location vars =========== ##
OP_VER = 0.1
OP_LOC = ''

# =================  Welcome Texts ================= ##
WELCOME_TEXT = ['Created By: Colton (Brandon) S. EndLine \\n',
                'Special Thanks to @ShaneSmiskol for all the help!!!',
                'Free to use! Free to Edit! Free to integrate!',
                'Design and contribute your themes today!',
                '(See the developer folder in this repo)',
                'It\'s your EON, do what you want!',
                'Version {}'.format(EON_CUSTOM_THEMES_VER)]
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
                '*NOTE* this is the backup & default restore program']
UTIL_WELCOME_TEXT = ['Created By: Colton (Brandon) S. EndLine \\n',
                'Special Thanks to @ShaneSmiskol for all the help!!!',
                'Free to use! Free to Edit! Free to integrate!',
                'Design and contribute your themes today!',
                '(See the developer folder in this repo)',
                'It\'s your EON, do what you want!',
                ' ',
                '*NOTE* this is the theme utility program for misc functions']

CLEANUP_TEXT = ['\n\nWelcome to the uninstall - cleanup utility',
                    "I'm sad to see you go... :",
                  '\nThis program removes the following files not stored in the main directory:',
                    '- WARNING!!!! ALL BACKUPS!!! Stored in /sdcard/theme-backups',
                    '- eon_custom_themes_self_installed.txt in /sdcard used as a marker to the auto installer',
                  '\nIt does not remove:',
                    '- The main project directory',
                    "- Any installed themes, please run 'Restore Comma-default' from",
                    'this program to restore the comma-default boot logo and boot animation',
                    'BEFORE running this utility!!!']