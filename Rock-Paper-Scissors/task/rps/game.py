from random import choice


class Game:
    def __init__(self):
        self.current_player = None
        self.score = 0
        self.player_option = None
        self.computer_option = None
        self.running = True
        self.file = open('rating.txt', 'w')
        self.file.close()

    def run(self):
        self.greeting()
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

        elif self.player_option == "!rating":
            print(f'Your rating: {self.score}')

        elif self.player_option == self.computer_option:
            print(f"There is a draw ({self.computer_option})")
            self.score += 50

        elif self.computer_option == condition[self.player_option]:
            print(f"Well done. Computer chose {self.computer_option} and failed")
            self.score += 100

        else:
            print(f"Sorry, but computer chose {self.computer_option}")

        self.file_set_score()

    def valid_option(self) -> bool:
        valid_options = ['rock', 'scissors', 'paper', '!exit']
        if self.player_option in valid_options:
            return True

        print('Invalid input')
        return False

    def greeting(self):
        name = input('Enter your name: ')
        print('Hello, ' + name)
        self.current_player = name
        self.file_get_score()

    def file_get_score(self):
        self.file = open('rating.txt', 'r')
        for line in self.file:
            name, score = line.split()
            if name == self.current_player:
                self.score = int(score)
        self.file.close()

    def file_set_score(self):
        self.file = open('rating.txt', 'a')
        print(self.current_player + str(self.score), file=self.file)
        self.file.close()


if __name__ == "__main__":
    r = Game()
    r.run()
