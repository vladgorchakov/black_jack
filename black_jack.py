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


class Game:
    def __init__(self, player_name: str) -> None:
        self.cards = DeskCard()
        self.player = Player(name=player_name)
        
        
    def start(self):
        self.player.hand = self.cards.get_card()
        self.player.hand = self.cards.get_card()
        print(self.player.hand)


def main() -> None:
    game = Game(input('your name: '))
    game.start()


if __name__ == "__main__":
    main()
