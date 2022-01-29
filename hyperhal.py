from ast import excepthandler
from cgi import test
from logging import exception
import time
import random
import os
from turtle import color
import click
import re

click.clear()

def shellprompt():
    global prompt
    prompt = input('user in ' + os.getcwd() + "> ")
    commandcheck()

def commandcheck():
    global cd
    global mkdir
    mkdir = 'mkdir '
    cd = 'cd '
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
    elif mkdir in prompt:
        dirtomake = prompt.rsplit('mkdir ', 2)[2]
        os.mkdir(dirtomake)
        shellprompt()
    for cd in prompt:
        dirtocdto = prompt.partition('cd ')[2]
        os.chdir(dirtocdto)
        shellprompt()
    else:
        print("File or command not found!")
        shellprompt()

def shell():
    print("eNix* [Version 0.1]")
    print("HyperHAL INTERACTIVE SHELL.")
    print()
    shellprompt()

shell()