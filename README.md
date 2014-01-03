# spin

a small utility to assist in setting usage modes of laptop-tablet devices

## quick start

### setup

- spin
    - Download [spin.py](https://raw.github.com/wdbm/spin/master/spin.py).
- docopts
    - Spin is dependent on the module [```docopt```](http://docopt.org/). ```docopt``` can be used directly by having [docopt.py](https://raw.github.com/wdbm/spin/master/docopt.py) in the same directory as spin.py or it can be installed: ```pip install docopt```

### run

Spin can be run in its default graphical mode or in a non-graphical mode. The graphical mode is engaged by running

    spin.py

while the non-graphical mode is engaged by using the command line argument ```--nogui```:

    spin.py --nogui

By default, the utility disables the touchscreen on detecting the stylus in proximity. This facility is provided by the non-graphical mode.
