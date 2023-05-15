#-*- coding:utf-8 -*-
from __future__ import division

from discovery_bot import Movement, pins
import time
from discovery_bot import Light

robot = Movement()

red = Light( pins.LED_RED )

blue = Light( pins.LED_BLUE )

green = Light( pins.LED_GREEN )


robot.forward()
time.sleep(2)
red.on()
robot.stop()
