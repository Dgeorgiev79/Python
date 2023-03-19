#!/usr/bin/python3.6
  
import subprocess

file = open('result.txt','a')

# enter one row white space in file
file.write("\n")

file.write("##### Date & Time ######\n")
dt = subprocess.Popen("date", stdout=subprocess.PIPE).stdout.read().decode()
file.write(dt)

# enter one row white space in file
file.write("\n")

file.write("##### CPU ######\n")
dt = subprocess.Popen("lscpu", stdout=subprocess.PIPE).stdout.read().decode()
file.write(dt)

# enter one row white space in file
file.write("\n")

file.close()
