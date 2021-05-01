#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep

LED = 40
STATE = False

def setup_gpio():
	global LED
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)       	# Use BOARD GPIO numbers
	GPIO.setup(LED, GPIO.OUT)  		
    
def toggle_led():
	global STATE, LED
	STATE = not STATE
	GPIO.output(LED, STATE)
	print("LED toggle -- LED state : {}".format(STATE))

def main():
	print("Started main()")
	setup_gpio()
	print("Setup Done")
	while True:
		toggle_led()
		sleep(1)
	
if __name__ == "__main__":
	main()
