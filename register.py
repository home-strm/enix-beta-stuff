import os
import time
import getpass

print("Welcome to account registeration!")
username = input("Username: ")
password = getpass.getpass("Password: ")
with open('username.txt', "w") as newusername:
    newusername.write(username)

with open('password.txt', "w") as newpassword:
    newpassword.write(password)

print("Your new username and password will be " + username + " and " + password)
time.sleep(3)
os.system("py login.py")