#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    def __init__ (self):
      self.width = ""
      self.height = ""
      self.background_color= ""

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            # De esta manera tomamos los valores de los atributos
            self.width = attrs.get('width', "")
            self.height = attrs.get('height', "")
            self.background_color = attrs.get('background-color', "")
            print(self.width)
            print(self.height)
            print(self.background_color)
        

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    #cHandler.imprimir(cHandler)
    
