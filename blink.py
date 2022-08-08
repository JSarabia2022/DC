import machine
import sys
import time

# Pin definitions
led    = machine.Pin(2, machine.Pin.OUT)

while True:
	led.value(1)
	time.sleep(1)
	led.value(0)
	time.sleep(1)
