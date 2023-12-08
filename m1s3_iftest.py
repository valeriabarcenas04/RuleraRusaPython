#Juego simple 
import random
#import os
#Ruleta rusa
number = random. randint(1,10)

guess = input( "Adivina un número entre 1 y 10: (Ingresa tu número) --> \t")
guess = int(guess)

if number == guess:
    print( "Ganaste ! " )

    
else:
    print( "Perdiste! " )
    print('\n el número es:',number)


print("La condicion es:")
print(number == guess)