import os
from random import choice


class Game:
    def __init__(self):
        self.current_player = None
        self.score = 0
        self.custom_options = None
        self.conditions = {}
        self.player_option = None
        self.computer_option = None
        self.running = True

    def play(self):
        self.greeting()
        self.set_up_custom_options()
        self.set_up_conditions()
        self.set_up_file()
        while self.running:
            self.player_option = input()
            self.computer_option = choice(self.custom_options)
            if self.valid_option():
                self.result()

    def set_up_custom_options(self):  # Would need to prevent some case
        self.custom_options = input().split(',')
        if self.custom_options == ['']:
            self.custom_options = 'rock,paper,scissors'.split(',')
        print("Okay, let's start")

    def set_up_conditions(self):
        new_options = self.custom_options.copy()
        length = len(new_options) - 1
        start = 1
        end = 1 + (length//2)
        new_options.reverse()
        new_options.extend(new_options)
        for index in range(0, length+1):
            self.conditions.update({new_options[index]: new_options[start: end]})
            start += 1
            end += 1

    def result(self):
        if self.player_option == "!exit":
            print("Bye!")
            self.running = False

        elif self.player_option == "!rating":
            print(f'Your rating: {self.score}')

        elif self.player_option == self.computer_option:
            print(f"There is a draw ({self.computer_option})")
            self.score += 50
            self.update_file_score()

        elif self.computer_option in self.conditions[self.player_option]:
            print(f"Well done. Computer chose {self.computer_option} and failed")
            self.score += 100
            self.update_file_score()

        else:
            print(f"Sorry, but computer chose {self.computer_option}")

    def valid_option(self) -> bool:
        valid_options = ['!exit', '!rating']
        valid_options.extend(self.custom_options)
        if self.player_option in valid_options:
            return True

        print('Invalid input')
        return False

    def greeting(self):
        name = input('Enter your name: ')
        print('Hello, ' + name)
        self.current_player = name

    def set_up_file(self):
        try:
            file_size = os.path.getsize('rating.txt')
            if file_size == 0:  # If File Empty
                file = open('rating.txt', 'a')
                print(self.current_player, self.score, file=file)
                #file.write(self.current_player + ' ' + str(self.score) + '\n')
                file.close()
            else:
                file = open('rating.txt', 'r')
                new_file_content = []
                for line in file:  # Broken its Doubling the name
                    name, score = line.split()
                    if name == self.current_player:  # If name Exist
                        self.score = int(score)
                        break
                    else:
                        new_line = self.current_player + ' ' + str(self.score)
                        new_file_content.append(new_line + "\n")
                        break
                file.close()

                file = open('rating.txt', 'a')
                file.writelines(new_file_content)
                file.close()

        except FileNotFoundError:
            file = open('rating.txt', 'w')
            file.write(self.current_player + ' ' + str(self.score))
            file.close()

    def update_file_score(self):
        file = open('rating.txt', 'r')
        new_file_content = []
        for line in file:
            split_line = line.split()
            if split_line[0] == self.current_player:
                new_line = split_line[0] + ' ' + str(self.score)
            else:
                new_line = split_line[0] + ' ' + split_line[1]
            new_file_content.append(new_line + "\n")
        file.close()

        writing_file = open("rating.txt", "w")
        writing_file.writelines(new_file_content)
        writing_file.close()


if __name__ == "__main__":
    Game().play()
