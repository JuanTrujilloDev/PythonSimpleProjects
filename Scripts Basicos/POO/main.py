# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:19:37 2020

@author: sarsu
"""


from Granja.Granja import *

vaca = Animales("Lola", 4, "Vaca", "Peludo", "Hembra")
cerdo = Animales("Ham", 4, "Cerdo", "Peludo", "Macho")
perro = Animales("Dinky", 4, "Perro", "Peludo", "Hembra")
gallo = Animales("Roco", 4, "Gallo", "Plumado", "Macho")

granja = Granja([vaca, cerdo, perro, gallo])

granja.getAnimales()

toro = Animales("Leo", 4, "Toro", "Peludo", "Macho")
granja.addAnimales(toro)

granja.getAnimales()