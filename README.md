# Seminar

# RaspberryPi Pinout
![GPIO-Pinout-Diagram-2](https://user-images.githubusercontent.com/34370544/116787684-23267680-aac3-11eb-806c-ba600c4b93f6.png)

# Bluetooth Setup

Run the following command : 

`sudo apt-get install bluetooth bluez blueman`

Reboot Pi

`sudo reboot now`

Check bluetooth service status

`service bluetooth status`

Setup SPP bluetooth profile by editing file given below

open file using command :

`sudo nano /etc/systemd/system/dbus-org.bluez.service`

Start bluetooth daemon in compatibility mode by adding `-C` at the end of line given below 

`ExecStart=/usr/lib/bluetooth/bluetoothd` to `ExecStart=/usr/lib/bluetooth/bluetoothd -C` 

Add SPP (Serial Port Profile) by adding this line 

`ExecStartPost=/usr/bin/sdptool add SP`

Save and Reboot Pi

## Enabling communication
Now Open terminal and run command given below. This command will enable device to watch for incoming bluetooth connections

`sudo rfcomm watch hci0`

Check available serial port using command:

`python3 -m serial.tools.list_ports`

Now reading data from serial using python script.

`python3 rpi_bluetooth_serial.py`
