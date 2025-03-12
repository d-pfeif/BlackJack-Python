# This file is the entry point of the game. It initializes the game, creates instances of the Player and Dealer, and manages the game loop, including user input for betting and actions (hit or stand).

from deck import Deck
from player import Player
from game import Game

def main():
    print("Welcome to BlackJack!")
    
    player_name = input("Enter your name: ")
    player_money = 100  # Starting money for the player
    player = Player(player_name, player_money)
    dealer = Player("Dealer", 0)  # Dealer does not have money to bet
    deck = Deck()

    game = Game(player, dealer, deck)

    while True:
        game.start_game()
        game.player_turn()
        game.dealer_turn()
        game.check_winner()

        if player.total_money <= 0:
            print("You have run out of money! Game over.")
            break

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()