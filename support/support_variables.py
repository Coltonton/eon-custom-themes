#!/usr/bin/python
# ===================  Misc vars =================== ##
SHOW_CONSOLE_OUTPUT = False                # Show the console output when 'make' is called?

# ==============  Backup related vars ============== ##
BACKUPS_DIR = '/storage/emulated/0/theme-backups'
BACKUP_OPTIONS = []

# =============  get_user_theme() vars ============= ##
CONTRIB_THEMES = 'contributed-themes'
EXCLUDED_THEMES = ['Example', 'ignoreme', 'Kumar-Nightmode-APK', 'Colton']
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
                '*NOTE* this is the backup & default restore program']
UTIL_WELCOME_TEXT = ['Created By: Colton (Brandon) S. EndLine \\n',
                'Special Thanks to @ShaneSmiskol for all the help!!!',
                'Free to use! Free to Edit! Free to integrate!',
                'Design and contribute your themes today!',
                '(See the developer folder in this repo)',
                'It\'s your EON, do what you want!',
                ' ',
                '*NOTE* this is the theme utility program for misc functions']

# =============== Spinner Notify Text ================ ##
SPINER_NOTIF_TEXT = ['\n\n ************************* PLEASE READ *************************',
                        'Before continuing please note! Due to the issues with',
                        'replacing files in OpenPilot due to it being git version cotrolled;',
                        'this program has a temporary workaround until its next verion.',
                        'In order to prevent local OpenPilot spinner changes from being',
                        'discarded at random without user prompt (if you choose) this',
                        'program will mark the changed spinner files to: `git update-index --skip-worktree`',
                        ' ',
                        'In essence this tells git that the files are always unchanged',
                        'thus when anything like `git stash`, `git pull` or `git reset` is called',
                        'the files are ignored and not changed and does NOT prevent pull updates!',
                        ' ',
                        'This does have the side effect where if the spinner files are',
                        'changed upstream (the OP repo) and you try to `git pull` it will',
                        'conflict and tell you to stash changes (which wont work) and prevent',
                        'you from pulling changes. You must undo the --skip-worktree flag',
                        'by running the `theme_utils.py` program  and choosing `Remove git --skip-worktree flag(s)`',
                        'with the command `/data/eon-custom-themes/theme_utils.py`']