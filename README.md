# Xkeysnail key mapping
Modify keys on Ubuntu like macOS

# Installation

+ xkeysnail  
```
sudo apt install python3-pip
sudo pip3 install xkeysnail
```

+ udev rules and systemd service
```
cd [working dir]
git clone git@github.com:MikiyaShibuya/xkeysnail.git
cd xkeysnail
sudo ./setup.sh
```

+ apply udev rules
```
sudo reboot
```

+ enable and start systemd service
```
systemctl --user enable xkeysnail
systemctl --user start xkeysnail
```
