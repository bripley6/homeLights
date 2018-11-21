import atticUtility as attic
     
from flask import Flask
from flask import request
app = Flask(__name__)

# create the LED output object for controlling attic light
leds = attic.LEDDriver()

# define some alternate names for the lights
atticNames = ['attic','kid hole', 'the attic', 'kid hall', 'kid Hall']
atticPartyNames = ['party', 'attic party']
livingroomNames = ['living room', 'living']
livingroomBrightNames = ['living room bright', 'living room full', 'living room max']
livingroomTVNames = ['living room tv', 'living room dim', 'living tv']


@app.route("/")
def default():
    return "<html><form action='switches/on' method='post'>\
    <input type='hidden' name='switch' value='attic'>\
  <input type='submit' value='Attic lights on'></form></html>"
  
    garbage = "<html>This little app will control some lights.<br>\
    <a href='switches/atticOn'>Attic Lights On</a></html>\
    <a href='switches/atticOff'>Attic Lights Off</a></html>"    
  
"""The app should pass an argument via get method like http://198.27.188.7:8000/switches/sw0\
This app uses pigpiod for controlling I/O. Start the demon from a console with 'sudo pigpiod'"""
@app.route('/switches/<onOff>', methods=['POST', 'GET'])
def updateSwitch(onOff):
    if (request.method == 'GET'):
        return "You used the GET method. This path needs to use the POST method."
    
    if (request.method == 'POST'):
        switch = request.values['switch']
        print "requesting to switch " + onOff + " " + switch + " lights."
    
    if switch in atticNames:
        if onOff == "on":
            attic.fadeOn(leds, 5)
        elif onOff == "off":
            attic.fadeOff(leds, 5)

    if switch in atticPartyNames:
        if onOff == "on":
          attic.strobe(leds, 5, .2)      
    else:
        return "I don't know this switch <i>" + switch + "</i>."
        
    return "ok"
        
    
if __name__ == "__main__":
    app.run(host='10.1.10.6', port=int("8000"), debug=True)