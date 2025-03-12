# Blackjack Game

Welcome to the Blackjack Game! This is a simple text-based implementation of the classic card game where you can play against an automated dealer.

## Overview

In this game, you will compete against the dealer by trying to get a hand value as close to 21 as possible without going over. You can choose to hit (take another card) or stand (keep your current hand). The game also allows you to place bets and keeps track of your total money.

## Features

- One player versus an automated dealer
- Ability to hit or stand
- Betting system to place bets
- Tracking of player's total money
- Alerts for wins, losses, and busts

## Files

- `src/main.py`: Entry point of the game. Initializes the game and manages the game loop.
- `src/deck.py`: Defines the Deck class for creating and managing a standard deck of cards.
- `src/player.py`: Defines the Player class, representing the player with properties for hand and money.
- `src/game.py`: Contains the Game class that manages game logic and interactions between player and dealer.
- `requirements.txt`: Lists the dependencies required for the project.

## How to Run the Game

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```
4. Run the game using:
   ```
   python src/main.py
   ```

## Game Rules

- The goal is to have a hand value closer to 21 than the dealer without exceeding 21.
- Number cards are worth their face value, face cards (Jack, Queen, King) are worth 10, and Aces can be worth 1 or 11.
- You can place a bet before the game starts.
- If your hand exceeds 21, you bust and lose your bet.
- The dealer must hit until their hand value is 17 or higher.

Enjoy the game and good luck!