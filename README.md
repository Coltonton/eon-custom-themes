[![](https://i.imgur.com/IcCeUD7.png)](#)
# EON-Custom-Themes
Upgrade your EON/Leon/Two's Looks!!! This is a pretty all inclusive guide to modify your device themingly, if you are wanting a simpler to the point guide [you can find that here!](https://github.com/Coltonton/EON-Custom-Themes/blob/master/GetANewTheme.md) It's your own device! You own it, do with it as you please despite what someeee people may say, which is ironic ain't it?.....

This is a new project, find any errors? submit an issue, or make a pull request! This is not my project but our project!! * **Soviet national anthem plays** *

Table of Contents
=======================
* [What is this?](#what-is-this)
* [Setting Up FileZilla](#Setting-Up-FileZilla)

### 3T-EON Boot Logo Instructions
* [Retrive 3T Boot Logo](#Retrive-3T-Boot-Logo)
* [Modifying 3T Files](#Modifying-3T-Files)
* [Uploading Modified 3T Logo/Custom Logo:](#Uploading-Modified-3T-Logo/Custom-Logo)


### LEON/TWO Boot Logo Instructions HALP ME!!!
* [HELP WANTED!!!!](#Help-Wanted)
* [Find The LEON/TWO logo.bin:](#Find-The-LEON/TWO-logo.bin)


### Boot Animation & OP Loading Screen
*  [Boot Animation:](#Boot-Animation)
*  [OpenPilot Loading Screen:](#OpenPilot-Loading-Screen)

### Themes

*  [How To Use:](#How-To-Use)
*  [List of themes:](#List-Of-Themes)
*  [Contribute Your Work!](#Contribute-Your-Work)

---
---
---

## What is this?

Thanks for asking young one! This is a project dedicated to de-comma-ing your EON! Wether you dont like Comma.ai the company or want to personalize your EON, I gotchu fam!

Included in this repository is all the info you need to start hacking around! This is also a community project so here you can find boot logos, boot animations, and OpenPilot loading annimations for your device! Created by myself and other community members, free to use!!! Made your own and want to share it with the world? Wonderful! check [Contribute Your Work!](#Contribute-Your-Work!)


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

3T-EON Instructions:
=======================

## 3T Boot Logo:
### Retrive 3T Boot Logo

1. Connect with FileZilla
2. and go to `/dev/block`
3. In the left handed pannel choose where you want to save.
4. Doubble click the file sde17 to transfer and backup

### Modifying 3T Files:
(Windows Required)

#### Extracting 3T Boot Images:
If you want to create your own boot logo(s) you can use the provided files in OnePlus3T assets folder, and can skip this section, use this section only if you wish to modify an existing bootlogo set.

1. Download this repo.
2. If you wish to modify a 3T boot logo, take it and replplace the sde17.bin file in `Boot Logo Tools\OnePlus3TInjector` with it, being sure to add the .bin extention 
4. Doubble click `Extractor.cmd`
5. All the files will extract and replace into the `Boot Logo Tools\OnePlus3TInjector` folder.

#### Editing 3T Boot Images
This is not a Photoshop or Gimp tutorial. 
Although there are a few files that get extracted you only need to worry about 3 of them (edit the others as you like, I have already made new horizontal themes, that you are free to use use).

* FHD_Charger... is the low battery screen shown while it is pluged in.
* FHD_lowpower... is the low battery screen shown while not pluged in.
* FHD_oppo... is the main boot logo.
0. Download this repo if you haven't.
1. GENTLEMEN! START... YOUR.... ENG..oh...favorite image editors...
2. Remember were dealing with a phone. So you can set your canvas to 1920w x 1080h  but you will need to rotate the image +90 degrees once done editing.
3. Do not go extravagant with the boot logo there is not alot of program memory for anything crazy.
4. Once you have made your logo(s), again remember to rotate it +90 degrees and export as a png file using the EXACT name as the file you want to change, and replace it in the `Boot Logo Tools\OnePlus3TInjector` directory that you are changing.
#### Reinjecting 3T Boot Images

0. Download this repo if you haven't.
1. Doubble click `Injector.cmd`
3. This will create a file called modified.logo.bin, rename it to sde17 (with no file extention)
4. FIN! You can now [Upload your modified 3T logo](#Uploading-modified/custom-3T-Logo:)

### Uploading modified/custom 3T Logo:
0. Make sure you are NOT about to follow these steps to install on a LeEco Based EON (LEON,GOLD,TWO) THIS IS ONLY FOR OP3T EON's, YOUR DEVICE WILL BE HARD BRICKED! DEAD! CAPUT! JEFFREY EPSTEIN'ED!!!!!
1. Connect with FileZilla.
2. Go to `/dev/block`
3. In the left pane area in FileZilla, navigate to the boot logo you want to use.
4. Right click and choose upload, then overwrite.

Reboot and enjoy! If EON shows a Linux penguin you done screwed sumthin' up! (Or somebody else did) Try again!


LEON/TWO_Instructions
=======================

## DO NOT DON NOT!!!!! TRY TO PUT A OP3T BOOT LOGO ON YOUR LEECO EON

## HELP WANTED!!

I do not have a LEON and I need your help! 
If you want to send in a LEON/Two logo.bin it would be much appriciated! 
Email it to Cole@endoflinetech.com and I will get a working! It would be appricieated if you would help verify my work is working
I'm also C-ton#2169 on discord if you want help / want to chat!



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



Community-Files:
=======================

## How To Use:

Looking to theme your EON? This is the place see [List Of Themes](#List-of-themes:) to see contributed themes! Just Clone/download this repo, and follow the guide relevant to you from the below list  

* [3T Boot Logo Upload Instructions](#Uploading-Modified-3T-Logo/Custom-Logo:)
* [LEON Boot Logo Upload Instructions](#null:) 
* [EON Boot Animation Instructions](#Boot-Animation:)
* Or the info/instructions provided by the author for other custom files.

## List Of Themes: 
| Theme Name            |Boot Logo?(3T)| Boot Logo? (LEO/Gold/Two) | Boot Animation? | Custom OP Files?                 | Contributor/ Author|
| ----------------------| -------------| ------------------------- | ----------------| ---------------------------------| -------------------|
| Acura                 | Yes          | No                        | No              | No                               | Colton             |
| Android               | Yes          | No                        | Yes             | No                               | Colton             |
| Apple                 | Yes          | No                        | No              | No                               | Colton             |
| Arne-Pilot            | Yes          | No                        | Yes             | No                               | Colton             |
| Chevy                 | Yes          | No                        | No              | No                               | Colton             |
| Colton-HooeyPilot     | Yes          | No                        | No              | Elements, & Sounds               | Colton             |
| Comma-Stock           | Yes          | No                        | Yes             | No                               | Comma.ai           |
| CommunityPilot        | Yes          | No                        | No              | No                               | Colton             |
| DragonPilot           | Yes          | No                        | Yes             | No                               | Colton             |
| A General Theme       | Yes          | No                        | Yes             | No                               | Colton             |
| Honda                 | Yes          | No                        | Yes             | No                               | Colton             |
| Hyundai               | Yes          | No                        | No              | No                               | Colton             |
| Kia                   | Yes          | No                        | No              | No                               | Colton             |
| Lexus                 | Yes          | No                        | No              | No                               | Colton             |
| OnePlus               | Yes          | No                        | No              | No                               | Colton             |
| Subaru                | Yes          | No                        | Yes             | No                               | Colton             |
| Toyota                | Yes          | No                        | Yes             | No                               | Colton             |

This is the default linup, I will be finishing up whats here, with maybe a coupple others. Happy to hear suggestions for others!!! 
I still need your help, to make LEON boot logos. Want to help? See [HELP WANTED!!!!](#Help-Wanted)

## Donations accepted and very much not required!:
I also hate to ask but I've put quite an ammount of time in to this project. If you like what I've done and do want to help you can buy me a bee....coffee! by donating on [PayPal](https://paypal.me/dattech?locale.x=en_US). Just a coupple dollary doo's will mean alot, plese dont feel overly generous I did this for my fun and the community!!

## Contribute Your Work!:

### How To Contribute:
Just Fork this repo, and clone it, add in youre theme following the example theme, looking at others, and the 
Looking to theme your EON? This is the place see [Directory Structure](#Directory-Structure:) You can add whatever you like! Made a custom boot logo? boot Animation? Wonderful!!! Did you edit UI.c? spinner.c? Spinner assets? OP assets? or make your own APK? You can also share your work!! share, you can do that too!!! Just leave instructions in your folder letting them know what to do!

Requirements To Contribute:
* Logo/animation/etc must be in the correct orientation.
* You must follow the directory structure/ how files & folders should be names.
* Inside `Other Files` is free rein.
* No Pornographic/Obscene/GreyLine content will we accepted - Keep it clean.
* No "off-color" or controversial content of any kind.
* You are willing to accept responsibility for your theme, I will not maintain your themes.
* You accept legal responsibility over anything in your theme folder, if I receive a copyright notice, I will take down your theme and forward the notice to you until you resolve the issue.
* Some form of contact is required either in `Contrib.txt`, or shared privately with me. 

Ready to submit? Create a pull request, I will reveiw and merge in!

### Directory Structure:

How to format your theme folder, only use what you need

    .
    └──Theme Name                 # Name Of your Theme
        |──APK                    #Your OP APK
        ├──Assets                 #OP/selfdrive/assets folder
        |──Other Files            #Edited UI.C or spinenr.c?
        |──Bootanimation.zip      # Android Boot Animation
        |──Contrib.txt            # Add your info here,
        |──Screenshots            # Place screenshots here so people can see what it looks like!!
        |──LEONLogo               # LEON/GOLD/TWO Boot Logo folder
        └──OP3TLogo               # 3T-EON Boot Logo folder - place the sde17 file in here
        
        
        
                                  