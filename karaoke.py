#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import smallsmilhandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class Karaoke:
    get_tagslist=[]
   
    def imprimir(self):
        get_tagslist=cHandler.get_tags()
        print(get_tagslist)
        
       format(get_tagslist)



if __name__ == '__main__':
    fichero = sys.argv[1]
    try:
        open(fichero)
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser = make_parser()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))
        Karaoke.imprimir(cHandler)

        
    except(FileNotFoundError,IndexError):
        print("Usage: python3 karaoke.py file.smil")
        
  
