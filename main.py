#!/usr/bin/env python3

import os
import os.path

# Functions 
def readFilesInDir( directory : str):
    path = directory
    numOfFiles = sum(os.path.isfile(os.path.join(path, f)) for f in os.listdir(path))
    return numOfFiles

def notify(message, title : str, subtitle : str, dirToOpen : str):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(title)
    m = '-message {!r}'.format(message)
    e = '-execute {!r}'.format(dirToOpen)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s, e])))   

# App Configuration
directory = '/Users/geronimo.weibel/Downloads/'
maxFiles = 10

# App variables 
numOfFiles = readFilesInDir(directory)

# Message Configuration
title = 'Download-manager'
subtitle = "Download-manager"
dirToOpen = 'open /Users/geronimo.weibel/Downloads/'

# Main
if numOfFiles >= maxFiles: 
    # Message creation
    modMessage = "We have %d files"%numOfFiles

    # Sending notfication
    notify(title = title,
    subtitle = subtitle,
    message  = modMessage,
    dirToOpen = dirToOpen)