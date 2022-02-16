import random


class GuessTheNumber:

    def __init__(self):
        self.LOWER_NUM = 1
        self.HIGHER_NUM = 10

    def get_random_num(self):
        return random.randint(self.LOWER_NUM, self.HIGHER_NUM)

    # метод запускающий игру
    def play(self):
        random_num = self.get_random_num()

        print(f"Угадай целое число в диапазоне от {self.LOWER_NUM} до {self.HIGHER_NUM}")

        # игровая механика
        attempts = 1
        while True:
            try:
                input_num = int(input("Введи число: "))
            except ValueError:
                print('--> Неверное значение, счет попыток обнулен.')
                self.play()
                break

            if input_num == random_num:
                print(
                    f"Верное число {random_num}. Угадано с {attempts}-ого раза")
                break

            elif input_num < random_num:
                print("Твое число меньше загаданного")

            else:
                print("Твое число больше загаданного")
            attempts += 1


guessTheNumberGame = GuessTheNumber()
guessTheNumberGame.play()
