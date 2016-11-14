#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02"""


class CustomError(Exception):
    """A subclass to Exception
    Attributes:
       None
    """
    def __init__(self, message, cause):
        """Constructor for CustomError
        Args:
           message(str): input
           cause(str): stores value
        """
        Exception.__init__(self, message)
        self.cause = cause
