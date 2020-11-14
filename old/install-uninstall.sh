# -----Install-----

# Create folder and copy scripts
mkdir ~/.podman-desktop-file-copy-to-user
cp file1 ~/.podman-desktop-file-copy-to-user
cp file2 ~/.podman-desktop-file-copy-to-user

# Make aliases to run scripts
alias script-install-app "sudo dnf install" 
alias script-remove-app 
alias script-remove-script 

# -----Uninstall-----

# Remove folder created folder

# Remove created aliases



#!/bin/bash

# manual input of folder
overlay_id="d0ed434fec06789afb233cd607dee2572efe8f30bf816c7edddc9372b4bd668f"

# get toolbox id
toolbox_id=$(toolbox list | grep running | awk '{print $1}')

echo "$toolbox_id"
echo "$overlay_id"
test="${HOME}/.local/share/applications/toolbox-${toolbox_id}"

# create backup
mv "${HOME}/.local/share/containers/storage/overlay/${overlay_id}/diff/usr/share/applications" \
"${HOME}/.local/share/containers/storage/overlay/${overlay_id}/diff/usr/share/applications-backup"

# create folder inside applications (host) to current toolbox
mkdir "${HOME}/.local/share/applications/toolbox-${toolbox_id}"

# create symbolic link
ln -s "${HOME}/.local/share/applications/toolbox-${toolbox_id}" \
"${HOME}/.local/share/containers/storage/overlay/${overlay_id}/diff/usr/share/applications"

# copy contents of the backup
cp "${HOME}/.local/share/containers/storage/overlay/${overlay_id}/diff/usr/share/applications-backup/." \
"${HOME}/.local/share/applications/toolbox-${toolbox_id}"

alias install 
