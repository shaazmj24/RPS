import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.model.Game import Game 
from src.model.Player import Player
import customtkinter as ctk 

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

if __name__ == "__main__":   
    root = ctk.CTk() 
    
    root.title("Rock Paper Scissor")
    root.geometry("400x300")

    # Example label
    label = ctk.CTkLabel(root, text="Welcome to Rock Paper Scissors!")
    label.pack(pady=20)

    root.mainloop()