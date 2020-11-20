#!/usr/bin/env python3

from pathlib import Path
import os
import subprocess
import sys

# _______________________________________________________________

# declaring some inicial variables

app_folder=os.environ['HOME']+"/.update_desktop_files"
c_overlay=os.environ['HOME']+"/.local/share/containers/storage/overlay"

# _______________________________________________________________

# -----------------------Auxiliar functions---------------------

# _______________________________________________________________

def msg_show_title():
    print("_____________________")
    print("_____________________")
    print("\nINSTALL DESKTOP FILES SCRIPT")
    print("_____________________")
    print("_____________________")    

def msg_container_nok():
    print("\nContainer not found.\nCreate one with the command \"toolbox create\" in the terminal")

# _______________________________________________________________

# ---------------------------Main code---------------------------

# _______________________________________________________________
msg_show_title()

#check if a container is created
if not Path(c_overlay).is_dir():
    sys.exit(msg_container_nok())

# create a shortcut in app grip for update desktop files
desktop_localshare=os.environ['HOME']+"/.local/share/applications/update_desktop_files.desktop"

desktop_appfolder=app_folder+"/update_desktop_files.desktop"
fileHandler = open(desktop_appfolder, "r")
replaced_content = ""

# _______________________________________________________________

# adapt file to the user directory
for line in fileHandler:

    line = line.strip()
    new_line=line

    # _______________________________________________________________

    if line.startswith("Exec="):
        if "bash" in line: break
        else:
            new_line = line.replace("Exec=","Exec=bash -c 'cd "+app_folder)
                      
    elif line.startswith("Icon="):
        new_line = line.replace("Icon=", "Icon="+app_folder+"/")

    replaced_content = replaced_content + new_line + "\n"


fileHandler.close()

#copy desktop file in .local/share 
sts = subprocess.Popen("cp" + " -n '"+desktop_appfolder+"' '"+desktop_localshare+"'", shell=True).wait()

#update the adapted version in .local/share
write_file = open(desktop_localshare, "w")
write_file.write(replaced_content)
write_file.close()
print("\n")


print("desktop file placed in: \n"+desktop_localshare)
print("\n")


# _______________________________________________________________

# start the main script
import update_desktop_files
