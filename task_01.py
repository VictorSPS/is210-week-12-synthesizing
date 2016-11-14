#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_01"""


class BaseError(Exception):
    """A subclassed to Exception
    Atributes:
       None
    """
    pass


class StringError(BaseError, TypeError):
    """A subclassed to BaseError and TypeError
    Attributes:
       None
    """
    pass


class NumberError(BaseError, TypeError):
    """A subclassed to BaseError and TypeError
    Attributes:
       None
    """
    pass


class NonZeroError(NumberError):
    """A subclass to NumberError
    Attributes:
       None
    """
    pass
