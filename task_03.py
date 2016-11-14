#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


def exception_test(arg1, arg2, arg3):
    """Exception function
    Args:
       arg1(list): input for arg1
       arg2(list): input for arg2
       arg3(list): input for arg3
    Return:
       returns True, False or error depends on condition
    Exampe:
       >>> exception_test(['apple'], 0, 'p')
       False
       >>> exception_test(43, 1, 1)
       True
       >>> exception_test(['apple'], 0, x)
       Traceback (most recent call last):
       File "<pyshell#3>", line 1, in <module>
       exception_test(['apple'], 0, x)
       NameError: name 'x' is not defined
    """
    caught = False
    try:
        arg1[arg2].index(arg3)
    except:
        caught = True
    return caught
