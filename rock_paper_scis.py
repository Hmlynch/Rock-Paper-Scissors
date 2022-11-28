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
                    # player_choice = self.choices[0]
                    break
                elif player_choice == 'paper':
                    # player_choice = self.choices[1]
                    break
                elif player_choice =='scissors':
                    # player_choice = self.choices[2]
                    break
                else:
                    print("Please enter a valid choice!")
            except ValueError:
                print("Please enter a valid choice!")
        self.player_option = player_choice
        

    def computer_move(self):
        self.computer_option = random.choice(self.choices).lower()

    def who_wins(self): # Should I be using self.player_option() instead of self.player_choice?

        # player = self.player_option
        # computer = self.computer_option
        
        if self.player_option == 'rock' and self.computer_option == 'scissors':
            self.player_wins += 1
            return "Player wins"
        elif self.computer_option == 'rock' and self.player_option == 'scissors':
            self.computer_wins += 1
            return "Computer wins"
        elif self.player_option == 'scissors' and self.computer_option == 'paper':
            self.player_wins += 1
            return "Player wins"
        elif self.computer_option =='scissors' and self.player_option == 'paper':
            self.computer_wins += 1
            return "Computer wins"
        elif self.player_option == 'paper' and self.computer_option == 'rock':
            self.player_wins += 1
            return "Player wins"
        elif self.computer_option == 'paper' and self.player_option == 'rock':
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
                print(f"Player Chose: {self.player_option}\nComputer Chose: {self.computer_option}")
                print(f"Player wins: {self.player_wins}\nComputer wins: {self.computer_wins}")
            elif self.player_wins == 3:
                print("Congratulations, you won!")
                break
            elif self.computer_wins == 3:
                print("Computer won.")
                break


    def main_driver(self):
        while True:
            print("Welcome to Rock Paper Scissors!")
            print("Pick from the following options: ")
            print("1) Play the game!")
            print("2) Tutorial")
            print("3) Exit")
            prompt_choice = input("What would you like to do?")
            if prompt_choice == '1':
                self.play_game()
                break
            elif prompt_choice == '2':
                print("Here is how you play...")
                print("------------------------")
                print("* Rock beats Scissors")
                print("* Scissors beats Paper")
                print("* Paper beats Rock")
                print("* If player and computer pick the same, they tie")
            elif prompt_choice == '3':
                exit()
            else:
                print("You have not entered a number to proceed.")
                

if __name__ == '__main__':
    play = Rock_Paper_Scissors()
    play.main_driver()