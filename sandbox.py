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