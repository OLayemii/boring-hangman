#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Hangman Game
# by GARUBA OLAYEMI
# 26/03/2018

# ##     ##    ###    ##    ##  ######   ##     ##    ###    ##    ## 
# ##     ##   ## ##   ###   ## ##    ##  ###   ###   ## ##   ###   ## 
# ##     ##  ##   ##  ####  ## ##        #### ####  ##   ##  ####  ## 
# ######### ##     ## ## ## ## ##   #### ## ### ## ##     ## ## ## ## 
# ##     ## ######### ##  #### ##    ##  ##     ## ######### ##  #### 
# ##     ## ##     ## ##   ### ##    ##  ##     ## ##     ## ##   ### 
# ##     ## ##     ## ##    ##  ######   ##     ## ##     ## ##    ## 

from hang_man.words import Words
from hang_man.player import Player
from random import randint
from collections import Counter
import re
class Game:
    
    def __init__(self):
        words = Words()
        self.wordlist = words.getwords()
        self.alpha = "[a b c d e f g h i j k l m n o p q r s t u v w x y z]"
        
        playername = input("Enter name of player > ")
        self.player = Player(playername)        
        #player = Player()
    def round_word(self):
        self.wordfr = self.wordlist[randint(0, len(self.wordlist))] 
        return self.wordfr
    
    def gameascii(self):
        return """
        ##     ##    ###    ##    ##  ######   ##     ##    ###    ##    ## 
        ##     ##   ## ##   ###   ## ##    ##  ###   ###   ## ##   ###   ## 
        ##     ##  ##   ##  ####  ## ##        #### ####  ##   ##  ####  ## 
        ######### ##     ## ## ## ## ##   #### ## ### ## ##     ## ## ## ## 
        ##     ## ######### ##  #### ##    ##  ##     ## ######### ##  #### 
        ##     ## ##     ## ##   ### ##    ##  ##     ## ##     ## ##   ### 
        ##     ## ##     ## ##    ##  ######   ##     ## ##     ## ##    ## 
        """
    def play(self):
        print(self.gameascii())
        print("\tWelcome {}".format(self.player.getplayer()))
        print("+"*100)
        
        #Proceed with game play
        
        self.tries = 0
        self.chances = 9
        self.roundword = self.wordlist[randint(0, len(self.wordlist))]
        self.correctguess = 0
        self.correctletters = ["_"] * len(self.roundword)
        
        print("\t" *10 , "tries left: {}".format(self.chances))
        
        
        print("\t"*2, self.alpha)
        print("\t"*5,"GUESS THE WORD")
        print("\t"*5 , " ".join(self.correctletters))
        
        
        #loop till correct answer or end of tries
        
        while (self.chances > 0 and self.correctguess < len(Counter(self.roundword))):
            letter = input("guess a letter > ").lower().strip()
            if(letter in self.roundword and letter != ""):           
                self.correctguess += 1
                self.roundword = self.roundword.replace(letter, letter.upper(), len(self.roundword))
                for i in range(0, len(self.roundword)):
                    if(self.roundword[i].isupper()):
                        self.correctletters[i] = self.roundword[i].lower()
                    else:
                        pass
                print("\t"*5 , " ".join(self.correctletters))    
                if self.correctguess == len(Counter(self.roundword)):
                    print("You win!!")
            
            elif(letter.upper() in self.roundword and letter != ""):
                print("Already guessed!")
            else:
                self.chances -= 1
                if(self.chances == 0):
                    print("Game Over!!!") 
                else:
                    print("Wrong Word!!!")
                    print("\t" *10 , "tries left: {}".format(self.chances)) 
        playa = input("Play again? (Y/N)> ").lower()
        if(playa == "y"):
            game.play()
        else:
            pass
                
                
game = Game()
game.play()