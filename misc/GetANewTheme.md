[![](https://i.imgur.com/IcCeUD7.png)](#)
# Get A New EON Theme!
Upgrade your EON/Leon/Two's Looks!!! Use this simplier guide with all the other technical/dev stuff removed! Made friendly for anyone to follow! Is it not? Sorry, please submit an issue on the [Github](https://github.com/Coltonton/EON-Custom-Themes/issues) page for this repo. 


It is broken up into 3 Main sections [Boot Logo](#Boot-Logo-Instructions:), [Boot Animation](#Boot-Animation-(EON-Universal):), and [OpenPilot Loading Screen](#OpenPilot-Boot-UI-(EON-Universal):)

The boot logo is the first thing to appear when you power EON on, it is just a static image, it also the screen you see when the battery needs charged, along with some other things

The boot animation is the animation that plays after the logo, as the phone is booting

THe OpenPilot Boot UI section is for the OpenPilot "spinner" loading page (the one with the progress bar)

This is a new project, find any errors? submit an issue, or make a pull request! This is not my project but our project!! * **Soviet national anthem plays** *

---

Table of Contents
=======================
## Boot Logo Instructions:
#### For 3T EONs:
* [Backup 3T Boot Logo](#Backup-3T-Boot-Logo:)
* [Uploading Modified 3T Logo/Custom Logo:](#Uploading-custom-3T-Logo:)

#### For LeEco EONS (Gold/Two)
* [HELP WANTED!!!!](#Help-Wanted)
* [Find The LEON/TWO logo.bin:](#Find-The-LEON/TWO-logo.bin)

## Boot Animation (EON Universal):
*  [Still In the works...](#Boot-Animation-(Any-EON):null )

## OpenPilot Boot UI (EON Universal):
*  [Still In the works...](#OpenPilot-Loading-Screen-(Any-EON):null)

## MISC:
*  [Setting Up FileZilla](#etting-Up-FileZilla:)
*  [Installing ADB](#Installing-ADB-(Windows):)
*  [FAQ](#FAQ:)

---
---
---
---


Boot Logo Instructions:
=======================
## For 3T Eons
---
### Backup 3T Boot Logo:

1. Connect with FileZilla
2. Go to `/dev/block`
3. In the left handed pannel choose where you want to save.
4. Doubble click the file sde17 to transfer and backup

### Uploading Custom 3T Logo:
1. Connect with FileZilla.
2. Go to `/dev/block` on the right side (EON's files)
3. In the left pane area in FileZilla, navigate to the boot logo you want to use (sde17).
4. Right click and choose upload, then overwrite.

Reboot and enjoy! If EON shows a Linux penguin you done screwed sumthin' up! (Or somebody else did) Try again! If you are ussing one of the community themes, and 200% sure you did it right open a Github issue.



---
## For LEON/GOLD/TWO EON's
---
## HELP WANTED!!

I do not have a LEON and I need your help! 
If you want to send in a LEON/Two logo.bin it would be much appriciated! 
Email it to Cole@endoflinetech.com and I will get a working! It would be appricieated if you would help verify my work is working


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
12. Exit from shell (ctl+D) then `adb pull /sdcard/logo.bin C:\ADB` (Or wherever you like)
13. Email to to Cole@endoflinetech.com including name/github/other info to be credited! 

There are other ways to find and get it too, message me on Discord @ C-Ton#2169, or if discord is a butt, i'm in the main Comma chat, CommunityPilot, and RetroPilot Servers, just serch in the users for me there!

---
## Boot Animation (Any EON):
---
Information Not Available At This Time :(

---
## OpenPilot Loading Screen (Any EON):
---
Information Not Available At This Time :(


---
---
---

MISC:
=======================
## Setting Up FileZilla:
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

## Installing ADB (Windows):
1. [Download ADB](https://dl.google.com/android/repository/platform-tools-latest-windows.zip)
2. Extract zip to c:\ADB

## FAQ:

Nothing here yet :()