# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 2020

@author: eleyf
"""

import Dominion
import random
from collections import defaultdict


# Get player names
def get_player_names():
    player_names = ["Annie", "*Ben", "*Carla"]
    return player_names


# number of victory cards
def get_numbe_of_victory_cards(number_of_players):
    if number_of_players > 2:
        return 12
    else:
        return 8


# number of curse cards
def get_number_of_curse_cards(number_of_players):
    return -10 + (10 * number_of_players)


# Define box
def get_box(number_of_victory_cards):
    box = {}
    box["Woodcutter"] = [Dominion.Woodcutter()] * 10
    box["Smithy"] = [Dominion.Smithy()] * 10
    box["Laboratory"] = [Dominion.Laboratory()] * 10
    box["Village"] = [Dominion.Village()] * 10
    box["Festival"] = [Dominion.Festival()] * 10
    box["Market"] = [Dominion.Market()] * 10
    box["Chancellor"] = [Dominion.Chancellor()] * 10
    box["Workshop"] = [Dominion.Workshop()] * 10
    box["Moneylender"] = [Dominion.Moneylender()] * 10
    box["Chapel"] = [Dominion.Chapel()] * 10
    box["Cellar"] = [Dominion.Cellar()] * 10
    box["Remodel"] = [Dominion.Remodel()] * 10
    box["Adventurer"] = [Dominion.Adventurer()] * 10
    box["Feast"] = [Dominion.Feast()] * 10
    box["Mine"] = [Dominion.Mine()] * 10
    box["Library"] = [Dominion.Library()] * 10
    box["Gardens"] = [Dominion.Gardens()] * number_of_victory_cards
    box["Moat"] = [Dominion.Moat()] * 10
    box["Council Room"] = [Dominion.Council_Room()] * 10
    box["Witch"] = [Dominion.Witch()] * 10
    box["Bureaucrat"] = [Dominion.Bureaucrat()] * 10
    box["Militia"] = [Dominion.Militia()] * 10
    box["Spy"] = [Dominion.Spy()] * 10
    box["Thief"] = [Dominion.Thief()] * 10
    box["Throne Room"] = [Dominion.Throne_Room()] * 10
    return box


def get_supply_order():
    supply_order = {0: ['Curse', 'Copper'], 2: ['Estate', 'Cellar', 'Chapel', 'Moat'],
                    3: ['Silver', 'Chancellor', 'Village', 'Woodcutter', 'Workshop'],
                    4: ['Gardens', 'Bureaucrat', 'Feast', 'Militia', 'Moneylender', 'Remodel', 'Smithy', 'Spy', 'Thief',
                        'Throne Room'],
                    5: ['Duchy', 'Market', 'Council Room', 'Festival', 'Laboratory', 'Library', 'Mine', 'Witch'],
                    6: ['Gold', 'Adventurer'], 8: ['Province']}

    return supply_order


# Pick 10 cards from box to be in the supply.
def pick_ten_cards(box):
    boxlist = [k for k in box]
    random.shuffle(boxlist)
    random10 = boxlist[:10]
    return defaultdict(list, [(k, box[k]) for k in random10])


# The supply always has these cards
def add_permanant_cards(supply, number_of_players, number_of_victory_cards, number_of_curse_cards):
    supply["Copper"] = [Dominion.Copper()] * (60 - number_of_players * 7)
    supply["Silver"] = [Dominion.Silver()] * 40
    supply["Gold"] = [Dominion.Gold()] * 30
    supply["Estate"] = [Dominion.Estate()] * number_of_victory_cards
    supply["Duchy"] = [Dominion.Duchy()] * number_of_victory_cards
    supply["Province"] = [Dominion.Province()] * number_of_victory_cards
    supply["Curse"] = [Dominion.Curse()] * number_of_curse_cards
    return supply


# Costruct the Player objects
def get_players(player_names):
    players = []
    for name in player_names:
        if name[0] == "*":
            players.append(Dominion.ComputerPlayer(name[1:]))
        elif name[0] == "^":
            players.append(Dominion.TablePlayer(name[1:]))
        else:
            players.append(Dominion.Player(name))
    return players


# Play the game
def play_game(supply, supply_order, players):
    trash = []
    turn = 0
    while not Dominion.gameover(supply):
        turn += 1
        print("\r")
        for value in supply_order:
            print(value)
            for stack in supply_order[value]:
                if stack in supply:
                    print(stack, len(supply[stack]))
        print("\r")
        for player in players:
            print(player.name, player.calcpoints())
        print("\rStart of turn " + str(turn))
        for player in players:
            if not Dominion.gameover(supply):
                print("\r")
                player.turn(players, supply, trash)


# Final score
def dispaly_score(players):
    card_summary = Dominion.cardsummaries(players)
    victory_points = card_summary.loc['VICTORY POINTS']
    victory_points_max = victory_points.max()
    winners = []
    for i in victory_points.index:
        if victory_points.loc[i] == victory_points_max:
            winners.append(i)
    if len(winners) > 1:
        winstring = ' and '.join(winners) + ' win!'
    else:
        winstring = ' '.join([winners[0], 'wins!'])

    print("\nGAME OVER!!!\n" + winstring + "\n")
    print(card_summary)
