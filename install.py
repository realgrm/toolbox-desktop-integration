#!/usr/bin/env python3

from pathlib import Path
import os

# _______________________________________________________________

# declare variables
link_app = os.environ['HOME']+"/.local/share/applications/toolbox"
link_icon = os.environ['HOME']+"/.local/share/icons/toolbox"
l=os.environ['HOME']+"/.local/share/folder/toolbox/"
overlay_id=""
c=os.environ['HOME']+"/.local/share/containers/storage/overlay/"

# _______________________________________________________________

# get the correct folder to the container

os.system("/usr/bin/toolbox run")

for d in os.listdir(c):
    if Path(c+d+"/diff/run/.containerenv").is_file():
        overlay_id=c+d+"/diff/usr/share/"
    else: pass

# _______________________________________________________________

# Check if links already exists, if not, create them

a=["applications","icons"]

for i in a:
    print("\n\n"+i+"\n")
    scr=l.replace("folder",i)   
    dst=overlay_id+i+"/"
    if str(Path(scr).resolve())==scr:
        print("created symlink:\n"+scr+"\n"+dst)
        os.symlink(scr, dst)
    else: print("symlink already exists:\n"+scr+"\n"+str(Path(scr).resolve()))

#Applications
# create link in usr/share
#os.symlink(src, dst)
#os.symlink(src, dst)
# create backup
