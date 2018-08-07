#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import setuptools

def main():
    setuptools.setup(
        name                 = "python_spin",
        version              = "2018.08.07.2230",
        description          = "a small utility to assist in setting usage modes of laptop-tablet devices",
        long_description     = long_description(),
        url                  = "https://github.com/wdbm/spin",
        author               = "Will Breaden Madden",
        author_email         = "wbm@protonmail.ch",
        license              = "GPLv3",
        packages             = setuptools.find_packages(),
        install_requires     = [
                               "docopt",
                               "technicolor"
                               ],
        entry_points         = {
                               "console_scripts": ("spin = python_spin.__init__:main")
                               },
        include_package_data = True,
        zip_safe             = False
    )

def long_description(filename = "README.md"):
    if os.path.isfile(os.path.expandvars(filename)):
      try:
          import pypandoc
          long_description = pypandoc.convert_file(filename, "rst")
      except ImportError:
          long_description = open(filename).read()
    else:
        long_description = ""
    return long_description

if __name__ == "__main__":
    main()
