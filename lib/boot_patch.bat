@echo off

if "%1"=="" call :Usage & exit /b 1
if "%1"=="-h" call :Usage & exit /b 0
if "%1"=="--help" call :Usage & exit /b 0

set "Path=%~dp0bin;%Path%"

if not exist %1 busybox printf "\033[031mError File [%1] not found...\033[0m\nPlease check your path if correct...\n" & exit /b 1

busybox printf "\033[033mWorking on [%1] image\033[0m\n"

if "%2"=="" set IS64BIT=true
if "%3"=="" set KEEPVERITY=false
if "%4"=="" set KEEPFORCEENCRYPT=false

busybox ash boot_patch.sh %1 %2 %3 %4
del stock_boot.img >nul 2>nul
del ramdisk.cpio >nul 2>nul
del dtb >nul 2>nul
del kernel >nul 2>nul
del kernel_dtb  >nul 2>nul

exit /b 0
:Usage
echo  Usage:
echo  %~nx0 ^<boot image^> ^<is 64 bit^> ^<keepverity^> ^<keepforceencrypt^>
echo      You can just provide boot.img
echo      But if you want different patch just provide more args
echo  Example:
echo  %~nx0 boot.img true true true
echo  Explain:
echo      Is64Bit : if your device is 64 bit device set arg2 is true default is [true]
echo      KEEPVERITY : if you want keep verity like dm-verity avb-verity in fstab or dt file
echo      KEEPFORCEENCRYPT : As it says keep force encrypt
echo.
goto:eof