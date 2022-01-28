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
        self.points = 100

    def draw(self,decide):
        """Generates a new random value and calculates the points for the die.
        
    
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
