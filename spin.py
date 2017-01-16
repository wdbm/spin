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
    -h,--help                display help message
    --version                display version and exit
    -v, --verbose            verbose logging
    -s, --silent             silent
    -u, --username=USERNAME  username
    --nogui                  non-GUI mode
    --debugpassive           display commands without executing
"""

name    = "spin"
version = "2017-01-16T1950Z"
logo    = None

import docopt
import glob
import logging
import multiprocessing
import os
import socket
import subprocess
import sys
import time

import propyte
from PyQt4 import QtGui

def main(options):

    global program
    program = propyte.Program(
        options = options,
        name    = name,
        version = version,
        logo    = logo
    )
    global log
    from propyte import log

    application = QtGui.QApplication(sys.argv)
    interface = Interface(options)
    sys.exit(application.exec_())

class Interface(QtGui.QWidget):

    def __init__(
        self,
        options = None
        ):
        self.options = options
        super(Interface, self).__init__()
        log.info("initiate {name}".format(name = name))
        # Audit the inputs available.
        self.names_devices = get_inputs()
        if options["--debugpassive"] is True:
            log.info("device names: {names_devices}".format(
                names_devices = self.names_devices
            ))
        # engage stylus proximity control
        self.stylus_proximity_control_switch(status = "on")
        # engage acceleration control
        #self.acceleration_control_switch(status = "on")
        # engage display position control
        self.display_position_status = "laptop"
        self.display_position_control_switch(status = "on")
        if not options["--nogui"]:
            # create buttons
            buttons_list = []
            # button: tablet mode
            button_mode_tablet = QtGui.QPushButton(
                "tablet mode",
                self
            )
            button_mode_tablet.clicked.connect(
                lambda: self.engage_mode(mode = "tablet")
            )
            buttons_list.append(button_mode_tablet)
            # button: laptop mode
            button_mode_laptop = QtGui.QPushButton(
                "laptop mode",
                self
            )
            button_mode_laptop.clicked.connect(
                lambda: self.engage_mode(mode = "laptop")
            )
            buttons_list.append(button_mode_laptop)
            # button: left
            button_left = QtGui.QPushButton(
                "left",
                self
            )
            button_left.clicked.connect(
                lambda: self.engage_mode(mode = "left")
            )
            buttons_list.append(button_left)
            # button: right
            button_right = QtGui.QPushButton(
                "right", self
            )
            button_right.clicked.connect(
                lambda: self.engage_mode(mode = "right")
            )
            buttons_list.append(button_right)
            # button: inverted
            button_inverted = QtGui.QPushButton(
                "inverted",
                self
            )
            button_inverted.clicked.connect(
                lambda: self.engage_mode(mode = "inverted")
            )
            buttons_list.append(button_inverted)
            # button: normal
            button_normal = QtGui.QPushButton(
                "normal",
                self
            )
            button_normal.clicked.connect(
                lambda: self.engage_mode(mode = "normal")
            )
            buttons_list.append(button_normal)
            # button: touchscreen on
            button_touchscreen_on = QtGui.QPushButton(
                "touchscreen on",
                self
            )
            button_touchscreen_on.clicked.connect(
                lambda: self.touchscreen_switch(status = "on")
            )
            buttons_list.append(button_touchscreen_on)
            # button: touchscreen off
            button_touchscreen_off = QtGui.QPushButton(
                "touchscreen off",
                self
            )
            button_touchscreen_off.clicked.connect(
                lambda: self.touchscreen_switch(status = "off")
            )
            buttons_list.append(button_touchscreen_off)
            # button: touchpad on
            button_touchpad_on = QtGui.QPushButton(
                "touchpad on",
                self
            )
            button_touchpad_on.clicked.connect(
                lambda: self.touchpad_switch(status = "on")
            )
            buttons_list.append(button_touchpad_on)
            # button: touchpad off
            button_touchpad_off = QtGui.QPushButton(
                "touchpad off",
                self
            )
            button_touchpad_off.clicked.connect(
                lambda: self.touchpad_switch(status = "off")
            )
            buttons_list.append(button_touchpad_off)
            # button: nipple on
            button_nipple_on = QtGui.QPushButton(
                "nipple on",
                self
            )
            button_nipple_on.clicked.connect(
                lambda: self.nipple_switch(status = "on")
            )
            buttons_list.append(button_nipple_on)
            # button: nipple off
            button_nipple_off = QtGui.QPushButton(
                "nipple off",
                self
            )
            button_nipple_off.clicked.connect(
                lambda: self.nipple_switch(status = "off")
            )
            buttons_list.append(button_nipple_off)
            # button: stylus proximity monitoring on
            button_stylus_proximity_control_on = QtGui.QPushButton(
                "stylus proximity monitoring on",
                self
            )
            button_stylus_proximity_control_on.clicked.connect(
                lambda: self.stylus_proximity_control_switch(status = "on")
            )
            buttons_list.append(button_stylus_proximity_control_on)
            # button: stylus proximity monitoring off
            button_stylus_proximity_control_off = QtGui.QPushButton(
                "stylus proximity monitoring off",
                self
            )
            button_stylus_proximity_control_off.clicked.connect(
                lambda: self.stylus_proximity_control_switch(status = "off")
            )
            buttons_list.append(button_stylus_proximity_control_off)
            # button: acceleration monitoring on
            button_acceleration_control_on = QtGui.QPushButton(
                "acceleration monitoring on",
                self
            )
            button_acceleration_control_on.clicked.connect(
                lambda: self.acceleration_control_switch(status = "on")
            )
            buttons_list.append(button_acceleration_control_on)
            # button: acceleration monitoring off
            button_acceleration_control_off = QtGui.QPushButton(
                "acceleration monitoring off",
                self
            )
            button_acceleration_control_off.clicked.connect(
                lambda: self.acceleration_control_switch(status = "off")
            )
            buttons_list.append(button_acceleration_control_off)
            # button: display position monitoring on
            button_display_position_control_on = QtGui.QPushButton(
                "display position monitoring on",
                self
            )
            button_display_position_control_on.clicked.connect(
                lambda: self.display_position_control_switch(status = "on")
            )
            buttons_list.append(button_display_position_control_on)
            # button: display position monitoring off
            button_display_position_control_off = QtGui.QPushButton(
                "display position monitoring off",
                self
            )
            button_display_position_control_off.clicked.connect(
                lambda: self.display_position_control_switch(status = "off")
            )
            buttons_list.append(button_display_position_control_off)
            # set button dimensions
            buttons_width  = 240
            buttons_height = 30
            for button in buttons_list:
                button.setFixedSize(
                    buttons_width,
                    buttons_height
                )
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
            for button in buttons_list:
                vbox.addWidget(button)
                vbox.addStretch(1)	
            self.setLayout(vbox)
            # window
            self.setWindowTitle(name)
            # set window position
            self.move(0, 0)
            self.show()
        elif options["--nogui"]:
            log.info("non-GUI mode")

    def closeEvent(
        self,
        event
        ):
        self.stylus_proximity_control_switch(status = "off")
        self.display_position_control_switch(status = "off")
        program.terminate()

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
        if "touchscreen" in self.names_devices:
            coordinate_transformation_matrix = {
                "left":     "0 -1 1 1 0 0 0 0 1",
                "right":    "0 1 0 -1 0 1 0 0 1",
                "inverted": "-1 0 1 0 -1 1 0 0 1",
                "normal":   "1 0 0 0 1 0 0 0 1"
            }
            if coordinate_transformation_matrix.has_key(orientation):
                log.info("change touchscreen to {orientation}".format(
                    orientation = orientation
                ))
                engage_command(
                    "xinput set-prop \"{name_device}\" \"Coordinate "
                    "Transformation Matrix\" "
                    "{matrix}".format(
                        name_device = self.names_devices["touchscreen"],
                        matrix = coordinate_transformation_matrix[orientation]
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
        if "touchscreen" in self.names_devices:
            status_xinput = {
                "on":  "enable",
                "off": "disable"
            }
            if status_xinput.has_key(status):
                log.info("change touchscreen to {status}".format(
                    status = status
                ))
                engage_command(
                    "xinput {status} \"{name_device}\"".format(
                        status = status_xinput[status],
                        name_device = self.names_devices["touchscreen"]
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
        if "touchpad" in self.names_devices:
            coordinate_transformation_matrix = {
                "left":     "0 -1 1 1 0 0 0 0 1",
                "right":    "0 1 0 -1 0 1 0 0 1",
                "inverted": "-1 0 1 0 -1 1 0 0 1",
                "normal":   "1 0 0 0 1 0 0 0 1"
            }
            if coordinate_transformation_matrix.has_key(orientation):
                log.info("change touchpad to {orientation}".format(
                    orientation = orientation
                ))
                engage_command(
                    "xinput set-prop \"{name_device}\" \"Coordinate "
                    "Transformation Matrix\" "
                    "{matrix}".format(
                        name_device = self.names_devices["touchpad"],
                        matrix = coordinate_transformation_matrix[orientation]
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
        if "touchpad" in self.names_devices:
            status_xinput = {
                "on":  "enable",
                "off": "disable"
            }
            if status_xinput.has_key(status):
                log.info("change touchpad to {status}".format(
                    status = status
                ))
                engage_command(
                    "xinput {status} \"{name_device}\"".format(
                        status = status_xinput[status],
                        name_device = self.names_devices["touchpad"]
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
        if "nipple" in self.names_devices:
            status_xinput = {
                "on":  "enable",
                "off": "disable"
            }
            if status_xinput.has_key(status):
                log.info("change nipple to {status}".format(
                    status = status
                ))
                engage_command(
                    "xinput {status} \"{name_device}\"".format(
                        status     = status_xinput[status],
                        name_device = self.names_devices["nipple"]
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
        self.previous_stylus_proximity_status = None
        while True:
            stylus_proximity_command = "xinput query-state "                +\
                                     "\"Wacom ISDv4 EC Pen stylus\" | "     +\
                                     "grep Proximity | cut -d \" \" -f3 | " +\
                                     " cut -d \"=\" -f2"
            self.stylus_proximity_status = subprocess.check_output(
                stylus_proximity_command,
                shell = True
            ).lower().rstrip()
            if\
                (self.stylus_proximity_status == "out") and \
                (self.previous_stylus_proximity_status != "out"):
                log.info("stylus inactive")
                self.touchscreen_switch(status = "on")
            elif\
                (self.stylus_proximity_status == "in") and \
                (self.previous_stylus_proximity_status != "in"):
                log.info("stylus active")
                self.touchscreen_switch(status = "off")
            self.previous_stylus_proximity_status = self.stylus_proximity_status
            time.sleep(0.15)

    def stylus_proximity_control_switch(
        self,
        status = None
        ):
        if status == "on":
            log.info("change stylus proximity control to on")
            self.process_stylus_proximity_control = multiprocessing.Process(
                target = self.stylus_proximity_control
            )
            self.process_stylus_proximity_control.start()
        elif status == "off":
            log.info("change stylus proximity control to off")
            self.process_stylus_proximity_control.terminate()
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
            number_of_measurements = 3
            measurements = []
            for measurement in range(0, number_of_measurements):
                measurements.append(Acceleration_Vector())
            stable_acceleration = mean_list(lists = measurements)
            log.info("stable acceleration vector: {vector}".format(
                vector = stable_acceleration
            ))
            table_orientations = {
                (True,  True):  "left",
                (True,  False): "right",
                (False, True):  "inverted",
                (False, False): "normal"
            }
            orientation = table_orientations[(
                abs(stable_acceleration[0]) > abs(stable_acceleration[1]),
                stable_acceleration[0] > 0
            )]
            self.engage_mode(mode = orientation)
            time.sleep(0.15)

    def acceleration_control_switch(
        self,
        status = None
        ):
        if status == "on":
            log.info("change acceleration control to on")
            self.process_acceleration_control = multiprocessing.Process(
                target = self.acceleration_control
            )
            self.process_acceleration_control.start()
        elif status == "off":
            log.info("change acceleration control to off")
            self.process_acceleration_control.terminate()
        else:
            log.error(
                "unknown acceleration control status \"{status}\" "
                "requested".format(
                    status = status
                )
            )
            sys.exit()

    def display_position_control(self):
        socket_ACPI = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        socket_ACPI.connect("/var/run/acpid.socket")
        log.info("display position is {display_position_status}".format(
            display_position_status = self.display_position_status
            )
        )
        while True:
            event_ACPI = socket_ACPI.recv(4096)
            # Ubuntu 13.10 compatibility:
            #event_ACPI_display_position_change = \
            #    "ibm/hotkey HKEY 00000080 000060c0\n"
            # Ubuntu 14.04 compatibility:
            event_ACPI_display_position_change = \
                "ibm/hotkey LEN0068:00 00000080 000060c0\n"
            if event_ACPI == event_ACPI_display_position_change:
                log.info("display position change")
                if self.display_position_status == "laptop":
                    self.engage_mode(mode = "tablet")
                    self.display_position_status = "tablet"
                    log.info(
                        "display position is {display_position_status}".format(
                            display_position_status =\
                                self.display_position_status
                        )
                    )
                elif self.display_position_status == "tablet":
                    self.engage_mode(mode = "laptop")
                    self.display_position_status = "laptop"
                    log.info(
                        "display position is {display_position_status}".format(
                            display_position_status =\
                                self.display_position_status
                        )
                    )
            time.sleep(0.15)

    def display_position_control_switch(
        self,
        status = None
        ):
        if status == "on":
            log.info("change display position control to on")
            self.process_display_position_control = multiprocessing.Process(
                target = self.display_position_control
            )
            self.process_display_position_control.start()
        elif status == "off":
            log.info("change display position control to off")
            self.process_display_position_control.terminate()
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
    devices_input = subprocess.Popen(
        ["xinput", "--list"],
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    ).communicate()[0]
    devices_and_keyphrases = {
        "touchscreen": ["SYNAPTICS Synaptics Touch Digitizer V04",
                        "ELAN Touchscreen"],
        "touchpad":    ["PS/2 Synaptics TouchPad",
                        "SynPS/2 Synaptics TouchPad"],
        "nipple":      ["TPPS/2 IBM TrackPoint"],
        "stylus":      ["Wacom ISDv4 EC Pen stylus"]
    }
    names_devices = {}
    for device, keyphrases in devices_and_keyphrases.iteritems():
        for keyphrase in keyphrases:
            if keyphrase in devices_input:
                names_devices[device] = keyphrase
    for device, keyphrases in devices_and_keyphrases.iteritems():
        if device in names_devices:
            log.info("input {device} detected as \"{name_device}\"".format(
                device     = device,
                name_device = names_devices[device]
            ))
        else:
            log.info("input {device} not detected".format(
                device = device
            ))
    return names_devices

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
    return [sum(element) / len(element) for element in zip(*lists)]

class Acceleration_Vector(list):

    def __init__(
        self
        ):
        list.__init__(self)  
        # Access the IIO interface to the accelerometer.
        directories_devices = glob.glob("/sys/bus/iio/devices/iio:device*")
        for directory in directories_devices:
            if "accel_3d" in open(os.path.join(directory, "name")).read():
                self.directory_accelerometer = directory
        self.accelerometer_scale_file_full_path =\
            self.directory_accelerometer + "/" + "in_accel_scale"
        self.accelerometer_axis_x_file_full_path =\
            self.directory_accelerometer + "/" + "in_accel_x_raw"
        self.accelerometer_axis_y_file_full_path =\
            self.directory_accelerometer + "/" + "in_accel_y_raw"
        self.accelerometer_axis_z_file_full_path =\
            self.directory_accelerometer + "/" + "in_accel_z_raw"
        self.file_accelerometer_scale  = open(
            self.accelerometer_scale_file_full_path
        )
        self.file_accelerometer_axis_x = open(
            self.accelerometer_axis_x_file_full_path
        )
        self.file_accelerometer_axis_y = open(
            self.accelerometer_axis_y_file_full_path
        )
        self.file_accelerometer_axis_z = open(
            self.accelerometer_axis_z_file_full_path
        )
        # Access the scale.
        self.scale = float(self.file_accelerometer_scale.read())
        # Initialise the vector.
        self.extend([0, 0, 0])
        self.update()

    def update(
        self
        ):
        # Access the acceleration.
        self.file_accelerometer_axis_x.seek(0)
        self.file_accelerometer_axis_y.seek(0)
        self.file_accelerometer_axis_z.seek(0)
        acceleration_x =\
            float(self.file_accelerometer_axis_x.read()) * self.scale
        acceleration_y =\
            float(self.file_accelerometer_axis_y.read()) * self.scale
        acceleration_z =\
            float(self.file_accelerometer_axis_z.read()) * self.scale
        # Update the vector.
        self[0] = acceleration_x
        self[1] = acceleration_y
        self[2] = acceleration_z

    def __repr__(
        self
        ):
        self.update()
        return list.__repr__(self)

if __name__ == "__main__":
    options = docopt.docopt(__doc__)
    if options["--version"]:
        print(version)
        exit()
    main(options)
