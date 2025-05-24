from random import choice 

class Game:  
    name = "Robot"

    def __init__(self, player): 
        self.player = player  
        self.round = 0 
        self.score = 0

    def addRound(self): 
        self.round += 1
    
    def robot_score(self): 
        self.score += 1

    def reset_round(self): 
        self.round = 0  

    def exceed_round(self): 
        return self.round > 4 
    
    def play_round(self, option):   
        robot_move = choice(["rock", "scissor", "paper"])
        if option == robot_move:  
            return "draw"
        elif ((option == "paper" and robot_move == "rock") or 
              (option == "scissor" and robot_move == "paper") or 
              (option == "rock" and robot_move == "scissor")): 
            self.player.addScore()
            return "Win!"
        else: 
            self.robot_score()
            return "lose"
    
    def determine_winner(self): 
        if self.player.score > self.score: 
            self.player.addW()
            return "You are victorious!"
        elif self.player.score < self.score: 
            self.player.addL()
            return "You lost..."
        else: 
            return "Draw"

