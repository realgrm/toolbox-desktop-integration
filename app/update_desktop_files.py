#!/usr/bin/env python3

import os
from pathlib import Path
import shutil
import subprocess
import sys

# _______________________________________________________________

# declare key variables

backup_folder=os.environ['HOME']+"/.local/share/applications_backup/"
usrshare=os.environ['HOME']+"/.local/share"
app_folder=os.environ['HOME']+"/.update_desktop_files"


# _______________________________________________________________

# defining functions

#Print title of the script
def msg_title():
    print("_____________________")
    print("\nUPDATE DESKTOP FILES SCRIPT")
    print("_____________________")
    print("")

#show application's folders  
def msg_apps_folder():
    print("applications folder: \n")
    for i in applink_toolbox:
        print(usrshare+"/"+"applications"+"/"+i)

#show icon's folders
def msg_icons_folder():
    print("\nicons_folder: \n")
    for i in applink_toolbox:
        print(usrshare+"/"+"icons"+"/"+i)

#show all desktop files
def msg_all_desktop():
    print("_____________________")
    print("\nall .desktop files in folder ("+str(len(all_files))+"):\n")

    for i in all_files:
        print(str(i))

#show all desktop files that needs to be altered
def msg_dektop():
    print("_____________________")
    print("\ndesktop files not ok ("+str(len(files))+"):\n")

    for i in files:
        print(str(i))

        print("\nLines changed:\n")
     
#show changes in each line
def print_changes(line,new_line):
    print(line+" [old]")
    print(new_line+" [new]")


# show messages about icon
def print_user_icon(icon, icons, string):
    print("\n"+string+ " found (" +str(len(icons))+") and its size:")
    print(icons)
    print("\nchosen icon (larger): ")
    print(str(icon)+"\n")

 
# get size of file
def file_size(fname):
    info = os.stat(fname)
    return float(info.st_size)

# _______________________________________________________________

# Main code

# _______________________________________________________________

# get all desktop files inside folders

all_files=[]
files=[]
applink_toolbox=[]


# create a list of folders inside "~/usr/share/applications" that contain "toolbox_" in their names
for i in os.listdir(usrshare+"/applications"):
    if "toolbox_" in i:
        applink_toolbox.append(i)

for id_trim in applink_toolbox:
        toolbox_apps_folder=usrshare+"/"+"applications"+"/"+id_trim 
        
        # filter the desktop apps and make a list
        for app in Path(toolbox_apps_folder).glob('*.desktop'):
            all_files.append(app)

            #check those that doesn't run in toolbox
            with open(app,"r") as f:
                if "Exec=toolbox run" not in f.read():

                    #list of .desktop files that dont contain "toolbox run"
                    files.append(app)
                    
            f.close


# _______________________________________________________________

#show info to user

msg_title()
msg_apps_folder()
msg_icons_folder()
msg_all_desktop()
msg_dektop()

# _______________________________________________________________

# Configure all desktop files in the list

icons={}



for f in files:
    print(str(f))

    #get folder name

    folder_name=str(f)[:str(f).rindex("/")]
    folder_name=folder_name[folder_name.rindex("/"):]


    #open file in read mode
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
            new_line = line.replace("Exec=","Exec=toolbox run ")
            print_changes(line,new_line)
                
        elif line.startswith("Name="):
            new_line = line+" (container)"
            print_changes(line,new_line)
                
        elif line.startswith("DBusActivatable=true"):
            new_line = line.replace("DBusActivatable=true", "DBusActivatable=false")
            print_changes(line,new_line)

        # _______________________________________________________________
        
        # GETTING ICON PATH


        # checking and changing line: getting icon
        elif  line.startswith("Icon="):
            


            #remove file name
            icons_folder=usrshare+"/icons"+folder_name
            
            #get the name of icon
            icon_name=line[len("Icon="):]
     
            # _______________________________________________________________

            #searching for a svg version of the icon

            print("\nSearching for icon \""+icon_name+"\" in: \n"+ icons_folder)
            print("\nSearching for svg file")            
            
            #if no icon is specified, jump this step
            if icon_name=="": next

            icons={}
            
            # Check if it's there a svg file (prefer)
            for app in Path(icons_folder).glob('**/*'+icon_name+'.svg'):
                icons[app]=file_size(app)
                
      

            # if found, get the larger icon from the list
            if len(icons)>0:
                icon=max(icons, key=icons.get)
                print_user_icon(icon,icons,"svg icons")
                new_line = "Icon="+str(icon)
                
            # _______________________________________________________________

            #searching for other formats of icon, if svg not found
               
            else:
                
                print("svg not found. Searching all matching filename instead")
                
                for app in Path(icons_folder).glob('**/*'+icon_name+'*'):
                    icons[app]=file_size(app)

                # if found, get the larger icon from the list
                if len(icons)>0:
                    icon=max(icons, key=icons.get)
                    print_user_icon(icon,icons,"all files")
                    new_line = "Icon="+str(icon)
                
                else: print("Icon not found. Try to edit the desktop file manually later")
        # _______________________________________________________________

        #concatenate the new string and add an end-line break
        replaced_content = replaced_content + new_line + "\n"
    


    #close the file
    fileHandler.close()

    #create a backup
    backup_folder=app_folder+"/applications_backup"+folder_name
    shutil.copy(str(f),backup_folder)
    print("\nbackup of file created in:\n"+backup_folder+"\n")
    
    #Open file in write mode
    write_file = open(f, "w")

    #overwriting the old file contents with the new/replaced content
    write_file.write(replaced_content)

    #close the file
    write_file.close()
    print("\n")

#update app shortcuts in app grid
sts = subprocess.Popen("update-desktop-database" + " ~/.local/share/applications", shell=True).wait()

#sys.exit("teste")
