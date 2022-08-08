'''
usando template para usar o codeon-dangeous
https://dnds.gocoder.one/getting-started/game-documentation
'''

import random
import copy


class Vizinho:
    def __init__(self, coord, ac):
        self.coord = coord  # tupla
        self.ac = ac


class Node:
    def __init__(self, pai=None, coord=None, action=None):
        self.pai = pai
        self.coord = coord  # tupla
        self.action = action
        self.hx = 0
        self.gx = 0
        self.hg = 0


class Agent:

    def __init__(self):
        arv = []
        # your agent's initialization code goes here, if any
        pass

    def movimentos(self, ptr: Node):
        acoes = []
        while ptr.pai:
            acoes.append(ptr.acao)
            ptr = ptr.pai
        return acoes

    def next_move(self, game_state, player_state):
        actions = ['', 'u', 'd', 'l', 'r', 'p']
        bau = game_state.treasure
        ore = game_state.ore_blocks
        ammo = game_state.ammo
        ad = game_state.opponents(player_state.id)
        print('ammo')
        print(ammo)
        print('ore')
        print(ore)
        print('bau')
        print(bau)
        action = ''
        if len(bau) != 0:
            heu = self.a_estrela(game_state, player_state.location, bau)
            ac = self.movimentos(heu)
            print('ac')
            print(ac)
            if ac:
                action = ac.pop()
        else:
            action = random.choice(actions)

        return action

    def manhattan_distance(self, start, end):
        distance = abs(start[0] - end[0]) + abs(start[1] - end[1])

        return distance

    def pushN(self, ptr):
        arv = []
        while ptr.pai:
            arv.append(ptr)
            ptr = ptr.pai
            return arv

    def get_vizinhos(self, game_state, coordenada):
        cima = (coordenada[0], coordenada[1] + 1)
        baixo = (coordenada[0], coordenada[1] - 1)
        esquerda = (coordenada[0] - 1, coordenada[1])
        direita = (coordenada[0] + 1, coordenada[1])
        # Verificar se vizinho é valido
        campos = [Vizinho(cima, 'u'), Vizinho(baixo, 'd'), Vizinho(esquerda, 'l'), Vizinho(direita, 'r')]
        for campo in campos:
            if not game_state.is_in_bounds(campo):
                campos.remove(campo)

        return campos

    def a_estrela(self, game_state, start, objetivo):
        # cria open list
        openL = [Node(None, start, None)]
        ptr = Node(None, start, None)

        # cria close list
        closeL = [()]
        cont = 0
        while len(openL) != 0 and cont < 10:
            delV = 0  # Posição de openL (valor menos significativo) que será removida
            i = 0
            while i is not len(openL):
                if ptr.hg < openL[i].hg:
                    ptr = openL[i]
                    delV = i
                ++i

            if ptr.coord == objetivo:
                return self.pushN(ptr)

            closeL.append(openL[delV])
            del openL[delV]

            vizinhos = self.get_vizinhos(game_state, ptr.coord)
            vizinhosAux = []
            for vizinho in vizinhos:
                j = 0;
                opV = False
                clV = False
                vizinhosAux.append(Node(None, vizinho.coord, vizinho.ac))
                custo = ++vizinhosAux[j].gx

                for op in openL:
                    if op.coord == vizinhosAux[j].coord and custo < vizinhosAux[j].gx:
                        openL.remove(vizinhosAux[j])
                        opV = True
                for cl in closeL:
                    if cl.coord == vizinhosAux[j].coord and custo < vizinhosAux[j].gx:
                        closeL.remove(vizinhosAux[j])
                        clV = False

                if not clV and not opV:
                    vizinhosAux[j].g = custo
                    vizinhosAux[j].h = self.manhattan_distance(vizinhosAux[j].coord, objetivo)
                    vizinhosAux[j].f = custo + vizinhosAux[j].h
                    openL.append(vizinhosAux[j])

                ++j
                ++cont

