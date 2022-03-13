from random import randint

from Game import Game


class SecondGame(Game):

    def start_game(self) -> None:
        print(f"Пользователь загадывает число в диапазоне от: {self.LOWER_NUM} до: {self.HIGHER_NUM}")

        while True:
            print(f"Компьютер пробует угадать загаданное число: {self.get_random_num}")
            user_answer = input(f" (=) - Компьютер угадал загаданное пользователем число\n "
                                f"(<) - Загаданное число меньше предложенного\n "
                                f"(>) - Загаданное число больше предложенного\n Введи ответ:")
            if self.result(user_answer):
                break
        print("Компьютер угадал загаданное пользователем число")

    def result(self, user_answer):
        while True:
            try:
                if user_answer == '=':
                    return True

                elif user_answer == '>':
                    self.LOWER_NUM = int(self.get_random_num) + 1
                    self.get_random_num = randint(self.LOWER_NUM, self.HIGHER_NUM)
                    return False

                elif user_answer == '<':
                    self.HIGHER_NUM = (self.get_random_num) - 1
                    self.get_random_num = randint(self.LOWER_NUM, self.HIGHER_NUM)
                    return False

                else:
                    print("--> Неверное значение, попробуй снова -->")
                    return False
            except ValueError:
                print("--> Выход из диапазона чисел, попробуй снова -->")
                break


SecondGame()
