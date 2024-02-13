#!/bin/bash

# This script generates two files listing installed packages (regualr and from AUR) in the homedir of the user, intended for backup/recovery purposes

echo "exporting list of explicitly installed regular packages into ~/pkglist.txt"
pacman -Qqen > ~/pkglist.txt

echo "exporting list of explicitly installed AUR packages into ~/pkglist_aur.txt"
pacman -Qqem > ~/pkglist_aur.txt

# RECOVERY
#
# 1. pacman -S --needed - < pkglist.txt
#
# 2. manually install yay from AUR
#      see https://wiki.archlinux.org/title/Arch_User_Repository
#      and https://github.com/Jguer/yay
#
# 3. [command TBC] yay -S --needed < pkglist_aur.txt
