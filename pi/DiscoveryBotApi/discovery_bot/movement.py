from .servo import Servo
from . import pins
import time


class Movement():

    def __init__( self ):
        self.left = Servo( pins.SERVO_LEFT_MOTOR )
        self.right = Servo( pins.SERVO_RIGHT_MOTOR )

    def normalize( self, val ):
        scale = 0.5 / 100
        speed = val * scale

        if val >= 0:
            speed += 0.5

        if val < 0:
            speed += 0.35

        return speed

    def setMotorSpeed( self, motor=None, speed=0 ):
        if (motor == pins.SERVO_LEFT_MOTOR):
            self.left.set_normalized( self.normalize( speed ) )
        if (motor == pins.SERVO_RIGHT_MOTOR):
            self.right.set_normalized( self.normalize( -speed ) )

    def forward( self, speed=100, time=None ):
        self.left.set_normalized( self.normalize( speed ) )
        self.right.set_normalized( self.normalize( -speed ) )
        if (speed == 0):
            self.left.set_normalized( -1 )
            self.right.set_normalized( -1 )

        if time != None:
            time.sleep( time )
            self.stop()

    def backward( self, speed=100, time=None ):
        self.left.set_normalized( self.normalize( -speed ) )
        self.right.set_normalized( self.normalize( speed ) )
        if (speed == 0):
            self.left.set_normalized( -1 )
            self.right.set_normalized( -1 )

        if time != None:
            time.sleep( time )
            self.stop()

    def turn_left( self, speed=100, time=None ):
        self.left.set_normalized( self.normalize( 10 ) )
        self.right.set_normalized( self.normalize( -100 ) )

        if (speed == 0):
            self.left.set_normalized( -1 )
            self.right.set_normalized( -1 )

        if time != None:
            time.sleep( time )
            self.stop()

    def rotate_right( self, speed=50 ):
        self.left.set_normalized( self.normalize( speed ) )
        self.right.set_normalized( self.normalize( speed ) )

    def rotate_left( self, speed=50 ):
        self.left.set_normalized( self.normalize( -speed ) )
        self.right.set_normalized( self.normalize( -speed ) )

    def turn_right( self, speed=100, time=None ):
        self.left.set_normalized( self.normalize( 100 ) )
        self.right.set_normalized( self.normalize( -10 ) )

        if (speed == 0):
            self.left.set_normalized( -1 )
            self.right.set_normalized( -1 )

        if time != None:
            time.sleep( time )
            self.stop()

    #    def move(self, left = 100, right = 100, time = None)
    #	self.left.set_normalized(self.normalize(left))
    #        self.right.set_normalized(self.normalize(right))
    #	if time != None:
    #	    time.sleep(time)
    #	    self.stop()

    def stop( self ):
        self.left.set_normalized( -1 )
        self.right.set_normalized( -1 )

    def test( self ):
        # self.left.set_normalized(0)
        self.right.set_normalized( 0.40 )

# robot = Movement()
# print(robot.normalize(-20))
# print(robot.normalize(20))
# robot.test()
# robot.turn_right(20)
# time.sleep(2)
# robot.stop()
