class Game:
    def __init__(self):
        option = input()
        loses_from = {'scissors': 'rock', 'paper': 'scissors', 'rock': 'paper'}
        end_text = "Sorry, but computer chose {}"
        print(end_text.format(loses_from.get(option)))


if __name__ == "__main__":
    Game()
