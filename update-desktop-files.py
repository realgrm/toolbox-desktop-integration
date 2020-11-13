#!/usr/bin/env python3
import os
from pathlib import Path

folder=os.environ['HOME']+'/Documents/Test'
icon_folder=os.environ['HOME']+"/.local/share/applications/toolbox"
files=[]


#get all .dektop files in (sub)folders
for file_path in Path(folder).glob('**/*.desktop'):
    #check those that doesn't run in toolbox
    with open(file_path,"r") as f:
        if "Exec=toolbox run" not in f.read():
            #list of .desktop files that dont contain "toolbox run"
            files.append(file_path)
    f.close

# Configure all desktop files in the list
for file in files:
    #open file in read mode
    fileHandler = open(file, "r")
    replaced_content = ""


    #looping through the file
    for line in fileHandler:
        
        #stripping line break
        line = line.strip()
        print(line)
        #checking string and replacing
        if line.startswith("Exec="):
            new_line = line.replace("Exec=", "Exec=toolbox run ")
        elif line.startswith("Name="):
            new_line = line+" (container)"
        elif line.startswith("Icon="):
            new_line = line.replace("Icon=", "Icon="+icon_folder)+".svg"
        else: 
            new_line = line.replace("DBusActivatable=true", "DBusActivatable=false")
        #concatenate the new string and add an end-line break
        replaced_content = replaced_content + new_line + "\n"
        
    #close the file
    fileHandler.close()

    #Open file in write mode
    write_file = open(file, "w")
    #overwriting the old file contents with the new/replaced content
    write_file.write(replaced_content)
    #close the file
    write_file.close()
