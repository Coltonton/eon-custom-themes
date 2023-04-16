#!/bin/bash
echo What Program Would You Like To Run?
echo 1.Theme-Installer
echo 2.Theme-Restorer
echo 3.Theme-Utilities
read varname

if [ $varname -eq 1 ]
then
   exec ./theme_install.py
fi
if [ $varname -eq 2 ]
then
   exec ./theme_restore.py
fi
if [ $varname -eq 3 ]
then
   exec ./theme_utility.py
fi