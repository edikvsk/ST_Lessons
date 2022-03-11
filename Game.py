from random import randint


class Game:
    def __init__(self):
        self.LOWER_NUM: int = int(1)
        self.HIGHER_NUM: int = int(10)
        self.get_random_num: int = int(randint(self.LOWER_NUM, self.HIGHER_NUM))
        self.start_game()

    def __del__(self):
        print('--> Победа!')
