# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 11:28:24 2020

@author: sarsu
"""
import time
from io import open
from random import randint

while(True):
    print("\nBienvenido al ahorcado en ingles digita: \n1.Para jugar \n2.Para salir: ")

    while(True):
        try:
            op = int(input())
            if(op != 1 and op !=2):
                raise ValueError
        except:
            print("\nHaz digitado incorrectamente, intenta nuevamente: ")
        else:
            break
    
    if(op == 1):
        lista = []
        f = open('usa.txt','r')
        j = 0
        for i in f:
            j+=1
            lista.append(i)
        r = randint(0,j)
        word = str(lista[r])
        word = word.lower()
        word= word.strip()
        
        #wait for 1 second
        time.sleep(1)

        print ("Empieza a adivinar...")
        time.sleep(0.5)
        print("\nLa palabra contiene",len(word),"letras.")
        print("\nRecueda que es en ingles!")
    
        guesses = ''
        turns = 10
        usadas = []
        #check if the turns are more than zero
        while turns > 0:         
            
            # make a counter that starts with zero
            failed = 0             

            # for every character in secret_word    
            for char in word:      

            # see if the character is in the players guess
                if char in guesses:    
    
                    # print then out the character
                    print (char, )   
                    
                else:
    
                    #if not found, print a dash
                    print ("_",)     
       
                    # and increase the failed counter with one
                    failed += 1    

                # if failed is equal to zero

            # print You Won
            if failed == 0:        
                print ("\nGanaste! La palabra era:" , word)

            # exit the script
                break              

            print

            # ask the user go guess a character
            while(True):
                try:
                    guess = input("\n Adivina una letra: ") 
                    
                    if((guess.isdigit()) or len(guess)>1):
                        raise VakyeError
                except:
                    print("\n Haz digitado incorrectamente, digitanuevamente")
                else:
                    break
            # set the players guess to guesses
            guesses += guess                    
            usadas.append(guess)
            # if the guess is not found in the secret word
            if guess not in word:  
 
                # turns counter decreases with 1 (now 9)
                turns -= 1        
 
                # print wrong
                print ("\nError" )  
                
            # how many turns are left
            print ("\nTe quedan", + turns, 'vidas') 
            print("\nLetras usadas:", usadas)
            # if the turns are equal to zero
            if turns == 0:           
    
            # print "You Lose"
                print ("\nPerdiste la palabra era", word)  
            
            
        
    elif(op == 2):
        break

f.close()
del(f)