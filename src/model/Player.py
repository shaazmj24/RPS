class Player:  

    def __init__(self, name):     #equivalent to public Player(String name) {} 
        self.name = name    
        self.score = 0   
        self.win = 0  
        self.defeat = 0

    def addScore(self): 
        self.score += 1 

    def addW(self): 
        self.win += 1
    
    def addL(self): 
        self.defeat += 1    
    
    def reset_score(self): 
        self.score = 0 



