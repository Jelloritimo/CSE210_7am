import random

class Cards:
    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
    """

    def __init__(self):
        """Constructs a new instance of Die.

        Args:
            self (Die): An instance of Die.
        """
        self.current_card = 0
        self.next_card = 0
        self.points = 0

    def draw(self):
        """Generates a new random value and calculates the points for the die.
        
        Args:
            self (Die): An instance of Die.
        """
        self.current_card = random.randint(1, 13)
        print(f"The card is: {self.current_card}")
        # self.points = 50 if self.current_card == "" else 100 if self.current_card == 1 else 0
    
    # def next_draw(self):
    #     self.next_card = random.randint(1, 13)
    #     print(f"Next card was: {self.next_card}")



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
        self.card = []
        self.is_playing = True
        self.score = 300
        self.total_score = 0

        # for i in range(13):
        #     card = Cards()
        #     self.card.append(Cards)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            cards = Cards()
            cards.draw()
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        guess_card = input("Guess card? Higher or Lower [h/l] ")
        if guess_card == "h":
            self.is_playing = (guess_card == "h")
        elif guess_card == "l":
            self.is_playing = (guess_card == "l")

    # def determiner(self.current_card, self.next_card, guess_card):
    #     if self.next_card > self.current_card

       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        for i in range(len(self.card)):
            cards = self.card[i]
            cards.draw()
            self.score += cards.points 
        self.total_score += self.score

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)


director = Director()
director.start_game()
