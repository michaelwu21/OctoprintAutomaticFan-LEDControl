from __future__ import absolute_import
import octoprint.plugin
import RPi.GPIO as GPIO

def initPins():
    GPIO.setmode(GPIO.BCM)
    #uses gpio pins 12, 16, and 20 from bcm wiring layout
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, GPIO.LOW)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, GPIO.LOW)
    GPIO.setup(20, GPIO.OUT)
    GPIO.output(20, GPIO.LOW)
    
def fan(comm, parsed_temps):
    invert = false #--> based off the type of relay, low trigger vs high trigger
    if parsed_temps.has_key('T0'):
        if int(list(parsed_temps['T0'])[0]) >= 50:
            if invert:
                GPIO.output(12, GPIO.LOW)
            else:
                GPIO.output(12, GPIO.HIGH)
            #print "Extruder 1 Fan On"
        else:
            if invert:
                GPIO.output(12, GPIO.HIGH)
            else:
                GPIO.output(12, GPIO.LOW)
            #print "Extruder 1 Fan Off"
        
    if parsed_temps.has_key('T1'):
        if int(list(parsed_temps['T1'])[0]) >= 50:
            if invert:
                GPIO.output(16, GPIO.LOW)
            else:
                GPIO.output(16, GPIO.HIGH)
            #print "Extruder 2 Fan On"
        else:
            if invert:
                GPIO.output(16, GPIO.HIGH)
            else:
                GPIO.output(16, GPIO.LOW)
            #print "Extruder 2 Fan Off"
            
    if parsed_temps.has_key('T2'):
        if int(list(parsed_temps['T2'])[0]) >= 50:
            if invert:
                GPIO.output(20, GPIO.LOW)
            else:
                GPIO.output(20, GPIO.HIGH)
            #print "Extruder 3 Fan On"
        else:
            if invert:
                GPIO.output(20, GPIO.HIGH)
            else:
                GPIO.output(20, GPIO.LOW)
            #print "Extruder 3 Fan Off"
    return parsed_temps

__plugin_name__ = "Octoprint Automatic Fan Control"
__plugin_author__ = "Michaelwu21"
__plugin_author_email__ = "Michaelwu21@gmail.com"
__plugin_version__ = "1.0"
__plugin_description__ = """Automatically control the extruder fan based off extruder temperature"""
__plugin_implementation__ = initPins()
__plugin_hooks__ = {
    "octoprint.comm.protocol.temperatures.received": fan
}
