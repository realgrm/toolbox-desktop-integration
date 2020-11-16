#!/usr/bin/env python3

from pathlib import Path
import os
import subprocess
import sys

# _______________________________________________________________

# declare variables
l=os.environ['HOME']+"/.local/share/folder/toolbox"
c_usrshare=""
c_overlay=os.environ['HOME']+"/.local/share/containers/storage/overlay/"
file_check="/diff/usr/share/"
#/var/home/realgrm/.local/share/containers/storage/overlay/b4fa6ff1346dec95ce4454464201fdadfd816e10eb7322048829c551ce032d08/diff

# _______________________________________________________________

# defining functions

# to show informations to the user

def msg_link_created():
    print("created symlink:\n"+click+"\n\nthat redirects to:\n"+havetolink)

def msg_link_ok():
    print("all ok, symlink already exists:\n"+click+"\n\nit redirects to:\n"+linksto)

def msg_link_nok():
    print("can't create symlink, because another symlink already exists:\n"+click+"\n\nit redirects to:\n"+linksto)

def msg_file_nok():
    print("can't create symlink, because file/folder already exists\n"+click+"\n\nplease delete (with backup?) or rename it, then try again.")

def msg_container_nok():
    print("Container not found.\nCreate one with the command \"toolbox create\" in the terminal")

def msg_container_file_nok():
    print("File that check  not found.\nMake sure a container is created using the command \"toolbox list\" or try to change the file_check variable")

# to show debug info

def msg_debug():
    print("debug locations:")
    print("where do i click (exists: "+str(Path(click).exists())+" is symlink: "+str(Path(click).is_symlink())+")\n"+click)
    print("have to link:\n"+havetolink)
    print("currently links to:\n"+linksto)
    print("click=link"+str(click==linksto))
    print("link ok: "+str(havetolink==linksto))

# _______________________________________________________________

print("\n\n_____________________")
print("\nINSTALL DESKTOP FILES SCRIPT")
print("_____________________\n")

# _______________________________________________________________

# get the correct folder to the container

if not Path(c_overlay).is_dir():
    sys.exit(msg_container_nok())

for id in os.listdir(c_overlay):
    i=c_overlay+id+file_check
    j=i+"applications"
    print(str(Path(j).exists())+": "+j)
    
    if Path(j).is_dir():
        c_usrshare=i
        c_id=id

if c_usrshare == "": 
    sys.exit(msg_container_file_nok())

print("\nfolder of container: \n"+c_usrshare)

# _______________________________________________________________


# Check if links already exists, if not, create them

a=["applications","icons"]

for i in a:
    print("\n"+"_____________________\n")
    print(i+"\n")
    click=l.replace("folder",i)   
    havetolink=c_usrshare+i
    linksto=str(Path(click).resolve())

    #uncomment the line bellow to show more info
    #msg_debug

    if not Path(click).exists() and click==linksto:
        os.symlink(havetolink, click)
        msg_link_created()
    elif Path(click).is_symlink():
        if havetolink==linksto:
            msg_link_ok()
        else: msg_link_nok()
    else: msg_file_nok()

print("\n")
# _______________________________________________________________

#create backup folder for desktop files
backup_folder=os.environ['HOME']+"/.local/share/containers/storage/overlay/"+c_id+"/diff/usr/share/applications_backup/"

try:
    os.mkdir(backup_folder)
    print("backup folder created:") 
except:
  print("backup folder already exists:")

print(backup_folder)
# _______________________________________________________________

# create a shortcut in app grip

print("\n")

currentDirectory = os.getcwd()
desktop_file=os.environ['HOME']+"/.local/share/applications/update_desktop_files.desktop"

f=currentDirectory+"/update_desktop_files.desktop"
fileHandler = open(f, "r")
replaced_content = ""
#looping through the file
for line in fileHandler:

    #stripping line break
    line = line.strip()

    # if the criterias bellow don't match, the default is to keep the value
    new_line=line

    # _______________________________________________________________

    # checking and changing line

    if line.startswith("Exec="):
        if "bash" in line: break
        else:
            new_line = line.replace("Exec=","Exec=bash -c 'cd "+currentDirectory)
                      
    elif line.startswith("Icon="):
        new_line = line.replace("Icon=", "Icon="+currentDirectory+"/")

    replaced_content = replaced_content + new_line + "\n"

#close the file
fileHandler.close()

sts = subprocess.Popen("cp" + " -n '"+f+"' '"+desktop_file+"'", shell=True).wait()

#Open file in write mode
write_file = open(desktop_file, "w")

#overwriting the old file contents with the new/replaced content
write_file.write(replaced_content)

#close the file
write_file.close()
print("\n")


print("desktop file placed in: \n"+desktop_file)
print("\n")

# _______________________________________________________________

#try to update apps in App Grid
sts = subprocess.Popen("update-desktop-database" + " ~/.local/share/applications", shell=True).wait()

# _______________________________________________________________
# start another script
import update_desktop_files
