#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import smallsmilhandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class Karaoke:
    
    def ___init__(self,fichero):
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser = make_parser()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))
        self.get_tagslist=cHandler.get_tags()
        print(self.get_tagslist)

if __name__ == '__main__':
    fichero = sys.argv[1]
    try:
        open(fichero)
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser = make_parser()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))
        get_tagslist=cHandler.get_tags()
        print(get_tagslist)
        
    except(FileNotFoundError,IndexError):
        print("Usage: python3 karaoke.py file.smil")
        
  
