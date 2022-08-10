import tkinter as tk
from tkinter.filedialog import askopenfilename
import time
import subprocess
import os

def path():
    tk.Tk().withdraw()
    loc = askopenfilename()
    loc = loc[::-1]
    x = loc.find("/")
    loc = loc[x+1:]
    loc= loc[::-1]
    print("Path : ",loc,"\n")
    return loc

def execute(command,working_directory):
    p = subprocess.Popen(command,cwd= working_directory)
    p.wait()
    print("----------------------------------\n\n")

print("\n\n----- Welcome to automatic CS50 project submitting script -----\n\n")
print("Select any file from the folder which to be submitted...\n")

time.sleep(3.0)

location = path()
repo = input("Enter the repository name : ")
comment = input("Enter a Comment : ")
user_name = input("Enter the Git User name : ")

commands = [ #"cd /d {}".format(location),
            "git init",
            "git checkout -b {}".format(repo),
            "git status",
            "git add -A",
            '''git commit -am "{}"'''.format(comment),
            "git remote add origin https://github.com/me50/{}.git".format(user_name),
            "git remote",
            "git push origin --all"
]

guides = [
    #"Changing Path to : {}".format(location),
    "Initializing Git ",
    "Git creating Repository : {}".format(repo),
    "Checking Git status",
    "Adding Files ",
    "Commiting Changes",
    "Adding remote origin",
    "Checking git remote",
    "Pushing all files"
]

loop = len(commands)

for i in range(loop):
    print (guides[i],commands[i])
    #os.system('{}'.format(commands[i]))
    execute(commands[i],location)

print("\n\n--------------- Successfully Uploaded ---------------\n\n")

print("Dont forget to submit gforms\n\n")
print("Press:")
print("1 : To launch Github Branches")
print("2 : To open CS50 gradebook")
print("3 : To launch both")

case = input("Your Choice: ")

if (case == "1"):
    os.startfile("https://github.com/me50/{}/branches".format(user_name))
    print("Launched Github\n\n ----------The Program will terminate after 30 seconds----------")
elif(case == "2"):
    os.startfile("https://cs50.me/cs50ai")
    print("Launched Gradebook\n\n ----------The Program will terminate after 30 seconds----------")
elif(case == "3"):
    os.startfile("https://github.com/me50/{}/branches".format(user_name))
    os.startfile("https://cs50.me/cs50ai")
    print("Launched Github and Gradebook\n\n ----------The Program will terminate after 30 seconds----------")
else:
    print("Invalid command\n\n ----------The Program will terminate after 30 seconds----------")

time.sleep(30)