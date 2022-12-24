#librarys
from time import sleep
from getpass import getpass
from system.lib import ftp
from system.lib.colors import *
from system.lib import audio
from sys import platform
import os
try:
  from configparser import ConfigParser 
except:
  os.system("pip install configparser")
  from configparser import ConfigParser
#variables
red = colors.red
green = colors.green
yellow = colors.yellow
blue = colors.blue
purple = colors.purple
cyan = colors.cyan
white = colors.white
reset = colors.reset
input_msg = f"""{blue}┌─[OPTION]─[~]
└──❯❯❯ {white}"""
#functions
def title():
  os.system("bash title.sh")
#execute
if platform == "linux" or platform == "linux2":
  title()
  print(f"{red}[1]{yellow} START\n{red}[2] {yellow}PARAMETERS\n{red}[3] {purple}ABOUT\n{cyan}[4] EXIT{reset}")
  option = input(input_msg)
  if option == "1":
    if os.path.exists("system/res/login.cfg") == True:
      parser = ConfigParser()
      parser.read_file(open("system/res/login.cfg", "r"))
      try:
        host = parser.get("login", "host")
        user = parser.get("login", "user")
        password = parser.get("login", "password")
        ftp.login(host, user, password, red)
      except:
        print(f"{red}error: missing login file{reset}")
        exit()
    elif os.path.exists("system/res/login.cfg") == False:
      host = input(f"{blue}host:{white}")
      user = input(f"{blue}user:{white}")
      password = getpass(f"{purple}password:")
      ftp.login_input(host, user, password, green, white, red)
    title()
    print(f"{red}[1] {yellow}UPLOAD\t{red}[5] {yellow}MKDIR\n{red}[2] {yellow}DOWNLOAD\t{red}[6] {yellow}RMDIR\n{red}[3] {yellow}DELETE\t{red}[7] {yellow}RENAME\n{red}[4] {yellow}LIST\t{purple}[8] {cyan}EXIT")
    while True:
      option = input(input_msg)
      try:
        if option == "1":
          file_name = input(f"{purple}filename:{white}")
          directory = input(f"{purple}directory:{white}")
          ftp.upload(host, user, password, file_name, directory)
        elif option == "2":
          file_name = input(f"{purple}filename:{white}")
          directory = input(f"{purple}directory:{white}")
          ftp.download(host, user, password, file_name, directory)
        elif option == "3":
          file_name = input(f"{purple}filename:{white}")
          directory = input(f"{purple}directory:{white}")
          ftp.delete(host, user, password, file_name, directory)
        elif option == "4":
          directory = input(f"{purple}directory:{white}")
          ftp.list(host, user, password, directory)
        elif option == "5":
          dir_name = input(f"{purple}directory name:{white}")
          directory = input(f"{purple}directory:{white}")
          ftp.rmdir(host, user, password, dir_name, directory)
        elif option == "6":
          dir_name = input(f"{purple}directory name:{white}")
          directory = input(f"{purple}directory:{white}")
          ftp.mkdir(host, user, password, dir_name, directory)
        elif option == "7":
          file_name = input(f"{purple}file/directory name:{white}")
          new_name = input(f"{purple}new name:{white}")
          directory = input(f"{purple}directory:{white}")
          ftp.download(host, user, password, file_name, new_name, directory)
        elif option == "8":
          break
          exit()
      except:
        print(f"{red}error{white}")
  elif option == "2":
    ques = (f"{green}delete saved login information? [y/n]:{white}")
    if ques == "y":
      os.remove("system/res/login.cfg")
      os.system("python  main.sh")
  elif option == "3":
    os.system("clear")
    audio.play("system/assets/about.mp3")
    os.system("python main.py")
  elif option == "4":
    exit()
  else:
    print(f"{red}error: invalide option{white}")
    sleep(1)
    os.system("python main.py")