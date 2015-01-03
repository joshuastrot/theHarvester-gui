#!/bin/bash

if [ $# -ge 5 ]; then
    if [ $1 == "-d" ]; then
        directory=$2
    elif [ $2 == "-d" ]; then
        directory=$3
    elif [ $3 == "-d" ]; then
        directory=$4
    elif [ $4 == "-d" ]; then
        directory=$5
    else
        directory="/"
    fi
    if [ $1 == "-v" ]; then
        if [ $2 == "qt4" ]; then
            version="qt4"
        elif [ $2 == "qt5" ]; then
            version="qt5"
        else
            echo "Invalid version specified."
            exit 1
        fi
    elif [ $2 == "-v" ]; then
        if [ $3 == "qt4" ]; then
            version="qt4"
        elif [ $3 == "qt5" ]; then
            version="qt5"
        else
            echo "Invalid version specified."
            exit 1
        fi
    elif [ $3 == "-v" ]; then
        if [ $4 == "qt4" ]; then
            version="qt4"
        elif [ $4 == "qt5" ]; then
            version="qt5"
        else
            echo "Invalid version specified."
            exit 1
        fi
    elif [ $4 == "-v" ]; then
        if [ $5 == "qt4" ]; then
            version="qt4"
        elif [ $5 == "qt5" ]; then
            version="qt5"
        else
            echo "Invalid version specified."
            exit 1
        fi
    else
        version="qt5"
    fi
    if [ $1 == "-r" ];then 
        remove="yes"
    elif [ $2 == "-r" ]; then
        remove="yes"
    elif [ $3 == "-r" ]; then
        remove="yes"
    elif [ $4 == "-r" ]; then
        remove="yes"
    elif [ $5 == "-r" ]; then
        remove="yes"
    else
        remove="no"
    fi
elif [ $# -eq 4 ]; then
    if [ $1 == "-d" ]; then
        directory=$2
    elif [ $2 == "-d" ]; then
        directory=$3
    elif [ $3 == "-d" ]; then
        directory=$4
    else
        directory="/"
    fi
    if [ $1 == "-v" ]; then
        if [ $2 == "qt4" ]; then
            version="qt4"
        elif [ $2 == "qt5" ]; then
            version="qt5"
        else
            echo "Invalid version specified."
            exit 1
        fi
    elif [ $2 == "-v" ]; then
        if [ $3 == "qt4" ]; then
            version="qt4"
        elif [ $3 == "qt5" ]; then
            version="qt5"
        else
            echo "Invalid version specified."
            exit 1
        fi
    elif [ $3 == "-v" ]; then
        if [ $4 == "qt4" ]; then
            version="qt4"
        elif [ $4 == "qt5" ]; then
            version="qt5"
        else
            echo "Invalid version specified."
            exit 1
        fi
    else
        version="qt5"
    fi
    if [ $1 == "-r" ];then 
        remove="yes"
    elif [ $2 == "-r" ]; then
        remove="yes"
    elif [ $3 == "-r" ]; then
        remove="yes"
    elif [ $4 == "-r" ]; then
        remove="yes"
    else
        remove="no"
    fi
elif [ $# -eq 3 ]; then
    if [ $1 == "-d" ]; then
        directory=$2
    elif [ $2 == "-d" ]; then
        directory=$3
    else
        directory="/"
    fi
    if [ $1 == "-v" ]; then
        if [ $2 == "qt4" ]; then
            version="qt4"
        elif [ $2 == "qt5" ]; then
            version="qt5"
        else
            echo "Invalid version specified."
            exit 1
        fi
    elif [ $2 == "-v" ]; then
        if [ $3 == "qt4" ]; then
            version="qt4"
        elif [ $3 == "qt5" ]; then
            version="qt5"
        else
            echo "Invalid version specified."
            exit 1
        fi
    else
        version="qt5"
    fi
    if [ $1 == "-r" ];then 
        remove="yes"
    elif [ $2 == "-r" ]; then
        remove="yes"
    elif [ $3 == "-r" ]; then
        remove="yes"
    else
        remove="no"
    fi
elif [ $# -eq 2 ]; then
    if [ $1 == "-d" ]; then
        directory=$2
    else
        directory="/"
    fi
    if [ $1 == "-v" ]; then
        if [ $2 == "qt4" ]; then
            version="qt4"
        elif [ $2 == "qt5" ]; then
            version="qt5"
        else
            echo "Invalid version specified."
            exit 1
        fi
    else
        version="qt5"
    fi
    if [ $1 == "-r" ];then 
        remove="yes"
    elif [ $2 == "-r" ]; then
        remove="yes"
    else
        remove="no"
    fi
elif [ $# -eq 1 ]; then
    directory="/"
    version="qt5"
    
    if [ $1 == "-h" ]; then
        echo """
This script installs theHarvester-gui.

Options:

-d             Directory to install to.
               (Default is / so if you're unsure
               of what to use here, just use a
               forward slash.)

-v             Version of qt to use.
               Options are: 
               
               qt4 
               qt5 (Default)
               
-r             Remove theharvester-gui.

Examples:

1). Install theHarvester-gui to the whole system with qt5

sudo bash install.sh -d / -v qt5

2). Install theHarvester-gui to the \$pkgdir for arch PKGBUILDS with qt4

sudo bash install.sh -d \"\$pkgdir\" -v qt4

3). Remove theHarvester-gui from the whole system.

sudo bash install.sh -d / -r
        """
        exit 1
    fi
    if [ $1 == "-r" ]; then 
        remove="yes"
    else
        echo "Invalid options specified."
        exit 1
    fi
fi

if [ $remove == "yes" ]; then
    printf "Are you sure you would like to remove theharvester-gui? [y/n]:"
    read areYouSure
    
    if [ $areYouSure != "y" ] && [ $areYouSure != "Y" ]; then
        echo "Okay, Exiting."
        exit 1
    fi
    
    rm -r "$directory/usr/share/theHarvester-gui/"
    rm -r "$directory/usr/bin/theharvestergui"
    
    exit 1
fi

printf "Are you sure you would like install theharvester-gui? [y/n]:"
read areYouSure

if [ $areYouSure != "y" ] && [ $areYouSure != "Y" ]; then
    echo "Okay, exiting."
    exit 1
fi

if [ ! -f "theharvestergui" ] || [ ! -d "gui_" ] || [ ! -d "tools_" ] || [ ! -d ".git" ]; then
    echo "Some of the required files are missing. Are you sure you're in theharvester-gui directory?"
    exit 1
fi

echo "Starting install..."

if [ $version == "qt4" ]; then
    git checkout qt4
fi

echo "Creating necessary directories."
mkdir -p "$directory/usr/bin"
mkdir -p "$directory/usr/share/theHarvester-gui"

echo "Moving files to the proper place."
cp -r "tools_" "$directory/usr/share/theHarvester-gui/"
cp -r "gui_" "$directory/usr/share/theHarvester-gui/"
cp -r "theharvestergui" "$directory/usr/bin/"
cp -r "theharvestergui-launcher.py" "$directory/usr/share/theHarvester-gui/"
cp -r "README.md" "$directory/usr/share/theHarvester-gui/"
cp -r "LICENSE" "$directory/usr/share/theHarvester-gui/"

echo "Making files executable."
chmod +x "$directory/usr/bin/theharvestergui"
chmod +x "$directory/usr/share/theHarvester-gui/theharvestergui-launcher.py"