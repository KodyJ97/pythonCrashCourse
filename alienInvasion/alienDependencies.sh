#!/bin/bash

echo "If not working run chmod +x alienDependencies.sh"

# Libraries that Pygame requires
sudo apt-get install python3-dev mercurial
sudo apt-get install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev

# Advanced functionality for Pygame such as the ability to add sounds
sudo apt-get install libsdl-mixer1.2-dev libportmidi-dev
sudo apt-get install libswscale-dev libsmpeg-dev libavformat-dev libavcodec-dev
sudo apt-get install python-numpy

# Error freetype-config: not found. This dependency was missing.
sudo apt-get install libfreetype6-dev

# Install pygame use pip3 if for python3 or pip for python 2*.
pip3 install --user hg+http://bitbucket.org/pygame/pygame

echo "if not working install dependencies at https://www.pygame.org/wiki/CompileUbuntu?parent="
