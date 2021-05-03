# seminar

## RaspberryPi Pinout
![GPIO-Pinout-Diagram-2](https://user-images.githubusercontent.com/34370544/116787684-23267680-aac3-11eb-806c-ba600c4b93f6.png)

# Bluetooth Setup

Run the following command : `sudo apt-get install bluetooth bluez blueman`

Reboot Pi



Setup SPP bluetooth profile by editing file given below

open file using command :

`sudo nano /etc/systemd/system/dbus-org.bluez.service`

Start bluetooth daemon in compatibility mode

`ExecStart=/usr/lib/bluetooth/bluetoothhd -C`

Add spp profile

`ExecStartPost=/usr/bin/sdptool add SP`

Save and Reboot Pi

## Enabling communication
Now Open terminal and run command:

`sudo rfcomm watch hci0`

Enable device to watch for incoming Bluetooth connections

Now reading data from serial using python script.

`python3 rpi_bluetooth_serial.py`
