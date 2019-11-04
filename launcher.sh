#!/bin/bash
sleep 10
if [ -x /opt/xkeysnail/bin/xkeysnail ]; then
    xhost +SI:localuser:root
    sudo -u root DISPLAY=$DISPLAY /opt/xkeysnail/bin/xkeysnail /opt/xkeysnail/config.py 1> /dev/null
fi
