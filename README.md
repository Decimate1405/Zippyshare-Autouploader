# Zippyshare-Autouploader
This is an auto-uploading script for Zippyshare made in Python3.

This script has been tested on Linux servers.

Download the script:

`git clone https://github.com/Decimate1405/Zippyshare-Autouploader`

Run it using `python3 zl.py` (do not run the script with `sudo`).

Before you run the script, create two folders: `archives` and `links` in the same directory as the `zl.py` script.

The script makes rar files of 500M each and saves them temporarily in the `archives` folder. 
Then it uploads the files using Plowshare and exports the links to the `links` folder saved as the original file name.

# Credits 
Credits to [mcrapet](https://github.com/mcrapet/plowshare-modules-legacy) for the Zippyshare Plowshare module.
