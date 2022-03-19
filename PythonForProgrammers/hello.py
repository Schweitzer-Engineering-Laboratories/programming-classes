#!/usr/bin/env python3
"""Minimum working example of a module that can be run as a script"""

def say_hello(arg=None):
    """Print 'Hello, arg' for any arg"""
    if arg is not None:
        print("Hello,", arg)
    else:
        print("Hello")

if __name__ == "__main__":
    from sys import argv
    if len(argv)>1:
        say_hello(argv[1])
    else:
        say_hello()