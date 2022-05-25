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
    
    
    def get_card(self) -> Card:
        return self.__cards.pop()
    
    
    def set_card(self, card: Card) -> None:
        self.__cards.append(card)

    
    @property
    def cards(self):
        return self.__cards
    


"""This class create player"""
class Player:
    def __init__(self, name) -> None:
        self.__name = name
        self.__hand = []
        self.__count = 0
        print('whoami')
     
     
    def get_card(self):
        return self.__hand
    
    
    def choose_ace_value(self, card: Card) -> int:
        if self.__count <=10:
            return card.get_value()[1]
        else:
            return card.get_value()[0]
        
    
    def set_card(self, card: Card) -> None:
        if card.rank == 'Т':
            self.__count += self.choose_ace_value(card)
        else:
            self.__count += card.get_value()
        
        self.__hand.append(card)
            
    
    def remove_cards(self):
        self.__hand.clear()
        self.__count = 0
        return self
    
    
    def show_info(self):
        return f'\n*{self.__name}*: {self.__hand} {self.__count};\n'
    
    
    def __repr__(self):
        return self.show_info()
    
    
    @property
    def name(self):
        return self.__name
    
    
    @property
    def count(self):
        return self.__count
    
    hand = property(get_card, set_card)
    

class Dealer(Player):
        
    def make_choice(self) -> bool:
        if self._Player__count < 18:
            return True
        else:
            return False
    

class Game:
    def __init__(self, player_name: str) -> None:
        self.player = Player(player_name)
        self.card_deck = CardDeck()
        self.dealer = Dealer('Dealer')
        print(self.dealer.__dict__)


    def start(self) -> None:
        print(f'Hello, {self.player.name}!')
        self.card_deck.create_deck()
        
        self.player.hand = self.card_deck.get_card()
        self.player.hand = self.card_deck.get_card()
        
        self.dealer.hand = self.card_deck.get_card()
        self.dealer.hand = self.card_deck.get_card()
        
        
        print(self.player)
        while self.player.count < 21:
            ans = input('Do you want to take new card (y/n): ').lower()
            if ans == 'y':
                self.player.hand = self.card_deck.get_card()
                print(self.player)
            
            elif ans == 'n':
                while self.dealer.make_choice():
                    self.dealer.hand = self.card_deck.get_card()
                break
            
            
        if self.player.count == 21:
            print('You are winner!')
        elif self.player.count > 21:
            print(f'Перебор!')
            
        print(self.player)    
        print(self.dealer)
        
        
game = Game('Vlad')
game.start()
