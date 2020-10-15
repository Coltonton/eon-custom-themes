@echo off
echo.-------------------------------------------
echo.LeEco Le Pro 3 Splash Image Maker
echo.
echo.	By **Gokul NC**
echo.-------------------------------------------
echo.
echo.&echo.
echo.Creating splash.img ........&echo.&echo.&echo.
if not exist "output\" mkdir "output\"
del /Q output\*
if exist "splash.img" del /Q splash.img

set resolution=1080x1920

call :VERIFY_FILES

call :CONVERT_TO_RAW

call :JOIN_ALL_RAW_FILES

if exist "output\splash.img" ( echo.SUCCESS!&echo.splash.img created in "output" folder
) else (echo.PROCESS FAILED.. Try Again&echo.&echo.&pause&exit)

echo.&echo.&set /P INPUT=Do you want to create a flashable zip? [yes/no]
If /I "%INPUT%"=="y" goto :CREATE_ZIP
If /I "%INPUT%"=="yes" goto :CREATE_ZIP

echo.&echo.&echo Flashable ZIP not created..&echo.&echo.&pause&exit


:VERIFY_FILES
if not exist "pics\logo1.png" echo.logo1.png not found in 'pics' folder.. EXITING&echo.&echo.&pause&exit
if not exist "pics\logo2.png" echo.logo2.png not found in 'pics' folder.. EXITING&echo.&echo.&pause&exit
if not exist "pics\logo3.png" echo.logo3.png not found in 'pics' folder.. EXITING&echo.&echo.&pause&exit
if not exist "pics\recovery.png" echo.recovery.png not found in 'pics' folder.. EXITING&echo.&echo.&pause&exit
if not exist "pics\battery.png" echo.battery.png not found in 'pics' folder.. EXITING&echo.&echo.&pause&exit
if not exist "pics\fastboot.png" echo.fastboot.png not found in 'pics' folder.. EXITING&echo.&echo.&pause&exit
goto :eof


:CONVERT_TO_RAW
bin\ffmpeg.exe -hide_banner -loglevel quiet -i pics\logo1.png -f rawvideo -vcodec rawvideo -pix_fmt bgr24 -s %resolution% -y "output\splash1.raw" > NUL
bin\ffmpeg.exe -hide_banner -loglevel quiet -i pics\logo2.png -f rawvideo -vcodec rawvideo -pix_fmt bgr24 -s %resolution% -y "output\splash2.raw" > NUL
bin\ffmpeg.exe -hide_banner -loglevel quiet -i pics\logo3.png -f rawvideo -vcodec rawvideo -pix_fmt bgr24 -s %resolution% -y "output\splash3.raw" > NUL
bin\ffmpeg.exe -hide_banner -loglevel quiet -i pics\recovery.png -f rawvideo -vcodec rawvideo -pix_fmt bgr24 -s %resolution% -y "output\splash4.raw" > NUL
bin\ffmpeg.exe -hide_banner -loglevel quiet -i pics\battery.png -f rawvideo -vcodec rawvideo -pix_fmt bgr24 -s %resolution% -y "output\splash5.raw" > NUL
bin\ffmpeg.exe -hide_banner -loglevel quiet -i pics\fastboot.png -f rawvideo -vcodec rawvideo -pix_fmt bgr24 -s %resolution% -y "output\splash6.raw" > NUL
goto :eof


:JOIN_ALL_RAW_FILES
:: Below is the default splash header for all pictures
set H="bin\%resolution%_header.img"

:: Below is just additional padding for each picture's raw image, since 12MB is allocated for each splash image it seems, WTF
set P="bin\padding.img"

copy /b %H%+"output\splash1.raw"+%P%+%H%+"output\splash2.raw"+%P%+%H%+"output\splash3.raw"+%P%+%H%+"output\splash4.raw"+%P%+%H%+"output\splash5.raw"+%P%+%H%+"output\splash6.raw"+%P% "output\splash.img" >NUL
del /Q output\*.raw
goto :eof

:CREATE_ZIP
copy /Y bin\New_Splash.zip output\flashable_splash.zip >NUL
cd output
..\bin\7za a flashable_splash.zip splash.img >NUL
cd..

if exist "output\flashable_splash.zip" (
 echo.&echo.&echo.SUCCESS!
 echo.Flashable zip file created in "output" folder
 echo.You can flash the flashable_splash.zip from any custom recovery like TWRP or CWM or Philz
) else ( echo.&echo.&echo Flashable ZIP not created.. )

echo.&echo.&pause&exit