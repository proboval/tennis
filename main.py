from Game.game import Game


if __name__ == '__main__':
    tennis = Game()

    flag = -1
    while flag == -1:
        flag = tennis.start()

    tennis.set_length()
    tennis.start_game()
