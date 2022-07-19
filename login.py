import os
import click
import time
import getpass
from os.path import exists

usernameexists = exists('username.txt')

if usernameexists == True:  
    with open('username.txt', 'r') as file:
        username = file.read().replace('\n', '')
    with open('password.txt', 'r') as file:
        password = file.read().replace('\n', '')

click.clear()
def usernameCheck2():
    click.clear
    global usernameCheck1
    global passwordCheck1
    print("eNix [eficcient Nix*].")
    print("Version 0.1 alpha")
    print()
    usernameCheck1 = input("Username: ")
    passwordCheck1 = getpass.getpass("Password: ")
    usernameCheck3()

def usernameCheck3():    
    if usernameCheck1 == username:
        if passwordCheck1 == password:
            os.system('python3 hyperhal.py')
        else:
            print("Incorrect password!")
            time.sleep(2)
            click.clear()
            usernameCheck2()
    else:
        print("Incorrect username!")
        time.sleep(2)
        click.clear()
        usernameCheck2()

if usernameexists == True:
    usernameCheck2()
else:
    os.system('python3 register.py')

