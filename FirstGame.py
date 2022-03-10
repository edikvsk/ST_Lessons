from Game import Game


class FirstGame(Game):

    def start_game(self):
        random_num = self.get_random_num

        print(f"Угадай целое число в диапазоне от {self.LOWER_NUM} до {self.HIGHER_NUM}")

        while True:
            try:
                input_num = int(input("Введи число: "))
            except ValueError:
                print("-->  Неверное значение, попробуй снова  -->")
                continue

            if self.result(random_num, input_num):
                break

    def result(self, input_num, random_num):
        if input_num == random_num:
            print(f"-->  Правильно! Ответ: {random_num}")
            return True

        elif input_num > random_num:
            print("Твое число меньше загаданного")
            return False

        else:
            print("Твое число больше загаданного")
            return False


FirstGame()