class Game:
    def __init__(self, player, dealer, deck):
        self.player = player
        self.dealer = dealer
        self.deck = deck
        self.bets = {}

    def start_game(self):
        self.player.played = False
        self.dealer.played = False
        self.player.reset_hand()
        self.dealer.reset_hand()
        self.anty()
        self.deck.shuffle()
        self.deal_initial_cards()
        self.check_winner()

    def anty(self):
        while True:
            try:
                print(f"\nYour total money: ${self.player.total_money}")
                anty_amount = int(input("Enter the amount you'd like to anty: "))
                if anty_amount > self.player.total_money:
                    print("You don't have enough money.")
                elif anty_amount > 0:
                    self.player.anty(anty_amount)
                    self.bets[self.player.name] = anty_amount
                    break
                else:
                    print("Anty amount must be greater than zero.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def deal_initial_cards(self):
        for _ in range(2):
            self.player.add_card(self.deck.deal_card())
            self.dealer.add_card(self.deck.deal_card())

    def player_turn(self):
        while True:
            print(f"\nYour hand: {self.player.hand}, Total: {self.player.get_hand_value()}")
            print(f"Dealer's hand: {self.dealer.hand[0]}\n")
            
            action = input("Do you want to hit or stand? (h/s): ").lower()
            if action == 'h':
                self.player.hit(self.deck.deal_card())
                if self.player.busted():
                    print("You busted!")
                    break
            elif action == 's':
                self.player.stand()
                break
            else:
                print("Invalid input. Please enter 'h' or 's'.")

    def dealer_turn(self):
        while self.dealer.get_hand_value() < 17:
            self.dealer.add_card(self.deck.deal_card())

    def check_winner(self):
        player_value = self.player.get_hand_value()
        dealer_value = self.dealer.get_hand_value()


        if self.player.played:
            print(f"\nYour hand: {self.player.hand}, Total: {self.player.get_hand_value()}")
            print(f"Dealer's hand: {self.dealer.hand}, Total: {self.dealer.get_hand_value()}\n")

            if self.player.busted():
                print("You lose!")
            elif dealer_value > 21 or player_value > dealer_value:
                print("Congratulations!")
                amount_won = self.bets[self.player.name] * 2

                if player_value == 21 and len(self.player.hand) == 2:
                    print("You have BlackJack!")
                    amount_won += self.bets[self.player.name] // 2

                self.player.update_money(amount_won)
                print(f"You won ${amount_won}! Total money: ${self.player.total_money}")
            elif player_value < dealer_value:
                print("You lose! Sorry!")
            else:
                print("It's a tie!")
        elif dealer_value == 21:
            if player_value != 21:
                print("Dealer has BlackJack! You lose!")
            else:
                print("You both have BlackJack! It's a tie!")
                
    
        