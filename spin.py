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
# copyright (C) 2013 2014 William Breaden Madden                               #
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
version = "2015-03-16T2207Z"

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
        log.info("run spin")
        # engage stylus proximity control
        self.stylusProximityControlSwitch(status = "on")
        # engage display position control
        self.displayPositionStatus = "laptop"
        self.displayPositionControlSwitch(status = "on")
        if not options["--nogui"]:
            # create buttons
            buttonsList = []
            # button: tablet mode
            buttonModeTablet = QtGui.QPushButton(
                "tablet mode",
                self
            )
            buttonModeTablet.clicked.connect(
                lambda: self.engageMode(mode = "tablet")
            )
            buttonsList.append(buttonModeTablet)
            # button: laptop mode
            buttonModeLaptop = QtGui.QPushButton(
                "laptop mode",
                self
            )
            buttonModeLaptop.clicked.connect(
                lambda: self.engageMode(mode = "laptop")
            )
            buttonsList.append(buttonModeLaptop)
            # button: left
            buttonLeft = QtGui.QPushButton(
                "left",
                self
            )
            buttonLeft.clicked.connect(
                lambda: self.engageMode(mode = "left")
            )
            buttonsList.append(buttonLeft)
            # button: right
            buttonRight = QtGui.QPushButton(
                "right", self
            )
            buttonRight.clicked.connect(
                lambda: self.engageMode(mode = "right")
            )
            buttonsList.append(buttonRight)
            # button: inverted
            buttonInverted = QtGui.QPushButton(
                "inverted",
                self
            )
            buttonInverted.clicked.connect(
                lambda: self.engageMode(mode = "inverted")
            )
            buttonsList.append(buttonInverted)
            # button: normal
            buttonNormal = QtGui.QPushButton(
                "normal",
                self
            )
            buttonNormal.clicked.connect(
                lambda: self.engageMode(mode = "normal")
            )
            buttonsList.append(buttonNormal)
            # button: touchscreen on
            buttonTouchscreenOn = QtGui.QPushButton(
                "touchscreen on",
                self
            )
            buttonTouchscreenOn.clicked.connect(
                lambda: self.touchscreenSwitch(status = "on")
            )
            buttonsList.append(buttonTouchscreenOn)
            # button: touchscreen off
            buttonTouchscreenOff = QtGui.QPushButton(
                "touchscreen off",
                self
            )
            buttonTouchscreenOff.clicked.connect(
                lambda: self.touchscreenSwitch(status = "off")
            )
            buttonsList.append(buttonTouchscreenOff)
            # button: touchpad on
            buttonTouchpadOn = QtGui.QPushButton(
                "touchpad on",
                self
            )
            buttonTouchpadOn.clicked.connect(
                lambda: self.touchpadSwitch(status = "on")
            )
            buttonsList.append(buttonTouchpadOn)
            # button: touchpad off
            buttonTouchpadOff = QtGui.QPushButton(
                "touchpad off",
                self
            )
            buttonTouchpadOff.clicked.connect(
                lambda: self.touchpadSwitch(status = "off")
            )
            buttonsList.append(buttonTouchpadOff)
            # button: nipple on
            buttonNippleOn = QtGui.QPushButton(
                "nipple on",
                self
            )
            buttonNippleOn.clicked.connect(
                lambda: self.nippleSwitch(status = "on")
            )
            buttonsList.append(buttonNippleOn)
            # button: nipple off
            buttonNippleOff = QtGui.QPushButton(
                "nipple off",
                self
            )
            buttonNippleOff.clicked.connect(
                lambda: self.nippleSwitch(status = "off")
            )
            buttonsList.append(buttonNippleOff)
            # button: stylus proximity monitoring on
            buttonStylusProximityControlOn = QtGui.QPushButton(
                "stylus proximity monitoring on",
                self
            )
            buttonStylusProximityControlOn.clicked.connect(
                lambda: self.stylusProximityControlSwitch(status = "on")
            )
            buttonsList.append(buttonStylusProximityControlOn)
            # button: stylus proximity monitoring off
            buttonStylusProximityControlOff = QtGui.QPushButton(
                "stylus proximity monitoring off",
                self
            )
            buttonStylusProximityControlOff.clicked.connect(
                lambda: self.stylusProximityControlSwitch(status = "off")
            )
            buttonsList.append(buttonStylusProximityControlOff)
            # button: display position monitoring on
            buttonDisplayPositionControlOn = QtGui.QPushButton(
                "display position monitoring on",
                self
            )
            buttonDisplayPositionControlOn.clicked.connect(
                lambda: self.displayPositionControlSwitch(status = "on")
            )
            buttonsList.append(buttonDisplayPositionControlOn)
            # button: display position monitoring off
            buttonDisplayPositionControlOff = QtGui.QPushButton(
                "display position monitoring off",
                self
            )
            buttonDisplayPositionControlOff.clicked.connect(
                lambda: self.displayPositionControlSwitch(status = "off")
            )
            buttonsList.append(buttonDisplayPositionControlOff)
            # set button dimensions
            buttonsWidth  = 250
            buttonsHeight = 50
            for button in buttonsList:
                button.setFixedSize(buttonsWidth, buttonsHeight)
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
    def closeEvent(self, event):
        log.info("stopping spin")
        self.stylusProximityControlSwitch(status = "off")
        self.displayPositionControlSwitch(status = "off")
        self.deleteLater() 
    def displayOrientation(
        self,
        orientation = None
        ):
        if orientation in ["left", "right", "inverted", "normal"]:
            log.info("change display to {orientation}".format(
                orientation = orientation
            ))
            engageCommand(
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
    def touchscreenOrientation(
        self,
        orientation = None
        ):
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
            engageCommand(
                "xinput set-prop \"ELAN Touchscreen\" \"Coordinate "
                "Transformation Matrix\" "
                "{matrix}".format(
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
    def touchscreenSwitch(
        self,
        status = None
        ):
        xinputStatus = {
            "on":  "enable",
            "off": "disable"
        }
        if xinputStatus.has_key(status):
            log.info("change touchscreen to {status}".format(
                status = status
            ))
            engageCommand(
                "xinput {status} \"ELAN Touchscreen\"".format(
                    status = xinputStatus[status]
                )
            )
        else:
            log.error(
                "unknown touchscreen status \"{orientation}\" requested".format(
                    status = status
                )
            )
            sys.exit()
    def touchpadSwitch(
        self,
        status = None
        ):
        xinputStatus = {
            "on":  "enable",
            "off": "disable"
        }
        if xinputStatus.has_key(status):
            log.info("change touchpad to {status}".format(
                status = status
            ))
            engageCommand(
                "xinput {status} \"SynPS/2 Synaptics TouchPad\"".format(
                    status = xinputStatus[status]
                )
            )
        else:
            log.error(
                "unknown touchpad status \"{orientation}\" requested".format(
                    status = status
                )
            )
            sys.exit()
    def nippleSwitch(
        self,
        status = None
        ):
        xinputStatus = {
            "on":  "enable",
            "off": "disable"
        }
        if xinputStatus.has_key(status):
            log.info("change nipple to {status}".format(
                status = status
            ))
            engageCommand(
                "xinput {status} \"TPPS/2 IBM TrackPoint\"".format(
                    status = xinputStatus[status]
                )
            )
        else:
            log.error(
                "unknown nipple status \"{orientation}\" requested".format(
                    status = status
                )
            )
            sys.exit()
    def stylusProximityControl(self):
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
                self.touchscreenSwitch(status = "on")
            elif \
                (self.stylusProximityStatus == "in") and \
                (self.previousStylusProximityStatus != "in"):
                log.info("stylus active")
                self.touchscreenSwitch(status = "off")
            self.previousStylusProximityStatus = self.stylusProximityStatus
            time.sleep(0.25)
    def stylusProximityControlSwitch(
        self,
        status = None
        ):
        if status == "on":
            log.info("change stylus proximity control to on")
            self.processStylusProximityControl = multiprocessing.Process(
                target = self.stylusProximityControl
            )
            self.processStylusProximityControl.start()
        elif status == "off":
            log.info("change stylus proximity control to off")
            self.processStylusProximityControl.terminate()
        else:
            log.error(
                "unknown stylus proximity control status \"{orientation}\" "
                "requested".format(
                    status = status
                )
            )
            sys.exit()
    def displayPositionControl(self):
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
                    self.engageMode(mode = "tablet")
                    self.displayPositionStatus = "tablet"
                    log.info(
                        "display position is {displayPositionStatus}".format(
                            displayPositionStatus = self.displayPositionStatus
                        )
                    )
                elif self.displayPositionStatus == "tablet":
                    self.engageMode(mode = "laptop")
                    self.displayPositionStatus = "laptop"
                    log.info(
                        "display position is {displayPositionStatus}".format(
                            displayPositionStatus = self.displayPositionStatus
                        )
                    )
            time.sleep(0.25)
    def displayPositionControlSwitch(
        self,
        status = None
        ):
        if status == "on":
            log.info("change display position control to on")
            self.processDisplayPositionControl = multiprocessing.Process(
                target = self.displayPositionControl
            )
            self.processDisplayPositionControl.start()
        elif status == "off":
            log.info("change display position control to off")
            self.processDisplayPositionControl.terminate()
        else:
            log.error(
                "unknown display position control status \"{orientation}\" "
                "requested".format(
                    status = status
                )
            )
            sys.exit()
    def engageMode(
        self,
        mode = None
        ):
        log.info("engage mode {mode}".format(
            mode = mode
        ))
        if mode == "tablet":
            self.displayOrientation(orientation     = "left")
            self.touchscreenOrientation(orientation = "left")
            self.touchpadSwitch(status              = "off")
            self.nippleSwitch(status                = "off") 
        elif mode == "laptop":
            self.displayOrientation(orientation     = "normal")
            self.touchscreenOrientation(orientation = "normal")
            self.touchscreenSwitch(status           = "on")
            self.touchpadSwitch(status              = "on")
            self.nippleSwitch(status                = "on")
        elif mode in ["left", "right", "inverted", "normal"]:
            self.displayOrientation(orientation     = mode)
            self.touchscreenOrientation(orientation = mode)
        else:
            log.error(
                "unknown mode \"{mode}\" requested".format(
                    mode = mode
                )
            )
            sys.exit()

def engageCommand(command = None):
    if options["--debugpassive"] is True:
        log.debug("command: {command}".format(
            command = command
        ))
    else:
        os.system(command)

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
