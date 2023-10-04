#!/usr/bin/env pytyhon

import random 

def musicgenre():
    """Start a music genre guessing game."""
    print ("guessing the music genre ! try 3 times only ")

    music =[
      "rock",
      "hip hop",
      "metal",
      "pop",
      "reggae", 
      "classical",
      "jazz",
    ]
 
    x = random.choice(music)
    guess = None
    print(x)


    score=0
    for trial in range(3):
 
        guess=str(input("what music genre am I thinking: "))

        if guess == x:
            print("correct! very good ")
            score +=3
            break

        else:
            print("Incorrect.. try again")
            
            
    
    print (" ur score :", score)

musicgenre() 