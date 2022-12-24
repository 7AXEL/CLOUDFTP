#!/bin/bash
clear
printf "\033[0;92mInstallation started..\n"
sleep 2
printf "\033[0;94m Setting up python\n"
sleep 1
printf "\033[0;94m Setting up java\n"
sleep 1
printf "\033[0;94m Setting up ruby\n"
sleep 1
printf "\033[0;94m Setting up mplayer\033[0;0m\n"
sleep 1
apt-get update -y
apt-get upgrade -y
apt-get install python openjdk17 ruby mplayer
printf "\033[0;93mInstallation Complete\n"
sleep 2
clear
printf "\033[0;94mDo you want to start the programe? [y/n]: "
read ask
if [ $ask = "y" ]
then
  rm -rf install.sh README.md
  python main.py
fi
rm -rf install.sh README.md