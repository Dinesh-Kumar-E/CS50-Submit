import tkinter as tk
from tkinter.filedialog import askopenfilename
import time
import subprocess
import os

def path():
    
    '''This function opens a file explorer window to select any particular file
    form the directory which should be uploaded to git.
    The necessary functions below are used to extract the exact path of the directory
    arguments:  -> None
    returns :   -> Folder path of the dir to be uploaded to git'''
    
    tk.Tk().withdraw()
    loc = askopenfilename()
    loc = loc[::-1]
    x = loc.find("/")
    loc = loc[x+1:]
    loc= loc[::-1]
    print("Path : ",loc,"\n")
    return loc

def execute(command,working_directory):

    '''This function executes the necessary commands on command prompt on particular location
        arguments:  -> commmand (The cmd command to be executed [required])
                    -> working_directory (Path in thich the cmd command to be executed [required])
                    
        returns :   -> None'''
    
    p = subprocess.Popen(command,cwd= working_directory)
    p.wait()
    print("----------------------------------\n\n")

print("\n\n----- Welcome to automatic CS50 project submitting script -----\n\n")
print("Select any file from the folder which to be submitted...\n")

time.sleep(3.0)

location = path()  #getting the path from path() function.

#Collecting required details from users.

repo = input("Enter the repository name : ")
comment = input("Enter a Comment : ")
user_name = input("Enter the Git User name : ")

#necessary commands to be executed.

commands = [
            "git init",
            "git checkout -b {}".format(repo),
            "git status",
            "git add -A",
            '''git commit -am "{}"'''.format(comment),
            "git remote add origin https://github.com/me50/{}.git".format(user_name),
            "git remote",
            "git push origin --all"
]

#user friendly messages

guides = [
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

#Executing every commands using for loop.

for i in range(loop):
    print (guides[i],commands[i])
    execute(commands[i],location)

print("\n\n--------------- Successfully Uploaded ---------------\n\n")


#Giving users requied prompts and helping them to verify whether the bot has done the job.

print("Dont forget to submit gforms\n\n")
print("Press:")
print("1 : To launch Github Branches")
print("2 : To open CS50 gradebook")
print("3 : To launch both")

case = input("Your Choice: ")

if (case == "1"):
    os.startfile("https://github.com/me50/{}/branches".format(user_name))
    print("\n\n************ All the Best************\n\n")
    print("Launched Github\n\n ----------The Program will terminate after 30 seconds----------")
elif(case == "2"):
    os.startfile("https://cs50.me")
    print("\n\n************ All the Best************\n\n")
    print("Launched Gradebook\n\n ----------The Program will terminate after 30 seconds----------")
elif(case == "3"):
    os.startfile("https://github.com/me50/{}/branches".format(user_name))
    os.startfile("https://cs50.me")
    print("\n\n************ All the Best************\n\n")
    print("Launched Github and Gradebook\n\n ----------The Program will terminate after 30 seconds----------")
else:
    print("\n\n************ All the Best************\n\n")
    print("Invalid command\n\n ----------The Program will terminate after 30 seconds----------")

time.sleep(30)