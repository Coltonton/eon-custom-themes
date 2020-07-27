[![](https://i.imgur.com/IcCeUD7.png)](#)
# EON-Custom-Bootscreens
Upgrade your EON/Leon/Two's Looks!!!

Table of Contents
=======================
* [What is this?](#what-is-this)
* [Prerequisites:](#Prerequisites:)
* [Setting Up FileZilla](#Setting-Up-FileZilla:)


## [3T-EON Boot Logo Instructions](#3T-EON-Instructions:)
* [Retrive Boot Logo](#Retrive-Boot-Logo)
* [Modifying Files](#Modifying-Files:)
* [Uploading Modified Logo/Custom Logo:](#Uploading-Modified-Logo/Custom-Logo:)


## [LEON/TWO Boot Logo Instructions HALP ME!!!](#LEON/TWO_Instructions)
* [HELP WANTED!!!!](#Help-Wanted!!)
* [Install ADB:](#Installing-ADB-(Windows):)
* [Find The LEON/TWO logo.bin:](#Find-The-LEON/TWO-logo.bin:)


## [Boot Animation & OP Loading Screen](#Boot-Animation-&-OP-Loading-Screen)
*  [Boot Animation:](#Boot-Animation:)
*  [OpenPilot Loading Animation:](#OpenPilot-Loading-Screen:)

## [Community Files](#LEON/TWO_Instructions)
*  [How To Use:](#How-To-Use: )
*  [List of themes: ](#List-Of-Themes:)
*  [Contribute Your Work!](#Contribute-Your-Work!)

---

What is this?
------
Thanks for asking young one! This is a project dedicated to de-comma-ing your EON! Wether you dont like Comma.ai the company or want to personalize your EON, I gotchu fam!

Included in this repository is all the info you need to start hacking around! This is also a community project so here you can find Boot Logos, Boot Animations, and OpenPilot loading annimations for your device! Created by myself and other community members, free to use!!! Made your own and want to share it with the world? Wonderful! check [Contribute Your Work!](#Contribute-Your-Work!)

Prerequisites:
------
* Windows(Only needed if you plan on making your own Logo files)
* FileZilla
* An EON (Any will do! FreeT-ON, Free-LeON, 3T-ON, Gold/LEON, TWO)


Setting Up FileZilla:
------
0. [Download Filezilla](https://filezilla-project.org/download.php?type=client)
1. Install FileZilla
2. Open Site Manager (Top leftmost icon - looks like 3 server racks)
3. Create a new site and call it EON
4. For Protocol select SFTP
5. Enter the IP adress of your eon in Host
6. Port: 8022
7. Login Type: Key File
8. User: root
9. Key File: choose eonkey.pem from root in this repo

3T-EON Instructions:
=======================

## Boot Logo:
### Retrive Boot Logo

1. Connect with FileZilla
2. and go to `/dev/block`
3. In the left handed pannel choose where you want to save.
4. Doubble click the file sde17 to transfer and backup

### Modifying Files:
* Not Available yet sorry :(

### Uploading Modified Logo/Custom Logo:
1. Find the boot logo in this repo you want, and rename it sde17 keeping it with no extention
2. Connect with FileZilla
3. Go to `/dev/block`
4. In the left pane area in FileZilla, navigate to the boot logo you just renamed and want to use
5. right click and choose upload, then noverwrite

Reboot and enjoy! If EON shows a Linux penguin you done screwed sumthin' up! (Or somebody else did) Try again!


LEON/TWO_Instructions
=======================

## HELP WANTED!!

I do not have a LEON and I need your help! 
If you want to send in a LEON/Two logo.bin it would be much appriciated! 
Email it to Cole@endoflinetech.com and I will get a working! It would be appricieated if you would help verify my work is working



## Installing ADB (Windows):
1. [Download ADB](https://dl.google.com/android/repository/platform-tools-latest-windows.zip)
2. Extract zip to c:\ADB

## Find The LEON/TWO logo.bin:

0. [Install ADB](#Installing-ADB-(Windows):)
1. SSH Into Eon
2. Run `am start -a android.settings.SETTINGS`
3. Find Developer Options and verify/enable *ADB over Network*
4. Open windows command prompt and navigate to cd /ADB/platform-tools 
5. `adb connect YOUR_EON_IP:5555`
6. `adb shell`
7. `su`
8. `cd /dev/block/bootdevice/byname`
9. `ls -all`
10. You will need to look through the list and detrimine where LOGO is; on the 3T-ON
    it is /dev/block/sde17
11. Save to sdard memory making sure if=/location_of_LOGO ex: `dd if=/dev/block/sde17 of=/sdcard/logo.img`
12. Exit from shell (ctl+D) `adb pull /sdcard/logo.bin C:\ADB` (Or wherever you like)
13. Email to to Cole@endoflinetech.com including name/github/other info to be credited! 


Boot Animation & OP Loading Screen
=======================
## Boot Animation:
* Not Available yet sorry :(

## OpenPilot Loading Screen:
* Not Available yet sorry :(

Community Files
=======================

## How To Use:

Looking to theme your EON? This is the place see [List Of Themes](#List-of-themes:) bellow to see user contributed themes. 

## List-Of-Themes: 
| Theme             | What EONs? (3T/LEO)  | Boot Logo? | Boot Animation?     | Custom OP UI?                     | Contributor     |
| ------------------| ---------------------| -----------| --------------------| ----------------------------------| ----------------|
| Colton HooeyPilot | 3T                   | Yes        | No                  | Yes, Loading, Elements, & Sounds  | Colton          |


i'll be adding and making more in the coming days :)

## Contribute Your Work!:

### How To Contribute:
Just Fork this repo, and clone it, add in youre theme following the example theme, looking at others, and the 
Looking to theme your EON? This is the place see [Directory Structure](#Directory-Structure:) You can add whatever you like! Made a custom boot logo? boot Animation? Wonderful!!! Did you edit UI.c? spinner.c? Spinner assets? OP assets? or make your own APK? You can also share your work!! share, you can do that too!!! Just leave instructions in your folder letting them know what to do!

Ready to submit? Create a pull request, I will reveiw and merge in!

### Directory Structure:

How to format your theme folder, only use what you need

    .
    └──Theme Name                 # Name Of your Theme
        |──APK                    #Your OP APK
        ├──assets                 #OP/selfdrive/assets folder
        |──other Files            #Edited UI.C or spinenr.c?
        |──bootanimation.zip      # Android Boot Animation
        |──Contrib.txt            # Add your info here
        |──LEOLogo(no extention)  # LEON/GOLD/TWO Boot Logo
        └──3TLogo(no extention)   # 3T-EON Boot Logo
        
        
        
                                  