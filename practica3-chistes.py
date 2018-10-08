#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class ChistesHandler(ContentHandler):
    """
    Clase para manejar chistes malos
    """

    def __init__ (self):
        """
        Constructor. Inicializamos las variables
        """
        self.calificacion = ""
        self.pregunta = ""
        self.inPregunta = False
        self.respuesta = ""
        self.inRespuesta = False
        self.chistes=[]

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'chiste':
            # De esta manera tomamos los valores de los atributos
            self.calificacion = attrs.get('calificacion', "")
        elif name == 'pregunta':
            self.inPregunta = True
        elif name == 'respuesta':
            self.inRespuesta = True

    def endElement(self, name):
        """
        Método que se llama al cerrar una etiqueta
        """
        if name == 'pregunta':
            self.chistes.append(self.pregunta)
            self.pregunta = ""
            self.inPregunta = False
        if name == 'respuesta':
            self.chistes.append(self.respuesta)
            self.respuesta = ""
            self.inRespuesta = False
        """
        Otra forma de imprimir todo al final y no necesitariamos el método
        
        if name == 'humor':
            print(self.chistes)
        """

    def characters(self, char):
        """
        Método para tomar contenido de la etiqueta
        """
        if self.inPregunta:
            self.pregunta = self.pregunta + char
        if self.inRespuesta:
            self.respuesta += char
    """
    Método imprimir que llamamos al final del programa
    Gregorio me ha dicho que mejor este
    """
    def imprimir(self,chistes):
        print(self.chistes)

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = ChistesHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('chistes2.xml'))
    cHandler.imprimir(cHandler)
    
