# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 10:55:12 2020

@author: sarsu
"""
from random import randint

while(True):
    print("Bienvenido a piedra, papel o tijeras! Selecciona:",
      "\n 1. Para jugar",
      "\n 2. Para salir")

    while(True):
        try:
            op = int(input())
        except:
            print("Digitaste incorrectamente, vuelve a intentar: ")
        else:
            break
        
    if(op == 1):
        
        while(True):
            try:
                print("Selecciona: "
              , "\n 1. Para Piedra"
              , "\n 2. Para Papel"
              , "\n 3. Para Tijeras")
                com = int(input())
            except:
                print("Digitaste incorrectamente, vuelve a intentar: ")
            else:
                break

        x = 3
        for i in range(3):
            print("\n Tu oponente escogera en ", x)
            x-=1

        ia = randint(1,3)

        if(ia == 1):
            s = "Piedra"
        elif(ia == 2):
            s = "Papel"
        elif(ia == 3):
            s = "Tijeras"

        if(com == 1):
            s2 = "Piedra"
        elif(com == 2):
            s2 = "Papel"
        elif(com == 3):
            s2 = "Tijeras"
    
        if((ia == 1 and com == 2) or (ia == 2 and com == 3) or (ia == 3 and com == 1)):
            print("\n Haz ganado! \n Seleccionaste:", s2, "\n Tu oponente selecciono:", s)
        elif(ia == com):
            print("\n Empate! \n Seleccionaste:", s2, "\n Tu oponente selecciono:", s)
        else:
            print("\n Haz perdido! \n Seleccionaste:", s2, "\n Tu oponente selecciono:", s)
            
        
    if(op == 2):
        print("\n Gracias por haber jugado!")
        break
