#!/usr/bin/env python3
import serial

'''
Read more about serial visit the link given below:
https://pyserial.readthedocs.io/en/latest/pyserial_api.html
'''

bluetooth_serial = serial.Serial('/dev/rfcomm0')

while True:
	data = bluetooth_serial.readline()
	filtered_data = data.decode('utf-8').rstrip()
	print(filtered_data)
