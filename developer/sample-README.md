Table of Contents (Pre-Made, if you have...)
=======================

### Minimal Self Installer Assistance (Included with OP Forks)
* [Main Info](#EON-Custom-Themes)
* [Disable auto installer](#Disable-auto-installer)
* [WHY DID MY EONS THEME CHANGE NO ONE TOLD ME](#WHY-DID-MY-EONS-THEME-CHANGE-NO-ONE-TOLD-ME)
* [Features](#Features)
* [Support](#Support)

### Un-Installing EON-Custom-Themes
* [Main Info](#UnInstalling-EON-Custom-Themes)









(Include this somewhere in the top or your installation instructions)
### PLEASE NOTE!!
 This version of OpenPilot includes the auto installer of the [EON-Custom-Themes](https://github.com/Coltonton/eon-custom-themes) project created by [@Coltonton](https://github.com/Coltonton/eon-custom-themes) and will replace your EON's Android boot logo and boot animation on next reboot. See the [EON-Custom-Themes](#EON-Custom-Themes) section of this README to learn more or how to [disable the auto installer.](#Disable-auto-installer)











(Include this anywhere)
## EON Custom Themes:
[EON Custom Themes](https://github.com/Coltonton/eon-custom-themes) is community project brain-child of @Coltonton and allows you to easily change your EON's (3T,Gold,Two) boot logo, boot animation, and OP spinner. This version of ArnePilot has a minmal version installed as part of this repo to automagiclly install the ArnePilot theme on your EON by default. It only includes minimal necessary files for this theme to work, and does not include all the other themes, please see the  [main project](https://github.com/Coltonton/eon-custom-themes) for more!

### Disable auto installer:

- If you do not wish to have the ArnePilot boot logo and boot animation installed as part of your EON (change will stick despite what OpenPilot fork you run) follow the instructions to come, but please read everythting here!

- If you installed a different theme before hand from the main EON-Custom-Theme project you need not worry about this step. The program is intellegent enough to know if another theme was already installed and it's assumed you probably want that one.

- *psst* hey you, yeah you... dont want Arne's theme? Well.... how about one to go with your Honda/Toyota/Subaru/Hyundai etc? there are plenty to choose from  [over here](https://github.com/Coltonton/eon-custom-themes)!!!

- To disable the auto installation process simply ssh into your eon and `nano /data/arnepilot/eon-custom-themes/support/do_not_auto.txt` by changing the 0 to a 1. This will prevent any auto install attempts, this MUST BE done before the next reboot after you clone or pull this version to prevent the auto installer from running next reboot!!

### WHY DID MY EONS THEME CHANGE NO ONE TOLD ME!!
- Didn't know this version of ArnePilot auto installs a custom theme and dont like it or Simply want to go back to the Comma stock EON theme? Firstly may I recomend the main [EON Custom Themes](https://github.com/Coltonton/eon-custom-themes) project that this minimal version is a subsidiary of? If you dont know it is a community project created by @Coltonton for the community and allows you to chage your EONs boot logo and boot animation, and OP spinenr (as you saw if you're reading this...) With many themes available for all the major supported cars! ex. Honda, Hyundai, Toyota, Subaru, and much more, including others! [Check it out!!](https://github.com/Coltonton/eon-custom-themes) N...No? Oh...Okay you want the Comma stock one back eh? You Sure? Colton put many weeks of work into creating that project and making it easy and intuitive for you to get a custom look!! O..oh... okay... still not interested.... that's fine! This wonderfully overengineered and overthought program made a backup when it installed this theme automagicly! To restore the comma stock theme ssh into your EON and:
- - `exec /data/openpilot/eon-custom-themes/restore_theme.py` and follow the prompts of the easy to use program! You will not need to follow the steps above and set the `do_not_auto.txt` file to 1 (unless you want to) since you used the program to install a chosen theme (or restore in this case) it will remember that! Even if its a backup! 
- - If you lost the backup somehow please clone the [main project here](https://github.com/Coltonton/eon-custom-themes), and use the simple program to install the 'comma-default' theme

### Features:

- Don't like the white boot animation? Get it in ArneBlue! just edit `AUTO_INSTALL_CONF = {anicolor}` in `/openpilot/eon-custom-themes/support_variables/.py` under the `AUTO_INSTALL_CONF` var to `color_`
- You can disable automatic installation by editing `/openpilot/eon-custom-themes/support/do_not_auto.txt ` by changing the 0 to a 1 
- This program has the ability to auto update themes so dont be alarmed if it changes
- Backups are stored in `/sdcard/theme-backups` and can also be easily restored by running `exec /data/openpilot/eon-custom-themes/restore_theme.py` and following the prompts.
- If you already used the EON-Custom-Themes program to install/restore a new custom theme of your choosing this intelligent program will not auto install this theme 
- The Installer and this project was designed so the main program and this minimal program would be able to work togeter in unision. No stones were left unturned in development....

### Support:
- For any support with this program please check the 'Minimal Self Installer Assistance' section in the main projects [README HERE!](https://github.com/Coltonton/eon-custom-themes/blob/master/README.md) Covering FAQs such as....
- - How do I restore a previous theme?
- - I have a custom theme installed but I want to switch over to get the ArnePilot theme with possible updates? 
- - This project is cool! are there other themes other then this ArnePilot One? (YES!)
- - Or anything else, check it out there is alot answered there! 
- - Feel free to check out the [main unoffical community discord server](http://discord.gg/4UKcsmGJDq), and find my own little chat #custom-themes for more support from other then just me! Or just to catch me easier!!


### UnInstalling EON-Custom-Themes:
Well... this is akward.... I'LL CHANGE!!!! Haha but seriously... Want to remove EON-Custom-Themes without a trace? It couldnt be more simple!!

0.  (Optional, to restore default boot logo & boot animation) run `exec /data/eon-custom-themes/restore_theme.py` and enter `r` to restore the Comma.ai factory boot logo and boot animation for your device. 
1. Run `exec /data/eon-custom-themes/support/cleanup_files.py` reading and following the prompts, this program will remove any files from EON-Custom-Themes not stored in the main project directory!
2. Run `cd /data && rm -rf eon-custom-themes` to finish un-installation there should now be no trace of EON-Custom-Themes (unless you skipped step 0)
3. Cry because you removed EON-Custom-Themes
4. If doing this because you are sending your device back to Comma/selling be sure to delete all versions of OpenPilot and install their main repo.
5. Don't forget to unpair your device in the Comma connect app ;)