#!/bin/python
"""
Given N teams of size K, how many combinations of N teams are there from a population of N x K x C (where C is an integer)?

{0: {'games': 5717712, 'wins': 77618},
 1: {'games': 5717712, 'wins': 2306592},
 2: {'games': 5717712, 'wins': 2577679},
 3: {'games': 5717712, 'wins': 2708399},
 4: {'games': 5717712, 'wins': 2806219},
 5: {'games': 5717712, 'wins': 2884107},
 6: {'games': 5717712, 'wins': 2948632},
 7: {'games': 5717712, 'wins': 3003931},
 8: {'games': 5717712, 'wins': 3052745},
 9: {'games': 5717712, 'wins': 3096873},
 10: {'games': 5717712, 'wins': 3136763},
 11: {'games': 5717712, 'wins': 3173620},
 12: {'games': 5717712, 'wins': 3207676},
 13: {'games': 5717712, 'wins': 3239329},
 14: {'games': 5717712, 'wins': 3269204},
 15: {'games': 5717712, 'wins': 3297152},
 16: {'games': 5717712, 'wins': 3323785},
 17: {'games': 5717712, 'wins': 3349084}}

Maybe permutation match making is not the best at this level?
Need to figure out a scoring mechanism that will result in a normalized distribution.

"""

import pprint

def choose_permute(population, choose):
    position = 0
    stack = [None for i in xrange(choose)]

    yield_value = range(choose)
    next_start = 0

    while True:
        if stack[position] is None:
            stack[position] = iter(xrange(next_start, population - (choose - position - 1)))

        iterator = stack[position]

        try:
            value = next(iterator)

            yield_value[position] = value

            if position < choose - 1:
                next_start = value + 1
                position = position + 1
            else:
                yield yield_value
        except StopIteration:
            if position > 0:
                stack[position] = None
                position = position - 1
            else:
                return


total_players = 18

win_dict = {}
for i in xrange(total_players):
    win_dict[i] = {'games': 0, 'wins': 0}
    
game_players = 12
team_players = game_players / 2

game_players_two_team = game_players - 1
team_players_two_team = team_players - 1

games_played = 0

def score_algorithm(team):
    return reduce(lambda a, e: a * e + 1, team, reduce(lambda a, e: a + e + 1, team))

for players in choose_permute(total_players, game_players):
    print players

    for team_1_offsets in choose_permute(game_players_two_team, team_players_two_team):
        team_1 = [players[0]]
        team_2 = []

        for i in xrange(1, game_players):
            player = players[i]

            if i - 1 in team_1_offsets:
                team_1.append(player)
            else:
                team_2.append(player)

        team_1_score = score_algorithm(tuple(team_1))
        team_2_score = score_algorithm(tuple(team_2))

        #print "%s (%s) vs %s (%s)" % (team_1, team_1_score, team_2, team_2_score)

        games_played = games_played + 1

        if (team_1_score > team_2_score):
            winners = team_1
            losers = team_2
        else:
            winners = team_2
            losers = team_1

        for i in winners:
            win_dict[i]['wins'] = win_dict[i]['wins'] + 1

        for i in players:
            win_dict[i]['games'] = win_dict[i]['games'] + 1

pprint.pprint(win_dict)
