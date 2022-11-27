import random

class Rock_Paper_Scissors():
    def __init__(self): # the init method is called every time an object is created from a class.
        self.choices = ["Rock", "Paper", "Scissors"]
        self.player_wins = 0
        self.computer_wins = 0

    def player_move(self):
        while True:
            try:
                player_choice = input("Enter your choice: Rock, Paper, or Scissors: ").lower()
                if player_choice == 'rock':
                    break
                elif player_choice == 'paper':
                    break
                elif player_choice =='scissors':
                    break
                else:
                    print("Please enter a valid choice!")
            except ValueError:
                print("Please enter a valid choice!")
        return player_choice
        

    def computer_move(self):
        computer_choice = random.choice(self.choices)
        return computer_choice

    def who_wins(self): # Should I be using self.player_move() instead of self.player_choice?
        
        if self.player_move == 'rock' and self.computer_move == 'scissors':
            self.player_wins += 1
            return "Player wins"
        elif self.computer_move == 'rock' and self.player_move == 'scissors':
            self.computer_wins += 1
            return "Computer wins"
        elif self.player_move == 'scissors' and self.computer_move == 'paper':
            self.player_wins += 1
            return "Player wins"
        elif self.computer_move =='scissors' and self.player_move == 'paper':
            self.computer_wins += 1
            return "Computer wins"
        elif self.player_move == 'paper' and self.computer_move == 'rock':
            self.player_wins += 1
            return "Player wins"
        elif self.computer_move == 'paper' and self.player_move == 'rock':
            self.computer_wins += 1
            return "Computer wins"
        else:
            return "Tie"
                       

    def play_game(self):
        while True:
            if self.player_wins < 3 and self.computer_wins < 3:
                self.player_move()
                self.computer_move()
                self.who_wins()
                print(f"Player Chose: {self.player_move}\nComputer Chose: {self.computer_move}")
                print(f"Player wins: {self.player_wins}\nComputer wins: {self.computer_wins}")
            elif self.player_wins == 3:
                print("Congratulations, you won!")
            elif self.computer_wins == 3:
                print("Computer won.")


    def main_driver(self):
        self.play_game()
                


if __name__ == '__main__':
    play = Rock_Paper_Scissors()
    play.main_driver()