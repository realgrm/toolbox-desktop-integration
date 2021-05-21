#!/bin/bash

DESKTOPFILE="podman_di.desktop"
DESKTOPFOLDER="$HOME/.local/share/applications/"
ICONFILE="podman_di.png"
ICONFOLDER="$HOME/.local/share/icons/hicolor/1024x1024/apps"
UPDATEFILE="podman_di_update.sh"
UPDATEFOLDER="$HOME/.local/bin"
THISFOLDER=$(dirname $(realpath $0))

cp -f $THISFOLDER/$UPDATEFILE $UPDATEFOLDER/

[[ $PATH != *$UPDATEFOLDER* ]] && \
	PATH=$UPDATEFOLDER:$PATH

chmod +x $UPDATEFOLDER/$UPDATEFILE

cp -f $THISFOLDER/$DESKTOPFILE $DESKTOPFOLDER

sed -i "s/^Exec=/Exec=$UPDATEFILE/" $DESKTOPFOLDER

mkdir -p $ICONFOLDER

cp -f $THISFOLDER/$ICONFILE $ICONFOLDER


$UPDATEFILE
