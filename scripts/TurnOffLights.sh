#!/bin/sh

# Find Script Location
DIR="$(dirname "$0")"

# Move to the Directory
cd "$DIR" || exit
cd ".."
cd "src" || exit

# Simple Bash Script used to turn on the lights for the Prusa Printer using the Python Script. Neccessary for Octolapse Plugin
echo "Turning off Shelf Lights"
python3 main.py --off >/dev/null 2>&1 # Redirecting so Octolapse doesnt fail
exit 0
