# podman-desktop-file-copy-to-user

## Summary
[Preface](./README.md#Preface)  
[Goal](./README.md#Goal)  
[Manual Process](./README.md#Manual-Process)  
[Results](./README.md#Results)  
[How it works](./README.md#How-it-works)  
[Installation](./README.md#Installation)  
[Usage](./README.md#Usage)  

# Preface

Currently, to install something in Silverblue, the main options are (with its main drawbacks):
- rpm-ostree  
It have to reboot to login with the image that contains the new installed packages
- flatpak  
Many apps are not ported to this format yet
- inside podman container trough toolbox  
Is design to install CLI programs and not GUI programs. So when a GUI app is installed, it is not fully integrated to the system. For example, ther's no app shortcut in the App Grip. In other words, the desktop file is not present in the correct location to be visible.

So this page shows the manual steps taken to minimally integrate this desktop file with Silverblue.  
And aims to create some way of doing it automatically.  
The manual steps were tested with a few different apps, and in all of them, only one toolbox was created.

All the drawbacks listed are my opinion, based on my current use of Silverblue. 

# Goal
This is a project that aims to create a script that automates the creation of a shortcut (desktop file) on the real machine whenever a new program is installed on Fedora Silverblue through the toolbox (podman).  
The manual process below will be used as the basis.

# Manual Process

- Made a copy of the desktop file and icon to the home folder:

| Description 	| Copy (container) 	| Paste (Silverblue) 	|
|-	|-	|-	|
| Desktop File Location 	| ~/.local/share/containers/storage/overlay/{overlay-id}/diff/usr/share/applications/blender.desktop 	| ~/.local/share/applications/toolbox-blender.desktop 	|
| Icon File Location 	| ~/.local/share/containers/storage/overlay/{overlay-id}/diff/usr/share/icons/hicolor/scalable/apps/blender.svg 	| /home/realgrm/.local/share/icons/hicolor/scalable/apps/toolbox/blender.svg 	|

Replace {overlay-id} with the folder created to your container. Mine was "d0ed434fec06789afb233cd607dee2572efe8f30bf816c7edddc9372b4bd668f" folder.  
I discover the correct folder by installing an app and searching for the app's desktop file inside ~/.local/share/containers/storage/overlay/  

- Edited the content of ~/.local/share/applications/toolbox-blender.desktop:

| Description 	| Before (container) 	| After (Silverblue) 	|
|-	|-	|-	|
| Name Line 	| Name=Blender 	| Name=Blender (container) 	|
| Exec Line 	| Exec=blender% f 	| Exec=toolbox run blender% f 	|

 # Results
 
Activities Overview: App is running and the system adds "(on toolbox)" in the title   
![image](https://user-images.githubusercontent.com/23300290/98615310-0ca01f00-22d9-11eb-853a-f9b45b307b42.png)

Show Applications: App icon in Dash indicates that it is running, however in the App Grid there is no indicator below the icon  
![image](https://user-images.githubusercontent.com/23300290/98615618-d616d400-22d9-11eb-8fce-3e3d3c09ffaa.png)

Menu Editor: The app shortcut is now visible to menu editors, such as Menulibre

# How it works
script install.py
- Checks if a container is created. If it is:
>- Create a desktop file to trigger the update_desktop_files.py script
>- run the script update_desktop_files.py


script update_desktop_files.py

- Search for ".desktop" files inside specific folders
>- Get overlay_id of these folders
>- Create a backup folder inside the app's folder
>>- Create link in ~/.local/share/applications
>>- Create link in ~/.local/share/icons
>>- Verify if the desktop file is already modified
>>>- get icon path for the unmodified ones
>>>- create a backup of original desktop file
>>>- save modified content
>>>>- Try to update app grid

# Installation
### Option 1: With one set of commands

```
mkdir -p ~/.update_desktop_files/
cd ~/.update_desktop_files/
wget https://raw.githubusercontent.com/realgrm/podman-desktop-file-copy-to-user/main/app/install.py
wget https://raw.githubusercontent.com/realgrm/podman-desktop-file-copy-to-user/main/app/update_desktop_files.py
wget https://raw.githubusercontent.com/realgrm/podman-desktop-file-copy-to-user/main/app/update_desktop_files.png
wget https://raw.githubusercontent.com/realgrm/podman-desktop-file-copy-to-user/main/app/update_desktop_files.desktop
chmod +x ~/.update_desktop_files/install.py
chmod +x ~/.update_desktop_files/update_desktop_files.py
~/.update_desktop_files/install.py
```
### Option 2: Step by step

- Create the folder ~/.update_desktop_files
>- Using terminal 
`mkdir ~/.update_desktop_files`
- Download the files
>- install.py
>- update_desktop_files.py
>- update_desktop_files.png
>- update_desktop_files.desktop  
  
Thanks to "[DownGit by Minhas Kamal](https://minhaskamal.github.io/DownGit/#/home) you can click ![here](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/realgrm/podman-desktop-file-copy-to-user/tree/main/app) to download  
- Paste all files of the app folder in ~/.update_desktop_files
![app_folder](https://user-images.githubusercontent.com/23300290/99392225-2255ab80-28ba-11eb-9615-89a62f13c0ed.png)
- Give execution permission to the scripts  
`chmod +x ~/.update_desktop_files/install.py`  
`chmod +x ~/.update_desktop_files/update_desktop_files.py`
- Run install.py from created folder
>- Using terminal `~/.update_desktop_files/install.py`

# Usage

When the install.py is executed:
- automatically the script update_desktop_files/install.py is also executed, so your GUI apps installed from toolbox should appear ins the app grid (may takes a few seconds to update the icon in the app grid)
- it creates an shortcut in AppGrid called Update Desktop Files, that can run the script update_desktop_files.py
![image](https://user-images.githubusercontent.com/23300290/99393880-c2accf80-28bc-11eb-8815-8b063d499fb7.png)

So every time you install a GUI app inside a toolbox, run the Update Desktop Files.

