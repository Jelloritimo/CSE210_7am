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
        # self.current_card = 0
        # self.next_card = 0
        # self.points = 100

    def draw(self,decide):
        """Generates a new random value and calculates the points for the die.
        
        Args:
            self (Die): An instance of Die.
        """
        if decide == "1":
            self.current_card = random.randint(1, 13)
            print(f"The card is: {self.current_card}")
            return self.current_card
        elif decide == "2":
            self.next_card = random.randint(1, 13)
            print(f"The next card was: {self.next_card}")
            return self.next_card            
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
            counter += 1

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        guess_card = input("Guess card? Higher or Lower [h/l] ")
        if guess_card == "h":
            # self.is_playing = (guess_card == "h")
            return guess_card
        elif guess_card == "l":
            return guess_card
            # self.is_playing = (guess_card == "l")
        else:
            print("Invalid Input")

    # def determiner(self.current_card, self.next_card, guess_card):
    #     if self.next_card > self.current_card

       
    def do_updates(self,current_card,next_card,guess,counter):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        # if not self.is_playing:
        #     return 
        if counter == 1:
            if current_card > next_card and guess == "l" or current_card < next_card and guess == "h":
                self.total_score = self.points + self.beginnerscore
            else:
                self.total_score = self.beginnerscore - self.points
        else:
            if current_card > next_card and guess == "l" or current_card < next_card and guess == "h":
                self.total_score += self.points
            else:
                self.total_score = self.total_score - self.points
         
        # elif :
        #     self.score += self.points

        # for i in range(len(self.card)):
        #     cards = self.card[i]
        #     cards.draw()
        #     self.score += cards.points 
        # self.total_score += self.total_score

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.total_score > 0)


director = Director()
director.start_game()
