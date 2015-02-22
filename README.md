# Contents:

1. [What is theHarvester-gui?](#what-is-theharvester-gui)
2. [Universal Dependencies](#universal-dependencies)
3. [Compatible Platforms](#compatible-platforms)
4. [Installation Instructions](#installation-instructions)
  1. [Arch](#arch) 
  2. [Debian/Kali](#debiankali)

# What is theHarvester-gui?

It's a graphical frontend to theHarvester, for ease of use and speed. It's written in PyQt5 and Python 3, or PyQt4 and Python 2, you can pick which one in the installation process. So you'll need to download you're dependencies accordingly to which you pick.

# Compatible Platforms:

* Arch
* Debian
* Kali

# Universal Dependencies:

* theHarvester from their [github page](http://github.com/laramies/theHarvester). v2.5

# Installation instructions
## Arch

theHarvester-gui is available on the AUR of [aur.archlinux.org](http://aur.archlinux.org) in QT4 and QT5. You can install it manually, or with an AUR helper. Check it out at [theharvester-gui](https://aur.archlinux.org/packages/theharvester-gui) or [theharvester-gui-qt4](https://aur.archlinux.org/packages/theharvester-gui-qt4)

### Installation instructions:

`yaourt -S theharvester-gui` 

Or for the QT4 version

`yaourt -S theharvester-gui-qt4` 

## Debian/Kali

You'll need to build this package manually, and install the dependencies manually. Currently, Debian Wheezy only has QT4 available, so unless you switch to Sid you'll have to use QT4.

### Dependencies:

* python-qt4

### Installation instructions:

```
git clone https://github.com/dcell/theharvester-gui ~/theharvester-gui
cd ~/theharvester-gui
sudo bash install.sh -d / -v qt4
theharvestergui
```