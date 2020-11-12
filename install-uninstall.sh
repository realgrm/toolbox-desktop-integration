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



# manual input of folder
overlay-id = "d0ed434fec06789afb233cd607dee2572efe8f30bf816c7edddc9372b4bd668f"

# get toolbox id
toolbox-id = toolbox list | grep running | awk '{print $1}'

# create backup
mv "${HOME}/.local/share/containers/storage/overlay/${overlay-id}/diff/usr/share/applications" \
	"${HOME}/.local/share/containers/storage/overlay/${overlay-id}/diff/usr/share/applications-backup"

# create folder inside applications (host) to current toolbox
mkdir "${HOME}/.local/share/applications/toolbox-${toolbox-id}"

# create symbolic link
ln -s "${HOME}/.local/share/applications/toolbox-${toolbox-id}" \
	"${HOME}/.local/share/containers/storage/overlay/${overlay-id}/diff/usr/share/applications-backup"

# copy contents of the backup
cp 
