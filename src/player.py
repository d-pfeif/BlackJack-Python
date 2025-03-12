class Player:
    def __init__(self, name, total_money):
        self.name = name
        self.total_money = total_money
        self.hand = []
        self.played = False

    def hit(self, card):
        self.played = True
        self.add_card(card)

    def stand(self):
        self.played = True
        return self.hand

    def anty(self, amount):
        self.total_money -= amount

    def update_money(self, amount):
        self.total_money += amount

    def reset_hand(self):
        self.hand = []

    def get_hand_value(self):
        value = 0
        ace_count = 0
        for card in self.hand:
            if card[0] in ['Jack', 'Queen', 'King']:
                value += 10
            elif card[0] == 'Ace':
                value += 11
                ace_count += 1
            else:
                value += int(card[0])

        while value > 21 and ace_count:
            value -= 10
            ace_count -= 1

        return value
    
    def add_card(self, card):
        self.hand.append(card)
    
    def busted(self):
        return self.get_hand_value() > 21

    def __str__(self):
        return f"{self.name} has {self.total_money} and hand: {self.hand}"