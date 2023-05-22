#-*- coding:utf-8 -*-
from __future__ import division

from pi.tiddlyServer.discovery_bot import Movement
from pi.tiddlyServer.discovery_bot import pins
import time
from pi.tiddlyServer.discovery_bot import Light

robot = Movement()

red = Light( pins.LED_RED )

blue = Light( pins.LED_BLUE )

green = Light( pins.LED_GREEN )


robot.forward()
time.sleep(2)
red.on()
robot.stop()
