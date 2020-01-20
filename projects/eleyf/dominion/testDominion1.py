# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 2020

@author: eleyf
"""
import Dominion
import testUtility

# Get player names
player_names = testUtility.get_player_names()

# Get number of victory and curse cards
number_of_victory_cards = testUtility.get_numbe_of_victory_cards(len(player_names))
number_of_curse_cards = testUtility.get_number_of_curse_cards(len(player_names))

# Define box
box = testUtility.get_box(number_of_victory_cards)

#Bug that changes the number of witch cards to 100
box["Witch"] = [Dominion.Witch()] * 100

# Define supply order
supply_order = testUtility.get_supply_order()

# Pick 10 cards from box to be in the supply.
supply = testUtility.pick_ten_cards(box)

# The supply always has these cards
supply = testUtility.add_permanant_cards(supply, len(player_names), number_of_victory_cards, number_of_curse_cards)

# Costruct the Player objects
players = testUtility.get_players(player_names)

# Play the game
testUtility.play_game(supply, supply_order, players)

# Final score
testUtility.dispaly_score(players)
