#library
try:
  import ftplib
except:
  import os
  os.system("pip install pyftplib")
  import ftplib
#functions
def login(host, user, password, color):
  try:
    ftp = ftplib.FTP(host, user, password)
    ftp.encoding = "utf-8"
    ftp.quit()
  except:
    print(f"{color}error: incorrect login information\033[0;0m")
    exit()
def login_input(host, user, password, color1, color2, color3):
  try:
    ftp = ftplib.FTP(host, user, password)
    ftp.ecoding = "utf-8"
    ftp.quit()
    ask = input(f"{color1}do you want to save login information? [y/n]:{color2}")
    data = f"""[login]
host = {host}
user = {user}
password = {password}"""
    if ask == "y":
      with open("system/res/login.cfg", "w") as file:
        file.write(data)
      file.close()
  except:
    print(f"{color3}error: incorrect login information\033[0;0m")
    exit()
def upload(host, user, password, file_name, directory):
  ftp = ftplib.FTP(host, user, password)
  ftp.encoding = "utf-8"
  ftp.cwd(directory)
  with open(file_name, "rb") as file:
    ftp.storbinary(f"STOR {file_name}", file)
    ftp.quit()
  file.close()
def download(host, user, password, file_name, directory):
  ftp = ftplib.FTP(host, user, password)
  ftp.encoding = "utf-8"
  ftp.cwd(directory)
  ftp.retrbinary(f"RETR {file_name}" ,open(file_name, 'wb').write)
  ftp.quit()
def rmdir(host, user,password, dir_name, directory):
  ftp = ftplib.FTP(host, user, password)
  ftp.encoding = "utf-8"
  ftp.cwd(directory)
  ftp.rmd(dir_name)
  frp.quit()
def mkdir(host, user, password, dir_name, directory):
  ftp = ftplib.FTP(host, user, password)
  ftp.encoding = "utf-8"
  ftp.cwd(directory)
  ftp.mkd(dir_name)
  ftp.quit()
def rename(host, user, password, default_name, new_name, directory):
  ftp = ftplib.FTP(host, user, password)
  ftp.encoding = "utf-8"
  ftp.cwd(directory)
  ftp.rename(default_name, new_name)
  ftp.quit()
def delete(host, user, password, file_name, directory):
  ftp = ftplib.FTP(host, user, password)
  ftp.encoding = "utf-8"
  ftp.cwd(directory)
  ftp.delete(file_name)
  ftp.quit()
def list(host, user, password, directory):
  ftp = ftplib.FTP(host, user, password)
  ftp.encoding = "utf-8"
  ftp.cwd(directory)
  print(ftp.nlst())
  ftp.quit()