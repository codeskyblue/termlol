#!/usr/bin/env python
# coding: utf-8
#
# Doc: http://tldp.org/HOWTO/Bash-Prompt-HOWTO/x361.html
#

FORE_RED = '\033[31m'
FORE_GREEN = '\033[32m'
FORE_YELLOW = '\033[33m'
FORE_BLUE = '\033[34m'
FORE_WHITE = '\033[37m'

BACK_RED = '\033[01;41m'
BACK_GREEN = '\033[01;42m'
BACK_YELLOW = '\033[01;43m'
BACK_BLUE = '\033[01;44m'
BACK_WHITE = '\033[01;47m'

RESET = '\033[0m'

KEYBOARD_MAGIC = '\x1b'
KEYBOARD_UP = '[A'
KEYBOARD_LEFT = '[D'
KEYBOARD_RIGHT = '[C'
KEYBOARD_DOWN = '[B'

if __name__ == '__main__':
	print FORE_BLUE + 'hello' + RESET
	print FORE_RED + 'hello' + RESET
	print FORE_YELLOW + 'hello' + RESET
	print BACK_RED+FORE_GREEN + 'hello' + RESET
	print BACK_YELLOW+FORE_GREEN + 'hello' + RESET
