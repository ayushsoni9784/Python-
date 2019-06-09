#!/usr/bin/python3

a=input().split()
for i in a :
    try :
        val=int(i)
        break ;
    except ValueError :
        print("string") 

import os 
import subprocess

name=input("Enter the name of user")
subprocess.call(["adduser",name])
subprocess.call(["passwd","hello{}".format(name),name])

