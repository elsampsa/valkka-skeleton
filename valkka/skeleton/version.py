"""
version.py : Handle program version numbers

This file is part of the python skeleton example library

Skeleton example library is free software: you can redistribute it and/or modify it under the terms of the MIT License.  This code is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the MIT License for more details.

@file    version.py
@author  Sampsa Riikonen
@date    2018
@version 0.1.0 
@brief   Handle program version numbers
"""

from valkka.core import VERSION_MAJOR as VALKKA_VERSION_MAJOR
from valkka.core import VERSION_MINOR as VALKKA_VERSION_MINOR
from valkka.core import VERSION_PATCH as VALKKA_VERSION_PATCH


valkka_core_not_found="""
Valkka core module is not installed

On Ubuntu you can install it with:

sudo apt-add-repository ppa:sampsa-riikonen/valkka
sudo apt-get update
sudo apt-get install valkka

Or alternatively, just use the following command:

install-valkka-core

For more information, see https://elsampsa.github.io/valkka-examples
"""


valkka_core_old="""

Valkka core module is not up to date

(required version %i.%i.%i, valkka-core version %i.%i.%i)

Please update with

sudo apt-get update
sudo apt-get install --only-upgrade valkka

Or alternatively, just use the following command:

update-valkka-core
"""

program_info="""

Valkka skeleton version %s

(Valkka core version %s)

Copyright Sampsa Riikonen 2018

"""



# the following three lines are modded by setver.bash:
VERSION_MAJOR=0
VERSION_MINOR=2
VERSION_PATCH=1

# required valkka version
MIN_VALKKA_VERSION_MAJOR = 0
MIN_VALKKA_VERSION_MINOR = 7
MIN_VALKKA_VERSION_PATCH = 0


def check():
    # check that the imported valkka is fresh enough
    if ( (MIN_VALKKA_VERSION_MAJOR > VALKKA_VERSION_MAJOR) 
        or (MIN_VALKKA_VERSION_MINOR > VALKKA_VERSION_MINOR) 
        or (MIN_VALKKA_VERSION_PATCH > VALKKA_VERSION_PATCH) ):
            print(valkka_core_old % (MIN_VALKKA_VERSION_MAJOR, 
                                        MIN_VALKKA_VERSION_MINOR, 
                                        MIN_VALKKA_VERSION_PATCH,
                                        VALKKA_VERSION_MAJOR, 
                                        VALKKA_VERSION_MINOR,
                                        VALKKA_VERSION_PATCH,))
            raise SystemExit()


def get():
    return "%i.%i.%i" % (VERSION_MAJOR, VERSION_MINOR, VERSION_PATCH)


def getValkka():
    return "%i.%i.%i" % (VALKKA_VERSION_MAJOR, VALKKA_VERSION_MINOR, VALKKA_VERSION_PATCH)
    
    
