#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# spin                                                                         #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# The program spin provides an interface for control of the usage modes of     #
# laptop-tablet and similar computer interface devices.                        #
#                                                                              #
# copyright (C) 2013 William Breaden Madden                                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################

Usage:
    spin.py [options]

Options:
    -h,--help        display help message
    --version        display version and exit
    --nogui          non-GUI mode
    --debugpassive   display commands without executing
"""

name    = "spin"
version = "2015-04-29T1702Z"

import imp
import urllib

def smuggle(
    moduleName = None,
    URL        = None
    ):
    if moduleName is None:
        moduleName = URL
    try:
        module = __import__(moduleName)
        return(module)
    except:
        try:
            moduleString = urllib.urlopen(URL).read()
            module = imp.new_module("module")
            exec moduleString in module.__dict__
            return(module)
        except: 
            raise(
                Exception(
                    "module {moduleName} import error".format(
                        moduleName = moduleName
                    )
                )
            )
            sys.exit()

import os
import sys
import glob
import subprocess
import multiprocessing
import socket
import time
import logging
from   PyQt4 import QtGui
docopt = smuggle(
    moduleName = "docopt",
    URL = "https://rawgit.com/docopt/docopt/master/docopt.py"
)

class interface(QtGui.QWidget):

    def __init__(
        self,
        options = None
        ):
        self.options = options
        super(interface, self).__init__()
        log.info("initiate {name}".format(name = name))
        # Audit the inputs available.
        self.deviceNames = get_inputs()
        if options["--debugpassive"] is True:
            log.info("device names: {deviceNames}".format(
                deviceNames = self.deviceNames
            ))
        # engage stylus proximity control
        self.stylus_proximity_control_switch(status = "on")
        # engage acceleration control
        #self.acceleration_control_switch(status = "on")
        # engage display position control
        self.displayPositionStatus = "laptop"
        self.display_position_control_switch(status = "on")
        if not options["--nogui"]:
            # create buttons
            buttonsList = []
            # button: tablet mode
            buttonModeTablet = QtGui.QPushButton(
                "tablet mode",
                self
            )
            buttonModeTablet.clicked.connect(
                lambda: self.engage_mode(mode = "tablet")
            )
            buttonsList.append(buttonModeTablet)
            # button: laptop mode
            buttonModeLaptop = QtGui.QPushButton(
                "laptop mode",
                self
            )
            buttonModeLaptop.clicked.connect(
                lambda: self.engage_mode(mode = "laptop")
            )
            buttonsList.append(buttonModeLaptop)
            # button: left
            buttonLeft = QtGui.QPushButton(
                "left",
                self
            )
            buttonLeft.clicked.connect(
                lambda: self.engage_mode(mode = "left")
            )
            buttonsList.append(buttonLeft)
            # button: right
            buttonRight = QtGui.QPushButton(
                "right", self
            )
            buttonRight.clicked.connect(
                lambda: self.engage_mode(mode = "right")
            )
            buttonsList.append(buttonRight)
            # button: inverted
            buttonInverted = QtGui.QPushButton(
                "inverted",
                self
            )
            buttonInverted.clicked.connect(
                lambda: self.engage_mode(mode = "inverted")
            )
            buttonsList.append(buttonInverted)
            # button: normal
            buttonNormal = QtGui.QPushButton(
                "normal",
                self
            )
            buttonNormal.clicked.connect(
                lambda: self.engage_mode(mode = "normal")
            )
            buttonsList.append(buttonNormal)
            # button: touchscreen on
            buttonTouchscreenOn = QtGui.QPushButton(
                "touchscreen on",
                self
            )
            buttonTouchscreenOn.clicked.connect(
                lambda: self.touchscreen_switch(status = "on")
            )
            buttonsList.append(buttonTouchscreenOn)
            # button: touchscreen off
            buttonTouchscreenOff = QtGui.QPushButton(
                "touchscreen off",
                self
            )
            buttonTouchscreenOff.clicked.connect(
                lambda: self.touchscreen_switch(status = "off")
            )
            buttonsList.append(buttonTouchscreenOff)
            # button: touchpad on
            buttonTouchpadOn = QtGui.QPushButton(
                "touchpad on",
                self
            )
            buttonTouchpadOn.clicked.connect(
                lambda: self.touchpad_switch(status = "on")
            )
            buttonsList.append(buttonTouchpadOn)
            # button: touchpad off
            buttonTouchpadOff = QtGui.QPushButton(
                "touchpad off",
                self
            )
            buttonTouchpadOff.clicked.connect(
                lambda: self.touchpad_switch(status = "off")
            )
            buttonsList.append(buttonTouchpadOff)
            # button: nipple on
            buttonNippleOn = QtGui.QPushButton(
                "nipple on",
                self
            )
            buttonNippleOn.clicked.connect(
                lambda: self.nipple_switch(status = "on")
            )
            buttonsList.append(buttonNippleOn)
            # button: nipple off
            buttonNippleOff = QtGui.QPushButton(
                "nipple off",
                self
            )
            buttonNippleOff.clicked.connect(
                lambda: self.nipple_switch(status = "off")
            )
            buttonsList.append(buttonNippleOff)
            # button: stylus proximity monitoring on
            buttonStylusProximityControlOn = QtGui.QPushButton(
                "stylus proximity monitoring on",
                self
            )
            buttonStylusProximityControlOn.clicked.connect(
                lambda: self.stylus_proximity_control_switch(status = "on")
            )
            buttonsList.append(buttonStylusProximityControlOn)
            # button: stylus proximity monitoring off
            buttonStylusProximityControlOff = QtGui.QPushButton(
                "stylus proximity monitoring off",
                self
            )
            buttonStylusProximityControlOff.clicked.connect(
                lambda: self.stylus_proximity_control_switch(status = "off")
            )
            buttonsList.append(buttonStylusProximityControlOff)
            # button: acceleration monitoring on
            buttonAccelerationControlOn = QtGui.QPushButton(
                "acceleration monitoring on",
                self
            )
            buttonAccelerationControlOn.clicked.connect(
                lambda: self.acceleration_control_switch(status = "on")
            )
            buttonsList.append(buttonAccelerationControlOn)
            # button: acceleration monitoring off
            buttonAccelerationControlOff = QtGui.QPushButton(
                "acceleration monitoring off",
                self
            )
            buttonAccelerationControlOff.clicked.connect(
                lambda: self.acceleration_control_switch(status = "off")
            )
            buttonsList.append(buttonAccelerationControlOff)
            # button: display position monitoring on
            buttondisplay_position_controlOn = QtGui.QPushButton(
                "display position monitoring on",
                self
            )
            buttondisplay_position_controlOn.clicked.connect(
                lambda: self.display_position_control_switch(status = "on")
            )
            buttonsList.append(buttondisplay_position_controlOn)
            # button: display position monitoring off
            buttondisplay_position_controlOff = QtGui.QPushButton(
                "display position monitoring off",
                self
            )
            buttondisplay_position_controlOff.clicked.connect(
                lambda: self.display_position_control_switch(status = "off")
            )
            buttonsList.append(buttondisplay_position_controlOff)
            # set button dimensions
            buttonsWidth  = 240
            buttonsHeight = 30
            for button in buttonsList:
                button.setFixedSize(buttonsWidth, buttonsHeight)
                button.setStyleSheet(
                    """
                    color: #000000;
                    background-color: #ffffff;
                    border: 1px solid #000000;
                    font-size: 10pt;
                    text-align: left;
                    padding-left: 10px;
                    padding-right: 10px;
                    """
                )
            # set layout
            vbox = QtGui.QVBoxLayout()
            vbox.addStretch(1)
            for button in buttonsList:
                vbox.addWidget(button)
                vbox.addStretch(1)	
            self.setLayout(vbox)
            # window
            self.setWindowTitle("spin")
            # set window position
            self.move(0, 0)
            self.show()
        elif options["--nogui"]:
            log.info("non-GUI mode")

    def close_event(self, event):
        log.info("terminate {name}".format(name = name))
        self.stylus_proximity_control_switch(status = "off")
        self.display_position_control_switch(status = "off")
        self.deleteLater() 

    def display_orientation(
        self,
        orientation = None
        ):
        if orientation in ["left", "right", "inverted", "normal"]:
            log.info("change display to {orientation}".format(
                orientation = orientation
            ))
            engage_command(
                "xrandr -o {orientation}".format(
                    orientation = orientation
                )
            )
        else:
            log.error(
                "unknown display orientation \"{orientation}\" "
                "requested".format(
                    orientation = orientation
                )
            )
            sys.exit()

    def touchscreen_orientation(
        self,
        orientation = None
        ):
        if "touchscreen" in self.deviceNames:
            coordinateTransformationMatrix = {
                "left":     "0 -1 1 1 0 0 0 0 1",
                "right":    "0 1 0 -1 0 1 0 0 1",
                "inverted": "-1 0 1 0 -1 1 0 0 1",
                "normal":   "1 0 0 0 1 0 0 0 1"
            }
            if coordinateTransformationMatrix.has_key(orientation):
                log.info("change touchscreen to {orientation}".format(
                    orientation = orientation
                ))
                engage_command(
                    "xinput set-prop \"{deviceName}\" \"Coordinate "
                    "Transformation Matrix\" "
                    "{matrix}".format(
                        deviceName = self.deviceNames["touchscreen"],
                        matrix = coordinateTransformationMatrix[orientation]
                    )
                )
            else:
                log.error(
                    "unknown touchscreen orientation \"{orientation}\""
                    " requested".format(
                        orientation = orientation
                    )
                )
                sys.exit()
        else:
            log.debug("touchscreen orientation unchanged")

    def touchscreen_switch(
        self,
        status = None
        ):
        if "touchscreen" in self.deviceNames:
            xinputStatus = {
                "on":  "enable",
                "off": "disable"
            }
            if xinputStatus.has_key(status):
                log.info("change touchscreen to {status}".format(
                    status = status
                ))
                engage_command(
                    "xinput {status} \"{deviceName}\"".format(
                        status = xinputStatus[status],
                        deviceName = self.deviceNames["touchscreen"]
                    )
                )
            else:
                _message = "unknown touchscreen status \"{status}\" " +\
                           "requested"
                log.error(
                    _message.format(
                        status = status
                    )
                )
                sys.exit()
        else:
            log.debug("touchscreen status unchanged")

    def touchpad_orientation(
        self,
        orientation = None
        ):
        if "touchpad" in self.deviceNames:
            coordinateTransformationMatrix = {
                "left":     "0 -1 1 1 0 0 0 0 1",
                "right":    "0 1 0 -1 0 1 0 0 1",
                "inverted": "-1 0 1 0 -1 1 0 0 1",
                "normal":   "1 0 0 0 1 0 0 0 1"
            }
            if coordinateTransformationMatrix.has_key(orientation):
                log.info("change touchpad to {orientation}".format(
                    orientation = orientation
                ))
                engage_command(
                    "xinput set-prop \"{deviceName}\" \"Coordinate "
                    "Transformation Matrix\" "
                    "{matrix}".format(
                        deviceName = self.deviceNames["touchpad"],
                        matrix = coordinateTransformationMatrix[orientation]
                    )
                )
            else:
                log.error(
                    "unknown touchpad orientation \"{orientation}\""
                    " requested".format(
                        orientation = orientation
                    )
                )
                sys.exit()
        else:
            log.debug("touchpad orientation unchanged")

    def touchpad_switch(
        self,
        status = None
        ):
        if "touchpad" in self.deviceNames:
            xinputStatus = {
                "on":  "enable",
                "off": "disable"
            }
            if xinputStatus.has_key(status):
                log.info("change touchpad to {status}".format(
                    status = status
                ))
                engage_command(
                    "xinput {status} \"{deviceName}\"".format(
                        status = xinputStatus[status],
                        deviceName = self.deviceNames["touchpad"]
                    )
                )
            else:
                _message = "unknown touchpad status \"{status}\" " +\
                           "requested"
                log.error(
                    _message.format(
                        status = status
                    )
                )
                sys.exit()
        else:
            log.debug("touchpad status unchanged")

    def nipple_switch(
        self,
        status = None
        ):
        if "nipple" in self.deviceNames:
            xinputStatus = {
                "on":  "enable",
                "off": "disable"
            }
            if xinputStatus.has_key(status):
                log.info("change nipple to {status}".format(
                    status = status
                ))
                engage_command(
                    "xinput {status} \"{deviceName}\"".format(
                        status = xinputStatus[status],
                        deviceName = self.deviceNames["nipple"]
                    )
                )
            else:
                _message = "unknown nipple status \"{status}\" " +\
                           "requested"
                log.error(
                    _message.format(
                        status = status
                    )
                )
                sys.exit()
        else:
            log.debug("nipple status unchanged")

    def stylus_proximity_control(
        self
        ):
        self.previousStylusProximityStatus = None
        while True:
            stylusProximityCommand = "xinput query-state " + \
                                     "\"Wacom ISDv4 EC Pen stylus\" | " + \
                                     "grep Proximity | cut -d \" \" -f3 | " + \
                                     " cut -d \"=\" -f2"
            self.stylusProximityStatus = subprocess.check_output(
                stylusProximityCommand,
                shell = True
            ).lower().rstrip()
            if \
                (self.stylusProximityStatus == "out") and \
                (self.previousStylusProximityStatus != "out"):
                log.info("stylus inactive")
                self.touchscreen_switch(status = "on")
            elif \
                (self.stylusProximityStatus == "in") and \
                (self.previousStylusProximityStatus != "in"):
                log.info("stylus active")
                self.touchscreen_switch(status = "off")
            self.previousStylusProximityStatus = self.stylusProximityStatus
            time.sleep(0.15)

    def stylus_proximity_control_switch(
        self,
        status = None
        ):
        if status == "on":
            log.info("change stylus proximity control to on")
            self.processStylusProximityControl = multiprocessing.Process(
                target = self.stylus_proximity_control
            )
            self.processStylusProximityControl.start()
        elif status == "off":
            log.info("change stylus proximity control to off")
            self.processStylusProximityControl.terminate()
        else:
            log.error(
                "unknown stylus proximity control status \"{status}\" "
                "requested".format(
                    status = status
                )
            )
            sys.exit()

    def acceleration_control(self):
        while True:
            # Get the mean of recent acceleration vectors.
            numberOfMeasurements = 3
            measurements = []
            for measurement in range(0, numberOfMeasurements):
                measurements.append(AccelerationVector())
            stableAcceleration = mean_list(lists = measurements)
            log.info("stable acceleration vector: {vector}".format(
                vector = stableAcceleration
            ))
            tableOrientations = {
                (True,  True):  "right",
                (True,  False): "left",
                (False, True):  "inverted",
                (False, False): "normal"
            }
            orientation = tableOrientations[(
                abs(stableAcceleration[0]) > abs(stableAcceleration[1]),
                stableAcceleration[0] > 0
            )]
            self.engage_mode(mode = orientation)
            time.sleep(0.15)

    def acceleration_control_switch(
        self,
        status = None
        ):
        if status == "on":
            log.info("change acceleration control to on")
            self.processAccelerationControl = multiprocessing.Process(
                target = self.acceleration_control
            )
            self.processAccelerationControl.start()
        elif status == "off":
            log.info("change acceleration control to off")
            self.processAccelerationControl.terminate()
        else:
            log.error(
                "unknown acceleration control status \"{status}\" "
                "requested".format(
                    status = status
                )
            )
            sys.exit()

    def display_position_control(self):
        socketACPI = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        socketACPI.connect("/var/run/acpid.socket")
        log.info("display position is {displayPositionStatus}".format(
            displayPositionStatus = self.displayPositionStatus
            )
        )
        while True:
            eventACPI = socketACPI.recv(4096)
            # Ubuntu 13.10 compatibility:
            #eventACPIDisplayPositionChange = \
            #    "ibm/hotkey HKEY 00000080 000060c0\n"
            # Ubuntu 14.04 compatibility:
            eventACPIDisplayPositionChange = \
                "ibm/hotkey LEN0068:00 00000080 000060c0\n"
            if eventACPI == eventACPIDisplayPositionChange:
                log.info("display position change")
                if self.displayPositionStatus == "laptop":
                    self.engage_mode(mode = "tablet")
                    self.displayPositionStatus = "tablet"
                    log.info(
                        "display position is {displayPositionStatus}".format(
                            displayPositionStatus = self.displayPositionStatus
                        )
                    )
                elif self.displayPositionStatus == "tablet":
                    self.engage_mode(mode = "laptop")
                    self.displayPositionStatus = "laptop"
                    log.info(
                        "display position is {displayPositionStatus}".format(
                            displayPositionStatus = self.displayPositionStatus
                        )
                    )
            time.sleep(0.15)

    def display_position_control_switch(
        self,
        status = None
        ):
        if status == "on":
            log.info("change display position control to on")
            self.processdisplay_position_control = multiprocessing.Process(
                target = self.display_position_control
            )
            self.processdisplay_position_control.start()
        elif status == "off":
            log.info("change display position control to off")
            self.processdisplay_position_control.terminate()
        else:
            log.error(
                "unknown display position control status \"{orientation}\" "
                "requested".format(
                    status = status
                )
            )
            sys.exit()

    def engage_mode(
        self,
        mode = None
        ):
        log.info("engage mode {mode}".format(
            mode = mode
        ))
        if mode == "tablet":
            self.display_orientation(orientation     = "left")
            self.touchscreen_orientation(orientation = "left")
            self.touchpad_switch(status              = "off")
            self.nipple_switch(status                = "off") 
        elif mode == "laptop":
            self.display_orientation(orientation     = "normal")
            self.touchscreen_orientation(orientation = "normal")
            self.touchscreen_switch(status           = "on")
            self.touchpad_orientation(orientation    = "normal")
            self.touchpad_switch(status              = "on")
            self.nipple_switch(status                = "on")
        elif mode in ["left", "right", "inverted", "normal"]:
            self.display_orientation(orientation     = mode)
            self.touchscreen_orientation(orientation = mode)
            self.touchpad_orientation(orientation    = mode)
        else:
            log.error(
                "unknown mode \"{mode}\" requested".format(
                    mode = mode
                )
            )
            sys.exit()

def get_inputs():
    log.info("audit inputs")
    inputDevices = subprocess.Popen(
        ["xinput", "--list"],
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    ).communicate()[0]
    devicesAndKeyphrases = {
        "touchscreen": ["SYNAPTICS Synaptics Touch Digitizer V04",
                        "ELAN Touchscreen"],
        "touchpad":    ["PS/2 Synaptics TouchPad",
                        "SynPS/2 Synaptics TouchPad"],
        "nipple":      ["TPPS/2 IBM TrackPoint"],
        "stylus":      ["Wacom ISDv4 EC Pen stylus"]
    }
    deviceNames = {}
    for device, keyphrases in devicesAndKeyphrases.iteritems():
        for keyphrase in keyphrases:
            if keyphrase in inputDevices:
                deviceNames[device] = keyphrase
    for device, keyphrases in devicesAndKeyphrases.iteritems():
        if device in deviceNames:
            log.info("input {device} detected as \"{deviceName}\"".format(
                device     = device,
                deviceName = deviceNames[device]
            ))
        else:
            log.info("input {device} not detected".format(
                device = device
            ))
    return(deviceNames)

def engage_command(
    command = None
    ):
    if options["--debugpassive"] is True:
        log.info("command: {command}".format(
            command = command
        ))
    else:
        os.system(command)

def mean_list(
    lists = None
    ):
    return([sum(element)/len(element) for element in zip(*lists)])

class AccelerationVector(list):

    def __init__(self):
        list.__init__(self)  
        # Access the IIO interface to the accelerometer.
        devicesDirectories = glob.glob("/sys/bus/iio/devices/iio:device*")
        for directory in devicesDirectories:
            if "accel_3d" in open(os.path.join(directory, "name")).read():
                self.accelerometerDirectory = directory
        self.accelerometerScaleFileFullPath =\
            self.accelerometerDirectory + "/" + "in_accel_scale"
        self.accelerometerAxisxFileFullPath =\
            self.accelerometerDirectory + "/" + "in_accel_x_raw"
        self.accelerometerAxisyFileFullPath =\
            self.accelerometerDirectory + "/" + "in_accel_y_raw"
        self.accelerometerAxiszFileFullPath =\
            self.accelerometerDirectory + "/" + "in_accel_z_raw"
        self.accelerometerScaleFile = open(self.accelerometerScaleFileFullPath)
        self.accelerometerAxisxFile = open(self.accelerometerAxisxFileFullPath)
        self.accelerometerAxisyFile = open(self.accelerometerAxisyFileFullPath)
        self.accelerometerAxiszFile = open(self.accelerometerAxiszFileFullPath)
        # Access the scale.
        self.scale = float(self.accelerometerScaleFile.read())
        # Initialise the vector.
        self.extend([0, 0, 0])
        self.update()

    def update(self):
        # Access the acceleration.
        self.accelerometerAxisxFile.seek(0)
        self.accelerometerAxisyFile.seek(0)
        self.accelerometerAxiszFile.seek(0)
        acceleration_x = float(self.accelerometerAxisxFile.read()) * self.scale
        acceleration_y = float(self.accelerometerAxisyFile.read()) * self.scale
        acceleration_z = float(self.accelerometerAxiszFile.read()) * self.scale
        # Update the vector.
        self[0] = acceleration_x
        self[1] = acceleration_y
        self[2] = acceleration_z

    def __repr__(self):
        self.update()
        return(list.__repr__(self))

def main(options):

    # logging
    logging.basicConfig()
    global log
    log       = logging.getLogger(__name__)
    log.level = logging.INFO

    application = QtGui.QApplication(sys.argv)
    interface1  = interface(options)
    sys.exit(application.exec_())

if __name__ == "__main__":
    options = docopt.docopt(__doc__)
    if options["--version"]:
        print(version)
        exit()
    main(options)
