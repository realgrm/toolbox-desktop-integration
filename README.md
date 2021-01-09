# toolbox-desktop-integration

# Summary
[Preface](./README.md#Preface)  
[Goal](./README.md#Goal)  
[Using with podman](./README.md#Using-with-podman)  
[Results](./README.md#Results)  
[How it works](./README.md#How-it-works)  
[Installation](./README.md#Installation)  
[Usage](./README.md#Usage)  
[Manual Process](./README.md#Manual-Process) 

[![toolbox-desktop-integration_gif](https://user-images.githubusercontent.com/23300290/99897700-9d341300-2c7a-11eb-8a08-34718dc26734.gif)](https://youtu.be/dKwHdcPl0cE)

# Preface

Currently, to install something in Silverblue, the main options are (with its main drawbacks):
- rpm-ostree  
It have to reboot to login with the image that contains the new installed packages
- flatpak  
Many apps are not ported to this format yet
- inside podman container trough toolbox  
Is design to install CLI programs and not GUI programs. So when a GUI app is installed, it is not fully integrated to the system. For example:
    - there's no app shortcut in the App Grip. In other words, the desktop file is not present in the correct location to be visible
    - if you use a different theme from the default, it is ignored

All the drawbacks listed are my opinion, based on my current use of Silverblue. 

# Goal
This project aims to integrate the toolboxes installed with the desktop, by:
- making avaliable to the host, shortcuts of GUI applications installed inside all toolbox containers
- making these apps run with applied theme by default

# Using with podman

Although this was created with toolbox in mind, it was tested with some toolboxes created with podman and it worked the same way.


 # Results
 
Activities Overview: App is running and the system adds "(on toolbox)" in the title   
![image](https://user-images.githubusercontent.com/23300290/98615310-0ca01f00-22d9-11eb-853a-f9b45b307b42.png)

Show Applications: App icon in Dash indicates that it is running, however in the App Grid there is no indicator below the icon  
![image](https://user-images.githubusercontent.com/23300290/98615618-d616d400-22d9-11eb-8fce-3e3d3c09ffaa.png)

Menu Editor: The app shortcut is now visible to menu editors, such as Menulibre

# How it works
script `install.py`
- Checks if a container is created. If it is:
- Create a desktop file to trigger the `toolbox-desktop-integration.py` script
- run the script `toolbox-desktop-integration.py`


script `toolbox-desktop-integration.py`

- Search for ".desktop" files inside specific folders
  - Get overlay_id of these folders
  - Create a backup folder inside the app's folder
    - Create link in `~/.local/share/applications`
    - Create link in `~/.local/share/icons`
    - Verify if the desktop file is already modified
      - get icon path for the unmodified ones
      - create a backup of original desktop file
      - save modified content
- Copy themes from `/usr/share/themes` to `~/.themes`, where is visible to all toolboxes
- Update app grid

# Installation

To install you can copy and paste this in your terminal:

```
# declaring constants
app_folder="~/.local/scripts/toolbox-desktop-integration/"
github_applink="https://raw.githubusercontent.com/realgrm/toolbox-desktop-integration/main/app/"

# creating folder where the app will be installed
mkdir -p $app_folder
cd $app_folder

# downloading the files
wget ${github_applink}install.py
wget ${github_applink}toolbox-desktop-integration.py
wget ${github_applink}toolbox-desktop-integration.png
wget ${github_applink}toolbox-desktop-integration.desktop

# making files executable
chmod +x $app/install.py
chmod +x ${app_folder}toolbox-desktop-integration.py

# runing the installation script
${app_folder}install.py
```
# Usage

When the `install.py` is executed:
- automatically the script `toolbox-desktop-integration.py` is also executed, so your GUI apps installed from toolbox should appear ins the app grid (may takes a few seconds to update the icon in the app grid)
- it creates an shortcut in AppGrid called Update toolbox, that can run the script `toolbox-desktop-integration.py` again.
![image](https://user-images.githubusercontent.com/23300290/99393880-c2accf80-28bc-11eb-8815-8b063d499fb7.png)

So every time you install a GUI app inside a toolbox, you can use this shortcut.

# Manual Process

The manual process below was used as the basis to the creation of these scripts. And is avaliable here if someone wishes to do the work manually instead of using scripts.

- Made a copy of the desktop file and icon to the home folder:

| Description 	| Copy (container) 	| Paste (Silverblue) 	|
|-	|-	|-	|
| Desktop File Location 	| `~/.local/share/containers/storage/overlay/{overlay-id}/diff/usr/share/applications/blender.desktop` 	| `~/.local/share/applications/toolbox-blender.desktop` 	|
| Icon File Location 	| `~/.local/share/containers/storage/overlay/{overlay-id}/diff/usr/share/icons/hicolor/scalable/apps/blender.svg` 	| `/home/realgrm/.local/share/icons/hicolor/scalable/apps/toolbox/blender.svg` 	|

Replace {overlay-id} with the folder created to your container. Mine was "d0ed434fec06789afb233cd607dee2572efe8f30bf816c7edddc9372b4bd668f" folder.  
I discover the correct folder by installing an app and searching for the app's desktop file inside `~/.local/share/containers/storage/overlay/`  

- Edited the content of ~/.local/share/applications/toolbox-blender.desktop:

| Description 	| Before (container) 	| After (Silverblue) 	|
|-	|-	|-	|
| Name Line 	| Name=Blender 	| Name=Blender (container) 	|
| Exec Line 	| Exec=blender% f 	| Exec=toolbox run blender% f 	|


