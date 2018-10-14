#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import smallsmilhandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class KaraokeLocal:
    
    def __init__(self,fichero):
        self.get_tags=[]
   
    def __str__(self):
        """
        Imprime el listado de etiquetas
        """
        self.get_tags=cHandler.get_tags()
        #print(self.get_tags)
        for linea in range(0,len (self.get_tags)):
            dicc=self.get_tags[linea]
            #print(dicc)
            #print ('{etiqueta}\t{width}\t{height}\t{background-color}\n'.format(**dicc))
            
            for clave, valor in dicc.items():
                if clave == 'etiqueta' :
                    print('{v}\t'.format(v=valor),end='\t')
                elif valor == '':
                    print('')
                else:
                    print ('{c}="{v}"'.format(c=clave,v=valor),end='\t')
            print('\n')
    def to_json(self,fichero,fichero_json=None):
        """
        Fichero JSON
        """
        if fichero_json == None:
            fichero_json = fichero.split('.')[0]+'.json'
        json.dump(self.get_tags,open(fichero_json,"w"))
        

if __name__ == '__main__':
    fichero = sys.argv[1]
    try:
        open(fichero)
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser = make_parser()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))
        KaraokeLocal.__str__(cHandler)
        KaraokeLocal.to_json(cHandler,fichero)

        
    except(FileNotFoundError,IndexError):
        print("Usage: python3 karaoke.py file.smil")
        
  
