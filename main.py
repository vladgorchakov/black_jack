from blackjack.game import Game


def main():
    g = Game(input('Введите своё имя: '))
    g.start()
    g.show_stat()


if __name__=='__main__':
    main()
