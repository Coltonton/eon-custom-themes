Version 1.2.0 (2023-04-16)
========================
* Multi-install Feature
* Condense installer code to run in dedicated functions
* Cleanup naming scheme to theme_xxxx.py
* ReDo Restore Code
* Remove traces of APK :(
* LOTS of cleanup / makinging proper / tons of neat logic
* Easter eggs??? Fake plastic ones maybe in this economy...
* I'm sure, and I know im forgetting ALOT yes its been a few years.
* TODO - V2 & V3?????!!!


Version 1.1.1 (2020-01-01)
========================
* Fix backup bug
* Make new utility theme_utils.py for utilities
* fix github hack to --skip-worktree and add option
* Add utility to undo that in theme_utils.py 
* move cleanup_files.py into theme_utils.py
* OP spinner now doesnt needlessly install files it doesnt have to
* re-orrenent spinner code for all
* make print_welcome_text just print_text to use for more then welcome

Version 1.1 (2020-11-03)
========================
* Add @ShaneSmiskol rave rainbow OpenPilot spinner option (It makes the progress bar turn into a rave!)
* Fix **ALL** LeEco based EON boot logos, showing the "battery dead but charging" boot screen when pluged in. These can still be identified by the red chevrons in the top cornors for troubleshooting reasons. Just in case the battery is not working/Comma2 Uno board is not working properly to signify "power issue" insted of making the user think there device is "boot looping" or stuck on the boot logo; when it's a power issue.... like Comma.ai's...
* Implement sloppy hack to prevent OpenPilot from overwriting custom spinner files!
* Added cleanup_files.py in /support for easy removal of files not kept in /data/eon-custom-themes
* Add all the developer info! So everyone can hack and make their EON their own
* Add OnePlus Boot Logo Option
* Add Genesis Theme
* Add discords @cgw1968 custom Bat theme!
* Add @ShaneSmiskol's custom theme for all his help! Thanks again!
* Modify user themes to have the prefix "User-"
* Make restore_backup.py restore_theme.py!
* Move Comma-Default restore utility to restore_theme.py to make it accessible to those with the minimal auto installer!
* Move backup override check to support_functions
* Code Cleanup & fixs
* Bug finding & squashing

Version 1.0 (2020-10-14)
========================
* This is a project dedicated to de-comma-ing your EON! Whether you don't like Comma.ai the company or want to personalize your EON and get a new fresh look, I gotchu fam! This is a community project so here you can find new boot logos, boot animations, OpenPilot loading animations, and even more for your device! Created/designed by myself with help from Shane Smiskol. With themes designed and made by myself and other community members. Remember this is a community project and I've designed it as such. Feel free to create your own themes and publish them to this community repo! (information coming later, see next paragraph) I have put a lot of work into making this project awesome and intelligent and intuitive with plenty more planned down the pipeline

* Soon to come will be all the information for you to easily make your own themes as well in release v1.1! (quite an about of work I have to do providing over the top documentation, because its important!!!)

* Happy Theming :)
Coltonton