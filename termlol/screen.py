# coding: utf-8
#
# Doc: http://tldp.org/HOWTO/Bash-Prompt-HOWTO/x361.html
#
#from . import const
import sys
import const

import threading

_lock = threading.Lock()

def c(fore, back, string):
    return fore + back + string + const.RESET

def echo(s):
    sys.stdout.write(s)
    sys.stdout.flush()

def show(x, y, s):
    _lock.acquire()
    move(x, y)
    echo(s)
    move(0, 0)
    _lock.release()

def move(x, y):
    echo('\033[%d;%dH' %(y, x))

def clear():
    echo('\033[2J')

def flush(x, y, w, h, char):
    for i in range(x, x+w):
        for j in range(y, y+h):
            move(i, j)
            echo(char)

def progress(x, y, cur, _max, length=10, color=const.BACK_GREEN):
    move(x, y)
    p = float(cur)/_max
    cur = int(p*length)
    _max = length
    for i in range(x, x+cur):
        echo(c(const.FORE_YELLOW, color, ' '))
    for i in range(x+cur, x+_max):
        echo(c(const.FORE_YELLOW, const.BACK_WHITE, ' '))


if __name__ == '__main__':
    clear()
    show(0, 0, c(const.FORE_WHITE, const.BACK_YELLOW, 'hello'))
    flush(5, 5, 10, 20, 'c')
    progress(2, 2, 10, 15)
