from .player import Player


class Dealer(Player):
        
    def make_choice(self) -> bool:
        if self.count < 18:
            print('Беру!')
            return True
        else:
            print('Не беру!')
            return False
