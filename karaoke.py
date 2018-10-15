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
        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))
        self.get_tags = cHandler.get_tags()

    def __str__(self):
        """
        Devuelve una cadena de texto con todo
        """
        list = []
        for linea in range(0, len(self.get_tags)):
            self.dicc = self.get_tags[linea]
            for clave, valor in self.dicc.items():
                if clave == 'etiqueta':
                    list += ('{v}''\t'.format(v=valor))
                elif valor == '':
                    list += ('')
                else:
                    list += ('{c}="{v}"''\t'.format(c=clave, v=valor))
            list += ('\n')
        return(''.join(list))

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
                    # urlretrieve(valor, newvalor)
                    """
                    urlretrieve No me funciona en casa,
                    en los laboratorios si
                    """
                    valor = newvalor


if __name__ == '__main__':
    fichero = sys.argv[1]
    try:
        open(fichero)
        karaoke_local = KaraokeLocal(fichero)
        print(karaoke_local)
        karaoke_local.to_json(fichero)
        karaoke_local.do_local()
        karaoke_local.to_json(fichero, 'local.json')
        print(karaoke_local)

    except(FileNotFoundError, IndexError):
        print("Usage: python3 karaoke.py file.smil")
