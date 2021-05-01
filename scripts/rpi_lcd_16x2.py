#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep

# Define GPIO to LCD mapping
LCD_RS = 7
LCD_E = 8
LCD_D4 = 16
LCD_D5 = 18
LCD_D6 = 22
LCD_D7 = 24

# Define some device constants
LCD_WIDTH = 16    	# Maximum characters per line
LCD_CHR = 1  		# True
LCD_CMD = 0  		# False

LCD_LINE_1 = 0x80  	# LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0  	# LCD RAM address for the 2nd line

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

def main():
    # Main program block
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)       	# Use BCM GPIO numbers
    GPIO.setup(LCD_E, GPIO.OUT)    	# E
    GPIO.setup(LCD_RS, GPIO.OUT)  	# RS
    GPIO.setup(LCD_D4, GPIO.OUT)  	# DB4
    GPIO.setup(LCD_D5, GPIO.OUT)  	# DB5
    GPIO.setup(LCD_D6, GPIO.OUT)  	# DB6
    GPIO.setup(LCD_D7, GPIO.OUT)  	# DB7

    print("RPi Info : {}".format(GPIO.RPI_INFO))
    #print("RPi version : {}".format(GPIO.VERSION))

    # Initialise display
    lcd_init()

    while True:
        # Send some test
        lcd_string("Learn Something", LCD_LINE_1)
        lcd_string(" of Everything", LCD_LINE_2)
        sleep(3)  # 3 second delay

        # Send some text
        lcd_string(" and Everything", LCD_LINE_1)
        lcd_string("  of Something", LCD_LINE_2)
        sleep(3)  # 3 second delay
 
        # Send some text
        lcd_string("  Written By:", LCD_LINE_1)
        lcd_string(" Thomas Huxley", LCD_LINE_2)
        sleep(3)
        
        lcd_string(" ", LCD_LINE_1)
        lcd_string(" ", LCD_LINE_2)
        sleep(2)

        print("Message Sending Done")

 
def lcd_init():
    lcd_display(0x28, LCD_CMD)  	# Selecting 4 - bit mode with two rows
    lcd_display(0x0C, LCD_CMD)  	# Display On,Cursor Off, Blink Off
    lcd_display(0x01, LCD_CMD)  	# Clear display
    sleep(E_DELAY)

def lcd_display(bits, mode):
    # Send byte to data pins
    # bits = data
    # mode = True  for character
    #        False for command
    GPIO.output(LCD_RS, mode)  		# RS

    # High bits
    GPIO.output(LCD_D4, GPIO.LOW)
    GPIO.output(LCD_D5, GPIO.LOW)
    GPIO.output(LCD_D6, GPIO.LOW)
    GPIO.output(LCD_D7, GPIO.LOW)
    if bits & 0x10 == 0x10:
        GPIO.output(LCD_D4, GPIO.HIGH)
    if bits & 0x20 == 0x20:
        GPIO.output(LCD_D5, GPIO.HIGH)
    if bits & 0x40 == 0x40:
        GPIO.output(LCD_D6, GPIO.HIGH)
    if bits & 0x80 == 0x80:
        GPIO.output(LCD_D7, GPIO.HIGH)

    # Toggle 'Enable' pin
    lcd_enable()

    # Low bits
    GPIO.output(LCD_D4, GPIO.LOW)
    GPIO.output(LCD_D5, GPIO.LOW)
    GPIO.output(LCD_D6, GPIO.LOW)
    GPIO.output(LCD_D7, GPIO.LOW)
    if bits & 0x01 == 0x01:
        GPIO.output(LCD_D4, GPIO.HIGH)
    if bits & 0x02 == 0x02:
        GPIO.output(LCD_D5, GPIO.HIGH)
    if bits & 0x04 == 0x04:
        GPIO.output(LCD_D6, GPIO.HIGH)
    if bits & 0x08 == 0x08:
        GPIO.output(LCD_D7, GPIO.HIGH)

    # Toggle 'Enable' pin
    lcd_enable()

def lcd_enable():
    # Toggle enable
    sleep(E_DELAY)
    GPIO.output(LCD_E, GPIO.HIGH)
    sleep(E_PULSE)
    GPIO.output(LCD_E, GPIO.LOW)
    sleep(E_DELAY)

def lcd_string(message, line):
    # Send string to display
    '''
    This function left aligns the string according to the width specified and fills remaining space
    of line with blank space if ‘ fillchr ‘ argument is not passed.
    '''
    message = message.ljust(LCD_WIDTH, " ")
    lcd_display(line, LCD_CMD)
    for i in range(LCD_WIDTH):
        lcd_display(ord(message[i]), LCD_CHR)

if __name__ == '__main__':
    try:
        main()
        print("Main")
    except KeyboardInterrupt:
        pass
    finally:
        lcd_display(0x01, LCD_CMD)
        GPIO.cleanup()
        print("LCD Cleanup")
