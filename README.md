# spin

a small utility to assist in setting usage modes of laptop-tablet devices

# introduction

This utility has been tested on the Lenovo ThinkPad S1 Yoga. There is evidence that it does not run with full functionality on the Lenovo ThinkPad Yoga 14. This utility has been tested on the following operating systems:

- Ubuntu 14.10

# prerequisites

## docopt

    sudo apt-get -y install python-docopt

## quick start

Spin can be run in its default graphical mode or in a non-graphical mode. The graphical mode is engaged by running

    spin.py

while the non-graphical mode is engaged by using the command line argument ```--nogui```:

    spin.py --nogui

By default, this utility disables the touchscreen on detecting the stylus in proximity and it changes between the laptop and tablet modes on detecting toggling between the laptop and tablet usage configurations. These default behaviours are provided by both the graphical and non-graphical modes of this utility. Spin should be started in the laptop usage configuration.
