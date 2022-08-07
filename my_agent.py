'''
usando template para usar o codeon-dangeous
https://dnds.gocoder.one/getting-started/game-documentation
'''

import random

class Agent:

    def __init__(self):

        pass

    def next_move(self, game_state, player_state):

        actions = ['', 'u', 'd', 'l', 'r', 'p']
        action = random.choice(actions)

        return action
