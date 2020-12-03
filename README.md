# DEAR ALL! The time has come, that I have been waiting for! Comma released their QT UI. at this time any information related to spinner/UI is outdated unless your OP version is .7.x and lower! Untill i start wrok again please do not install spinner assets! I will be keeping it live for legacy users for now untill I work on the new files and info!! You CAN still choose a boot Logo and Boot Animation!!!!!


Release 1.1

[![](https://i.imgur.com/w9jylkJ.png[/img])](#)
# EON-Custom-Themes
Upgrade your EON/Leon/Two's Looks!!! This is a pretty all inclusive guide to modify your device themingly. It's your own device! You own it, do with it as you please despite what someeee people may say, which is ironic dont you think?..... Lets Light It Up!!! (Contest)

This is a new project, find any errors? submit an issue, or make a pull request! This is not my project but our project!! * **Soviet national anthem plays** * You may also message me @C-ton#2169 on discord (I'm in all the servers)

Feel free to check out the [main unoffical community discord server](https://discord.gg/2rxE2r3ywe), and find my own little chat #custom-themes for more support from other then just me!

Table of Contents
=======================
* [What is this?](#what-is-this)

### Using This Project
* [How To Use](#how-to-use)
* [Navigating The Installer](#navigating-the-installer)
* [What Are The Availble Assets?](#what-are-the-availble-assets)
* [Restoring From Backup](#restoring-theme-assets-from-backup)
* [Restoring The Comma.ai Stock Theme (if backup lost)](#restoring-the-comma-stock-theme-if-backup-lost)

### List Of Themes:
*  [Stock Themes:](#stock-themes)
*  [Contributed Themes:](#contributed-themes)
*  [How To Contribute Your Work!](#contribute-your-work)

### Minimal Self Installer Assistance (Included with OP Forks)
* [Main Info](#Minimal-Self-Installer-Assistance)
* [Disable auto installer](#Disable-auto-installer)
* [WHY DID MY EONS THEME CHANGE NO ONE TOLD ME](#WHY-DID-MY-EONS-THEME-CHANGE-NO-ONE-TOLD-ME)
* [Features](#Features)
* [Support](#Support)

### Un-Installing EON-Custom-Themes
* [Main Info](#UnInstalling-EON-Custom-Themes)

[![](https://i.imgur.com/TSJz3iI.png)](#)
[![](https://i.imgur.com/qgRTseD.png)](#)

# Todo
- Make some more themes!
- All new auto installer!!!
- Have you heard the word???



# What is this?

Thanks for asking young one! This is a project dedicated to de-comma-ing your EON! Wether you dont like Comma.ai the company or want to personalize your EON, I gotchu fam!

This is a community project so here you can find new boot logos, boot animations, OpenPilot loading animations, and even more for your device! Created/designed by myself with help from Shane Smiskol. With themes designed and made by myself and other community members. 

Also included in this repository is all the info you need to start hacking and making your own extra custom themes! See the [DEVREADME](https://github.com/Coltonton/eon-custom-themes/blob/master/developer/DEVREADME.md) in this repo in the developer folder. 

Did you make your own and want to share it with the world? Wonderful! Check out that [DEVREADME](https://github.com/Coltonton/eon-custom-themes/blob/master/developer/DEVREADME.md) to learn how to contribute and submit!

Also feel free to check out the [main unoffical community discord server](http://discord.gg/4UKcsmGJDq), and find my own little chat #custom-themes for more support from other then just me! Or just to catch me easier!!

# How To Use:
Thanks to many hours of coding, thinking, and courtious help of @ShaneSmiskol this project couldn't be easier to install and run! If you have installed a custom fork of OpenPilot, can answer simple questions, or can just follow this simple guide you will be up and running with a new look in no time! 

**BEFORE YOU START**
- This program will automagicly backup the existing theme before copying the new; and saves them to the backups folder in this project. If replacing the Comma stock theme, just know I do provide the "stock" files as part of this project created and copyrighted by Comma.ai. Maybe I'll get sued because then I can then I'll be able to make a crappy rap and call it "The Light It Up Contest" cuz I'll be salty 
- - See [Restoring Backup](#restoring-theme-assets-from-backup) and [Restoring The Comma.ai Stock Theme If Backup Lost):](#restoring-the-comma-stock-theme-if-backup-lost)
- As per the [licence](https://github.com/Coltonton/eon-custom-themes/Licence), this software is provided "as is", without warranty of any kind and in no event shall I or any other authors be liable for any claim, damages, or other liability. Use this project at your own risk!

**Let's Begin:**

1. [SSH into your EON. (Workbench is the easist way)](https://medium.com/@jfrux/comma-eon-getting-connected-with-ssh-3ed6136e4a75)
2. In the terminal enter `cd /data`
3. `git clone https://github.com/Coltonton/eon-custom-themes.git`

4. `cd ./eon-custom-themes` after cloning has finished
5. `exec ./install_theme.py`
6. The installer will now run.

### Navigating The Installer:
1. The installer will firstly prompt you for what theme you would like to choose. Enter the name, or index number and press enter. If you misspelled the theme name from the shown theme name; the program will attempt to figure out what you ment and ask you to confirm. You will need to enter "y" or "1" on these prompts to confirm.
2. Now the installer will promt you with the available assets for that theme. You can choose (if availble) the **Boot Logo**, **Boot Animation**, **OpenPilot Spinner**, and **Additional Resources**. ([What do these mean?](#what-are-the-availble-assets))
3. One by one choose your desired theme assets and they will automagically install! Want to install diffrent assets from diffrent themes? YOU CAN! Sipmply select **-Main Menu-** from the options to be taken back to the theme picker!
- - Certian themes have a color and white boot animation, the "colored" ones are a matching color. ex. Toyota is red, and hyundai is blue!
4. Once done select **-Reboot-** to reboot your EON and see your new themes!!!! Please note there is an active unknown bug where the OpenPilot spinner does not take randomly. Just rerun the program and try again. [See The Issue In Github](https://github.com/Coltonton/eon-custom-themes/issues/11)
5. Having issues? Message me on discord @C-ton#2169

### What Are The Availble Assets?

- The **Boot Logo** is the first thing to show when you turn on your EON, it is a static image. It is also the images for when your EON is dead, or dead but charging!
- The **Boot Animation** plays right after the Boot Logo and is the animated animation for your device while Android loads!
- The **OpenPilot Spinner** is the second animation that shows while your EON boots, this is the loading animation for OpenPilot itself!
- **Additional Resources** (not an active feature) can be a variaty of things consult the contrib.txt file in the desired themes folder in `contributed-themes`. Possible additional resources are OpenPilot sounds, OpenPilot assets (like the home button icon and other things like the battery icon & cell strength), and even code patches!!

### Restoring Theme Assets From Backup:
- Simply SSH into your EON and run `exec /data/eon-custom-themes/restore_theme.py` and it works just like the main program but serches for all the backups that were made in `/sdcard` insted. The backup folders are created and named with the date/time the backup occured

### Restoring The Comma Stock Theme If Backup Lost:
- SSH into your eon and run `exec /data/eon-custom-themes/restore_theme.py` and use oprtion "r" to restore the Comma-Default theme. This will only restore the Boot-Logo and Boot-Animation. If you need to send your device back to Comma for any reason or selling, it's best to load the main Comma.ai OpenPilot branch, which will restore spinner and anything else.
- If you have the auto installer installed as part of your current OpenPilot fork and `Enter 'r' to restore the Comma-Default theme` is not an option please clone the [main repo from here](https://github.com/Coltonton/eon-custom-themes).



----
# List Of Themes:
You can see screenshots of what the theme looks like in the desired theme folders screenshots folder. All theme folders are located in the `contributed-themes` directory of this repo

## Stock Themes:
| Theme Name            |Boot Logo? (3T)| Boot Logo? (LeEco) | Boot Animation? | Custom OP Files?                 |
| ----------------------| --------------| ------------------ | ----------------| ---------------------------------|
| Acura                 | Yes           | Yes                | White           | OP Spinner                           |
| Android               | Yes           | Yes                | White & Color   | OP Spinner                           |
| ArnePilot             | Yes           | Yes                | White & Color   | OP Spinner                           |
| Chevy                 | Yes           | Yes                | White & Color   | OP Spinner                           |
| DragonPilot           | Yes           | Yes                | White           | OP Spinner                           |
| A General Theme       | Yes           | Yes                | White           | OP Spinner                           | 
| Genesis               | Yes           | Yes                | White           | OP Spinner                           |
| Honda                 | Yes           | Yes                | White & Color   | OP Spinner                           |
| Hyundai               | Yes           | Yes                | White & Color   | OP Spinner                           |
| Kia                   | Yes           | Yes                | White & Color   | OP Spinner                           |
| OnePlus               | Yes           | No                 | N/a             | N/a                                  |
| Subaru                | Yes           | Yes                | White & Color   | OP Spinner                           |
| Toyota                | Yes           | Yes                | White & Color   | OP Spinner                           |

This is the default linup, I will be creating coupple others. Happy to hear suggestions for others!!! 

## Contributed Themes
| Theme Name            |Boot Logo? (3T)| Boot Logo? (LeEco) | Boot Animation? | Custom OP Files?                 | Contributor/ Author|
| ----------------------| --------------| ------------------ | ----------------| ---------------------------------| -------------------|
| Comma-Stock           | Yes           | Yes                | Yes             | OP Spinner                       | Comma.ai           |
| cgw1968-Bat           | No            | Yes                | Color           | OP Spinner                       | Colton             |
| Khonsu-LemmonCurd     | Yes           | No                 | White           | OP Spinner                       | Colton             |
| ShaneSmiskol-Toyota   | Yes           | Yes                | White & Color   | OP Spinner                       | Colton             |
(Check out forks of this project for potentially more)

## Contribute Your Work!:

Please see the [DEVREADME](https://github.com/Coltonton/eon-custom-themes/blob/master/developer/DEVREADME.md)  in the developer folder of this repo to find out about contributing your designed theme! 


# Minimal Self Installer Assistance:

This program and project was designed with the intent to not just be a program users can run but also a program OpenPilot developers can include in their fork to theme their users EONs with their theme. Please see the [DEVREADME](https://github.com/Coltonton/eon-custom-themes/blob/master/developer/DEVREADME.md) for more information if you are a developer wanting to include the auto installer as part of your fork! If you have stumbled across this as part of an OpenPilot fork, bellow is alot of helpful information! 


### Disable auto installer:

- If you do not wish to have the selected auto boot logo and boot animation installed as part of your EON (change will stick despite what OpenPilot fork you run) follow the instructions to come, but please read everythting here!

- If you installed a different theme before hand from the main EON-Custom-Theme project you need not worry about this step. The program is intellegent enough to know if another theme was already installed and it's assumed you probably want that one.

- *psst* hey you, yeah you... dont want included chosen theme? Well.... how about one to go with your Honda/Toyota/Subaru/Hyundai etc? there are plenty to choose from  [over here](https://github.com/Coltonton/eon-custom-themes)!!!

- To disable the auto installation process simply [SSH into your EON](https://medium.com/@jfrux/comma-eon-getting-connected-with-ssh-3ed6136e4a75) and `nano /data/arnepilot/eon-custom-themes/support/do_not_auto.txt` by changing the 0 to a 1. This will prevent any auto install attempts, this MUST BE done before the next reboot after you clone or pull this version to prevent the auto installer from running next reboot!!

### WHY DID MY EONS THEME CHANGE NO ONE TOLD ME!!
- Didn't know that the auto installer was included   and dont like it or Simply want to go back to the Comma stock EON theme? Firstly may I recomend the main [EON Custom Themes](https://github.com/Coltonton/eon-custom-themes) project that the minimal version is a subsidiary of? If you dont know it is a community project created by @Coltonton for the community and allows you to chage your EONs boot logo and boot animation, and OP spinenr (as you saw if you're reading this...) With many themes available for all the major supported cars! ex. Honda, Hyundai, Toyota, Subaru, and much more, including others! [Check it out!!](https://github.com/Coltonton/eon-custom-themes) N...No? Oh...Okay you want the Comma stock one back eh? You Sure? Colton put many weeks of work into creating that project and making it easy and intuitive for you to get a custom look!! O..oh... okay... still not interested.... that's fine! This wonderfully overengineered and overthought program made a backup when it installed this theme automagicly! To restore the comma stock theme [SSH into your EON](https://medium.com/@jfrux/comma-eon-getting-connected-with-ssh-3ed6136e4a75) and:
- - `exec /data/'your_OP_directory_name'/eon-custom-themes/restore_theme.py` and follow the prompts of the easy to use program! You will not need to follow the steps above and set the `do_not_auto.txt` file to 1 (unless you want to) since you used the program to install a chosen theme (or restore in this case) it will remember that! Even if its a restoring a backup! 
- - If you lost the backup somehow please clone the [main project here](https://github.com/Coltonton/eon-custom-themes) to /data  using `git clone https://github.com/Coltonton/eon-custom-themes.git` and then `exec /data/eon-custom-themes/install_theme.py`, and use the simple program to install the 'comma-default' theme. 

### Features:

- Don't like the provided boot animation color? Many of the themes have a all-white and matching-color boot animation!! Just edit `AUTO_INSTALL_CONF = {anicolor}` in `/data/'your_OP_directory_name'/eon-custom-themes/support_variables/.py` under the `AUTO_INSTALL_CONF` var to `color_` or `white_`. Be sure to check [here](#stock-themes) for what options are available!
- You can disable automatic installation by editing `./eon-custom-themes/support/do_not_auto.txt ` by changing the 0 to a 1 
- This program has the ability to auto update themes so dont be alarmed if it changes
- Backups are stored in `/sdcard/theme-backups` and can also be easily restored by running `exec /data/'your_OP_directory_name'/eon-custom-themes/restore_theme.py` and following the prompts.
- If you already used the EON-Custom-Themes program to install/restore a new custom theme of your choosing this intelligent program will not auto install this theme 
- The Installer and this project was designed so the main program and this minimal program would be able to work togeter in unision. No stones were left unturned in development....

### Support:
- How do I restore a previous theme?
- - Restoring a previous theme can be done by running `exec ./restore_theme.py` in the eon-custom-themes directory. If you cloned the main project it should be in `/data` or it can be in `/data/'your_OP_directory_name'/` if your OpenPilot fork has the auto installer inbuilt. 
-  I installed a custom theme but I want to switch over to get the provided theme with possible updates? 
- - Easy! All you should need to do is delete the file `/sdcard/is_self_istaleld.txt` and next reboot the auto installer will run and install the provided theme. This will also unlock the potential for future updates.
- - The "self install themes" like arnepilot and dragonpilot are also usually available as part of the main project, so you can also manually install it yourself, but you will not recive auto updates (if applicable)
- This project is cool! are there other themes other then the one that was included? YES! [See here](#stock-themes)
- How does all this sorcery work? How do I include the self installer in my fork? How do I design my own theme to use? And possibly publish??
- - All good questions! The code is all open source so please take a look! There is also lotsss of information available on how the program works, how to include it in your fork, and even how to design your own in the [DEVREADME](https://github.com/Coltonton/eon-custom-themes/blob/master/developer/DEVREADME.md)
- Message me on discord @C-ton#2169 if you need any additional help :)
-  Feel free to check out the [main unoffical community discord server](http://discord.gg/4UKcsmGJDq), and find my own little chat #custom-themes for more support from other then just me! Or just to catch me easier!!

# UnInstalling EON-Custom-Themes:
Well... this is akward.... I'LL CHANGE!!!! Haha but seriously... Want to remove EON-Custom-Themes without a trace? It couldnt be more simple!!

0.  (Optional, to restore default boot logo & boot animation) run `exec /data/eon-custom-themes/restore_theme.py` and enter `r` to restore the Comma.ai factory boot logo and boot animation for your device. 
1. Run `exec /data/eon-custom-themes/support/cleanup_files.py` reading and following the prompts, this program will remove any files from EON-Custom-Themes not stored in the main project directory!
2. Run `cd /data && rm -rf eon-custom-themes` to finish un-installation there should now be no trace of EON-Custom-Themes (unless you skipped step 0)
3. Cry because you removed EON-Custom-Themes
4. If doing this because you are sending your device back to Comma/selling be sure to delete all versions of OpenPilot and install their main repo.
5. Don't forget to unpair your device in the Comma connect app ;)

# Shameless Plug For A Bee....Cup Of Coffee:
I also hate to ask but I've put quite an ammount of time in to this project. If you like what I've done and do want to help you can buy me a bee....coffee! By donating on [PayPal](paypal.me/BrandonSheaffer). Just a coupple dollary doo's will mean alot, plese dont feel overly generous I did this for my fun and the community!! 
        
        
        
                                  
