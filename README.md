# spin

a small utility to assist in setting usage modes of laptop-tablet devices

# features

- automatic palm rejection when using stylus
- automatic disable/enable of touchpad and nipple when device toggled between laptop and tablet states
- manual control of display orientation and input devices

# setup

This utility requires X11.

```Bash
sudo apt install python-qt5
sudo pip install python_spin
```

To set up globally a Linux desktop launcher with icon, execute the following:

```Bash
sudo wget --content-disposition -N -P /usr/share/icons/ https://raw.githubusercontent.com/wdbm/spin/master/python_spin/static/spin.svg

sudo wget --content-disposition -N -P /usr/share/applications/ https://raw.githubusercontent.com/wdbm/spin/master/python_spin/static/spin.desktop
```

# quick start

This utility can be run in its default graphical mode or in a non-graphical mode. The graphical mode is engaged by running

```Bash
spin
```

while the non-graphical mode is engaged by using the option `--no_GUI`:

```Bash
spin --no_GUI
```

By default, this utility disables the touchscreen on detecting the stylus in proximity and it changes between the laptop and tablet modes on detecting toggling between the laptop and tablet usage configurations. These default behaviours are provided by both the graphical and non-graphical modes of this utility. This utility should be initiated in the laptop usage configuration.

# compatibility

This utility has been tested on the following operating systems:

- Ubuntu 16.04 (X11, Unity)

This utility has been tested on the following computer models:

- ThinkPad S1 Yoga
- ThinkPad S120 Yoga

It may run on the ThinkPad Yoga P40 and there is evidence that it does not run with full functionality on the ThinkPad Yoga 14.

# acceleration control

There is an experimental acceleration control included which is deactivated by default. It can be activated by selecting the appropriate button in the graphical mode.

# future

Under consideration is state recording in order to avoid execution of unnecessary commands and better handling of subprocesses.
