#!/usr/bin/env python3
'''Task8 Complex types - functions'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creating a multiplier function.
    '''
    return lambda x: x * multiplier
