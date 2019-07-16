
'''
MAP Client Plugin
'''

__version__ = '0.1.0'
__author__ = 'Richard Christie'
__stepname__ = 'smoothfit'
__location__ = 'https://github.com/rchristie/mapclientplugins.smoothfitstep/archive/master.zip'

# import class that derives itself from the step mountpoint.
from mapclientplugins.smoothfitstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
from . import resources_rc
