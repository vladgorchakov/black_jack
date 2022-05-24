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
            return ['2', '3', '4', '5', '6', '7', '8', '9', '10'].index(rank) + 2
        
        
    def __repr__(self):
        return f'{self.rank}{self.suit}'
        

"""This class create card's deck"""
class CardDeck:
    def __init__(self) -> None:
        self.__cards = []
        self.__suits = ['П','Б','К','Ч']
        self.__ranks = ['Т', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Д', 'В', 'К']
    
    
    def create_deck(self) -> None:
        self.__cards = [Card(rank, suit) for rank in self.__ranks for suit in self.__suits]
        shuffle(self.__cards)
        return self.__cards
    
    
    def get_card(self) -> Card:
        return self.__cards.pop()
    
    
    def set_card(self, card):
        self.__cards.append(card)
        return self.__cards[-1]
    
    
    @property
    def cards(self):
        return self.__cards


c = CardDeck()
c.create_deck()
card = c.get_card()
print(*c.cards)
card = c.set_card(card)
del card
print(*c.cards)
