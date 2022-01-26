import random

class Cards:
    def __init__(self):
        self.first_turn = True
        self.current_card = 0
        self.next_card = 0
        self.points = 0

    def draw(self):
        if self.first_turn == True:
            self.current_card = random.randint(1, 13)
            print(f"The card is: {self.current_card}")
        else: print(f"The card is: {self.current_card}")

        return self.current_card
    
    def next_draw(self):
        self.next_card = random.randint(1, 13)
        print(f"Next card was: {self.next_card}")
        self.first_turn = False
        return self.next_card

    def looping_draws(self):
        self.next_card = self.current_card



class Director:
    def __init__(self):
        self.card = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

    def start_game(self):
        while self.is_playing:
            cards = Cards()
            cards.draw()
            self.get_inputs()
            cards.next_draw()
            self.do_updates()
            cards.looping_draws()
            self.do_outputs()

    def get_inputs(self):
        self.guess_card = input("Guess card? Higher or Lower [h/l] ")
        if self.guess_card != "h" or "l":
            print("Invalid input. Please try again.")
            quit()

    def do_updates(self):
        cards = Cards()
        current_card = cards.current_card
        next_card = cards.next_card
        if self.guess_card == "h" and current_card > next_card:
            self.total_score += 100
        elif self.guess_card == "h" and current_card < next_card:
            self.total_score -= 75
        elif self.guess_card == "l" and current_card > next_card:
            self.total_score -= 75
        elif self.guess_card == "l" and current_card < next_card:
            self.total_score += 100
        else: 
            print("An error has occured. Please try again.")
            quit()

    def do_outputs(self):
        print(f"Your score is: {self.total_score}\n")
        cont_play = input("Play again? [y/n]")

        if cont_play == "y":
            self.is_playing = True
        elif cont_play == "n":
            print("Goodbye.")
            self.is_playing = False
        else: 
            print("Invalid input. Please try again.")
            quit()

director = Director()
director.start_game()
