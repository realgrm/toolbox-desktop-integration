# podman-desktop-file-copy-to-user

### !! UNDER CONSTRUCTION !!

## Summary
[Preface](podman-desktop-file-copy-to-user/README.md#Preface)  
[Goal](podman-desktop-file-copy-to-user/README.md#Goal)  
[Manual Process](podman-desktop-file-copy-to-user/README.md#Manual Process)  
[Results](podman-desktop-file-copy-to-user/README.md#Results)  
[Installation](podman-desktop-file-copy-to-user/README.md#Installation)  



## Preface

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

## Goal
This is a project that aims to create a script that automates the creation of a shortcut (desktop file) on the real machine whenever a new program is installed on Fedora Silverblue through the toolbox (podman).  
The manual process below will be used as the basis.

## Manual Process

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

 ## Results
 
Activities Overview: App is running and the system adds "(on toolbox)" in the title   
![image](https://user-images.githubusercontent.com/23300290/98615310-0ca01f00-22d9-11eb-853a-f9b45b307b42.png)

Show Applications: App icon in Dash indicates that it is running, however in the App Grid there is no indicator below the icon  
![image](https://user-images.githubusercontent.com/23300290/98615618-d616d400-22d9-11eb-8fce-3e3d3c09ffaa.png)

# Installation

The first 

