#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
get keyboard input
"""

import sys 
import termios 

import const

def register(handler):
    ''' handler(c) '''
    fd = sys.stdin.fileno() 
    old = termios.tcgetattr( fd ) 
    new = termios.tcgetattr( fd ) 
    new[3] = new [3] & ~ termios . ICANON 

    try : 
        termios.tcsetattr(fd, termios.TCSADRAIN, new) 
        while True: 
            ipt = sys.stdin.read ( 1 ) 
            if ipt == const.KEYBOARD_MAGIC:
                ipt = sys.stdin.read(2)
            handler(ipt)
            if ipt == 'Q' : 
                break 
    finally: 
        termios.tcsetattr(fd, termios.TCSADRAIN, old) 

if __name__ == '__main__':
    def hdlr(c):
        print 'read', c
    register(hdlr)
    
