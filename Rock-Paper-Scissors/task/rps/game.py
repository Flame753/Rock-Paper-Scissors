from random import choice


class Game:
    def __init__(self):
        self.player_option = input()
        self.options = ['rock', 'scissors', 'paper']
        self.computer_option = choice(self.options)
        self.lose_text = "Sorry, but computer chose {}"
        self.draw_text = "There is a draw ({})"
        self.win_text = "Well done. Computer chose {} and failed"

    def run(self):
        self.compare_result()

    def compare_result(self):
        player = self.player_option
        computer = self.computer_option
        compare_results = (player, computer)
        win_results = [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]
        loss_results = [('rock', 'paper'), ('scissors', 'rock'), ('paper', 'scissors')]

        if compare_results in loss_results:
            print(self.lose_text.format(computer))
        if compare_results in win_results:
            print(self.win_text.format(computer))
        if player == computer:
            print(self.draw_text.format(computer))


if __name__ == "__main__":
    r = Game()
    r.run()
