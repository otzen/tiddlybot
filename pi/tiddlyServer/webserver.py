#!/usr/bin/python

import os
import os.path

import cherrypy
import blockly_runner


# from camera_streamer import Camera


class Page:
    def __init__(self, root: str = None, staticDir: str = 'static' ):
        if root :
            self.root = root
        else :
            self.root = os.path.abspath( os.path.dirname( __file__ ) )
        self.staticDir = os.path.join( self.root, staticDir )


class IndexPage( Page ):
    @cherrypy.expose
    def index( self ):
        return open( os.path.join( self.staticDir, 'index.html' ) )


class BlocklyPage( Page ):
    @cherrypy.expose
    def index( self ):
        return open( './static/blockly.html' )

    @cherrypy.expose
    def start( self, code ):
        app = open( '../DiscoveryNew/program.py', 'rw+' )
        code_write = """import discovery_bot
from discovery_bot import Movement
from discovery_bot import Servo
from discovery_bot import Ultrasound
from discovery_bot import Light
from discovery_bot import Infrared
from discovery_bot import Button
from discovery_bot import Buzzer
import time
robot = Movement()
red = Light(discovery_bot.pins.LED_RED)
blue = Light(discovery_bot.pins.LED_BLUE)
green = Light(discovery_bot.pins.LED_GREEN)
buzzer = Buzzer()
b = Button()
usound = Ultrasound()
"""
        code_write += code
        app.seek( 0 )
        app.write( code_write )
        app.truncate()
        app.close()
        blockly_runner.stop()
        blockly_runner.run( 'program.py' )

    @cherrypy.expose
    def stop( self ):
        blockly_runner.stop()


class ControllerPage( Page ):
    @cherrypy.expose
    def index( self ):
        os.system( 'sudo ./camera.sh  > cam.log &' )
        return open( os.path.join( self.staticDir, 'controller.html' ))


if __name__ == '__main__':
    rootFolder = os.path.abspath(os.path.dirname(__file__))
    staticFolder = os.path.join( rootFolder, 'static' )

    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': staticFolder,
        },
        '/generator': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [ ('Content-Type', 'text/plain') ],
        },
        '/js': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'js',
        },
        '/images': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'images',
        },
        '/css': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'css',
        },
    }

    cherrypy.tree.mount( IndexPage(), config=conf )
    cherrypy.tree.mount( BlocklyPage(), '/blockly', conf )
    cherrypy.tree.mount( ControllerPage(), '/controller', conf )

    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.server.socket_port = 8888
    cherrypy.engine.start()
    cherrypy.engine.block()
