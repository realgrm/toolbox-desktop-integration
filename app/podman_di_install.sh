#!/bin/bash

DESKTOPFILE="podman_di.desktop"
UPDATEFILE="podman_di_update.sh"
UPDATEFOLDER="$HOME/.local/bin"

cp -f $(dirname $(realpath $0))/$UPDATEFILE \
	$UPDATEFOLDER/

[[ $PATH != *$UPDATEFOLDER* ]] && \
	PATH=$UPDATEFOLDER:$PATH

chmod +x $UPDATEFOLDER/$UPDATEFILE

cp -f $(dirname $(realpath $0))/$DESKTOPFILE \
	$HOME/.local/share/applications/

sed -i "s/^Exec=/Exec=$UPDATEFILE/" \
	$HOME/.local/share/applications/

$UPDATEFILE
