import sys
import os
import time 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.model.Game import Game 
from src.model.Player import Player

if __name__ == "__main__":  
    name = input("Enter Name: ") 
    p1 = Player(name) 
    game = Game(p1)
    
    round = 1
    while(not round > 4): 
        print("Get ready...")
        for i in range(3, 0, -1): 
            print(i) 
            time.sleep(0.6)
        print("Go!")
        print("Round",round, "!") 
        for r in (["Rock...", "Paper..", "Scissor."]): 
            print(r)
            time.sleep(0.5)
        option = input("choose option ") 
        if (option == "q"): 
            break 
        while (not option == "rock" and not option == "paper" and not option == "scissor"):  
            print("1.rock 2. paper 3. scissor")  
            option = input("choose option ")
        round += 1
        print(game.play_round(option))
        time.sleep(2.42)
    
    print(game.determine_winner()) 




