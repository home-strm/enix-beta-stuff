from math import perm
import time
import random
import os
import turtle
import click
import re
import sys
import getpass

with open('username.txt', 'r') as file:
    username = file.read().replace('\n', '')

with open('password.txt', 'r') as file:
    password = file.read().replace('\n', '')

permisions = '0'

click.clear()

def shellprompt():
    global prompt
    prompt = input(username + ' in ~ ')
    commandcheck()

def commandcheck():
    global cd
    global mkdir
    global rm
    global esu
    global py
    rm = 'rm '
    mkdir = 'mkdir '
    cd = 'cd '
    esu = 'esu '
    py = 'py '
    if prompt == 'ls':
        global lscmd
        lscmd = os.listdir(os.getcwd())
        print(lscmd)
        shellprompt()
    elif prompt == 'exit':
        click.clear()
        exit()
    elif prompt == 'clear':
        click.clear()
        shellprompt()
    elif prompt == 'time':
        print(time.asctime())
        shellprompt()
    elif prompt == 'help':
        print("ls - List all files and folders in active directory.")
        print("cd - Change directorys. Usage - cd [Folder name]")
        print("mkdir - Make a new folder. Usage -  mkdir [Folder name]")
        print("clear - Clears screen.")
        print("time - Displays time and date.")
        print("rm - Removes a directory. Usage - rm [Folder name]")
        print("py - Opens a Python program.")
        print("esu - Runs a program with super user permisions.")
        print("su - Enables super user permisions.")
        print("sucheck - Checks permision level.")
        print("efetch -  Displays system information.")
        print("logout - Returns to log in screen.")
        shellprompt()
    elif prompt == 'logout':
        os.system('python3 login.py')
    elif prompt == 'su':
        suconfirm = getpass.getpass('Password: ')
        if suconfirm == password:
            global permisions
            permisions = '1'
            shellprompt()
        else:
            print('Incorrect password!')
            permisions = '0'
            shellprompt()
    elif prompt == 'efetch':
        os.system('python3 efetch.py')
        shellprompt()
    elif prompt == 'sucheck':
        if permisions == '1':
            print('Super user permisions enabled.')
            shellprompt()
        else:
            print('Super user permisions disabled.')
            shellprompt()
    elif mkdir in prompt:
        nfoldername = prompt.lstrip('mkdir ')
        os.mkdir(nfoldername)
        shellprompt()
    elif cd in prompt:
        try:
            dirtocdto = prompt.lstrip('cd ')
            os.chdir(dirtocdto)
            shellprompt()
        except:
            print("CD : File or folder not found!")
            shellprompt()
    elif rm in prompt:
        try:
            dirtorm = prompt.lstrip('rm ')
            os.rmdir(dirtorm)
            shellprompt()
        except:
            print("DIR : File or folder not found!")
            shellprompt()
    elif esu in prompt:
        esuconfirm = getpass.getpass('[ esu ] Password for ' + username + ': ')
        if esuconfirm == password:
            esudo = prompt.lstrip('esu ')
            os.system('python3 ' + esudo)
            shellprompt()
        else:
            print("Incorrect password!")
            shellprompt()
    elif py in prompt:
        filetoopen = prompt.lstrip('py ')
        os.system('py ' + filetoopen)
        shellprompt()
    else:
        print("HyperHAL : File or command not found! Type help for a list of commands!")
        shellprompt()

def shell():
    print("eNix [Version 0.1 alpha]")
    print("HyperHAL INTERACTIVE SHELL.")
    print()
    shellprompt()

shell()