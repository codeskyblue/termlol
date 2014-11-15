#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 hzsunshx <hzsunshx@onlinegame-14-51>
#
# Distributed under terms of the MIT license.

"""
an moving object
"""
import time
import threading

import const
import screen
import keyboard

class Hero(object):
    def __init__(self, name='unknown'):
        self.name = name
        self.pos = [10, 10]
        self.oldpos = None
        self.HP_TOTAL = 100
        self.hp = 50
        self.BP_TOTAL = 100 # fa li zhi
        self.bp = 50

        self.originX = 4
        self.originY = 4
        self.map_width = 60
        self.map_height = 20
        self.map_color = screen.c(const.FORE_WHITE, const.BACK_WHITE, ' ')
        self.start_time = time.time()

        screen.clear()
        self._draw_map()
        self._draw_status()

        def update_time():
            while True:
                self._draw_time(time.time()-self.start_time)
                time.sleep(0.5)
                self.damage(-1)
                self.consume(-2)
        t = threading.Thread(target=update_time, name='update_time')
        t.setDaemon(True)
        t.start()

    def _getpos(self):
        x, y = self.pos
        return (self.originX + x, self.originY + y)

    def _draw_map(self):
        for i in range(self.originX, self.originX+self.map_width+1):
            screen.show(i, self.originY-1, '-')
        for i in range(self.originX, self.originX+self.map_width+1):
            screen.show(i, self.originY+self.map_height+1, '-')
        for i in range(self.originY, self.originY+self.map_height+1):
            screen.show(self.originX-1, i, '|')
        for i in range(self.originY, self.originY+self.map_height+1):
            screen.show(self.originX+self.map_width+1, i, '|')
        screen.show(self.originX+5, self.originY-1, ' LOL ')

    def _draw_status(self):
        ox, oy = 7, 30
        screen.show(ox, oy, 'HP')
        length = 20
        screen.progress(ox+3, oy, self.hp, self.HP_TOTAL, length=length)
        screen.show(ox+length+4, oy, '[%d/%d]   ' %(self.hp, self.HP_TOTAL))

        screen.show(ox, oy+2, 'BP')
        screen.progress(ox+3, oy+2, self.bp, self.BP_TOTAL, color=const.BACK_BLUE, length=length)
        screen.show(ox+length+4, oy+2, '[%d/%d]   ' %(self.bp, self.BP_TOTAL))

    def _draw_time(self, curr=0.0):
        tstr = time.strftime(' [%0H:%0M:%0S] ', time.gmtime(curr))
        screen.show(self.originX+40, self.originY-1, tstr)

    def refresh(self):
        if self.oldpos:
            x, y = self.oldpos
            screen.show(x, y, ' ')

        x, y = self._getpos()
        self.oldpos = [x, y]
        screen.show(x, y, screen.c(const.FORE_WHITE, const.BACK_YELLOW, 'X'))

    def damage(self, cnt):
        self.hp = max(0, self.hp - cnt)
        self.hp = min(self.HP_TOTAL, self.hp)
        self._draw_status()

    def consume(self, cnt):
        self.bp = max(0, self.bp - cnt)
        self.bp = min(self.BP_TOTAL, self.bp)
        self._draw_status()

    def is_alive(self):
        return self.hp > 0

    def move(self, direction):
        c = direction
        x, y = pos = self.pos
        if c == const.KEYBOARD_UP or c == 'k':
            pos[1] = max(0, y-1) 
        elif c == const.KEYBOARD_DOWN or c == 'j':
            pos[1] = min(self.map_height, y+1) 
        elif c == const.KEYBOARD_LEFT or c == 'h':
            pos[0] = max(0, x-1) 
        elif c == const.KEYBOARD_RIGHT or c == 'l':
            pos[0] = min(self.map_width, x+1) 

    def action(self, act):
        if act != 'a':
            if self.bp < 15:
                return
            self.consume(15)

        weapon = screen.c(const.FORE_RED, const.BACK_BLUE, '*')
        maxlen = 20
        x, y = self._getpos()
        def fly():
            for i in range(1, maxlen):
                i == 1 or screen.show(x+i-1, y, ' ')
                screen.show(x+i, y, weapon)
                time.sleep(0.1)
            screen.show(x+maxlen-1, y, ' ')

        if act == 'q':
            weapon = screen.c(const.FORE_RED, const.BACK_BLUE, '!')
            t = threading.Thread(target=fly)
            t.daemon=True
            t.start()
        elif act == 'w':
            self.damage(-10)
        elif act == 'a':
            maxlen = 10
            weapon = screen.c(const.FORE_RED, const.BACK_WHITE, '-')
            t = threading.Thread(target=fly)
            t.daemon=True
            t.start()

        self._draw_status()

def main():
    hero = Hero()
    hero.refresh()
    def hdlr(c):
        if c.startswith('[') or c in 'hjkl': # direction keys
            hero.move(c)
        else:
            hero.action(c)
        hero.refresh()
            
    keyboard.register(hdlr)

if __name__ == '__main__':
    main()
