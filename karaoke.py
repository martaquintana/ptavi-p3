#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import smallsmilhandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class Karaoke:
    get_tags=[]
   
    def imprimir(self):
        get_tags=cHandler.get_tags()
        print(get_tags)
        for linea in range(0,len (get_tags)):
            dicc=get_tags[linea]
            print(dicc)
            #print ('{etiqueta}\t{width}\t{height}\t{background-color}\n'.format(**dicc))
  
            for clave, valor in dicc.items(): 
                print ('{c}={v}'.format(c=clave,v=valor),end='\t')
            print('\n')


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
        
  