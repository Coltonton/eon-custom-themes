Release 1.2

[![](https://i.imgur.com/w9jylkJ.png[/img])](#)
# EON-Custom-Themes
Upgrade your EON/Leon/Two's Looks!!! This is a pretty all inclusive guide to modify your device themingly. It's your own device! You own it, do with it as you please despite what someeee people may say, which is ironic dont you think?..... Lets Light It Up!!! (Contest)

This is a new project, find any errors? submit an issue, or make a pull request! This is not my project but our project!! * **Soviet national anthem plays** * You may also message me @Coltonton#2169 on discord (I'm in all the servers (Except the main comma because banned 😆 I'm proud!))

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

### Theme Utils Package
* [General Info](#)

### List Of Themes:
*  [Stock Themes:](#stock-themes)
*  [Contributed Themes:](#contributed-themes)
*  [How To Contribute Your Work!](#contribute-your-work)

### Minimal Self Installer Assistance (Included with OP Forks)
reserved

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
| Khonsu-LemmonCurd     | Yes           | Yes                | White           | OP Spinner                       | Colton             |
| ShaneSmiskol-Toyota   | Yes           | Yes                | White & Color   | OP Spinner                       | Colton             |
(Check out forks of this project for potentially more)

## Contribute Your Work!:

Please see the [DEVREADME](https://github.com/Coltonton/eon-custom-themes/blob/master/developer/DEVREADME.md)  in the developer folder of this repo to find out about contributing your designed theme! 


# Minimal Self Installer Assistance:

This program and project was designed with the intent to not just be a program users can run but also a program OpenPilot developers can include in their fork to theme their users EONs with their theme (Coming in Version 2). Please see the [DEVREADME](https://github.com/Coltonton/eon-custom-themes/blob/master/developer/DEVREADME.md) for more information if you are a developer wanting to include the auto installer as part of your fork! If you have stumbled across this as part of an OpenPilot fork, bellow is alot of helpful information! 


### Disable auto installer:
reserved


### WHY DID MY EONS THEME CHANGE NO ONE TOLD ME!!
reserved

### Features:

- Backups are stored in `/sdcard/theme-backups` and can also be easily restored by running `exec /data/'your_OP_directory_name'/eon-custom-themes/restore_theme.py` and following the prompts.
- If you already used the EON-Custom-Themes program to install/restore a new custom theme of your choosing this intelligent program will not auto install this theme 
- The Installer and this project was designed so the main program and this minimal program would be able to work togeter in unision. No stones were left unturned in development....

### Support:
- How do I restore a previous theme?
- - Restoring a previous theme can be done by running `exec ./restore_theme.py` in the eon-custom-themes directory. If you cloned the main project it should be in `/data` or it can be in `/data/'your_OP_directory_name'/` if your OpenPilot fork has the auto installer inbuilt. 
- This project is cool! are there other themes other then the one that was included? YES! [See here](#stock-themes)
- How does all this sorcery work? How do I design my own theme to use? And possibly publish??
- - All good questions! The code is all open source so please take a look! There is also lotsss of information available on how the program works, and even how to design your own in the [DEVREADME](https://github.com/Coltonton/eon-custom-themes/blob/master/developer/DEVREADME.md)
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
