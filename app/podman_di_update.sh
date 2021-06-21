#!/bin/bash

# constants: formats
f1="\e[1;34m" #format level 1
f2="\e[1;94m" #format level 2
fe="\e[0;31m" #format error
fs="\e[0;34m" #format success
rf="\e[0m" #reset format


# _______________________________________________________________

# ----------------------Functions: Messages----------------------

# _______________________________________________________________


msg_linkcreated(){
	printf "%b\n" \
		"Created symlink:" "$2" "$1"; }


# _______________________________________________________________

# ---------------------------Functions---------------------------

# _______________________________________________________________

createsymlink(){ #variables:target(path),link name(path)

	if [ -d $1 ]; then
		ln -sf $1 $2 && \
		msg_linkcreated $1 $2 && \
		link=true
	else
		printf "%b\n" "Symlink not created: directory don't exist" "$1"

	fi
}

iconpathfinder(){ #variables:container name,icon name
	local svg=$(find -L $USERHOME/.local/share/icons/$1 -regex ".*$2.svg$")
	local png=$(find -L $USERHOME/.local/share/icons/$1 -regex ".*$2.png$")

	if [ svg != "" ]
		then icon_path= $svg
		else icon_path= $png
	fi
}

editdesktopfile() { #variables:container name, desktop file
if ! grep -q "^Exec=podman start" "$2" && \
	 ! grep -q "^Hidden=true" "$2" && \
	 ! grep -q "^NoDisplay=true" "$2"

then
	local backupfolder=$(dirname $2)/backup
	local desktopfile="${2##*/}"

	mkdir -p $backupfolder 2>0
	cp --backup=numbered $2 $backupfolder/$desktopfile.backup

	appicon=$(grep -oP "^Icon=\K.*" $2)
	iconpathfinder $1 $appicon

	sed -i "/^Name=/s/$/ (podman)/; \
		s%^Icon=%Icon=$icon_path%g; \
		s/^Exec=/Exec=podman start $1 && podman exec -it $1 /g; \
		s/^DBusActivatable=true/DBusActivatable=false/g" \
		$2

	if grep -q "Keywords=" $2
        then sed -i "/^Keywords=/s/$/$1;/" $2
        else sed -i "s/^Exec=/Keywords=$1;\nExec=/" $2
        fi

	echo $2
fi
}

# _______________________________________________________________

# --------------------------Main code----------------------------

# _______________________________________________________________

$USERHOME=$HOME
sudo su

find $USERHOME/.local/share/applications/ -type l -name podman-\* -exec rm {} \;
find $USERHOME/.local/share/icons/ -type l -name podman-\* -exec rm {} \;
find $USERHOME/.local/share/themes/ -type l -name podman-\* -exec rm {} \;

containerlist=($(podman container list --all | \
	awk '{print $NF}' | \
	sed 1d))


for container in ${containerlist[@]}; do

	printf "\n\n\n${f1}########## container: ${container} ##########${rf}\n\n"

	UpperDir=($(podman container inspect ${container} | \
		grep UpperDir))

	UpperDir=$(sed -e \
		"s/\"//g; \
		 s/,//g" <<< ${UpperDir[1]})

	printf "container directory:\n$UpperDir"

	printf "\n\n${f2}##### applications link #####${rf}\n\n"
	createsymlink \
		$UpperDir/usr/share/applications \
		$USERHOME/.local/share/applications/podman-$container


	printf "\n\n${f2}##### icons link #####${rf}\n\n"
	createsymlink \
		$UpperDir/usr/share/icons \
		$USERHOME/.local/share/icons/podman-$container

	printf "\n\n${f2}##### editing desktop file #####${rf}\n\n"
	printf "\nEdited desktop files:\n"


	if [ -L $USERHOME/.local/share/applications/podman-$container ]
	then
		apps=$(find -L \
			$USERHOME/.local/share/applications/podman-$container \
			-regex ".*.desktop$")

		for app in ${apps[@]}; do
			editdesktopfile $container $app
		done
	else
		echo "Skipped"
	fi
done

printf "\n\n${f2}##### Themes #####${rf}\n\n"
printf "\nSymlinks created:\n\n"

usrthemes=$(find /usr/share/themes/ -maxdepth 1 -mindepth 1 -type d)

	mkdir -p "$USERHOME/.local/share/themes/"

	for theme in ${usrthemes[@]}; do
		themename="${theme##*/}"
		ln -s $theme $USERHOME/.local/share/themes/podman-$themename
		printf "%b\n" "$theme"  \
			"$USERHOME/.local/share/themes/podman-$themename\n"
	done

update-desktop-database $USERHOME/.local/share/applications

printf "\n\n${f2}############### End ###############${rf}\n\n"
