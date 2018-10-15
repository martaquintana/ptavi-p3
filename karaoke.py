#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import smallsmilhandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from urllib.request import urlretrieve


class KaraokeLocal:

    def __init__(self, fichero):
        self.get_tags = []
        self.dicc = {}

    def __str__(self):
        """
        Imprime el listado de etiquetas
        """
        self.get_tags = cHandler.get_tags()
        # print(self.get_tags)
        for linea in range(0, len(self.get_tags)):
            self.dicc = self.get_tags[linea]
            # print(dicc)
            # print('{etiqueta}\t{width}\t{height}\t{background-color}\n'.format(**dicc))

            for clave, valor in self.dicc.items():
                if clave == 'etiqueta':
                    print('{v}\t'.format(v=valor), end='\t')
                elif valor == '':
                    print('')
                else:
                    print('{c}="{v}"'.format(c=clave, v=valor), end='\t')
            print('\n')

    def to_json(self, fichero, fichero_json=None):
        """
        Fichero JSON
        """
        if fichero_json is None:
            fichero_json = fichero.split('.')[0]+'.json'
        json.dump(self.get_tags, open(fichero_json, "w"))

    def do_local(self):
        """
        Descarga en local el contenido multimedia
        """
        for linea in range(0, len(self.get_tags)):
            self.dicc = self.get_tags[linea]
            for clave, valor in self.dicc.items():
                if clave == 'src' and valor[0:5] == "http:":
                    newvalor = valor.split('/')[-1]
                    urlretrieve(valor, newvalor)
                    """
                    urlretrieve No me funciona en casa,
                    en los laboratorios si
                    """
                    valor = newvalor

                if clave == 'etiqueta':
                    print('{v}\t'.format(v=valor), end='\t')
                elif valor == '':
                    print('')
                else:
                    print('{c}="{v}"'.format(c=clave, v=valor), end='\t')
            print('\n')


if __name__ == '__main__':
    fichero = sys.argv[1]
    try:
        open(fichero)
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser = make_parser()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))
        KaraokeLocal.__str__(cHandler)
        KaraokeLocal.to_json(cHandler, fichero)
        KaraokeLocal.do_local(cHandler)

    except(FileNotFoundError,IndexError):
        print("Usage: python3 karaoke.py file.smil")
