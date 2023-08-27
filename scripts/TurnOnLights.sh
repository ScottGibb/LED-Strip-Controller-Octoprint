#!/bin/sh

# Find Script Location
DIR="$(dirname "$0")"

# Move to the Directory
cd "$DIR"
cd ".."
cd "src"

# Simple Bash Script used to turn on the lights for the Prusa Printer using the Python Script. Neccessary for Octolapse Plugin
#echo "Turning on Shelf Lights"
python3 main.py --on >/dev/null 2>&1 # Redirecting so that octolapse doesnt fail
exit 0

