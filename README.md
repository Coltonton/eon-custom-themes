Initial Release Coming Soon! Slowly Getting er done :)

[![](https://i.imgur.com/IcCeUD7.png)](#)
# EON-Custom-Themes
Upgrade your EON/Leon/Two's Looks!!! This is a pretty all inclusive guide to modify your device themingly. It's your own device! You own it, do with it as you please despite what someeee people may say, which is ironic dont you think?..... Lets Light It Up!!! (Contest)

This is a new project, find any errors? submit an issue, or make a pull request! This is not my project but our project!! * **Soviet national anthem plays** * You may also message me @C-ton#2169 on discord (I'm in all the servers)

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

### How To Contribute
*  [Contribute Your Work!](#contribute-your-work)

### Minimal Self Installer Assistance (Included with OP Forks)




# What is this?

Thanks for asking young one! This is a project dedicated to de-comma-ing your EON! Wether you dont like Comma.ai the company or want to personalize your EON, I gotchu fam!

This is a community project so here you can find new boot logos, boot animations, OpenPilot loading animations, and even more for your device! Created/designed by myself with help from Shane Smiskol. With themes designed and made by myself and other community members. 

Also included in this repository is all the info you need to start hacking and making your own extra custom themes! See the [DEVREADME](https://github.com/Coltonton/eon-custom-themes/blob/master/developer/DEVREADME.md) in this repo in the developer folder. 

Did you make your own and want to share it with the world? Wonderful! Check out that [DEVREADME](https://github.com/Coltonton/eon-custom-themes/blob/master/developer/DEVREADME.md) to learn how to submit!

# How To Use:
Thanks to many hours of coding, thinking, and courtious help of @ShaneSmiskol this project couldn't be easier to install and run! If you have installed a custom fork of OpenPilot, can answer simple questions, or can just follow this simple guide you will be up and running with a new look in no time! 

**BEFORE YOU START**
- This program will automagicly backup the existing theme before copying the new; and saves them to the backups folder in this project. If replacing the Comma.AI stock theme, be sure to keep to transfer the backups to a safe place off device just in case if you want to go back! **I DO NOT AND WILL NOT PROVIDE THESE FILES** for obvious legal reasons... Because they are assholes and would actually care and try to shut this project shut down, or even sue me... hmm... maybe I should cuz then I could make a crappy rap and call it "The Light It Up Contest" See [Restoring Backup](#restoring-theme-assets-from-backup) and [Restoring The Comma.ai Stock Theme If Backup Lost):](#restoring-the-comma-stock-theme-if-backup-lost)
- As per the [licence](https://github.com/Coltonton/eon-custom-themes/Licence), this software is provided "as is", without warranty of any kind and in no event shall I or any other authors be liable for any claim, damages, or other liability. Use this project at your own risk!

**Let's Begin:**

1. [SSH into your EON. (Workbench is the easist way)](https://medium.com/@jfrux/comma-eon-getting-connected-with-ssh-3ed6136e4a75)
2. In the terminal enter `cd /data`
3. `git clone https://github.com/Coltonton/eon-custom-themes.git`

4. `cd ./eon-custom-themes` after cloning has finished
5. `exec ./install_theme.py`
6. The installer will now run.

### Navigating The Installer:
1. The installer will firstly prompt you for what theme you would like to choose. Enter the name, or index number and press enter. If you misspelled the theme name from the shown theme name; the program will attempt to figure out what you ment and ask you to confirm.
2. Now the installer will promt you with the available assets for that theme. You can choose (if availble) the **Boot Logo**, **Boot Animation**, **OpenPilot Spinner**, and **Additional Resources**. ([What do these mean?](#what-are-the-availble-assets))
3. One by one choose your desired theme assets and they will automagically install! Want to install diffrent assets from diffrent themes? YOU CAN! Sipmply select **-Main Menu-** from the options to be taken back to the theme picker!
4. Once done select **-Reboot-** to reboot your EON and see your new themes!!!!
5. Having issues? Message me on discord @C-ton#2169

### What Are The Availble Assets?

- The **Boot Logo** is the first thing to show when you turn on your EON, it is a static image. It is also the images for when your EON is dead, or dead but charging!
- The **Boot Animation** plays right after the Boot Logo and is the animated animation for your device while Android loads!
- The **OpenPilot Spinner** is the second animation that shows while your EON boots, this is the loading animation for OpenPilot itself!
- **Additional Resources** can be a variaty of things consult the contrib.txt file in the desired themes folder in `contributed-themes`. Possible additional resources are OpenPilot sounds, OpenPilot assets (like the home button icon and other things like the battery icon & cell strength), and even code patches!!

### Restoring Theme Assets From Backup:
- Program releasing soon

### Restoring The Comma Stock Theme If Backup Lost:
- Information not yet provided



----
# List Of Themes:
You can see screenshots of what the theme looks like in the desired theme folders screenshots folder. All theme folders are located in the `contributed-themes` directory of this repo

## Stock Themes:
| Theme Name            |Boot Logo? (3T)| Boot Logo? (LeEco) | Boot Animation? | Custom OP Files?                 |
| ----------------------| --------------| ------------------ | ----------------| ---------------------------------|
| Acura                 | Yes           | Yes                | Yes             | No                               |
| Android               | Yes           | Yes                | Yes             | No                               |
| ArnePilot             | Yes           | Yes                | Yes             | No                               |
| Chevy                 | Yes           | Yes                | Yes             | No                               |
| DragonPilot           | Yes           | Yes                | Yes             | No                               |
| A General Theme       | Yes           | Yes                | Yes             | No                               | 
| Honda                 | Yes           | Yes                | Yes             | No                               |
| Hyundai               | Yes           | Yes                | Yes             | No                               |
| Kia                   | Yes           | Yes                | Yes             | No                               |
| Subaru                | Yes           | Yes                | Yes             | No                               |
| Toyota                | Yes           | Yes                | Yes             | No                               |

This is the default linup, I will be creating coupple others. Happy to hear suggestions for others!!! 

## Contributed Themes
| Theme Name            |Boot Logo? (3T)| Boot Logo? (LeEco) | Boot Animation? | Custom OP Files?                 | Contributor/ Author|
| ----------------------| --------------| ------------------ | ----------------| ---------------------------------| -------------------|
| Comma-Stock           | Yes           | Yes                | Yes             | OP Spinner                      | Comma.ai           |
| Colton-HooeyPilot     | Yes           | No                 | Yes             | Elements, & Sounds              | Colton             |
| Khonsu-LemmonCurd     | Yes           | No                 | Yes             | No                              | Colton             |
---
---

# Contribute Your Work!:

Please see the [DEVREADME](https://github.com/Coltonton/eon-custom-themes/blob/master/developer/DEVREADME.md)  in the developer folder of this repo to find out about contributing your designed theme! 

---

# Shameless Plug For A Bee....Cup Of Coffee:
I also hate to ask but I've put quite an ammount of time in to this project. If you like what I've done and do want to help you can buy me a bee....coffee! By donating on [PayPal](https://paypal.me/dattech?locale.x=en_US). Just a coupple dollary doo's will mean alot, plese dont feel overly generous I did this for my fun and the community!! 
        
        
        
                                  
