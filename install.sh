#!/usr/bin/bash

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
mkdir -p "/usr/bin"
mkdir -p "/usr/share/theHarvester-gui"

echo "Moving files to the proper place."
cp -r "tools_" "/usr/share/theHarvester-gui/"
cp -r "gui_" "/usr/share/theHarvester-gui/"
cp -r "theharvestergui" "/usr/bin/"
cp -r "theharvestergui-launcher.py" "/usr/share/theHarvester-gui/"
cp -r "README.md" "/usr/share/theHarvester-gui/"
cp -r "LICENSE" "/usr/share/theHarvester-gui/"

echo "Making files executable."
chmod +x "/usr/bin/theharvestergui"
chmod +x "/usr/share/theHarvester-gui/theharvestergui-launcher.py"