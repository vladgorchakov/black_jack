from .carddeck import CardDeck
from .card import Card


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
