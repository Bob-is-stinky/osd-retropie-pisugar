#!/bin/bash
sudo apt-get update
sudo apt-get install -y python3-pygame
wget https://github.com/PiSugar/pisugar-power-manager/releases/latest/download/pisugar-power-manager.deb
sudo dpkg -i pisugar-power-manager.deb
mkdir -p ~/osd-retropie-pisugar
cp osd.py ~/osd-retropie-pisugar/
(crontab -l ; echo "@reboot python3 ~/osd-retropie-pisugar/osd.py &") | crontab -
echo "Install complete! Reboot to start the OSD."
