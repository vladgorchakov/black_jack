from random import shuffle


"""This class create playing card"""
class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit
    
    
    def get_value(self) -> int:
        if self.rank in 'ДВК':
            return 10
        elif self.rank == 'Т':
            return (1, 11)
        else:
            return ['2', '3', '4', '5', '6', '7', '8', '9', '10'].index(self.rank) + 2
        
        
    def __repr__(self):
        return f'{self.rank}{self.suit}'
        

"""This class create card's deck"""
class CardDeck:
    def __init__(self) -> None:
        self.__suits = ['П','Б','К','Ч']
        self.__ranks = ['Т', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Д', 'В', 'К']
        self.__cards = [Card(rank, suit) for rank in self.__ranks for suit in self.__suits]
        shuffle(self.__cards)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.__cards:
            raise StopIteration
        
        item = self.__cards[0]
        del self.__cards[0]
        return item    
       

"""This class create player"""
class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.hand = []
        self.count = 0
        self.total_games = 0
        self.win_games = 0
        
        
    def choose_ace_value(self, card: Card) -> int:
        if self.count <=10:
            return card.get_value()[1]
        else:
            return card.get_value()[0]
     
    @property 
    def cards(self):
        return self.hand
    
    @cards.setter
    def cards(self, card: Card) -> None:
        if card.rank == 'Т':
            self.count += self.choose_ace_value(card)
        else:
            self.count += card.get_value()
        
        self.hand.append(card)        
    
    def remove_cards(self):
        self.hand.clear()
        self.count = 0
        return self
    
    
    def show_info(self):
        return f'\n*{self.name}*: {self.hand} {self.count};\n'
    
    def __repr__(self):
        return self.show_info()
    

class Dealer(Player):
        
    def make_choice(self) -> bool:
        if self.count < 18:
            print('Беру!')
            return True
        else:
            print('Не беру!')
            return False

class Game:
    def __init__(self, player_name: str) -> None:
        self.player = Player(player_name)
        self.card_deck = CardDeck()
        self.dealer = Dealer('Dealer')
    
    
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
        print(f'Hello, {self.player.name}!')
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
        
        
game = Game('Vlad')
game.start()