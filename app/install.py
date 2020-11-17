#!/usr/bin/env python3

from pathlib import Path
import os
import subprocess
import sys

# _______________________________________________________________

# declare variables
usrshare_toolbox=os.environ['HOME']+"/.local/share/folder/toolbox"
c_usrshare=""
c_overlay=os.environ['HOME']+"/.local/share/containers/storage/overlay"
c_usrshare_sufix="/diff/usr/share"
app_folder=os.environ['HOME']+"/.update_desktop_files"

# _______________________________________________________________

# defining functions

# to show informations to the user

def msg_show_title():
    print("\n\n_____________________")
    print("\nINSTALL DESKTOP FILES SCRIPT")
    print("_____________________\n")

def msg_link_created():
    print("created symlink:\n"+click+"\n\nthat redirects to:\n"+havetolink+"\n")

def msg_link_ok():
    print("all ok, symlink already exists:\n"+click+"\n\nit redirects to:\n"+linksto+"\n")

def msg_link_nok():
    print("can't create symlink, because another symlink already exists:\n"+click+"\n\nit redirects to:\n"+linksto+"\nit shoud be:\n"+havetolink+"\n")

def msg_file_nok():
    print("can't create symlink, because file/folder already exists\n"+click+"\n\nplease delete (with backup?) or rename it, then try again.")

def msg_container_nok():
    print("Container not found.\nCreate one with the command \"toolbox create\" in the terminal")

# to show debug info

def msg_debug():
    print("debug locations:")
    print("where do i click (exists: "+str(Path(click).exists())+" is symlink: "+str(Path(click).is_symlink())+")\n"+click)
    print("have to link:\n"+havetolink)
    print("currently links to:\n"+linksto)
    print("click=link"+str(click==linksto))
    print("link ok: "+str(havetolink==linksto))

# _______________________________________________________________

#Main code

# _______________________________________________________________

#show info to user

msg_show_title()

# _______________________________________________________________

# create folders if not exist

ids=[]

if not Path(c_overlay).is_dir():
    sys.exit(msg_container_nok())


for overlay_id in os.listdir(c_overlay):

    if not Path(c_overlay+"/"+overlay_id).is_dir() or len(overlay_id)<4:
        print("is not a valid folder:\n"+c_overlay+"/"+overlay_id+"\n")
        next
    
    else:

        ids.append(overlay_id)

        a=[c_overlay+"/"+overlay_id+c_usrshare_sufix+"/applications", \
        c_overlay+"/"+overlay_id+c_usrshare_sufix+"/icons", \
        app_folder+"/applications_backup/toolbox_"+overlay_id[:4]]
        
        for i in a:
            try: 
                if not os.path.exists(i):                
                	os.makedirs(i)
                	print("folder created: \n"+i+"\n")
                else: 
                	print("Folder alreay exists: \n"+i+"\n")
                	
            except FileExistsError:
                print("directory already exists:\n"+i+"\n")
            
# _______________________________________________________________



# Create links if not exist

a=["applications", "icons"]



for i in a:
    print("\n"+"_____________________\n")
    print(i+"\n")

    for overlay_id in ids:

        id_trim=overlay_id[:4]
    
        click=usrshare_toolbox.replace("folder",i)+"_"+id_trim   
        havetolink=c_overlay+"/"+overlay_id+c_usrshare_sufix+"/"+i
        linksto=str(Path(click).resolve())

        
        #msg_debug #uncomment this line to show more info

        try:
            os.symlink(havetolink, click)
            msg_link_created()
            
        except:
            if Path(click).is_symlink():
                if havetolink==linksto:
                    msg_link_ok()
                else: msg_link_nok()
            else: msg_file_nok()


# _______________________________________________________________


# create a shortcut in app grip for update desktop files
print("\n"+"_____________________\n")

desktop_localshare=os.environ['HOME']+"/.local/share/applications/update_desktop_files.desktop"

desktop_appfolder=app_folder+"/update_desktop_files.desktop"
fileHandler = open(desktop_appfolder, "r")
replaced_content = ""

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

#try to update apps in App Grid
sts = subprocess.Popen("update-desktop-database" + " ~/.local/share/applications", shell=True).wait()

# _______________________________________________________________
# start another script
import update_desktop_files
