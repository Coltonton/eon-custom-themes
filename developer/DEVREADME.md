# EON-Custom-Themes-DEVREADME
Here contains a whole lot of information on the technical aspects of this project. How to make boot logos, boot animations, and edit OpenPilot visual files! Please take a look at the Table of Contents... THere is alotttt of information here!

This is a new project, find any errors? submit an issue, or make a pull request! This is not my project but our project!! * **Soviet national anthem plays** *

Table of Contents
=======================
* [What is this?](#what-is-this)


### Boot Logo Information:
* [General Information](#Boot-Logo-Information)
* [Making a Boot Logo](Making-a-Boot-Logo)
* * [For OnePlus 3T EONs](#Making-For-OnePlus-EONs)
* * [For LeEco EONs](#Making-For-LeEco-EONs)
* [Creating The Boot Logo Package](#Creating-The-Boot-Logo-Package)
* [How To Install The Boot Logo](#How-To-Install-The-Boot-Logo)
* * [The Easy Way](#The-Easy-Way)
* * [The Manual Way](#The-Manual-Way)

### Boot Animation Information:
* [General Information](#Boot-Animation-Information)
* [Making a Boot Animation](#Making-a-Boot-Animation)
* [Zipping The Animation](#Zipping-The-Animation)
* [How To Install The Boot Animation](#How-To-Install-The-Boot-Animation)
* * [The Easy Way](#The-Easy-Way-Boot-Animation)
* * [The Manual Way](#The-Manual-Way-Boot-Animation)

### OpenPilot Spinner Information:
* [General Information](#OpenPilot-Spinner-Information)
* [Changing the Spinner Logo](#Changing-the-Spinner-Logo)
* [Changing the Spinner Track](#Changing-the-Spinner-Track)
* [Getting loading text](#Getting-loading-text)
* [Installing Spinner Changes](#Installing-Spinner.c-Code-Changes)

### OpenPilot UI Information:
* [General Information](#Boot-Animation-Information)


### Auto Installer Information:

### How to Make Your Own Theme Folder:
* [General Information](#Boot-Animation-Information)



### Misc Info:
* [FileZilla Mini Guide](#FileZilla-Mini-Guide)
* [ADB Mini Guide]((#ADB-Mini-Guide))

## What is this?

Thanks for asking young one! This is a project dedicated to de-comma-ing your EON! Wether you dont like Comma.ai the company or want to personalize your EON, I gotchu fam!

Included in this repository is all the info you need to start hacking around! This is also a community project so here you can find boot logos, boot animations, and OpenPilot loading annimations for your device! Created by myself and other community members, free to use!!! Made your own and want to share it with the world? Wonderful! check [Contribute Your Work!](#Contribute-Your-Work!)



# Boot Logo Information
The boot logo is really a simple part of an android device; it lives as part of the bootloader. Saying that means I have to give a big WARNING! Make sure you use the proper command if manually replacing the boot logo!! The OnePlus EON and LeEco EON have different paths for the boot logo. Using the wrong command / replacing the wrong file may lead to a corrupted bootloader!!!! requiring you to reinstall the bootloader.... and an expensive potato. If the file is dammaged or wrong then you should be okay but you will see a linux penguin as the boot logo. 

But now back to your regualar sceduled information; you need not read this unless you want to "learn you sumthin" or currious; just skip to the sub-sections below!!!! Anyhow... since the bootloader is a very "simple" program; tasked with getting android up and running; that means its not that complex. Everything you see up to the android boot animation is from the bootloader, such as the boot logo, the screen that appears when your battery does not have enough juice and is charging and some other things. All it does is displays a 1080*1920 image it's that simple! These images are built into a "partition" file of sorts. In the case of the OnePlus 3T it is the `sde17` (Aka logo) partition file located in `/dev/block` and for the LeEco LePro it is `sde32` (Aka splash) in `/dev/block`. In the case of the LeEco due to some funny buisness you need to actually replace `/dev/block/bootdevice/by-name/splash` but its all the same, just symlinks anyway. See the sub-sections bellow for more information! Particularly [Making a Boot Logo](#Making-a-Boot-Logo).

## Making a Boot Logo

 Using your favorite image creation program ex. Photoshop/Gimp create a canvas 1920*1080 and create your design). Once finished you will need to rotate the asset positive 90 degrees  (so its vertical - we are dealing with a phone afterall) and export as a png and replace the desired asset in the applicable boot logo maker tool outlined bellow.

### Making For OnePlus EONs:
- Clone or download this project to your Windows PC (yes... it is unfortunatly required) then navigate to where you cloned/downloaded this and go to `./Boot-Logo-Tools/OnePlus3TBootLogoMaker/`
- Here lies all the files you need, all the PNG files in this directory are all the possible 'bootloader' displays!
- - `fhd_oppo_1080_1920_result.raw` Is the main boot logo.
- - `fhd_charger_1080_1920_result.raw` Is the screen that shows up when your EONs battery is dead but charging
- - `fhd_lowpower_1080_1920_result.raw` (never appears) is supposed to be the "EON is dead, please plug in" display
- - `fhd_fastboot_1080_1920_result.raw` (never appears) but is the fastboot splash screen
- - `fhd_battery_1080_1920_result.raw` Is a battery error message
- Edit these files in your prefered image creator/editor (gimp/photoshop/etc) to your hearts desire then export as a png and overwrite the desired asset. 
- I have made new horizontal assets for the EON to match its orientation. These are free for you to use :) All the assets that are in the folder need to stay there, if you want to remove one for whatever reason just make it a full black image.
- Proceed to [Create the boot logo package](#Creating-the-boot-logo-package)
- (If you want to extract the assets from a given 3T boot logo simply move it to `./developer/boot-logo-tools/OnePlus3TBootLogoMaker` deleting the file sde17.bin then renaming the desired 3T logo to sde17.bin. Now run `EXTRACT_LOGO` and well... the logo file will be extracted!!!)

### Making For LeEco EONs:
- Clone or download this project to your Windows PC (yes... it is unfortunatly required) then navigate to where you cloned/downloaded this and go to `./Boot-Logo-Tools/LeEcoBootLogoMaker/pics/`
- Here lies all the files you need, all the PNG files in this directory are all the possible 'bootloader' displays! These are more self explanatory as to what they do but the LeEco has a special trick up its sleeve. You will notice there are 3 files `logo1`, `logo2`, and `logo3` these all are the main boot logo! The device will display these three images alternately!
- Edit these files in your prefered image creator/editor (gimp/photoshop/etc) to your hearts desire then export as a png and overwrite the desired asset. 
- I have made new horizontal assets for the EON to match its orientation. These are free for you to use :) All the assets that are in the folder need to stay there, if you want to remove one for whatever reason just make it a full black image.
- Proceed to [Create the boot logo package](#Creating-the-boot-logo-package)

## Creating the Boot Logo Package:
- Once you have all the assets you desire edited how you want all you need to do is run the `CREATE_LOGO` batch script and the provided tools (not created by me) will package up the logo automagically! 
- - The OnePlus3T tool a new file will appear (or overwite) called `modified.logo.bin`, go ahead and rename this to LOGO removing the extention (ensure '[show file name extentions](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)' is turned on for your machine to do this).
- - The LeEco tool it will appear in `/output/splash.img`, go ahead and rename this to SPLASH removing the extention (ensure '[show file name extentions](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)' is turned on for your machine to do this).

## How To Install The Boot Logo:
### The Easy Way!
- The easiest most convienient way to get your boot logo on your device is by forking this project and creating your own theme folder in `eon-custom-themes/contributed-themes` follow the guide HERE for information on how to properly structure your theme folder so the program recognizes it. You do not need to modify any code, just create your folder as outlined, clone your fork to your device, and run. If you did everything right it will show up and work! The program scans `contributed-themes` and thats how it populates available themes!
- Going this route allows for easyier future changes, automagic backuping, and no fiddling with commands/android stuff/filezilla. but you have to be somewhat familiar with git. 
### The Manual Way:
- Okay... Okay... its not as bad as it seems to go this route. You need to use ADB or Filezilla (click for guide) to upload your LOGO or SPLASH to /sdcard then run the respective command from SSH below. SECOND WARNING!!! Be careful doing this next step, replaacing the wrong file or using the wrong script may lead to a curropted bootloader!!!! 

To Backup (Recomended but optional): 
- - For OnePlus3T EONs run `if=/dev/block/sde17 of=/sdcard/LOGO.backup`
- - For LeEco EONs run `if=/dev/block/bootdevice/by-name/splash of=/sdcard/SPLASH.backup`

To install:
- - For OnePlus3T EONs run `if=/sdcard/LOGO of=/dev/block/sde17`
- - For LeEco EONs run `if=sdcard/SPLASH of=/dev/block/bootdevice/by-name/splash`

If you see a linux penguin on next reboot something is wrong with your file. you uploaded

# Boot Animation Information
The Android boot animation is also a pretty "simple" and non complex as well. It is Androids loading screen to tell the user... well... it's loading... Basicly its an "un-zipped gif" by what I mean you provide all of the "frames" of the animation, then the device does the rest! The "frames" consist of 1920*1080 jpg files in sequental name order. (yes jpg, you will see refrence to using png but EON doesnt like png that much...) To Start the boot animation is a non-compression zip folder containing a desc.txt, then folders for each 'part' of the animation. Most common and what Comma and I use is the 3 part animation (part0, part1, part2)(Intro, Main Loop, Outro). part0 is the first part and is only played once this typically is used to transiston from the boot logo then fade in the main boot animation to make the boot visual process look cleaner. part1 is the main animation that will play on loop until Android fully boots then finishes its current animation. part2 plays once as well and is used as an out-transistion. There is so much you can do with the "code" of the boot animation, the desc.text. [Here is Androids offical documentation on this](https://android.googlesource.com/platform/frameworks/base/+/master/cmds/bootanimation/FORMAT.md). But simply put it is a simple text file that acts as the progam and all you need to know is a few things if you decide to edit this. and you do have to mind your whitespaces, and newlines! The final line should have a newline after it or it will not work properly. 

-(unzip a bootanimation.zip to see if you are more visual, how everything operates) The very first line is formated as `WIDTH HEIGHT FPS`, this is the resolution you want it to show and at what speed (FPS). For example the default for my themes is `1920 1080 30` showing the animation at EONs full resolution, and at 30 frames per second targeted.
 The following lines are used to program the actual animation, in the format `TYPE COUNT PAUSE PATH` 
 - **TYPE:** a single char indicating what type of animation segment this is:
- - `p` -- this part will play until interrupted by the end of the boot
- - `c` -- this part will play to completion, no matter what
- **COUNT:** how many times to play the animation, or 0 to loop forever until boot is complete
- **PAUSE:** number of FRAMES to delay after this part ends
- **PATH:** directory in which to find the frames for this part (e.g. part0)

My desc.txt looks like:

    1920 1080 30
    c 1 0 part0
    c 0 0 part1
    c 1 30 part2



## Making a Boot Animation:
Designing is simple as well as the boot logo, and again ai wont teach you to design! But arguably one of the most time consuming parts. Just fire up your favorite editor again that allows you to make frames. I personally prefer photoshop as I'm very familiar with it but understand its an expensive option for most. But they do have a 7 day free trial you can exploit! You can also use the free tool Gimp with [this helpful plugin](https://github.com/khalim19/gimp-plugin-export-layers.git), that allows you to easily export each of your layers as images. Just create a layer for each frame! Back to photoshop see ###this link### to download the photoshop templetes I created and use to create my designs! More instructions will be provided with that on how to use them. Or you can use any tool you like that allows you to export each frame as an image **in sequential order**. This is important! Upon exporting you will want each frame sequentialy exported ex 00001.jpg 00002.jpg 00003.jpg... etc. As Android needs some way to know what order to display the immages. 


## Zipping The Animation
Once designed, export in an order like the standard above, put each 'part' of the animation in its own folder (again the standard way is starting with part0). And placing those part folders in a folder called `bootanimation` with the appropriate desc.txt. Zip with WinRar/7Zip with **NO** compression/store. you can also use the following command as provided from the android developer docs:

    cd <path-to-pieces>
    zip -0qry -i \*.txt \*.jpg @ ../bootanimation.zip *.txt part*

I have found this can be quite a pain to deal with so what I opt to do is select the part folders and desc.txt and inject them into a existing bootanimation.zip overwriting the files.
[![](https://i.imgur.com/s7wEUYt.png)](#)

## How To Install the Boot Animation
### The Easy Way Boot Animation!
- The easiest most convienient way to get your boot animation on your device is by forking this project and creating your own theme folder in `eon-custom-themes/contributed-themes` follow the guide ###HERE### for information on how to properly structure your theme folder so the program recognizes it. You do not need to modify any code, just create your folder as outlined, clone your fork to your device, and run. If you did everything right it will show up and work! The program scans `contributed-themes` and thats how it populates available themes!
- Going this route allows for easyier future changes, automagic backuping, and no fiddling with commands/android stuff/filezilla. but you have to be somewhat familiar with git. 
### The Manual Way Boot Animation:
- This manual way is a bit easier to deal with then the manual boot logo but still requires some work. Firstly you need to SSH into your eon and run `mount -o remount,rw /system` before you begin. Then you will need to use ADB or Filezilla (click for guide) to upload your bootanimation.zip to /system/media

- - For ADB, copy your bootanimaion.zip to your ADB directory and run:

        adb push bootanimation.zip /system/media

- - For FileZilla after connecting to your EON, on the left side naviagte to where your bootanimation.zip is on your computer and on the right to /system/media. Double click your bootanimation.zip on the left side to upload, and confirm to overwrite

- After you successfully copy it over you will need to run `chmod 666 /system/media/bootanimation.zip` from a SSH terminal



# OpenPilot Spinner Information
Ah, finally some simpler information, the OpenPilot loading spinner. I'm not going to go into 100% depth about how the spinner program works but I'll be sure to point out the main things most people would want to change. The `spinenr.c` program is located in `openpilot/selfdrive/common/` (well in unbuilt code form). And is the program responsible for the OpenPilot spinner! Who could of guessed!! 
## Changing the Spinner Logo:
- **To change** the spinner logo that appears all you have to do is edit/replace `openpilot/selfdrive/assets/img_spinner_comma.png` in your editing program of choice. To edit its just easiest to [download from here](#https://github.com/commaai/openpilot/blob/master/selfdrive/assets/img_spinner_comma.png) unless of course you run an OpenPilot fork which just makes this all easier! You also must maintain the 848*848 resolution. Just remember you dont have the full square to work with when designing; there is the spinner track that spins around the logo! Fortunatly it also is the same resolution as the logo file and the spinner track is ~848 pixles in diamater
- **To Upload** the spinner logo, the easiest way of course is to maintain your own OpenPilot fork and just replace the files there. As with the boot logo and boot animation you can also run your own fork of this project and create your own theme folder ###folowing this guide### to set up your theme folder properly. And ofcourse ADB and FileZilla work to

## Changing the Spinner Track:
- **To change** the spinner logo that appears all you have to do is edit/replace `openpilot/selfdrive/assets/img_spinner_track.png` in your editing program of choice. To edit its just easiest to [download from here](#https://github.com/commaai/openpilot/blob/master/selfdrive/assets/img_spinner_track.png) unless of course you run an OpenPilot fork which just makes this all easier! You also must maintain the 848*848 resolution! You can do what your heart desires, just know the code rotates the image, so best to stick to circular designs for it. Don't want the spinner track? All you need to do is erase all the pixles leaving a fully transparent png file.
- **To Upload** the spinner track, the easiest way as mentoned is to maintain your own OpenPilot fork and just replace the files there. As with the boot logo and boot animation you can also run your own fork of this project and create your own theme folder ###folowing this guide### to set up your theme folder properly. And ofcourse ADB and FileZilla work to

## Changing the Spinner Code:
Ah finally something interisting! Fortunatly for this you need not worry about an OpenPilot fork, EON-Custom-Theme fork, or trying to upload files to your EON, this all can be done from SSH/Workbench! (Well, you still can and if you are going the fork route you might as well continue down that path as you're already doing it) I have also actually documented the program (unlike comma has) giving even more information then what is shared here!
### Changing the progress bar:
- Changing The Progress Bar Color:
- - We need to edit spinner.c as located in `openpilot/selfdrive/common/` if editing on device over SSH run `nano /data/openpilot/selfdrive/common/spinner.c` then find line 162, and this is what you need to edit. 

        nvgRGB(245, 245, 245), nvgRGB(105, 105, 105));

    These are the RGB values for the loading bar the first is the "completed" portion of the bar, while the second is the "uncompleted" section. 
- Changing the Progress Bar Size:
- - This is accomplished in lines 144 - 147 in spinner.c. All the values are pretty self explanatory the only note I want to make is for `progress_x` for those of you who are not familiar with ui coding `fb_w/2-progress_width/2` translates to (framebuffer_width(or screen width) ÷ 2) - (the_width_of_the_progress_bar ÷ 2). This is to mathematically get the top left X point of the progress bar rectangle so that its centered on the display. When placing objects for most UI applications like this the point where the program draws the asset is the top left point, not the center; thats why we need to subtract half of the progress bar's width from half the screens width. Then `progress_y` (the Y component of the point) is just a number, for whatever reason. Sloppy programing Comma...

### Getting loading text:
- come back soon! sorry!


### Installing Spinner Changes:
As with the boot logo and boot animmation you have a few options, plus one more! 
- If you maintain your own OpenPilot fork just replace the changed files in your fork, if you `git pull` these changes to your eon you will need to run `cd /data/openpilot/selfdrive/ui/spinner && make` to make the new changes, if you fresh install OpenPilot, it will be made as part of the innital initialization of OP. Also doing it this way ensures you never have to worry about the spinner reverting.
- As with the others you can fork this project and create your own theme folder ###Following this guide### and use my installer to get it on device.
- FileZilla and ADB are options too, just use these tools to replace the appropriate files. See the guides on those for more.



# Auto Installer Information:
Well you want to include the auto installer as part of your OpenPilot fork? Well congrats I'm happy for you! Read this section to see how to implement it! Its actully quite easy to do dont worry! Also feel free to check out ArnePilot to see how I've implemented it there! So lets get started with the requirements, that seems like a good place!

## Requirments:
- The following files are required/not to remain as they are vital or contain licence information.
- - Install_theme.py & restore_backup.py are required
- - The main readme and the licence file are required
- - Everything in `/support` except `eonkey.pem`, `img_spinner_track`, and `spinenr.c` is required (note if you remove `img_spinner_track` and `spinner.c` you **MUST** have a copy of these files in your theme folder or the program will  not work!!!!!)
- - `/developer` and everything in it is not required
- - Any theme that is not the one you want to install & `ignoreme` & `example` are not required.
- - Git related files can be removed

- Plese do not modify the code or files in a way that may negatively effect the user, I have spent alot of time overthinking this project. If you have an idea about improving user experence, please create an issue on github.

- I expect the same community standards to be applied see [requirements to contribute](#How-To-Contribute)

## How It Works:
Inside `./support/support_variables.py` there is a section titled **Auto Installer Vars**; here is where you set up your theme and setting `IS_AUTO_INSTALL` to true when the program is executed it runs the auto installer checker first, and if it fails it checks it installs your theme how you desire based off the `AUTO_INSTALL_CONF` configuration. What are the checks? Glad you asked! There are a few! 
- Firstly it opens and checks the contents of `./support/do_not_auto.txt` This is a way for the user to easily disable auto installation if they choose, its all about the users choice not yours, if its a 0 the program is okay to continue, if its 1, it will lead to termination. 
- The next check, checks if `/sdcard/eon_custom_themes_self_installed.txt` exists; this allows the program to see if a user has installed a theme using the program previously of their choice. This is to not overwrite their earlier decision. Again the program will lead to temination if this exists. (The user can choose to run your theme by deleting that file, then next reboot it will install successfully)
- The third and final check is for version contol, so every boot the installer only runs if a.) it was not auto installed before (to prevent unnecessary, installs), and b.) there is a new "version" of your theme available(more on this later). This works with the `DESIRED_AUTO_VER` in the **Auto Installer Vars** and `./support/auto_install_ver.txt` file. You as the developer set the `DESIRED_AUTO_VER` for your current version adding 1 each time, the program will compare the `DESIRED_AUTO_VER` with the `auto_install_ver` and if they do not match it allows the program to continue. If they are the same value, it will lead the program to terminate. The program will update `auto_install_ver` to the `DESIRED_AUTO_VER` if all these checks 'fail' and the installer actully installs, this circles us back around to the top, next boot the program will not install anything as the most current version is already installed. If you make changes and want to update users devices just increment `DESIRED_AUTO_VER` by one; next time they pull your OP fork and reboot it will install your updated theme!

If users are having issues have them run `exec /data/openpilot/eon-custom-themes/install_theme.py`. The program will print the exit condion(s) and the output of the 3 checks above. 







# How To Make Your Own Theme Folder:
## General Information:
The EON-Custom-Themes installer is quite a complex program just to move a few files around; while designing I wanted to make it as intuitive for the developer to to develop as it is for the user to use! Alot of things are done automagiclly, such as finding available themes, and what all assets that particular theme supports. This requires your theme folder & files to be structrured and named properly so the program can recognize them. But first some backgroud on the program; I urge you to check it out if you havent already to see how it opperates. When the program starts it scans the `contributed-themes` folder for directories, then prints out everything it saw. After the user selects a theme they want the program again scans but this time the particular theme folder looking for the specific files it needs then presenting what it does find to the user!

Anyway enough rambling! lets get down to it 

## Directory Structure:

How to format your theme folder, only use what you need. But there are some important notes! 
- You do not need to include the kumar-black APK in your folder, it will auto populate with all themes! Only add an apk here if you made your own custom one, it will show with the the Kumar-Black APK. 
- By default just place your bootanimation.zip in the directory, you can use the two others if you want to be more specific, or have a color and white version. You can use all 3 if you choose.
- Inside the `spinner` folder you only need to include your `img_spinner_comma.png` minimum, the program will take the `img_spinner_track` and `spinner.c` from /support to reduce wasting storage with duplicate copies. Currently you need to always include the logo file (to be fixed) even if you only want to change the track (which I assume is not likely to be an issue so its at the bottom of my list to do.)


Structure example:

    .
    └──Theme Name                    # Name Of your Theme
        |──APK                       # Your OP APK 
        |──bootanimation.zip         # Default Boot Animation name
        |──white_bootanimation.zip   # A white theme boot animation
        |──color_bootanimation.zip   # A color theme boot animation
        |──Contrib.txt               # Add your info/licence here
        |──Screenshots               # Place screenshots in this folder
        |──Spinner                   # Folder for spinner assets
        |──LEONLogo                  # LEON/GOLD/TWO Boot Logo folder
        |  └──SPLASH
        └──OP3TLogo                  # 3T-EON Boot Logo folder
           └──LOGO


### How To Contribute:
Just Fork this repo, and clone it, add in your theme following the guidlines, and looking at others if you need assistance formating.

Looking to theme your EON? This is the place see [Directory Structure](#Directory-Structure:) You can add whatever you like! Made a custom boot logo? boot Animation? Wonderful!!! Did you edit UI.c? spinner.c? Spinner assets? OP assets? or make your own APK? You can also share your work!! share, you can do that too!!! Just leave instructions in your folder letting them know what to do!

Requirements To Contribute:
* Logo/animation/etc must be in the correct orientation.
* You must follow the directory structure/ how files & folders should be names.
* No Pornographic/Obscene/GreyLine content will be accepted - Keep it clean.
* No "off-color" or controversial content of any kind.
* You are willing to accept responsibility for your theme, I will not maintain your themes.
* You accept legal responsibility over anything in your theme folder, if I receive a copyright notice, I will take down your theme and forward the notice to you until you resolve the issue.
* Some form of contact is required either in `Contrib.txt`, or shared privately with me. 

Ready to submit? Create a pull request, I will reveiw and merge in!

# Misc Info

## FileZilla Mini Guide:
- Getting connected
- -  [Download Filezilla](https://filezilla-project.org/download.php?type=client)
- -  Install FileZilla
- -  Open Site Manager (Top leftmost icon - looks like 3 server racks)
- -  Create a new site and call it EON
- -  For Protocol select SFTP
- -  Enter the IP adress of your eon in Host
- -  Port: 8022
- -  Login Type: Key File
- -  User: root
- -  Key File: choose eonkey.pem from /support in this repo
- -  Click connect

- [How to use filezilla](https://wiki.filezilla-project.org/Using)



## ADB Mini Guide:
### Installing and Connecting with ADB
- [Download ADB](https://dl.google.com/android/repository/platform-tools-latest-windows.zip)
- Extract zip to c:\ADB
- SSH Into Eon
- Run `am start -a android.settings.SETTINGS`
- Find Developer Options and enable **ADB over Network** (this must be done after every reboot)
- Open windows command prompt and navigate to `cd /ADB/platform-tools`
- `adb connect YOUR_EON_IP:5555`


### Using ADB to Copy Files
- To "Push" Files To EON (After connecting)
       
      adb pull windows\path\to\file /eon/path/to/destiination 

- To "Pull" Files From EON (After connecting)
       
      adb push /eon/path/to/file %HOME%\Desktop\

- You can easily get the windows path of a file by selecting `HOME -> Copy Path` in the windows explore menu bar, or dragging the file onto the Windows Command Prompt.

- Copying things like the bootanimation.zip requires you to run `mount -o remount,rw /system` from an SSH terminal or the ADB Shell (type `adb shell` then `su`)(you can exit by pressing ctrl+D to get back to adb) as /system is a read-only file system.




# Donations accepted and very much not required!:
I also hate to ask but I've put quite an ammount of time in to this project. If you like what I've done and do want to help you can buy me a bee....coffee! by donating on [PayPal](paypal.me/BrandonSheaffer). Just a coupple dollary doo's will mean alot, plese dont feel overly generous I did this for my fun and the community!!


        
        
        
                                  