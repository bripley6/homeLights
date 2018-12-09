import atticUtility     
from flask import Flask
from flask import request
from flask import render_template
import wirelessLightsUtility as living 
import logging

# set these up for your host
hostIP = "10.1.10.5"
hostPort = 8000
debug = True
 
# create some objects
app = Flask(__name__)
attic = atticUtility.LEDDriver()
living.initializeButtons()
logging.basicConfig(filename='lightControl.log', level=logging.INFO) #filename='myapp.log', 

# define some alternate names that Google Assistant might respond with for the lights
atticNames = ['attic','kid hole', 'the attic', 'kid hall', 'kid Hall']
atticPartyNames = ['party', 'attic party']
livingRoomNames = ['living room', 'the living room', 'living', 'living room medium']
livingRoomBrightNames = ['living room bright', 'living room full', 'living room max']
livingRoomDimNames = ['living room TV', 'living room dim', 'living TV', 'living room low', 'dim living room']

 
class button():
    """A class for defining a button element to go into the manual webpage"""
    def __init__(o, path, switch, text):
      o.path = path
      o.switch = switch
      o.text = text

buttons = []  
buttons.append(button('on', 'attic',  'Attic lights - ON '))
buttons.append(button('on', 'party',  'Attic party - ON  '))
buttons.append(button('off', 'attic', 'Attic lights - OFF'))
buttons.append(button('on', 'living room full', 'Living room lights - FULL'))
buttons.append(button('on', 'living room', 'Living room lights - MED '))
buttons.append(button('on', 'living room tv', 'Living room lights - LOW'))
buttons.append(button('off', 'living room', 'Living room lights - OFF   '))

 
@app.route("/")
def default():
    return render_template('manualControl.html', buttons=buttons)
     
  
"""The app should pass an argument via post method like http://198.27.188.7:8000/switches/on\
This app uses pigpiod for controlling I/O. Start the demon from a console with 'sudo pigpiod'"""
@app.route('/switches/<onOff>', methods=['POST', 'GET'])
def updateSwitch(onOff):
    if (request.method == 'GET'):
        return "You used the GET method. This path needs to use the POST method."
    
    if (request.method == 'POST'):
        switch = request.values['switch']
        logging.info("requesting to switch " + onOff + " " + switch + " lights.")
    
    if switch in atticNames:
        if onOff == "on":
            attic.fadeOn(5)
        elif onOff == "off":
            attic.fadeOff(5)

    elif switch in atticPartyNames:
        if onOff == "on":
          attic.strobe(5, .2)
 
    elif switch in livingRoomBrightNames:
        if onOff == "on":
            living.pressButton(3)
                
    elif switch in livingRoomNames:
        if onOff == "on":
            living.pressButton(2)
        else:
            living.pressButton(0)
          
    elif switch in livingRoomDimNames:
        if onOff == "on":
            living.pressButton(1)          
            
    else:
        logging.warning("Unknown switch " + switch)
        return "I don't know this switch <i>" + switch + "</i>. <a href='../../'> Go back</a>"
        
    return render_template('manualControl.html', buttons=buttons, relPath='../../')


@app.route('/ajax/dim', methods=['POST'])
def dimSwitch():
    if (request.method == 'POST'):
        switch = request.values['switch']
        brightness = request.values['brightness']
    
    attic.led = int(brightness)
    attic.update()
    logging.info ("turning on "+ switch + " at " + brightness + " level")
    return "ok"
    
if __name__ == "__main__":
    app.run(host=hostIP, port=int(hostPort), debug=debug)