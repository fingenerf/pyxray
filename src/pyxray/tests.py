#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Philippe T. Pinard"
__email__ = "philippe.pinard@gmail.com"
__version__ = "0.1"
__copyright__ = "Copyright (c) 2013 Philippe T. Pinard"
__license__ = "GPL v3"

# Standard library modules.
import unittest

# Third party modules.

# Local modules.
import pyxray.test_element_properties as test_element_properties
import pyxray.test_subshell_data as test_subshell_data
import pyxray.test_subshell as test_subshell
import pyxray.test_transition_data as test_transition_data
import pyxray.test_transition as test_transition

# Globals and constants variables.

def test_all():
    suite = unittest.TestSuite()

    suite.addTests(unittest.makeSuite(test_element_properties.TestModule))
    suite.addTests(unittest.makeSuite(test_element_properties.Test_ElementPropertiesDatabase))
    suite.addTests(unittest.makeSuite(test_element_properties.TestModule))

    suite.addTests(unittest.makeSuite(test_subshell_data.TestIonizationData))

    suite.addTests(unittest.makeSuite(test_subshell.TestSubshell))

    suite.addTests(unittest.makeSuite(test_transition_data.TestRelaxationData))

    suite.addTests(unittest.makeSuite(test_transition.TestModule))
    suite.addTests(unittest.makeSuite(test_transition.TestTransition))
    suite.addTests(unittest.makeSuite(test_transition.Testtransitionset))

    return suite
