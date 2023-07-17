
import random


class RockPaperScissors (object) :
    def __init__(self, user_input) -> None:
        self.available_choices = ("rock", "paper", "scissors")
        self.bot_input = random.choice(self.available_choices)
        self.user_input = user_input.lower()
        self.result = False
        
    def compare_choices (self) -> None :
        match self.user_input:
            case "rock" :
                if self.bot_input == "scissors" :
                    self.result = True
            case "paper" :
                if self.bot_input == "rock" :
                    self.result = True
            case "scissors" :
                if self.bot_input == "paper" :
                    self.result = True
            case other :
                print (f"Choose one of following: {self.available_choices}")

    def print_result (self) -> None:
        message = "Congratulation. You win!"
        
        if not self.result :            
            message = "You lose!"
            if self.user_input == self.bot_input :
                message = "Draw!"

            message += f" Bot choice was {self.bot_input}"
        
        print (message)

def lets_play(user_input):
    new_game = RockPaperScissors(user_input)

    new_game.compare_choices()
    new_game.print_result()