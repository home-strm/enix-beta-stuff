import getpass
import time
import os

print("Welcome to account registeration!")
username = input("Username: ")
password = getpass.getpass("Password: ")
f = open("username.txt", "a")
f.write(username)
f.close
w = open("password.txt", "a")
w.write(password)
w.close

print("Your new username and password will be " + username + " and " + password)
time.sleep(3)
os.system("py login.py")
