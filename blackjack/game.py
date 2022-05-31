from .player import Player
from .dealer import Dealer
from .carddeck import CardDeck


class Game:
    def __init__(self, player_name: str) -> None:
        self.player = Player(player_name)
        self.card_deck = CardDeck()
        self.dealer = Dealer('Дилер')
    
    
    def print(self) -> str:
        return f'\n{self.player.name}:{self.player.hand} = {self.player.count}\n{self.dealer.name}:{self.dealer.hand} = {self.dealer.count}'
    
    
    def check_count(self) -> None:
        self.player.total_games += 1
        
        print(f'\n*Результаты игры: {self.player.total_games}*')
        if self.player.count > 21:
            print(f'Вы проиграли!', self.print())
        
        elif self.dealer.count > 21 and self.player.count <= 21:
            self.player.win_games += 1
            print(f'Вы выиграли!', self.print())
        
        elif self.player.count == self.dealer.count:
            print(f'Ничья!', self.print())
            
        elif self.dealer.count > self.player.count:
            print(f'Вы проиграли!', self.print())
            
        elif self.dealer.count < self.player.count:
            self.player.win_games += 1
            print(f'Вы выиграли!', self.print())
    
    
    def new_game(self):
        self.player.remove_cards()
        self.dealer.remove_cards()
        self.card_deck = CardDeck()
        
        
    def show_stat(self):
        print(f'\n*Результаты ваших игр:*')
        print(f'*Всего игр: {self.player.total_games}*')
        print(f'*Побед: {self.player.win_games}*')


    def start(self) -> None:
        print(f'Привет, {self.player.name}!')
        while True:
            
            for i in range(2):
                self.player.cards = next(self.card_deck)
                self.dealer.cards = next(self.card_deck)            
            
            print(f'Ваши карты: {self.player.cards} = {self.player.count}\n')
            while self.player.count < 21:
                ans = input('Взять ещё одну карту (y/n): ').lower()
                if ans == 'y':
                    self.player.cards = next(self.card_deck)
                    print(f'Ваши карты: {self.player.cards} = {self.player.count}\n')
                
                elif ans == 'n':
                    while self.dealer.make_choice():
                        self.dealer.cards = next(self.card_deck)
                    break
            
            self.check_count()
            
            ans = input('\nНачать новую игру (y)/(n): ')
            if ans == 'y':
                self.new_game()
            else:
                self.show_stat()
                break
