#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: test_example
.. moduleauthor:: Voornaam Achternaam <studentid_achternaam@zuyd.nl>

This is a sample test module.
"""

import pytest

"""
This is just an example test suite.  It will check the current project version
numbers against the original version numbers and will start failing as soon as
the current version numbers change.
"""


def test_example():
    """
    Arrange: Load the primary module.
    Act: Retrieve the versions.
    Assert: Versions match the version numbers at the time of project creation.
    """
    assert (
        '0.0.1' == __version__,
        "This test is expected to fail when the version increments. "
        "It is here only as an example and you can remove it."
    )

    """
    This is just an example test suite that demonstrates the very useful
    `parameterized` module.  It contains a test in which the squares of the
    first two parameters are added together and passes if that sum equals the
    third parameter.
    """
