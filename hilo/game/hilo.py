import random

from game.cards import Cards

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.beginnerscore = 300
        self.points = 100
        self.total_score = 0

        # for i in range(13):
        #     card = Cards()
        #     self.card.append(Cards)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        counter = 1
        while self.is_playing:
            current_card = Cards().draw(decide="1")
            guess = self.get_inputs()
            next_card = Cards().draw(decide="2")
            # print(f"{current_card} -> {next_card}")
            self.do_updates(current_card,next_card,guess,counter)
            self.do_outputs()
            "play again method to do y/n"
            self.play_again()

            counter += 1

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        if self.is_playing:
            guess_card = input("Guess card? Higher or Lower [h/l] ")
            if guess_card == "h":
                # self.is_playing = (guess_card == "h")
                return guess_card
            elif guess_card == "l":
                return guess_card
                # self.is_playing = (guess_card == "l")
            else:
                print("Invalid Input")

       
    def do_updates(self,current_card,next_card,guess,counter):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        # if not self.is_playing:
        #     return 
        if counter == 1:
            if current_card > next_card and guess == "l" or current_card < next_card and guess == "h":
                self.total_score = 100 + self.beginnerscore
            else:
                self.total_score = self.beginnerscore - 75
        else:
            if current_card > next_card and guess == "l" or current_card < next_card and guess == "h":
                self.total_score += 100
            else:
                self.total_score = self.total_score - 75
        
        if self.total_score <= 0: 
                print ("Game Over. You are out of points")
                self.is_playing = False

    def do_outputs(self):
        """Displays the total score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.total_score > 0)


    def play_again (self):
        "This method asks the user if they want to play again or not"

        # Input validation
        play_again = "J"
        while play_again not in ("y","n"):
            play_again = input("Do you want to play again? [y/n] ")
        # self.is_playing = (play_again == "y")
        
        if play_again== "n":
            print ("Game over")
            self.is_playing = False
    
