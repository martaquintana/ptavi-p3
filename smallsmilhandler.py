#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.diccionario = {
            "root-layout": ['width', 'height', 'background-color'],
            "region": ['id', 'top', 'left', 'right'],
            "img": ['src', 'region', 'begin', 'dur'],
            "audio": ['src', 'begin', 'dur'],
            "textstream": ['src', 'region', ]
            }
        self.tag_list = []
        self.etiquetas = self.diccionario.keys()

    def startElement(self, name, attrs):

        dic_tag = {}
        if name in self.etiquetas:
            dic_tag['etiqueta'] = name
            # De esta manera tomamos los valores de los atributos
            for atributo in self.diccionario[name]:
                dic_tag[atributo] = attrs.get(atributo, "")
            self.tag_list.append(dic_tag)

    def get_tags(self):
        """
        Devuelve la lista de etiquetas,
        sus atributos y el contenido de los atributos
        """
        return self.tag_list
