# coding: utf-8
#
# Doc: http://tldp.org/HOWTO/Bash-Prompt-HOWTO/x361.html
#
#from . import const
import sys
import const

def c(fore, back, string):
	return fore + back + string + const.RESET

def echo(s):
	sys.stdout.write(s)

def move(x, y):
	echo('\033[%d;%dH' %(x, y))

def clear():
	echo('\033[2J')
	
def show_str(x, y, string):
	move(x, y)
	echo(string)

if __name__ == '__main__':
	clear()
	show_str(0, 0, c(const.FORE_WHITE, const.BACK_YELLOW, 'hello'))
