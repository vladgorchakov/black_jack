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
        self.__cards = []
        self.__suits = ['П','Б','К','Ч']
        self.__ranks = ['Т', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Д', 'В', 'К']
    
    
    def create_deck(self) -> None:
        self.__cards = [Card(rank, suit) for rank in self.__ranks for suit in self.__suits]
        shuffle(self.__cards)
        return self.__cards
    
    
    def get_card(self) -> Card:
        return self.__cards.pop()
    
    
    def set_card(self, card: Card):
        self.__cards.append(card)
        return self.__cards[-1]
    
    
    @property
    def cards(self):
        return self.__cards


"""This class create player"""
class Player:
    def __init__(self, name) -> None:
        self.__name = name
        self.__hand = []
        self.__count = 0
     
     
    def get_card(self):
        return self.__hand
    
    
    def set_card(self, card: Card) -> None:
        self.__hand.append(card)
        self.__count += card.get_value()
        
    
    def remove_cards(self):
        self.__hand.clear()
        self.__count = 0
        return self
    
    
    def show_info(self):
        return f'{self.__name}: {self.__hand} {self.__count}'
    
    
    def __repr__(self):
        return self.show_info()
    
    
    cards = property(get_card, set_card)
    

c = CardDeck()
c.create_deck()
print(*c.cards)
vlad = Player('Vlad')
vlad.cards = c.get_card()
print(vlad.cards)
