# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 10:39:08 2020

@author: sarsu
"""
from random import randint
print("Bienvenido, en este script deberas adivinar un numero entre el 0 al 20!")

x = randint(0,20)

while(True):
    try:
        y = int(input("Adivina un numero entero entre el 0 al 20: "))
    except:
        print("Digitaste incorrectamente, vuelve a intentar: ")
    else:
        break

while(True):
    if(x < y):
        while(True):
            try:
                y = int(input("Ups.. te pasaste, digita nuevamente: "))
            except:
                print("Digitaste incorrectamente, vuelve a intentar: ")
            else:
                break
    elif(x > y):
        while(True):
            try:
                y = int(input("Ups.. te quedaste corto, digita nuevamente: "))
            except:
                print("Digitaste incorrectamente, vuelve a intentar: ")
            else:
                break
    else:
        print("Haz ganado! El numero era:" , x)
        break
