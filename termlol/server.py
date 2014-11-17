#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
LoL server
"""

import xmlrpclib
import res.canvas

ROOMS = {}

class BaseUnit(object):
    def __init__(self):
        self.style = None
        self.pos = None
        self.name = None

class NPCUnit(BaseUnit):
    def __init__(self):
        super(NPCUnit).__init__(self)
    pass

class HeroUnit(BaseUnit):
    pass

ERR_MAPNOTFOUND = RuntimeError('map not found')
ERR_ROOMEXISTS = RuntimeError('room already exists')
ERR_ROOMNOTFOUND = RuntimeError('room not found')

def _new_room(name, map_name):
    '''
    @return: error (like golang)
    '''
    if ROOMS.has_key(name):
        return ERR_ROOMEXISTS
    map_info = res.canvas.get(map_name)
    if not map_info:
        return ERR_MAPNOTFOUND
    ROOMS[name] = dict(map_name=map_name, map_info=map_info, persons=set())
    return

def _join_room(name, client_ip):
    room = ROOMS.get(name)
    if not room:
        return '', ERR_ROOMNOTFOUND
    room['persons'].add(client_ip)
    return room, None

def main():
    err = _new_room('hello', 'yy')
    assert err == ERR_MAPNOTFOUND
    
    err = _new_room('hello', 'plain')
    assert err == None

    err = _new_room('hello', 'plain')
    assert err == ERR_ROOMEXISTS

if __name__ == '__main__':
    main()
