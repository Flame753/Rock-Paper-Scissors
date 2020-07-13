from random import choice


class Game:
    def __init__(self):
        self.player_option = input()
        self.computer_option = choice(['rock', 'scissors', 'paper'])

    def run(self):
        player = self.player_option
        computer = self.computer_option
        condition = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

        if player == computer:
            print(f"There is a draw ({computer})")
        elif computer == condition[player]:
            print(f"Well done. Computer chose {computer} and failed")
        else:
            print(f"Sorry, but computer chose {computer}")


if __name__ == "__main__":
    r = Game()
    r.run()
