#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# spin                                                                         #
#                                                                              #
# version: 2014-01-01T2346                                                     #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# The program spin provides an interface for control of the usage modes of     #
# laptop-tablet and similar computer interface devices.                        #
#	                                                                       #
# copyright (C) 2013 2014 William Breaden Madden                              #
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
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for    #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################
"""

import os
import sys
import subprocess
from PyQt4 import QtGui
import logging

# logging
logger = logging.getLogger(__name__)
logging.basicConfig()
logger.level = logging.INFO

class interface(QtGui.QWidget):
    def __init__(self):
        super(interface, self).__init__()
        # create buttons
        buttonsList = []
        # button: tablet mode
        buttonModeTablet = QtGui.QPushButton('tablet mode', self)
        buttonModeTablet.clicked.connect(self.engageModeTablet)
        buttonsList.append(buttonModeTablet)
        # button: laptop mode
        buttonModeLaptop = QtGui.QPushButton('laptop mode', self)
        buttonModeLaptop.clicked.connect(self.engageModeLaptop)
        buttonsList.append(buttonModeLaptop)
        # button: left
        buttonLeft = QtGui.QPushButton('left', self)
        buttonLeft.clicked.connect(self.engageLeft)
        buttonsList.append(buttonLeft)
        # button: right
        buttonRight = QtGui.QPushButton('right', self)
        buttonRight.clicked.connect(self.engageRight)
        buttonsList.append(buttonRight)
        # button: inverted
        buttonInverted = QtGui.QPushButton('inverted', self)
        buttonInverted.clicked.connect(self.engageInverted)
        buttonsList.append(buttonInverted)
        # button: normal
        buttonNormal = QtGui.QPushButton('normal', self)
        buttonNormal.clicked.connect(self.engageNormal)
        buttonsList.append(buttonNormal)
        # button: touchscreen on
        buttonTouchscreenOn = QtGui.QPushButton('touchscreen on', self)
        buttonTouchscreenOn.clicked.connect(self.engageTouchscreenOn)
        buttonsList.append(buttonTouchscreenOn)
        # button: touchscreen off
        buttonTouchscreenOff = QtGui.QPushButton('touchscreen off', self)
        buttonTouchscreenOff.clicked.connect(self.engageTouchscreenOff)
        buttonsList.append(buttonTouchscreenOff)
        # button: touchpad on
        buttonTouchpadOn = QtGui.QPushButton('touchpad on', self)
        buttonTouchpadOn.clicked.connect(self.engageTouchpadOn)
        buttonsList.append(buttonTouchpadOn)
        # button: touchpad off
        buttonTouchpadOff = QtGui.QPushButton('touchpad off', self)
        buttonTouchpadOff.clicked.connect(self.engageTouchpadOff)
        buttonsList.append(buttonTouchpadOff)
        # button: nipple on
        buttonNippleOn = QtGui.QPushButton('nipple on', self)
        buttonNippleOn.clicked.connect(self.engageNippleOn)
        buttonsList.append(buttonNippleOn)
        # button: nipple off
        buttonNippleOff = QtGui.QPushButton('nipple off', self)
        buttonNippleOff.clicked.connect(self.engageNippleOff)
        buttonsList.append(buttonNippleOff)
        # set button dimensions
        buttonsWidth=150
        buttonsHeight=60
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
        self.setGeometry(200, 200, 150, 100)
        self.setWindowTitle('spin')
        self.show()
    def displayLeft(self):
        logger.info("changing display to left")
        os.system('xrandr -o left')
    def displayRight(self):
        logger.info("changing display to right")
        os.system('xrandr -o right')
    def displayInverted(self):
        logger.info("changing display to inverted")
        os.system('xrandr -o inverted')
    def displayNormal(self):
        logger.info("changing display to normal")
        os.system('xrandr -o normal')
    def touchscreenLeft(self):
        logger.info("changing touchscreen to left")
        os.system('xinput set-prop "ELAN Touchscreen" "Coordinate Transformation Matrix" 0 -1 1 1 0 0 0 0 1')
    def touchscreenRight(self):
        logger.info("changing touchscreen to right")
        os.system('xinput set-prop "ELAN Touchscreen" "Coordinate Transformation Matrix" 0 1 0 -1 0 1 0 0 1')
    def touchscreenInverted(self):
        logger.info("changing touchscreen to inverted")
        os.system('xinput set-prop "ELAN Touchscreen" "Coordinate Transformation Matrix" -1 0 1 0 -1 1 0 0 1')
    def touchscreenNormal(self):
        logger.info("changing touchscreen to normal")
        os.system('xinput set-prop "ELAN Touchscreen" "Coordinate Transformation Matrix" 1 0 0 0 1 0 0 0 1')
    def touchscreenOn(self):
        logger.info("changing touchscreen to on")
        os.system('xinput enable "ELAN Touchscreen"')
    def touchscreenOff(self):
        logger.info("changing touchscreen to off")
        os.system('xinput disable "ELAN Touchscreen"')
    def touchpadOn(self):
        logger.info("changing touchpad to on")
        os.system('xinput enable "SynPS/2 Synaptics TouchPad"')
    def touchpadOff(self):
        logger.info("changing touchpad to off")
        os.system('xinput disable "SynPS/2 Synaptics TouchPad"')
    def nippleOn(self):
        logger.info("changing nipple to on")
        os.system('xinput enable "TPPS/2 IBM TrackPoint"')
    def nippleOff(self):
        logger.info("changing nipple to off")
        os.system('xinput disable "TPPS/2 IBM TrackPoint"')
    def engageModeTablet(self):
        logger.info("engaging mode tablet")
        self.displayLeft()
	self.touchscreenLeft()
        self.touchscreenOff()
        self.touchpadOff()
        self.nippleOff()
    def engageModeLaptop(self):
        logger.info("engaging mode laptop")
        self.displayNormal()
        self.touchscreenNormal()
        self.touchscreenOn()
        self.touchpadOn()
        self.nippleOn()
    def engageLeft(self):
        logger.info("engaging mode left")
        self.displayLeft()
        self.touchscreenLeft()
    def engageRight(self):
        logger.info("engaging mode right")
        self.displayRight()
        self.touchscreenRight()
    def engageInverted(self):
        logger.info("engaging mode inverted")
        self.displayInverted()
        self.touchscreenInverted()
    def engageNormal(self):
        logger.info("engaging mode normal")
        self.displayNormal()
        self.touchscreenNormal()
    def engageTouchscreenOn(self):
        self.touchscreenOn()
    def engageTouchscreenOff(self):
        self.touchscreenOff()
    def engageTouchpadOn(self):
        self.touchpadOn()
    def engageTouchpadOff(self):
        self.touchpadOff()
    def engageNippleOn(self):
        self.nippleOn()
    def engageNippleOff(self):
        self.nippleOff()
def main():
    logger.info("running spin")
    application = QtGui.QApplication(sys.argv)
    interface1 = interface()
    sys.exit(application.exec_())
if __name__ == '__main__':
    main()