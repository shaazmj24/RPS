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
    
    def play_round(self, option):   
        robot_move = choice(["rock", "scissor", "paper"])
        if option == robot_move:  
            return "Robot chose " + robot_move + " .it's a tie!"
        elif ((option == "paper" and robot_move == "rock") or 
              (option == "scissor" and robot_move == "paper") or 
              (option == "rock" and robot_move == "scissor")): 
            self.player.addScore()
            return "Robot chose " + robot_move + " .You won this round!"
        else: 
            self.robot_score()
            return "Robot chose " + robot_move + " .You lost this round!"
    
    def determine_winner(self): 
        if self.player.score > self.score: 
            self.player.addW()
            return self.player.name + " is victorious!"
        elif self.player.score < self.score: 
            self.player.addL()
            return self.player.name + " lost..."
        else: 
            return "Draw......."

