#!/usr/bin/env python3

import os
from pathlib import Path
import shutil

# _______________________________________________________________

# declare variables
applications_folder=os.environ['HOME']+'/.local/share/applications/toolbox/'
icons_folder=os.environ['HOME']+".local/share/icons/toolbox/"
icons={}
all_files=[]
files=[]

# _______________________________________________________________

# defining functions


def print_changes(line,new_line):
    print(line+" [old]")
    print(new_line+" [new]")


# print messages about icon
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

# get all desktop files of the folder

# to get subfolders: glob('**/*.desktop'). But this will override the backup
for file_path in Path(applications_folder).glob('*.desktop'):
    all_files.append(file_path)

    #check those that doesn't run in toolbox
    with open(file_path,"r") as f:
        if "Exec=toolbox run" not in f.read():

            #list of .desktop files that dont contain "toolbox run"
            files.append(file_path)
            
    f.close


# _______________________________________________________________

# Print info to user
print("_____________________")
print("\nUPDATE DESKTOP FILES SCRIPT")
print("_____________________")
print("\n")
print("applications_folder: "+applications_folder)
print("icons_folder: "+icons_folder+"\n")
print("_____________________")
print("\nall .desktop files in folder ("+str(len(all_files))+"):\n")

i=""
for i in all_files:
    print(str(i))


print("_____________________")
print("\ndesktop files not ok ("+str(len(files))+"):\n")

i=""
for i in files:
    print(str(i))

    print("\nLines changed:\n")

# _______________________________________________________________

# Configure all desktop files in the list
for file in files:
    print(str(file))

        #open file in read mode
    fileHandler = open(file, "r")
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

        # checking and changing line: getting icon
        elif  line.startswith("Icon="):
            icon_name=line[len("Icon="):]
            print("\nSearching for svg images inside folder: \n"+ icons_folder)

            # Check if it's there a svg file (prefer)
            for file_path in Path(icons_folder).glob('**/*'+icon_name+'.svg'):
                icons[file_path]=file_size(file_path)

            # if found, get the larger icon from the list
            if len(icons)>0:
                icon=max(icons, key=icons.get)
                print_user_icon(icon,icons,"svg icons")
                new_line = "Icon="+str(icon)
                
                
            # if not found, try to look for all files matching the name in the parent folder
            else:
                
                print("\nIcon not found. Searching all matching filename inside folder: \n"+icons_folder)
                
                for file_path in Path(icons_folder).glob('**/*'+icon_name+'*'):
                    icons[file_path]=file_size(file_path)

                # if found, get the larger icon from the list
                if len(icons)>0:
                    icon=max(icons, key=icons.get)
                    print_user_icon(icon,icons,"all files")
                    new_line = "Icon="+str(icon)

                
                else: print("\nIcon not found. Try to edit the desktop file manually later")
        # _______________________________________________________________

        #concatenate the new string and add an end-line break
        replaced_content = replaced_content + new_line + "\n"
        
    #close the file
    fileHandler.close()

    #create a backup
    shutil.copy2(str(file),str(file).replace("/toolbox/","/toolbox/backup/")+".backup") 

    #Open file in write mode
    write_file = open(file, "w")

    #overwriting the old file contents with the new/replaced content
    write_file.write(replaced_content)

    #close the file
    write_file.close()
    print("\n")

os.system("update-desktop-database ~/.local/share/applications")
