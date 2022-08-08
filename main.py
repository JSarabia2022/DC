import machine
import sys
import time

from hcsr04 import HCSR04
from time   import sleep

class intrusion_detection_system():
    """docstring for ."""
    def __init__(self, threa=0.1):
        self.threa   = 1 - threa
        self.sensor0 = HCSR04(trigger_pin=19, echo_pin=18, echo_timeout_us=10000)
        self.sensor1 = HCSR04(trigger_pin=14, echo_pin=13, echo_timeout_us=10000)
        self.sensor2 = HCSR04(trigger_pin=27, echo_pin=26, echo_timeout_us=10000)
        self.sensor3 = HCSR04(trigger_pin=22, echo_pin=23, echo_timeout_us=10000)
    #
    def distances(self):
        d0 = sensor0.distance_cm()
        d1 = sensor1.distance_cm()
        d2 = sensor2.distance_cm()
        d3 = sensor3.distance_cm()
        print(f"distance 0: {d0:6.3f} cm")
        print(f"distance 1: {d1:6.3f} cm")
        print(f"distance 2: {d2:6.3f} cm")
        print(f"distance 3: {d3:6.3f} cm")
        sleep(0.2)
        return [d0, d1, d2, d3]
    #
    def run(self):
        print("Starting system...")
        print("Init automatic calibration...\n")
        sleep(10)
        print("calibration succeded\n")
        while True:
#            d = distances()
#
main = intrusion_detection_system()
main.run()
