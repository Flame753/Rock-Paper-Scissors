from random import choice


class Game:
    def __init__(self):
        self.player_option = None
        self.computer_option = None
        self.running = True

    def run(self):
        while self.running:
            self.player_option = input()
            self.computer_option = choice(['rock', 'scissors', 'paper'])
            if self.valid_option():
                self.result()

    def result(self):
        condition = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

        if self.player_option == "!exit":
            print("Bye!")
            self.running = False
        elif self.player_option == self.computer_option:
            print(f"There is a draw ({self.computer_option})")
        elif self.computer_option == condition[self.player_option]:
            print(f"Well done. Computer chose {self.computer_option} and failed")
        else:
            print(f"Sorry, but computer chose {self.computer_option}")

    def valid_option(self):
        valid_options = ['rock', 'scissors', 'paper', '!exit']
        if self.player_option in valid_options:
            return True

        print('Invalid input')
        return False


if __name__ == "__main__":
    r = Game()
    r.run()
