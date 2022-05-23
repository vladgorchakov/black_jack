import random


class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit
        
    def get_volue(self) -> int:
        if self.rank in "ТДВК":
            return 10
        else:
            return " А23456789".index(self.rank)
        
    def get_rank(self) -> str:
        return f'{self.suit}{self.rank}'
    
    def __repr__(self):
        return f'{self.suit}{self.rank}'
    
    
class DeskCard:
    def __init__(self):
        self._rank = "А23456789ТДВК"
        self._suit = "ПБЧК"
        self.cards = [Card(rank, suit) for rank in self._rank for suit in self._suit]
        random.shuffle(self.cards)
        
    
    def get_card(self) -> Card:
        return self.cards.pop()
    

class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self._hand = []
        self.count = 0
     
     
    @property
    def hand(self):
        return f'Карты в руке: {self._hand}; Очков - {self.count}'
    
    
    @hand.setter
    def hand(self, card: Card) -> None:
        self._hand.append(card.get_rank())
        self.count += card.get_volue()


class Dealer(Player):
    #def get_card(self, cards: DeskCard):
        #while self.count < 18:
            #self.hand = cards.get_card()
    
    def get_card(self, cards: DeskCard):
        while self.count < 21:
            _card = cards.get_card()
            if _card.get_volue() + self.count <= 21:
                self.hand = _card
            else:
                break
    
class Game:
    def __init__(self, player_name: str) -> None:
        self.cards = DeskCard()
        self.player = Player(name=player_name)
        self.dealer = Dealer('Dealer')
        
    def print(self) -> str:
        return f'\n{self.player.name}:\n{self.player.hand}\n{self.dealer.name}:\n{self.dealer.hand}'
    
    def check_count(self) -> None:
        if self.player.count > 21:
            print(f'Вы проиграли!', self.print())
        
        elif self.dealer.count > 21 and self.player.count <= 21:
            print(f'Вы выиграли!', self.print())
        
        elif self.player.count == self.dealer.count:
            print(f'Ничья!', self.print())
            
        elif self.dealer.count > self.player.count:
            print(f'Вы проиграли!', self.print())
            
        elif self.dealer.count < self.player.count:
            print(f'Вы выиграли!', self.print())
            
    def start(self):
        self.player.hand = self.cards.get_card()
        self.player.hand = self.cards.get_card()
        print(self.player.hand)
        
        self.dealer.hand = self.cards.get_card()
        self.dealer.hand = self.cards.get_card()
        
        while self.player.count < 21:
    
            answer = input('Do you want to take one card Yes(y)/No(n)')
            if answer == 'y':
                self.player.hand = self.cards.get_card()
                print(self.player.hand)
                
            elif answer == 'n':
                self.dealer.get_card(self.cards)
                break
        
        self.check_count()


def main() -> None:
    game = Game('Vlad')
    game.start()


if __name__ == "__main__":
    main()
