# vulture_bee_cam
Code and installation instructions for raspberry pi based camera monitoring system
Vulture bee project
Costa Rica 2024 (Lapa Verde and La Selva)

# Install OS

Install latest Pi OS (Desktop: tested December 2023)
Setup locale, timezone, keyboard, hostname, ssh


# Clone this repository and dependencies

Prepare for and clone this repository
```bash
. ~/.bashrc
mkdir -p ~/r/braingram
cd ~/r/braingram
git clone https://github.com/Crall-Lab/pollinatorcam.git
cd pollinatorcam
git switch detection_network

cd ~
git clone https://github.com/Crall-Lab/pollinatorcam.git
git clone https://github.com/Crall-Lab/vulture_bee_cam.git
```

# Install python dependencies
```bash
sudo apt update
sudo apt install python3-numpy python3-opencv
```

# Setup storage location
Before running these lines, make sure to have your external USB device (e.g., thumb drive) connected to te pi

This assumes you're using an external storage drive that shows up as /dev/sda1. You can check thumbdrive mounting location using - "sudo fdisk -l"
One option is to setup the drive as ntfs.
To format the drive as ntfs (to allow for >2TB volumes) in fdisk you will need to do the following:
```bash
# confirm /dev/sda is your external drive before proceeding
# open fdisk
sudo fdisk /dev/sda
# switch to gpt: g
# delete all partions: d (for each partion)
# make a new partion that takes up all disk space: n (use all defaults)
# switch the partion type to microsoft basic data: t 11
# write fdisk: w
# make ntfs filesystem
sudo mkfs.ntfs -f /dev/sda1
```

Mount storage location

#NB adjust user name below as needed
```bash
echo "/dev/sda1 /mnt/data auto defaults,user,uid=1000,gid=124,umask=002  0 0" | sudo tee -a /etc/fstab
sudo mkdir /mnt/data
sudo mount /mnt/data
sudo mkdir -p /mnt/data/logs
sudo chown bombus /mnt/data
sudo chgrp ftp /mnt/data
sudo chmod 775 /mnt/data
```

# Install MCC134 libraries and script

Attach the MCC134 thermocouple ontop of the Pi's 40 pin GPIO, then run commands below
```bash
cd ~
git clone https://github.com/mccdaq/daqhats.git
cd ~/daqhats
sudo ./install.sh
```
```bash
sudo chmod 775 ~/vulture_bee_cam/scripts/tempSensor.py
sudo cp ~/vulture_bee_cam/scripts/tempSensor.py ~/daqhats/examples/python/mcc134/tempSensor.py
```
Open crontab and add this line
```bash
* * * * * sudo python3 ~/daqhats/examples/python/mcc134/tempSensor.py
```
Run sudo python ~/daqhats/examples/python/mcc134/tempSensor.py
Confirm a folder in /home/pi/ titled "tempProbes" and a csv with a temp reading is generated

# Set up and test video recording

Modify script permissions
```bash
cd ~/vulture_bee_cam/scripts/
chmod a+x record_video.sh
```

Test recording
```bash
sudo ~/vulture_bee_cam/scripts/record_video.sh
```

Now add recoding script to crontab
```bash
@reboot sudo ~/vulture_bee_cam/scripts/record_video.sh
```

# Install wittyPi libraries and script

Attach the wittyPi on top of the thermocouples 40 pin GPIO (NB change 'WittyPi3' to 'WittyPi4' depending on model you're using)
```bash
cd ~
wget http://www.uugear.com/repo/WittyPi3/install.sh
sudo sh install.sh
```
```bash
sudo cp ~/vulture_bee_cam/scripts/schedule.wpi ~/wittypi/schedule.wpi
sudo ~/wittypi/runScript.sh
```
