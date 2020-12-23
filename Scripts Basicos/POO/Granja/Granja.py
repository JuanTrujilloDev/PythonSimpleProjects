# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:05:44 2020

@author: sarsu
"""


class Animales:
    
    def __init__(self, nombre, patas, tipo, pelaje, sexo):
        self.nombre = nombre
        self.patas = patas
        self.tipo = tipo
        self.pelaje = pelaje
        self.sexo = sexo
        print("Se ha creado un nuevo animal de tipo:", self.tipo)
    
    def setNombre(self, nombre):
        self.nombre = nombre
        print("Se ha cambiado el nombre del animal a:", nombre)
    
    def getNombre(self):
        print ("El animal {} de tipo {} con {} patas, tiene pelaje {} y es un {}".format(self.nombre, self.tipo, self.patas, self.pelaje, self.sexo))
    
class Granja(Animales):
    
    def __init__(self, animales = []):
        self.animales = animales
        print("Se ha creado una nueva granja")
    
    def getAnimales(self):
        for animal in self.animales:
            animal.getNombre()
            
    def addAnimales(self, a):
        self.animales.append(a)
        print("Se ha agregado un nuevo animal")
        

