#!/usr/bin/bash

if [ $1 == "-r" ]; then
    printf "Are you sure you would like to remove theharvester-gui? [y/n]:"
    read areYouSure
    
    if [ $areYouSure != "y" ] && [ $areYouSure != "Y" ]; then
        echo "Okay, Exiting."
        exit 1
    fi
    
    rm -r "$2/usr/share/theHarvester-gui/"
    rm -r "$2/usr/bin/theharvestergui"
    
    exit 1
fi

printf "Are you sure you would like install theharvester-gui? [y/n]:"
read areYouSure

if [ $areYouSure != "y" ] && [ $areYouSure != "Y" ]; then
    echo "Okay, exiting."
    exit 1
fi

if [ ! -f "theharvestergui" ] || [ ! -d "gui_" ] || [ ! -d "tools_" ]; then
    echo "Some of the required files are missing. Are you sure you're in theharvester-gui directory?"
    exit 1
fi

echo "Starting install..."

echo "Creating necessary directories."
mkdir -p "$1/usr/bin"
mkdir -p "$1/usr/share/theHarvester-gui"

echo "Moving files to the proper place."
cp -r "tools_" "$1/usr/share/theHarvester-gui/"
cp -r "gui_" "$1/usr/share/theHarvester-gui/"
cp -r "theharvestergui" "$1/usr/bin/"
cp -r "theharvestergui-launcher.py" "$1/usr/share/theHarvester-gui/"
cp -r "README.md" "$1/usr/share/theHarvester-gui/"
cp -r "LICENSE" "$1/usr/share/theHarvester-gui/"

echo "Making files executable."
chmod +x "$1/usr/bin/theharvestergui"
chmod +x "$1/usr/share/theHarvester-gui/theharvestergui-launcher.py"