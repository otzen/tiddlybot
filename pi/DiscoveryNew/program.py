from pi.tiddlyServer.discovery_bot import Movement
from pi.tiddlyServer.discovery_bot import Ultrasound
from pi.tiddlyServer.discovery_bot import Light
from pi.tiddlyServer.discovery_bot import Button
from pi.tiddlyServer.discovery_bot import Buzzer
import time
robot = Movement()
red = Light( pi.tiddlyServer.discovery_bot.pins.LED_RED )
blue = Light( pi.tiddlyServer.discovery_bot.pins.LED_BLUE )
green = Light( pi.tiddlyServer.discovery_bot.pins.LED_GREEN )
buzzer = Buzzer()
b = Button()
usound = Ultrasound()
buzzer.on();
time.sleep(1 )
buzzer.off()
