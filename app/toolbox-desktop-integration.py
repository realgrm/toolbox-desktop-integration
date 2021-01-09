#!/usr/bin/env python3

import os
from pathlib import Path
import shutil
import subprocess
import sys

# _______________________________________________________________

# declaring some inicial variables

usrshare=os.environ['HOME']+"/.local/share"
c_overlay=os.environ['HOME']+"/.local/share/containers/storage/overlay"
c_usrshare="diff/usr/share"
app_folder=os.environ['HOME']+"/.local/scripts/toolbox-desktop-integration"
backups_folder=app_folder+"/applications_backup"


# _______________________________________________________________

# -----------------------Auxiliar functions---------------------

# _______________________________________________________________

#Print title of the script
def msg_title():
    print("_____________________")
    print("_____________________")
    print("\nUPDATE DESKTOP FILES SCRIPT")
    print("_____________________")
    print("_____________________")
    print("")

def msg_title_symlink():
    print("\n_____________________")
    print("\nVERIFYING SYMLINKS")
    print("_____________________\n")

def msg_title_summary():
    print("\n\n_____________________")
    print("\nSUMMARY")
    print("_____________________\n")

def msg_verifying_files():
    print("\n_____________________")
    print("\nVERIFYING FILES")
    print("_____________________\n")

def msg_link_created(click,havetolink):
    print("created symlink:\n" \
        +click+"\n\nthat redirects to:\n" \
        +havetolink+"\n")


def msg_link_ok(click,linksto):
    print("all ok, symlink already exists:\n" \
        +click+"\n\nit redirects to:\n" \
        +linksto+"\n")


def msg_link_nok(click,linksto,havetolink):
    print("can't create symlink, because another symlink already exists:\n" \
        +click+"\n\nit redirects to:\n" \
        +linksto+"\n\nit shoud be:\n" \
        +havetolink+"\n")


def msg_file_nok(click):
    print("can't create symlink, because file/folder already exists\n" \
        +click+"\n\nplease delete (with backup?) or rename it, then try again.")


def msg_container_nok():
    print("Container not found.\n \
    Create one with the command \"toolbox create\" in the terminal")


def msg__invalid_link(click,linksto,havetolink):
    print("deleted link:\n" \
    +click+"\n\n \
    it was redirecting to a non existing location:\n" \
    +linksto \
    +"\n\nnow it redirects to:\n" \
    +havetolink)


def msg_backup(backup_folder):
    print("\nbackup of file created in:\n"+backup_folder+"\n") 


# to show debug info
def msg_debug(click,linksto,havetolink):
    print("\n_____________________")
    print("debug locations:")
    print("where do i click (exists: "+str(Path(click).exists())+" is symlink: "+str(Path(click).is_symlink())+")\n"+click)
    print("have to link:\n"+havetolink)
    print("currently links to:\n"+linksto)
    print("click=link: "+str(click==linksto))
    print("link ok: "+str(havetolink==linksto))
    print("_____________________\n")

#all symlinks
def msg_symlink_list(symlink_list):
    symlink_list=sorted(list(dict.fromkeys(symlink_list)))
    print("all symlink ("+str(len(symlink_list))+"):\n")

    for i in symlink_list:
        print(str(i))

# symlinks with errors
def msg_symlink_l_nok(symlink_l_nok):
    print("_____________________") 
    symlink_l_nok=sorted(list(dict.fromkeys(symlink_l_nok)))
    print("\nsymlink with error ("+str(len(symlink_l_nok))+"):\n")

    for i in symlink_l_nok:
        print(str(i))

#show all desktop files
def msg_all_desktop(all_files):
    print("_____________________")   
    print("\nall .desktop files from toolbox folder ("+str(len(all_files))+"):\n")

    for i in all_files:
        print(str(i))


#show all desktop files that needs to be altered
def msg_desktop(files_nok):
    print("_____________________")
    print("\ndesktop files changed ("+str(len(files_nok))+"):\n")

    for i in files_nok:
        print(str(i))
     

#show changes in each line
def msg_changes(line,new_line):
    if not new_line==line:
        print(line+" [old]")
        print(new_line+" [new]")


def msg_search_icon_svg(icon_name,icons_folder):
    print("\nSearching for icon \""+icon_name+"\" in: \n"+ icons_folder)
    print("\nSearching for svg file")


# show messages about icon
def msg_user_icon(icon, icons, string):
    print("\n"+string+ " found (" +str(len(icons))+") and its size:")
    print(icons)
    print("\nchosen icon (larger): ")
    print(str(icon)+"\n")

# _______________________________________________________________

# ---------------------------Functions---------------------------

# _______________________________________________________________
 
# get size of file
def file_size(fname):
    info = os.stat(fname)
    return float(info.st_size)


#create backup
def backup(desktopfile,backup_folder):

    if not Path(backup_folder).exists():
        os.makedirs(backup_folder)
    if not Path(backup_folder+"/"+desktopfile.name).exists():
        shutil.copy(desktopfile,backup_folder)
        msg_backup(backup_folder)


# Create links
def create_link(click,havetolink):        
    global symlink_l_nok
    symlink_l_nok=[]
    linksto=str(Path(click).resolve())

    try:
        os.symlink(havetolink, click)
        msg_link_created(click,havetolink)
        
    except:               
        if Path(click).is_symlink():
            if not Path(click).exists():
                os.remove(click)
                os.symlink(havetolink, click)
                msg__invalid_link(click,linksto,havetolink)
            elif havetolink==linksto:
                msg_link_ok(click,linksto)
            else:
                msg_link_nok(click,linksto,havetolink)
                symlink_l_nok.append(click)
        else:
            msg_file_nok(click)
            symlink_l_nok.append(click)

    #uncomment line below to show more info
    #msg_debug(click,linksto,havetolink) 



# Verify if desktop file is ok
def desktopfileok(desktopfile):
    global f
    with open(desktopfile,"r") as f:
        if "Exec=toolbox run" in f.read():
            f.close
            return True
                  


# getting icon path
def icon_path(usrshare,desktopfile,line):
    
    icons_folder=str(desktopfile.parent).replace("applications","icons")
    icons={}
    icon_name=line[len("Icon="):]

    #if no icon is specified, jump this step
    if icon_name=="":
        return line
   
    # Check if it's there a svg file (prefer)
    for icon in Path(icons_folder).glob('**/'+icon_name+'.*'):
        if str(icon).rsplit(".",1)[1]=="svg":
            return "Icon="+str(icon)
        elif str(icon).rsplit(".",1)[1]=="png":
            icons[icon]=file_size(icon)
        
    # if found, get the larger icon from the list
    if len(icons)>0:
        icon=max(icons, key=icons.get)
        msg_user_icon(icon,icons,"svg icons")
        return "Icon="+str(icon)
    
    else: 
        print("\nIcon not found. Try to edit the desktop file manually later")
        return line
# _______________________________________________________________

# ---------------------------Main code---------------------------

# _______________________________________________________________

all_files=[]
files_nok=[]
symlink_list=[]
symlink_l_nok=[]


msg_title()




#get ids of folders that contains desktop files
for o_id in os.listdir(c_overlay):
    for desktopfile in \
        Path(c_overlay+"/"+o_id+"/") \
            .glob(c_usrshare+"/applications/"+"*.desktop"):
        
        msg_title_symlink()
        all_files.append(desktopfile.name)

        #create links to folders
        create_link(usrshare+"/applications/toolbox_"+o_id[:4], \
            str(desktopfile).rsplit("/",1)[0])
        
        symlink_list.append(usrshare+"/applications/toolbox_"+o_id[:4])
        
        create_link(usrshare+"/icons/toolbox_"+o_id[:4], \
            str(desktopfile).rsplit("/",1)[0] \
            .replace("applications","icons"))

        symlink_list.append(usrshare+"/icons/toolbox_"+o_id[:4])

        #create bakup folder
        backup(desktopfile, 
            backups_folder+"/toolbox_"+o_id[:4]+"\n")
        
        msg_verifying_files()
        folder_name=str(desktopfile.parents[1])
        print("folder:\n"+folder_name)


        if desktopfileok(desktopfile)==True:
            print("\nfile ok:\n"+desktopfile.name)
        else:
            f=open(desktopfile,"r")
            files_nok.append(desktopfile.name)
           
            # _______________________________________________________________

            # Configure all lines desktop files in the list

            icons={}

            print("\nchanging file content:\n"+desktopfile.name+"\n")

            

            replaced_content = ""
            
            #looping through the file
            for line in f:

                line = line.strip()
                new_line=line

                # _______________________________________________________________

                # checking and changing line

                if line.startswith("Exec="):
                    new_line = line.replace("Exec=","Exec=toolbox run ")
                    msg_changes(line,new_line)
                        
                elif line.startswith("Name="):
                    new_line = line+" (container)"
                    msg_changes(line,new_line)
                        
                elif line.startswith("DBusActivatable=true"):
                    new_line = line.replace("DBusActivatable=true", "DBusActivatable=false")
                    msg_changes(line,new_line)

                elif  line.startswith("Icon="):
                    new_line=icon_path(usrshare,desktopfile,line)
                    msg_changes(line,new_line)
                
                replaced_content = replaced_content + new_line + "\n"

            f.close()
                       
            # _______________________________________________________________
            
            #save file
            with open(desktopfile,"w") as f:
                f.write(replaced_content)
                f.close()
            
            print("\n")
            

# _______________________________________________________________

# making themes avaliable to toolbox, since it has access to home folder


source = os.listdir("/usr/share/themes")
destination = os.environ['HOME']+"/.themes"
for files in source:
    shutil.copy(files,destination)


# show messages to user
msg_title_summary()
msg_symlink_list(symlink_list)
msg_symlink_l_nok(symlink_l_nok)
msg_all_desktop(all_files)
msg_desktop(files_nok)

#try to update apps in App Grid
sts = subprocess.Popen("update-desktop-database ~/.local/share/applications", shell=True).wait()

