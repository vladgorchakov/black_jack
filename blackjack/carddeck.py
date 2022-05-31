from .card import Card
from random import shuffle


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
