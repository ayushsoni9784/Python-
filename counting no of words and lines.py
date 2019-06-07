#!/usr/bin/python
file_name=input("enter the name or address of file :")
f=open(file_name)
data=f.read()
words=len(data.split())
num_lines=len(data.splitlines())
print("no of words=",words)
print(num_lines)

